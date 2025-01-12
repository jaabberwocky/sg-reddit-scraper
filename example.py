import yaml
from reddit_scraper.scraper import RedditScraper

def main():
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
    rs.write_submissions_data('submissions.csv')

if __name__ == "__main__":
    main()
