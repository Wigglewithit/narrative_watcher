import feedparser
import urllib.request

def scrape_cbc_canada():
    url = "https://news.google.com/rss/search?q=when:24h+allinurl:cbc.ca&hl=en-US&gl=CA&ceid=CA:en"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=6) as response:
        feed = feedparser.parse(response)
    headlines = [entry.title for entry in feed.entries if len(entry.title) > 30]
    return headlines
