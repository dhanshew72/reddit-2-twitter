import os
import requests


class Downloader:

    def __init__(self, path_prefix):
        self.path_prefix = path_prefix
        self._create_image_path(self.path_prefix)

    def batch(self, urls):
        paths = []
        for url in urls:
            path = self.download(url)
            paths.append(path)
        return paths

    def download(self, url):
        response = requests.get(url)
        filename = self._get_file_name(url)
        path = self.path_prefix + filename
        open(path, "wb").write(response.content)
        return path

    def _create_image_path(self, prefix):
        if not os.path.exists(prefix):
            os.makedirs(prefix)

    def _get_file_name(self, url):
        return url.split('/')[-1]
