import pytest
from reddit_scraper.scraper import RedditScraper

@pytest.fixture
def scraper():
    return RedditScraper(
        client_id='YOUR_CLIENT_ID',
        client_secret='YOUR_CLIENT_SECRET',
        user_agent='YOUR_USER_AGENT',
        subreddits=['python'],
        days_back=1,
        scrape_comments=False
    )

def test_scrape(scraper):
    # This is a placeholder test. You would implement actual tests here.
    assert scraper is not None 
