import shelve
from states import *
import parameters as p


class Save:
    def __init__(self):
        self.file = shelve.open('data')

    def save(self):
        self.file['usr_y'] = p.usr_y

    def add(self, name, value):
        self.file[name] = value

    def get(self, name):
        try:
            return self.file[name]
        except Exception:
            return 0

    def __del__(self):
        self.file.close()
