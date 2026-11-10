import json
import os
import re
import sys

import requests


AUTHOR_ID = os.getenv("GOOGLE_SCHOLAR_AUTHOR_ID", "Un02rhgAAAAJ")
API_KEY   = os.getenv("SERPAPI_KEY")
# SerpApi truncates long author lists with "...". Set to 1 to fetch the full list
# per article (costs one extra SerpApi search per publication).
FULL_AUTHORS = os.getenv("SCHOLAR_FULL_AUTHORS", "0") == "1"

SERPAPI_URL = "https://serpapi.com/search.json"
PAGE_SIZE = 100

# Variations of your name to bold
MY_NAME_PATTERNS = [
    r"Giovanni Qui[nñ]ones(?:[- ]Valdez)?",
    r"G\.? Qui[nñ]ones-Valdez",
    r"GQ Valdez"
]


def serpapi(**params):
    params.update(engine="google_scholar_author", author_id=AUTHOR_ID, api_key=API_KEY)
    resp = requests.get(SERPAPI_URL, params=params, timeout=60)
    resp.raise_for_status()
    data = resp.json()
    if "error" in data:
        raise RuntimeError(f"SerpApi error: {data['error']}")
    return data


def format_author_name(authors_str):
    if not authors_str:
        return ""

    # Wrap matched name variations in bold tags
    formatted = authors_str
    for pattern in MY_NAME_PATTERNS:
        formatted = re.sub(
            f"({pattern})",
            r"<strong>\1</strong>",
            formatted,
            flags=re.IGNORECASE
        )
    return formatted


def fetch_full_authors(citation_id):
    try:
        data = serpapi(view_op="view_citation", citation_id=citation_id)
        return data.get("citation", {}).get("authors", "")
    except Exception as e:
        print(f"  Could not fetch full authors for {citation_id}: {e}")
        return ""


if not API_KEY:
    sys.exit("SERPAPI_KEY environment variable is not set.")

print(f"Fetching Google Scholar profile for: {AUTHOR_ID}")

# First page also carries the author info and citation metrics
first_page = serpapi(start=0, num=PAGE_SIZE)
articles = list(first_page.get("articles", []))

page = first_page
start = PAGE_SIZE
while "next" in page.get("serpapi_pagination", {}):
    page = serpapi(start=start, num=PAGE_SIZE)
    if not page.get("articles"):
        break
    articles.extend(page["articles"])
    start += PAGE_SIZE

print(f"Found {len(articles)} publications.")

author_info = first_page.get("author", {})
formatted_data = {
    "author": {
        "name": author_info.get("name", ""),
        "affiliations": author_info.get("affiliations", ""),
        "thumbnail": author_info.get("thumbnail", "")
    },
    "cited_by": first_page.get("cited_by", {}),
    "articles": []
}

for article in articles:
    authors = article.get("authors", "")
    if FULL_AUTHORS and article.get("citation_id"):
        authors = fetch_full_authors(article["citation_id"]) or authors
    formatted_authors = format_author_name(authors)

    formatted_data["articles"].append({
        "title": article.get("title", ""),
        "link": article.get("link", ""),
        "authors": formatted_authors,
        "author": formatted_authors,
        "publication": article.get("publication", ""),
        "cited_by": {
            "value": (article.get("cited_by") or {}).get("value") or 0
        },
        "year": str(article.get("year", ""))
    })

output_path = os.path.join(os.path.dirname(__file__), "..", "_data", "scholar.json")
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(formatted_data, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {output_path}")
