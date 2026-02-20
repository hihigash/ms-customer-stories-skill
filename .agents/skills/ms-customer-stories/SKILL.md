---
name: ms-customer-stories
description: Search and retrieve Microsoft Customer Stories from the official Microsoft Customer Stories site (https://www.microsoft.com/en-us/customers/search). Use when the user asks to find customer case studies, success stories, or reference examples of Microsoft technology adoption. Supports filtering by product (Azure, M365, Dynamics 365, etc.), region/country, industry, business need, organization size, and keyword search. Can also fetch individual story details. Typical triggers include questions like "Find customer stories about Azure OpenAI in Japan", "Show me healthcare companies using Microsoft 365 Copilot", or "日本の製造業でAIを活用した事例を探して".
---

# Microsoft Customer Stories

## Overview

Search and retrieve customer stories from Microsoft's official Customer Stories site via its internal API.

## Workflow

1. Analyze the user's request to determine appropriate filters
2. Run `scripts/search_stories.py` with selected filters to find matching stories
3. Review results and optionally run `scripts/fetch_story.py` on specific stories for full details
4. Summarize findings for the user

## Prerequisites

Install `requests` in the Python environment: `pip install requests`

## Step 1: Map User Request to Filters

Translate the user's natural language request into API filter parameters. Consult `references/filters.md` for the complete list of available filter values.

**Mapping guidelines:**

| User mentions | Filter to use |
|---|---|
| Country/region names (Japan, US, etc.) | `--region` (e.g., `asia/japan`) |
| Product names (Azure, Teams, etc.) | `--products` (e.g., `azure/azure-openai`) |
| Industry terms (healthcare, finance, etc.) | `--industry` (e.g., `healthcare`) |
| Business concepts (AI, automation, etc.) | `--business-need` (e.g., `artificial-intelligence`) |
| Company size (SMB, enterprise, etc.) | `--org-size` (e.g., `50-999-employees`) |
| Specific technology terms (RAG, etc.) | `--query` (free text search) |

**Common mappings:**
- "中小企業" / "SMB" → `--org-size 50-999-employees` or `--org-size 1-49-employees`
- "大企業" / "Enterprise" → `--org-size 10000-employees`
- "RAG" / "検索拡張生成" → `--query RAG` + `--products azure/azure-openai`
- "日本" → `--region asia/japan`

## Step 2: Search Stories

Run the search script:

```bash
python scripts/search_stories.py --products azure/azure-openai --region asia/japan --query "RAG" --top 10
```

**Arguments:**
- `--query` / `-q`: Free text search
- `--products` / `-p`: Product filter (e.g., `azure/azure-openai`, `azure/azure-ai-search`)
- `--region` / `-r`: Region filter (e.g., `asia/japan`, `europe/germany`)
- `--industry` / `-i`: Industry filter (e.g., `healthcare`, `manufacturing`)
- `--business-need` / `-b`: Business need (e.g., `artificial-intelligence`)
- `--org-size` / `-o`: Organization size (e.g., `50-999-employees`)
- `--service` / `-s`: Service filter (e.g., `fasttrack`)
- `--includes`: Stories that include (e.g., `videos,partners`)
- `--top` / `-t`: Number of results (default: 12)
- `--skip`: Pagination offset

Output is JSON with `totalCount`, `hasMorePages`, and `stories` array.

## Step 3: Fetch Story Details

For interesting stories, fetch the full content:

```bash
python scripts/fetch_story.py 25666-softbank-corp-azure-ai-foundry
```

Accepts a story slug or full URL. Returns JSON with `title`, `description`, `content`.

## Output Format

**Always respond in the same language the user used.** If the user asks in Japanese, reply in Japanese. If in English, reply in English.

Present results to the user in this format:

```
## Search Results: {totalCount} stories

### 1. {title}
- **Industry**: {industry}
- **URL**: {url}
- **Summary**: {summary from content}

### 2. {title}
...
```

When the user asks for details on a specific story, provide a more detailed summary of the story content including key challenges, solutions, and outcomes.
