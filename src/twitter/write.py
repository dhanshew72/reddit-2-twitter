import tweepy


class Writer:

    def __init__(self, credentials):
        self.wrapper = tweepy.API(tweepy.OAuth2BearerHandler(credentials['bearer_token']))
        pass

    def batch_write(self):
        pass

    def write(self):
        pass

    def _upload_image(self):
        self.wrapper.media_upload('')
        pass
