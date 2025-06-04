import feedparser

def scrape_nyt():
    url = "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"
    feed = feedparser.parse(url)

    headlines = []

    for entry in feed.entries:
        title = entry.title
        if title and len(title) > 30:
            if not any(bad in title.lower() for bad in ["newsletter", "watch", "opinion"]):
                headlines.append(title)

    return headlines
