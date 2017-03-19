from mpd import MPDClient


class Jukebox:

    def __init__(self, playlists, mpd_host, mpd_port=6600):
        self.playlists = playlists
        self.client = MPDClient()
        self.client.connect(mpd_host, mpd_port)

    def count_playlists(self):
        return len(self.playlists)

    def playlist_name(self, index):
        return self.playlists[index]

    def toggle_play_pause(self):
        if self.is_stopped():
            self.client.play(0)
        else:
            self.client.pause()

    def prev(self):
        self.client.previous()

    def next(self):
        self.client.next()

    def toggle_playlist(self, index):
        if self.is_playlist_enabled(index):
            self.disable_playlist(index)
        else:
            self.enable_playlist(index)

    def is_playlist_enabled(self, index):
        current_playlist = self.current_playlist()
        playlist = self.playlist_by_index(index)

        return all([
            song in current_playlist
            for song in playlist
        ])

    def enable_playlist(self, index):
        playlist = self.playlist_by_index(index)
        current_playlist = self.current_playlist()
        current_pos = self.current_playing_pos()

        songs_to_add = [
            song
            for song in playlist
            if song not in current_playlist
        ]

        for song in songs_to_add:
            self.client.add(song)

        self.client.shuffle('%d:' % current_pos)

    def disable_playlist(self, index):
        playlist = self.playlist_by_index(index)
        current_playlist = self.current_playlist()
        current_pos = self.current_playing_pos()

        songs_to_delete = [
            i
            for i, song in enumerate(current_playlist)
            if song in playlist and i > current_pos
        ]

        for i in reversed(songs_to_delete):
            self.client.delete(i)

    def playlist_by_index(self, index):
        playlist_name = self.playlists[index]
        return self.client.listplaylist(playlist_name)

    def is_stopped(self):
        status = self.client.status()
        return status.get('state') == 'stop'

    def is_playing(self):
        status = self.client.status()
        return status.get('state') == 'play'

    def current_playlist(self):
        return [info['file']
                for info in self.client.playlistinfo()]

    def current_playing_pos(self):
        status = self.client.status()
        return int(status.get('song', 0))
