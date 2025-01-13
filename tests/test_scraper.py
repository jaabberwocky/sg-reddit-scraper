import pytest
from reddit_scraper.scraper import RedditScraper
import yaml
import os

@pytest.fixture(scope="session")
def scraper():
    # delete the test.csv file if it exists
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
    # check if is instance of RedditScraper
    assert isinstance(scraper, RedditScraper)

def test_scrape_comments(scraper):
    assert len(scraper.data['submissions']) > 0

def test_write_submissions_data(scraper):
    scraper.write_submissions_data('test.csv')
    assert os.path.exists('test.csv')

def test_write_submissions_data_append(scraper):
    # Write initial data
    scraper.write_submissions_data('test.csv')
    
    # Get the initial file size
    initial_size = os.path.getsize('test.csv')
    
    # Write more data to test appending
    scraper.data['submissions'].append({'submission': 'test submission'})
    scraper.write_submissions_data('test.csv')
    
    # Get the new file size
    new_size = os.path.getsize('test.csv')
    
    # Check if the file size has increased
    assert new_size > initial_size