import os


class Cleaner:

    def __init__(self, path_prefix):
        self.path_prefix = path_prefix

    def batch(self, files):
        for file in files:
            self.remove(file)
        self._remove_dir()

    def remove(self, file):
        os.remove(file)

    def _remove_dir(self):
        # Remove files even if a upload fails, not the end of the world if we miss something
        os.removedirs(self.path_prefix)
