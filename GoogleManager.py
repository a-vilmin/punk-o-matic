from zipfile import ZipFile
from gmusicapi import Musicmanager
from os import walk
from os.path import join


class GoogleManager():

    def __init__(self, directory):
        self.music_dir = directory

        self.Google = Musicmanager()
        self.Google.login()

    def upload(self):
        files = []
        for dirpath, dirnames, filenames in walk(self.music_dir):
            for name in filenames:
                if name.endswith('.mp3'):
                    files += [join(dirpath, name)]

        for f in files:
            ret = self.Google.upload(f)
            print(ret)

if __name__ == '__main__':
    test = GoogleManager("/home/vilmin2/Music/harm_done")
    test.upload()
