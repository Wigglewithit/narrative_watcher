import feedparser

def scrape_vox():
    url = "https://www.vox.com/rss/index.xml"
    feed = feedparser.parse(url)
    headlines = [entry.title for entry in feed.entries if len(entry.title) > 30]
    return headlines
