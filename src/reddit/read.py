import praw


class Reader:

    def __init__(self, credentials, subreddit):
        self.wrapper = praw.Reddit(
            client_id=credentials['client_id'],
            client_secret=credentials['client_secret'],
            refresh_token=credentials['refresh_token'],
            user_agent="get refresh token/v0 by u/{}".format(credentials['username'])
        )
        self.subreddit = subreddit

    def read(self):
        urls = []
        submissions = self.wrapper.subreddit(self.subreddit).top(time_filter="day")
        for submission in submissions:
            urls.append(submission.url)
        return urls
