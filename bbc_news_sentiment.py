import csv
from datetime import date
from pathlib import Path

import requests
from bs4 import BeautifulSoup

# Optional sentiment support
try:
    from textblob import TextBlob
    TEXTBLOB_AVAILABLE = True
except ImportError:
    TEXTBLOB_AVAILABLE = False


TODAY = date.today()
OUTPUT_DIR = Path("/Users/sujaymuramalla/Documents/Projects/python_training/output_bbc")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

TXT_FILE = OUTPUT_DIR / f"bbc_news_topics_{TODAY}.txt"
CSV_FILE = OUTPUT_DIR / f"bbc_news_topics_{TODAY}.csv"

RSS_URL = "https://feeds.bbci.co.uk/news/rss.xml"
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

# Simple cleanup filter for promo/non-topic entries
IGNORE_KEYWORDS = [
    "bbc news app",
    "5 live",
    "podcast",
    "news daily",
    "sounds",
]


def get_sentiment(text: str) -> tuple[str, float]:
    """
    Return a simple sentiment label and polarity score.
    Uses TextBlob if installed; otherwise returns neutral.
    """
    if not text.strip():
        return "neutral", 0.0

    if not TEXTBLOB_AVAILABLE:
        return "neutral", 0.0

    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0.1:
        return "positive", polarity
    if polarity < -0.1:
        return "negative", polarity
    return "neutral", polarity


def is_valid_topic(title: str) -> bool:
    """
    Filter out empty, promo-like, or obviously irrelevant titles.
    """
    if not title or not title.strip():
        return False

    title_lower = title.strip().lower()

    for keyword in IGNORE_KEYWORDS:
        if keyword in title_lower:
            return False

    return True


def fetch_bbc_rss() -> bytes:
    """
    Download BBC RSS feed content.
    """
    response = requests.get(RSS_URL, headers=HEADERS, timeout=20)
    print(f"Request to {RSS_URL} returned status {response.status_code}")
    response.raise_for_status()
    return response.content


def parse_feed(xml_content: bytes) -> list[dict]:
    """
    Parse RSS XML and extract article fields.
    """
    soup = BeautifulSoup(xml_content, "xml")
    items = soup.find_all("item")

    print("-" * 70)
    print(f"Items found in RSS feed: {len(items)}")
    print("-" * 70)

    articles = []
    seen_titles = set()

    for item in items:
        title_tag = item.find("title")
        link_tag = item.find("link")
        desc_tag = item.find("description")
        pubdate_tag = item.find("pubDate")

        title = title_tag.text.strip() if title_tag and title_tag.text else ""
        link = link_tag.text.strip() if link_tag and link_tag.text else ""
        description = desc_tag.text.strip() if desc_tag and desc_tag.text else ""
        pub_date = pubdate_tag.text.strip() if pubdate_tag and pubdate_tag.text else ""

        if not is_valid_topic(title):
            continue

        if title in seen_titles:
            continue

        seen_titles.add(title)

        sentiment_input = f"{title}. {description}".strip()
        sentiment_label, sentiment_score = get_sentiment(sentiment_input)

        articles.append({
            "title": title,
            "link": link,
            "description": description,
            "pub_date": pub_date,
            "sentiment_label": sentiment_label,
            "sentiment_score": round(sentiment_score, 3),
        })

    return articles


def save_to_txt(articles: list[dict], filename: Path) -> None:
    """
    Save readable text output.
    """
    with open(filename, "w", encoding="utf-8") as f:
        for index, article in enumerate(articles, start=1):
            f.write(f"{index}. {article['title']}\n")
            f.write(f"   Link: {article['link']}\n")
            f.write(f"   Published: {article['pub_date']}\n")
            f.write(f"   Description: {article['description']}\n")
            f.write(
                f"   Sentiment: {article['sentiment_label']} "
                f"(score={article['sentiment_score']})\n\n"
            )


def save_to_csv(articles: list[dict], filename: Path) -> None:
    """
    Save structured CSV output.
    """
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "title",
            "link",
            "pub_date",
            "description",
            "sentiment_label",
            "sentiment_score",
        ])

        for article in articles:
            writer.writerow([
                article["title"],
                article["link"],
                article["pub_date"],
                article["description"],
                article["sentiment_label"],
                article["sentiment_score"],
            ])


def print_summary(articles: list[dict]) -> None:
    """
    Print extracted topics to terminal.
    """
    print(f"\nCleaned topics extracted: {len(articles)}\n")

    for index, article in enumerate(articles, start=1):
        print(
            f"{index}. {article['title']} "
            f"[{article['sentiment_label']} | {article['sentiment_score']}]"
        )


def main() -> None:
    print(f"Today's date: {TODAY}")
    print(f"TXT output: {TXT_FILE}")
    print(f"CSV output: {CSV_FILE}")

    if not TEXTBLOB_AVAILABLE:
        print("\nNote: TextBlob is not installed. Sentiment will default to neutral.")
        print("Install it with:")
        print("  pip3 install textblob")
        print("Then download corpora once with:")
        print("  python3 -m textblob.download_corpora\n")

    try:
        xml_content = fetch_bbc_rss()
        articles = parse_feed(xml_content)

        if not articles:
            print("No valid topics found after filtering.")
            return

        print_summary(articles)
        save_to_txt(articles, TXT_FILE)
        save_to_csv(articles, CSV_FILE)

        print("\nDone.")
        print(f"Saved TXT to: {TXT_FILE}")
        print(f"Saved CSV to: {CSV_FILE}")

    except requests.RequestException as exc:
        print(f"Network/request error: {exc}")
    except Exception as exc:
        print(f"Unexpected error: {exc}")


if __name__ == "__main__":
    main()