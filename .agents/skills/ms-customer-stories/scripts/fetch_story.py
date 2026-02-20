#!/usr/bin/env python3
"""Fetch a Microsoft Customer Story page and extract its content.

Usage:
    python fetch_story.py <story_url_or_slug>

Examples:
    python fetch_story.py 25666-softbank-corp-azure-ai-foundry
    python fetch_story.py https://www.microsoft.com/en/customers/story/25666-softbank-corp-azure-ai-foundry
"""
import html
import json
import re
import sys

try:
    import requests
except ImportError:
    print("Error: 'requests' package is required. Install with: pip install requests", file=sys.stderr)
    sys.exit(1)

STORY_BASE_URL = "https://www.microsoft.com/en/customers/story"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
}


def extract_text_from_html(html_str):
    """Extract readable text from HTML, removing tags and excessive whitespace."""
    # Remove script and style elements
    html_str = re.sub(r'<script[^>]*>.*?</script>', '', html_str, flags=re.DOTALL | re.IGNORECASE)
    html_str = re.sub(r'<style[^>]*>.*?</style>', '', html_str, flags=re.DOTALL | re.IGNORECASE)
    # Remove header and footer
    html_str = re.sub(r'<header[^>]*>.*?</header>', '', html_str, flags=re.DOTALL | re.IGNORECASE)
    html_str = re.sub(r'<footer[^>]*>.*?</footer>', '', html_str, flags=re.DOTALL | re.IGNORECASE)
    # Remove nav
    html_str = re.sub(r'<nav[^>]*>.*?</nav>', '', html_str, flags=re.DOTALL | re.IGNORECASE)
    # Remove elements with aria-hidden="true"
    html_str = re.sub(r'<[^>]+aria-hidden="true"[^>]*>.*?</[^>]+>', '', html_str, flags=re.DOTALL)
    # Remove remaining HTML attributes like "> that appear in text
    html_str = re.sub(r'\s*">\s*', ' ', html_str)
    # Convert common block elements to newlines
    html_str = re.sub(r'<(?:p|div|h[1-6]|li|br|tr)[^>]*>', '\n', html_str, flags=re.IGNORECASE)
    # Remove all remaining HTML tags
    text = re.sub(r'<[^>]+>', '', html_str)
    # Decode HTML entities
    text = html.unescape(text)
    # Normalize whitespace
    lines = []
    for line in text.split('\n'):
        line = ' '.join(line.split())
        if line:
            lines.append(line)
    return '\n'.join(lines)


def fetch_story(url_or_slug):
    """Fetch and parse a customer story page."""
    if url_or_slug.startswith("http"):
        url = url_or_slug
    else:
        url = f"{STORY_BASE_URL}/{url_or_slug}"

    resp = requests.get(url, headers=HEADERS, timeout=15)
    resp.raise_for_status()
    html = resp.text

    # Extract title from <title> tag
    title_match = re.search(r'<title[^>]*>([^<]+)</title>', html, re.IGNORECASE)
    title = title_match.group(1).strip() if title_match else ""
    # Remove common suffix
    title = re.sub(r'\s*\|\s*Microsoft Customer Stories\s*$', '', title)

    # Extract meta description
    desc_match = re.search(r'<meta\s+name="description"\s+content="([^"]*)"', html, re.IGNORECASE)
    description = desc_match.group(1) if desc_match else ""

    # Extract main content
    # Try to find the main content area
    main_match = re.search(r'<main[^>]*>(.*?)</main>', html, flags=re.DOTALL | re.IGNORECASE)
    if main_match:
        content_html = main_match.group(1)
    else:
        content_html = html

    content = extract_text_from_html(content_html)

    return {
        "url": url,
        "title": title,
        "description": description,
        "content": content,
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: python fetch_story.py <story_url_or_slug>", file=sys.stderr)
        sys.exit(1)

    url_or_slug = sys.argv[1]
    result = fetch_story(url_or_slug)
    output = json.dumps(result, indent=2, ensure_ascii=False)
    sys.stdout.buffer.write(output.encode("utf-8"))
    sys.stdout.buffer.write(b"\n")


if __name__ == "__main__":
    main()
