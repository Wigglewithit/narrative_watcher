import feedparser

def scrape_bbc():
    url = "http://feeds.bbci.co.uk/news/rss.xml"
    feed = feedparser.parse(url)
    headlines = [entry.title for entry in feed.entries if len(entry.title) > 30]
    return headlines
