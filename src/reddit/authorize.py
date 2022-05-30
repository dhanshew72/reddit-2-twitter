import random
import praw
from utils.connection import receive


class Authorize:

    def __init__(self, client_id, client_secret, username):
        self.client_id = client_id
        self.client_secret = client_secret
        self.username = username
        self.client = self._get_client()

    def _get_client(self):
        client = praw.Reddit(
            client_id=self.client_id,
            client_secret=self.client_secret,
            redirect_uri='http://localhost:8080',
            user_agent="get refresh token/v0 by u/{}".format(self.username)
        )
        return client

    @staticmethod
    def _get_params():
        client = receive()
        data = client.recv(1024).decode('utf-8')
        tokens = data.split(' ', 2)[1].split('?', 1)[1].split('&')
        params = {
            key: value for (key, value) in [token.split('=') for token in tokens]
        }
        return params

    def get_refresh_token(self):
        url = self.client.auth.url(duration='permanent', scopes=['read'], state=str(random.randint(0, 65000)))
        print("Open this url in your browser to get refresh token: {url}".format(url=url))
        params = self._get_params()
        refresh_token = self.client.auth.authorize(params["code"])
        return refresh_token


if __name__ == '__main__':
    import sys
    token = Authorize(sys.argv[1], sys.argv[2], sys.argv[3]).get_refresh_token()
    print("Add this refresh token for all reddit calls: {token}".format(token=token))
