import feedparser

def scrape_skynewsuk():
    url = "https://feeds.skynews.com/feeds/rss/home.xml"
    feed = feedparser.parse(url)
    headlines = [entry.title for entry in feed.entries if len(entry.title) > 30]
    return headlines
