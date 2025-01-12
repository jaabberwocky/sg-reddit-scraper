import praw
from datetime import datetime, timedelta, UTC

class RedditScraper:
    def __init__(self, client_id, client_secret, user_agent, subreddits, days_back=1, scrape_comments=False):
        self.reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent
        )
        self.subreddits = subreddits
        self.days_back = days_back
        self.scrape_comments = scrape_comments

    def scrape(self):
        time_threshold = datetime.now(datetime.UTC) - timedelta(days=self.days_back)

        for subreddit_name in self.subreddits:
            subreddit = self.reddit.subreddit(subreddit_name)
            print(f"Scraping subreddit: {subreddit_name}")

            for submission in subreddit.new(limit=None):
                submission_time = datetime.utcfromtimestamp(submission.created_utc)
                if submission_time < time_threshold:
                    break

                print(f"Title: {submission.title}, Created: {submission_time}")

                if self.scrape_comments:
                    submission.comments.replace_more(limit=0)
                    for comment in submission.comments.list():
                        print(f"Comment: {comment.body}")

