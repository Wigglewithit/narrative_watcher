import feedparser

def scrape_marketwatch():
    url = "https://www.marketwatch.com/rss/topstories"
    feed = feedparser.parse(url)
    headlines = [entry.title for entry in feed.entries if len(entry.title) > 30]
    return headlines
