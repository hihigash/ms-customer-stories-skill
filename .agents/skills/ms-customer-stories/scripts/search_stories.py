#!/usr/bin/env python3
"""Search Microsoft Customer Stories via internal API.

Usage:
    python search_stories.py [options]

Examples:
    python search_stories.py --region asia/japan --products azure/azure-openai
    python search_stories.py --query "RAG" --region asia/japan
    python search_stories.py --industry healthcare --org-size 50-999-employees --top 5
    python search_stories.py --products azure --business-need artificial-intelligence --region asia/japan
"""
import argparse
import json
import sys

try:
    import requests
except ImportError:
    print("Error: 'requests' package is required. Install with: pip install requests", file=sys.stderr)
    sys.exit(1)

API_URL = "https://www.microsoft.com/msstoreapiprod/api/customerstoriessearch"
STORY_BASE_URL = "https://www.microsoft.com/en/customers/story"
HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Origin": "https://www.microsoft.com",
    "Referer": "https://www.microsoft.com/en-us/customers/search",
}


def search(query=None, products=None, region=None, industry=None,
           business_need=None, org_size=None, service=None,
           includes=None, top=12, skip=0, locale="en-ww"):
    """Search customer stories. Returns parsed JSON response."""
    body = {"locale": locale, "top": top, "skip": skip}

    if query:
        body["query"] = query
    if products:
        tag = ",".join(f"product:{p}" for p in products.split(","))
        body["products"] = tag
        body["product"] = tag
    if region:
        body["region"] = f"region:{region}"
    if industry:
        body["industries"] = ",".join(f"industry:{i}" for i in industry.split(","))
    if business_need:
        body["businessneed"] = ",".join(f"business-need:{b}" for b in business_need.split(","))
    if org_size:
        body["organizationSize"] = f"organization-size:{org_size}"
    if service:
        body["service"] = f"service:{service}"
    if includes:
        body["storiesThatInclude"] = ",".join(f"stories-that-include:{i}" for i in includes.split(","))

    resp = requests.post(API_URL, json=body, headers=HEADERS, timeout=15)
    resp.raise_for_status()
    return resp.json()


def format_results(data):
    """Format API response into readable output."""
    total = data.get("totalCount", 0)
    has_more = data.get("hasMorePages", False)
    cards = data.get("cards", [])

    output = {
        "totalCount": total,
        "hasMorePages": has_more,
        "resultsReturned": len(cards),
        "stories": [],
    }

    for card in cards:
        content = card.get("content", {})
        action = content.get("action", {})
        href = action.get("href", "")
        industries = [ind.get("text", "") for ind in content.get("industries", [])]

        # Extract related products
        related_products = []
        footer = content.get("footer", {})
        rp = footer.get("relatedProducts", {}).get("products", [])
        for prod in rp:
            badge = prod.get("badge", {})
            icon = badge.get("icon", {})
            label = icon.get("alt", "") or icon.get("image", {}).get("alt", "")
            if label:
                related_products.append(label)

        story = {
            "title": content.get("title", ""),
            "url": f"{STORY_BASE_URL}/{href}" if href else "",
            "industry": content.get("eyebrow", "").replace("Industry: ", ""),
            "industries": industries,
        }
        if related_products:
            story["relatedProducts"] = related_products

        output["stories"].append(story)

    return output


def main():
    parser = argparse.ArgumentParser(description="Search Microsoft Customer Stories")
    parser.add_argument("--query", "-q", help="Text search query")
    parser.add_argument("--products", "-p", help="Product filter (e.g., azure/azure-openai)")
    parser.add_argument("--region", "-r", help="Region filter (e.g., asia/japan)")
    parser.add_argument("--industry", "-i", help="Industry filter (e.g., healthcare)")
    parser.add_argument("--business-need", "-b", help="Business need filter (e.g., artificial-intelligence)")
    parser.add_argument("--org-size", "-o", help="Organization size (e.g., 50-999-employees)")
    parser.add_argument("--service", "-s", help="Service filter (e.g., fasttrack)")
    parser.add_argument("--includes", help="Stories that include (e.g., videos,partners)")
    parser.add_argument("--top", "-t", type=int, default=12, help="Number of results (default: 12)")
    parser.add_argument("--skip", type=int, default=0, help="Skip N results for pagination")
    parser.add_argument("--locale", default="en-ww", help="Locale (default: en-ww)")

    args = parser.parse_args()

    data = search(
        query=args.query,
        products=args.products,
        region=args.region,
        industry=args.industry,
        business_need=args.business_need,
        org_size=args.org_size,
        service=args.service,
        includes=args.includes,
        top=args.top,
        skip=args.skip,
        locale=args.locale,
    )

    output = format_results(data)
    result = json.dumps(output, indent=2, ensure_ascii=False)
    sys.stdout.buffer.write(result.encode("utf-8"))
    sys.stdout.buffer.write(b"\n")


if __name__ == "__main__":
    main()
