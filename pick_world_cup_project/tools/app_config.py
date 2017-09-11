import os
import sys

class AppConfig(object):
    def __init__(self, section, config_file):
        self.section = section
        self.file = config_file

    def __getitem__(self, item):
        if sys.version_info >= (3, 0):
            from configparser import SafeConfigParser
            config = SafeConfigParser(os.environ)
        else:
            from ConfigParser import SafeConfigParser
            config = SafeConfigParser(os.environ)
        config.read(self.file)
        return config.get(self.section, item)
