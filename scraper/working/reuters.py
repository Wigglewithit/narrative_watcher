import feedparser
import logging

def scrape_reuters():
    url = "http://feeds.reuters.com/reuters/topNews"
    try:
        feed = feedparser.parse(url)

        if not feed.entries:
            logging.warning(f"[Reuters] No entries found: {url}")
            return []

        return [entry.title for entry in feed.entries]

    except Exception as e:
        logging.error(f"[Reuters] Scraper failed: {e}")
        return []
