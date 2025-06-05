from scraper.working.reuters import scrape_reuters

def test_reuters_scraper_returns_headlines():
    headlines = scrape_reuters()
    assert isinstance(headlines, list), "Expected a list of headlines"
    assert len(headlines) > 0, "Expected at least one headline"
    assert all(isinstance(h, str) for h in headlines), "All headlines should be strings"
