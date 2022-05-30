from configparser import ConfigParser
import os


class Config:

    def __init__(self):
        self.filename = os.environ['CONFIG_FILE']
        self.parser = ConfigParser()
        self.parser.read(self.filename)

    def read(self, section):
        return self.parser[section]
