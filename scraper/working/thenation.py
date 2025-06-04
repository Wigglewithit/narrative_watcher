import feedparser

def scrape_thenation():
    url = "https://www.thenation.com/feed/?post_type=article"
    feed = feedparser.parse(url)
    headlines = [entry.title for entry in feed.entries if len(entry.title) > 30]
    return headlines
