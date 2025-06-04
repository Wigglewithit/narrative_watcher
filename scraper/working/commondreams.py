import feedparser

def scrape_commondreams():
    url = "https://www.commondreams.org/rss.xml"
    feed = feedparser.parse(url)
    headlines = [entry.title for entry in feed.entries if len(entry.title) > 30]
    return headlines
