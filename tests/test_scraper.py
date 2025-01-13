import pytest
from reddit_scraper.scraper import RedditScraper
import yaml
import os

@pytest.fixture(scope="session")
def scraper():
    if os.path.exists('test.csv'):
        os.remove('test.csv')
    config = yaml.safe_load(open("config.yaml"))
    rs = RedditScraper(
        client_id=config['client_id'],
        client_secret=config['client_secret'],
        user_agent='USER_AGENT',
        subreddits=['singapore'],
        days_back=1,
        scrape_comments=False
    )
    rs.scrape()
    return rs

def test_scrape(scraper):
    assert scraper is not None 

def test_scrape2(scraper):
    assert isinstance(scraper, RedditScraper)

def test_scrape_comments(scraper):
    assert len(scraper.data['submissions']) > 0

def test_write_submissions_data(scraper):
    scraper.write_submissions_data('test.csv')
    assert os.path.exists('test.csv')

def test_write_submissions_data_append(scraper):
    scraper.write_submissions_data('test.csv')
    initial_size = os.path.getsize('test.csv')
    
    scraper.data['submissions'].append({'submission': 'test submission'})
    scraper.write_submissions_data('test.csv')
    
    new_size = os.path.getsize('test.csv')
    assert new_size > initial_size