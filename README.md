# Microsoft Customer Stories Skill

A [GitHub Copilot Skill](https://docs.github.com/en/copilot/customizing-copilot/copilot-extensions/building-copilot-skills) that searches and retrieves customer stories from the official [Microsoft Customer Stories](https://www.microsoft.com/en-us/customers/search) site.

## Features

- **Search** customer stories by product, region, industry, business need, organization size, and keyword
- **Fetch** full story details including title, description, and content
- Supports all Microsoft product categories (Azure, M365, Dynamics 365, Power Platform, etc.)
- Covers 245 regions/countries and 16 industries

## Prerequisites

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

## Setup

```bash
uv venv .venv
uv pip install requests --python .venv/Scripts/python.exe
```

## Project Structure

```
├── .agents/skills/ms-customer-stories/   # Installed skill files
│   ├── SKILL.md                          # Skill definition
│   ├── references/filters.md             # Filter reference (products, regions, industries, etc.)
│   └── scripts/
│       ├── search_stories.py             # Search API client
│       └── fetch_story.py                # Story page fetcher
└── ms-customer-stories.skill             # Packaged skill archive
```

## Usage Examples

Search for stories:

```bash
python .agents/skills/ms-customer-stories/scripts/search_stories.py \
  --products azure/azure-openai --region asia/japan --top 5
```

Fetch a specific story:

```bash
python .agents/skills/ms-customer-stories/scripts/fetch_story.py \
  25666-softbank-corp-azure-ai-foundry
```

## License

This project is provided as-is for use with GitHub Copilot.
