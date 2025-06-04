import feedparser

def scrape_cnbc():
    url = "https://www.cnbc.com/id/100003114/device/rss/rss.html"
    feed = feedparser.parse(url)
    headlines = [entry.title for entry in feed.entries if len(entry.title) > 30]
    return headlines
