import requests
from bs4 import BeautifulSoup

def scrape_fox():
    url = "https://www.foxnews.com"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    headlines = []

    # FOX uses h2 and h3 for headlines
    for item in soup.select('h2, h3'):
        text = item.get_text(strip=True)
        if text and len(text) > 30:
            if not any(bad in text.lower() for bad in ["video", "watch", "trending", "read"]):
                headlines.append(text)

    return headlines
