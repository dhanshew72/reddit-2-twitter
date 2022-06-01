from images.download import Downloader
from images.clean import Cleaner
from reddit.read import Reader
from twitter.write import Writer
from config import Config


def main():
    config = Config()
    path_prefix = config.read('DOWNLOADER')['path_prefix']
    posts = Reader(config.read('REDDIT'), "memes").read()
    files = Downloader(path_prefix).batch(filter_gifs(posts))
    Writer(config.read('TWITTER')).batch(files)
    Cleaner(path_prefix).batch(files)


def filter_gifs(posts):
    jpegs = []
    # Only grabbing top 3 jpg posts for now otherwise just all jpg posts,
    # if anything more comes up I'll separate this out into a module for filtering
    for post in posts:
        if post.split('.')[-1] == 'jpg':
            jpegs.append(post)
        if len(jpegs) >= 3:
            break
    return jpegs


if __name__ == '__main__':
    main()
