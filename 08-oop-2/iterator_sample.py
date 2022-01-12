import random


class PlayListIterator:
    def __init__(self, playlist):
        self.playlist = playlist
        self.index = 0
        self.repeat = self.playlist.repeat

        self.items = len(self.playlist.songs)
        self.indexes = list(range(self.items))

        if self.playlist.random:
            random.shuffle(self.indexes)

    def _check_position(self):
        if self.index >= self.items:
            if self.repeat:
                self.index = 0
            else:
                raise StopIteration()

    def next(self):
        self._check_position()

        value = self.playlist.songs[self.indexes[self.index]]
        self.index += 1
        return value


class Playlist:
    def __init__(self, songs):
        self.songs = songs
        self.repeat = False
        self.random = False

    def __iter__(self):
        return PlayListIterator(self)



c = Playlist(['a', 'b', 'c', 'd'])
c.repeat = False
c.random = False

print("Songs by order no repeat")
for song in c:
    print song


print("\n10 Songs by order with repeat")
c.repeat = True
for index, song in enumerate(c, start=1):
    print song
    if index >= 10:
        break

c.random = True
c.repeat = False

print("\nSongs by random no repeat")
for song in c:
    print song


print("\n10 Songs by random with repeat")
c.repeat = True

for index, song in enumerate(c, start=1):
    print song
    if index >= 10:
        break
