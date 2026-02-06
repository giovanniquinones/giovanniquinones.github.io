import json
import os
import urllib.parse
import urllib.request

AUTHOR_ID = os.getenv("GOOGLE_SCHOLAR_AUTHOR_ID", "Un02rhgAAAAJ")
API_KEY = os.getenv("SERPAPI_KEY", "684876bd9aa453b096534062f770ec86a2f1ebfc708106d23334604a35b6d110")

if not API_KEY:
    raise SystemExit("SERPAPI_KEY is required")

params = {
    "engine": "google_scholar_author",
    "author_id": AUTHOR_ID,
    "api_key": API_KEY,
}

url = "https://serpapi.com/search.json?" + urllib.parse.urlencode(params)

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode("utf-8"))

output_path = os.path.join(os.path.dirname(__file__), "..", "_data", "scholar.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Wrote {output_path}")
