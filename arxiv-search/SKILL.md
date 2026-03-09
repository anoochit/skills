---
name: arxiv-search
description: Search academic research papers on arXiv. Use when the user asks for scientific papers, research on specific topics, or abstracts from arXiv.
version: 1.0.0
author: Your Name
category: research
---

# arXiv Search

This skill provides the ability to search for academic research papers on arXiv using its official API.

## Search Workflow

To search for papers, use the `scripts/search_arxiv.py` script. It accepts a search query and an optional `--max_results` parameter.

### Basic Search

Run the script with a search query:

```bash
python scripts/search_arxiv.py "machine learning"
```

### Advanced Search with Result Limit

Specify the number of results to return:

```bash
python scripts/search_arxiv.py "quantum computing" --max_results 10
```

## Output Format

The script outputs:
- **Title**: The title of the paper.
- **Authors**: List of authors.
- **Published**: Publication date.
- **Link**: Link to the paper on arXiv.
- **Summary**: A brief abstract of the paper.
