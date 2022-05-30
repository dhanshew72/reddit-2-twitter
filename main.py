from reddit.read import Reader
from config import Config


def main():
    posts = Reader(Config().read('REDDIT'), "memes").read()
    print("Submitting post to instagram: ", posts[1])
    pass


if __name__ == '__main__':
    main()
