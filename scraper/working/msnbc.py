import requests
from bs4 import BeautifulSoup

def scrape_msnbc():
    url = "https://www.msnbc.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    headlines = []

    for item in soup.select('h2'):
        text = item.get_text(strip=True)
        if text and len(text) > 30:
            if not any(word in text.lower() for word in ["subscribe", "read", "opinion"]):
                headlines.append(text)

    return headlines
