from analysis.keywords import extract_keywords
from utils.storage import save_headlines

# All working scrapers (you can remove or add as needed)
from scraper.working.abc import scrape_abc
from scraper.working.aljazeera import scrape_aljazeera
from scraper.working.bbc import scrape_bbc
from scraper.working.breitbart import scrape_breitbart
from scraper.working.bloomberg import scrape_bloomberg
from scraper.working.cbc_canada import scrape_cbc
from scraper.working.cbs import scrape_cbs
from scraper.working.cnbc import scrape_cnbc
from scraper.working.commondreams import scrape_commondreams
from scraper.working.democracynow import scrape_democracynow
from scraper.working.deutschewelle import scrape_deutschewelle
from scraper.working.fox import scrape_fox
from scraper.working.huffpost import scrape_huffpost
from scraper.working.marketwatch import scrape_marketwatch
from scraper.working.motherjones import scrape_motherjones
from scraper.working.msnbc import scrape_msnbc
from scraper.working.nbc import scrape_nbc
from scraper.working.newsmax import scrape_newsmax
from scraper.working.npr import scrape_npr
from scraper.working.nyt import scrape_nyt
from scraper.working.propublica import scrape_propublica
from scraper.working.reuters import scrape_reuters
from scraper.working.salon import scrape_salon
from scraper.working.skynewsuk import scrape_skynewsuk
from scraper.working.techcrunch import scrape_techcrunch
from scraper.working.theblaze import scrape_theblaze
from scraper.working.thegrayzone import scrape_thegrayzone
from scraper.working.theguardian_us import scrape_theguardian_us
from scraper.working.thehill import scrape_thehill
from scraper.working.theintercept import scrape_theintercept
from scraper.working.thenation import scrape_thenation
from scraper.working.theverge import scrape_theverge
from scraper.working.truthout import scrape_truthout
from scraper.working.usatoday import scrape_usatoday
from scraper.working.vox import scrape_vox
from scraper.working.wired import scrape_wired
from scraper.working.thefederalist import scrape_thefederalist
from scraper.working.townhall import scrape_townhall
from scraper.working.pjmedia import scrape_pjmedia
from scraper.working.dailycaller import scrape_dailycaller
from scraper.working.westernjournal import scrape_westernjournal
from scraper.working.justthenews import scrape_justthenews

import requests


import concurrent.futures
from datetime import datetime

def run_with_timeout(scraper_func, timeout=10):
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(scraper_func)
        try:
            return future.result(timeout=timeout)
        except concurrent.futures.TimeoutError:
            print(f"    ⏱️  Timeout after {timeout}s")
            return []
        except Exception as e:
            print(f"    ❌ Error: {e}")
            return []

def log_status(message):
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] {message}")

def main():
    sources = {
        "abc": scrape_abc,
        "aljazeera": scrape_aljazeera,
        "bbc": scrape_bbc,
        "breitbart": scrape_breitbart,
        "bloomberg": scrape_bloomberg,
        "cbc_canada": scrape_cbc,
        # ... (rest of your sources) ...
        "justthenews": scrape_justthenews,
    }

    log_status("🚀 Starting headline collection...\n")

    for name, scraper_func in sources.items():
        log_status(f"▶️  Scraping {name.upper()}...")

        headlines = run_with_timeout(scraper_func, timeout=10)

        if not headlines:
            log_status(f"⚠️  No headlines from {name.upper()} — skipped.\n")
            continue

        for line in headlines:
            print(f"- {line}")

        print(f"\nTop Keywords ({name.upper()}):")
        for word, count in extract_keywords(headlines):
            print(f"{word}: {count}")

        save_headlines(headlines, name)
        log_status(f"✅ Finished {name.upper()}\n")

    log_status("🎉 All scraping complete. Data saved to data/processed/")


if __name__ == "__main__":
    main()
