import feedparser
import logging

def scrape_wired():
    url = "https://www.wired.com/feed/rss"
    try:
        feed = feedparser.parse(url)

        if not feed.entries:
            logging.warning(f"[Wired] No entries found: {url}")
            return []

        return [entry.title for entry in feed.entries]

    except Exception as e:
        logging.error(f"[Wired] Scraper failed: {e}")
        return []
