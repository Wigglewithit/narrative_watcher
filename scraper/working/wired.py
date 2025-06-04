import feedparser

def scrape_wired():
    url = "https://www.wired.com/feed/rss"
    feed = feedparser.parse(url)
    headlines = [entry.title for entry in feed.entries if len(entry.title) > 30]
    return headlines
