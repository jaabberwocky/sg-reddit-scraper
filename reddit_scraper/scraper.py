import praw
from datetime import datetime, timedelta, timezone
import pandas as pd

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
        self.data = {'submissions': [], 'comments': []}

    def write_submissions_data(self, path):
        submissions_df = pd.DataFrame(self.data['submissions'])
        submissions_df.to_csv(path, mode='a+')

    def write_comments_data(self, path):
        comments_df = pd.DataFrame(self.data['comments'])
        comments_df.to_csv(path, mode='a+')

    def add_submission(self, submission):
        self.data['submissions'].append(submission)

    def add_comment(self, submission):
        self.data['comments'].append(submission)

    def scrape(self):
        time_threshold = datetime.now(timezone.utc) - timedelta(days=self.days_back)

        for subreddit_name in self.subreddits:
            subreddit = self.reddit.subreddit(subreddit_name)
            print(f"Scraping subreddit: {subreddit_name}")

            for submission in subreddit.new(limit=None):
                submission_time = datetime.fromtimestamp(submission.created_utc, timezone.utc)
                if submission_time < time_threshold:
                    break

                print(f"Title: {submission.title}, Created: {submission_time}, Text: {submission.selftext}")

                self.add_submission({
                    # store all the data in the submission object
                    'title': submission.title,
                    'created': submission_time,
                    'text': submission.selftext,
                    'subreddit': subreddit_name,
                    'score': submission.score,
                    'num_comments': submission.num_comments,
                    'url': submission.url,
                    'author': submission.author.name,
                    'id': submission.id
                })

                if self.scrape_comments:
                    submission.comments.replace_more(limit=0)
                    for comment in submission.comments.list():
                        print(f"Comment: {comment.body}")

                    self.add_comment({
                        'submission_id': submission.id,
                        'comment_body': comment.body,
                        'author': comment.author.name,
                        'created': comment.created_utc,
                        'score': comment.score,
                        'id': comment.id
                    })


