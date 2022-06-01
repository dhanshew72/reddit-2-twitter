import tweepy


class Writer:

    def __init__(self, credentials):
        auth = tweepy.OAuthHandler(credentials['api_key'], credentials['api_key_secret'])
        auth.set_access_token(credentials['access_token'], credentials['access_token_secret'])
        self.wrapper = tweepy.API(auth)
        self.caption = "Follow @boredcovidsurv1 (this page) for more memes #memes #dailymemes #funny #funny #memes #memepage" # noqa

    def batch(self, files):
        for file in files:
            try:
                self.write(file)
            except Exception as ex:
                print('Error uploading to twitter: ', ex)

    def write(self, file):
        self.wrapper.update_status_with_media(self.caption, file)
