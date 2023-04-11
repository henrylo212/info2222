'''
This module handles loading various configuration constants from a
`server_conf.json` file.
'''

from collections import UserDict
import json


class Config(UserDict):
    '''
    A dictionary that can load itself from a config file.
    '''
    file_path: str
    _loaded: bool

    def __init__(self, file_path, *args):
        super().__init__(*args)
        self.file_path = file_path
        self._loaded = False

    def __setitem__(self, key, item):
        raise RuntimeError("Config structure is read-only")

    def __getitem__(self, key):
        self._check_loaded()
        return super().__getitem__(key)

    def _check_loaded(self):
        if not self._loaded:
            # Load the config file
            with open(self.file_path, "r", encoding="utf-8") as file:
                for key, value in json.load(file).items():
                    super().__setitem__(key, value)

            self._loaded = True


# The path to the config file
CONFIG_FILE_PATH = "server_conf.json"
CONFIG = Config(CONFIG_FILE_PATH)
