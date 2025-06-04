import feedparser

def scrape_abc():
    url = "https://abcnews.go.com/abcnews/topstories"
    feed = feedparser.parse(url)
    headlines = [entry.title for entry in feed.entries if len(entry.title) > 30]
    return headlines
