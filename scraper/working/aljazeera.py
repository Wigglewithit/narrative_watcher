import feedparser

def scrape_aljazeera():
    url = "https://www.aljazeera.com/xml/rss/all.xml"
    feed = feedparser.parse(url)
    headlines = [entry.title for entry in feed.entries if len(entry.title) > 30]
    return headlines
