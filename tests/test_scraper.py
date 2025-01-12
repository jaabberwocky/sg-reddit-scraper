import pytest
from reddit_scraper.scraper import RedditScraper
import yaml
import os

@pytest.fixture
def scraper():
    # delete the test.csv file if it exists
    if os.path.exists('test.csv'):
        os.remove('test.csv')
    config = yaml.safe_load(open("config.yaml"))
    return RedditScraper(
        client_id=config['client_id'],
        client_secret=config['client_secret'],
        user_agent='USER_AGENT',
        subreddits=['singapore'],
        days_back=1,
        scrape_comments=False
    )

def test_scrape(scraper):
    # This is a placeholder test. You would implement actual tests here.
    print("hey")
    assert scraper is not None 

def test_scrape2(scraper):
    # check if is instance of RedditScraper
    assert isinstance(scraper, RedditScraper)

def test_scrape_comments(scraper):
    scraper.scrape_comments = False
    scraper.scrape()
    assert len(scraper.data['submissions']) > 0

# def test_scrape_comments2(scraper):
#     scraper.scrape_comments = True
#     scraper.scrape()
#     assert len(scraper.data['comments']) > 0

def test_write_submissions_data(scraper):
    scraper.scrape()    
    scraper.write_submissions_data('test.csv')
    assert os.path.exists('test.csv')
