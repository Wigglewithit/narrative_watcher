import feedparser

def scrape_cbs():
    url = "https://www.cbsnews.com/latest/rss/main"
    feed = feedparser.parse(url)
    headlines = [entry.title for entry in feed.entries if len(entry.title) > 30]
    return headlines
