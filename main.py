from reddit.read import Reader
from twitter.write import Writer
from config import Config


def main():
    config = Config()
    posts = Reader(config.read('REDDIT'), "memes").read()
    Writer(config.read('TWITTER')).write()
    pass


if __name__ == '__main__':
    main()
