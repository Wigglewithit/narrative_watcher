import feedparser

def scrape_npr():
    url = "https://feeds.npr.org/1001/rss.xml"
    feed = feedparser.parse(url)
    headlines = [entry.title for entry in feed.entries if len(entry.title) > 30]
    return headlines
