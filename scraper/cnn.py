import requests
from bs4 import BeautifulSoup

def scrape_cnn():
    url = "https://edition.cnn.com"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    headlines = []

    for item in soup.select('h2'):
        text = item.get_text(strip=True)
        if text and len(text) > 30:  # filter short/unhelpful stuff
            if not any(word in text.lower() for word in ["photo", "video", "watch", "missed"]):
                headlines.append(text)

    return headlines
