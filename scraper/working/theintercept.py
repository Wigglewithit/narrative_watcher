import feedparser

def scrape_theintercept():
    url = "https://theintercept.com/feed/?lang=en"
    feed = feedparser.parse(url)
    headlines = [entry.title for entry in feed.entries if len(entry.title) > 30]
    return headlines
