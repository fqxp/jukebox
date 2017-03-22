import mpd


def reconnecting(method):
    def reconnecting(self, *args, **kwargs):
        try:
            return method(self, *args, **kwargs)
        except mpd.ConnectionError:
            print('connection lost - reconnecting')
            self.client.connect(self._host, self._port)
            return method(self, *args, **kwargs)
    return reconnecting


class SafeMPDClient:
    def __init__(self):
        self.client = mpd.MPDClient()

    def connect(self, host, port):
        self._host = host
        self._port = port
        self.client.connect(self._host, self._port)

    @reconnecting
    def play(self, songpos):
        self.client.play(songpos)

    @reconnecting
    def pause(self):
        self.client.pause()

    @reconnecting
    def next(self):
        self.client.next()

    @reconnecting
    def previous(self):
        self.client.previous()

    @reconnecting
    def add(self, song):
        self.client.add(song)

    @reconnecting
    def shuffle(self, pos):
        self.client.shuffle(pos)

    @reconnecting
    def listplaylist(self, playlist_name):
        return self.client.listplaylist(playlist_name)

    @reconnecting
    def playlistinfo(self):
        return self.client.playlistinfo()

    @reconnecting
    def status(self):
        return self.client.status()

    @reconnecting
    def delete(self, pos):
        self.client.delete(pos)
