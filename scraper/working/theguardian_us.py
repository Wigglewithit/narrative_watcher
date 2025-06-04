import feedparser

def scrape_theguardian_us():
    url = "https://www.theguardian.com/us/rss"
    feed = feedparser.parse(url)
    headlines = [entry.title for entry in feed.entries if len(entry.title) > 30]
    return headlines
