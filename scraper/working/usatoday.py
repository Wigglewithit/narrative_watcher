import feedparser
import urllib.request

def scrape_usatoday():
    url = "https://news.google.com/rss/search?q=when:24h+allinurl:usatoday.com&hl=en-US&gl=US&ceid=US:en"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=6) as response:
        feed = feedparser.parse(response)
    headlines = [entry.title for entry in feed.entries if len(entry.title) > 30]
    return headlines
