import feedparser

def scrape_deutschewelle():
    url = "https://rss.dw.com/rdf/rss-en-all"
    feed = feedparser.parse(url)
    headlines = [entry.title for entry in feed.entries if len(entry.title) > 30]
    return headlines
