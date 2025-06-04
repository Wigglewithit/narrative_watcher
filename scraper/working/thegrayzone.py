import feedparser

def scrape_thegrayzone():
    url = "https://thegrayzone.com/feed/"
    feed = feedparser.parse(url)
    headlines = [entry.title for entry in feed.entries if len(entry.title) > 30]
    return headlines
