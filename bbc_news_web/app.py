from flask import Flask, render_template, request
from bs4 import BeautifulSoup
from textblob import TextBlob
from urllib.parse import quote_plus
import requests

app = Flask(__name__)

HEADERS = {"User-Agent": "Mozilla/5.0"}

IGNORE_KEYWORDS = [
    "podcast",
    "bbc news app",
    "5 live",
    "sounds",
]


def get_sentiment(text: str) -> tuple[str, float]:
    """
    Return a sentiment label and score using TextBlob polarity.
    """
    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0.1:
        return "positive", round(polarity, 3)
    if polarity < -0.1:
        return "negative", round(polarity, 3)
    return "neutral", round(polarity, 3)


def is_valid_topic(title: str) -> bool:
    """
    Filter out empty or obviously unwanted titles.
    """
    if not title or not title.strip():
        return False

    title_lower = title.lower()
    return not any(word in title_lower for word in IGNORE_KEYWORDS)


def clean_description_text(text: str) -> str:
    """
    Clean and shorten noisy RSS description text.
    """
    if not text:
        return ""

    cleaned = " ".join(text.split())

    if "Google News" in cleaned:
        cleaned = cleaned.replace("Google News", "").strip()

    max_len = 220
    if len(cleaned) > max_len:
        cleaned = cleaned[:max_len].rstrip() + "..."

    return cleaned


def parse_rss_feed(url: str, default_source: str) -> list[dict]:
    """
    Fetch and parse a generic RSS feed into normalized article dicts.
    """
    response = requests.get(url, headers=HEADERS, timeout=20)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "xml")
    items = soup.find_all("item")

    articles = []

    for item in items:
        title_tag = item.find("title")
        link_tag = item.find("link")
        desc_tag = item.find("description")
        pubdate_tag = item.find("pubDate")
        source_tag = item.find("source")

        title = title_tag.text.strip() if title_tag and title_tag.text else ""
        link = link_tag.text.strip() if link_tag and link_tag.text else ""
        pub_date = pubdate_tag.text.strip() if pubdate_tag and pubdate_tag.text else ""
        source = source_tag.text.strip() if source_tag and source_tag.text else default_source

        raw_description = desc_tag.text.strip() if desc_tag and desc_tag.text else ""

        clean_description = ""
        if raw_description:
            desc_soup = BeautifulSoup(raw_description, "html.parser")
            clean_description = clean_description_text(
                desc_soup.get_text(" ", strip=True)
            )

        if not is_valid_topic(title):
            continue

        sentiment_text = f"{title}. {clean_description}"
        sentiment_label, sentiment_score = get_sentiment(sentiment_text)

        articles.append({
            "source": source,
            "title": title,
            "link": link,
            "description": clean_description,
            "pub_date": pub_date,
            "sentiment_label": sentiment_label,
            "sentiment_score": sentiment_score,
        })

    return articles


def deduplicate_articles(articles: list[dict]) -> list[dict]:
    """
    Remove duplicates using title + link as the uniqueness key.
    """
    seen = set()
    result = []

    for article in articles:
        key = (
            article["title"].strip().lower(),
            article["link"].strip().lower(),
        )
        if key not in seen:
            seen.add(key)
            result.append(article)

    return result


def fetch_bbc_news() -> list[dict]:
    """
    Default homepage feed from BBC.
    """
    url = "https://feeds.bbci.co.uk/news/rss.xml"
    return parse_rss_feed(url, "BBC")


def fetch_google_news_by_topic(topic: str) -> list[dict]:
    """
    Topic-based search using Google News RSS.
    Added when:30d to broaden and improve recency.
    """
    encoded_topic = quote_plus(topic)
    url = (
        f"https://news.google.com/rss/search?"
        f"q={encoded_topic}+when:30d&hl=en-US&gl=US&ceid=US:en"
    )
    return parse_rss_feed(url, "Google News")


def fetch_default_headlines() -> list[dict]:
    """
    Show BBC headlines when no search topic is provided.
    """
    return deduplicate_articles(fetch_bbc_news())


def fetch_all_sources(topic: str) -> list[dict]:
    """
    For topic search, use topic-based search results only.
    No strict relevance filter for now, so you get broader results.
    """
    articles = fetch_google_news_by_topic(topic)
    return deduplicate_articles(articles)


@app.route("/", methods=["GET", "POST"])
def home():
    articles = []
    topic = ""

    try:
        if request.method == "POST":
            topic = request.form.get("topic", "").strip()

            if topic:
                articles = fetch_all_sources(topic)
            else:
                articles = fetch_default_headlines()
        else:
            articles = fetch_default_headlines()

    except requests.RequestException as exc:
        return render_template(
            "index.html",
            articles=[],
            topic=topic,
            error=f"Network error: {exc}",
        )
    except Exception as exc:
        return render_template(
            "index.html",
            articles=[],
            topic=topic,
            error=f"Unexpected error: {exc}",
        )

    return render_template(
        "index.html",
        articles=articles,
        topic=topic,
        error=None,
    )


if __name__ == "__main__":
    app.run(debug=True)