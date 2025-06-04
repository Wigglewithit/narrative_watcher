import feedparser

def scrape_breitbart():
    url = "https://feeds.feedburner.com/breitbart"
    feed = feedparser.parse(url)
    headlines = [entry.title for entry in feed.entries if len(entry.title) > 30]
    return headlines
