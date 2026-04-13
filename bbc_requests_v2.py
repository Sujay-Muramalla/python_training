import requests
from bs4 import BeautifulSoup
from datetime import date
from pathlib import Path

today = date.today()
print("Today's date:", today)

output_dir = Path("/Users/sujaymuramalla/Documents/Projects/python_training/output_bbc")
output_dir.mkdir(parents=True, exist_ok=True)

filename = output_dir / f"bbc_requests_topics_{today}.txt"
print(filename)

def write_bbc_data(lines):
    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")

# BBC RSS feed
url = "https://feeds.bbci.co.uk/news/rss.xml"

headers = {
    "User-Agent": "Mozilla/5.0"
}

res = requests.get(url, headers=headers, timeout=20)
print(f"your request to {url} came back with status {res.status_code}")
res.raise_for_status()

soup = BeautifulSoup(res.content, "xml")

items = soup.find_all("item")
print("--------------------------------------------------")
print(f"length of result set: {len(items)}")
print("--------------------------------------------------")

topics = []

for item in items:
    title_tag = item.find("title")
    if title_tag and title_tag.text.strip():
        title = title_tag.text.strip()
        topics.append(title)

# remove duplicates while preserving order
topics = list(dict.fromkeys(topics))

for topic in topics:
    print(topic)

write_bbc_data(topics)
print(f"\nSaved {len(topics)} topics to: {filename}")