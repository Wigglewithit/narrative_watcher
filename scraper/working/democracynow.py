import feedparser

def scrape_democracynow():
    url = "https://www.democracynow.org/democracynow.rss"
    feed = feedparser.parse(url)
    headlines = [entry.title for entry in feed.entries if len(entry.title) > 30]
    return headlines
