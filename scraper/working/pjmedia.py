import feedparser

def scrape_pjmedia():
    url = "https://pjmedia.com/feed/"
    feed = feedparser.parse(url)

    headlines = []

    for entry in feed.entries:
        title = entry.title
        if title and len(title) > 30:
            if not any(word in title.lower() for word in ["opinion", "watch", "sponsored"]):
                headlines.append(title)

    return headlines
