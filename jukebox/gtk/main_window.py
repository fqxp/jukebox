from gi.repository import Gtk


class MainWindow(Gtk.Window):

    ENABLED_TEXT = '<span foreground="green">Enabled</span>'
    DISABLED_TEXT = '<span foreground="red">Disabled</span>'

    def __init__(self, jukebox):
        Gtk.Window.__init__(self, title='Jukebox')
        self.jukebox = jukebox
        self._create_labels()
        self._create_buttons()
        self._create_playback_buttons()
        self._create_layout()

    def update_label_text(self, index):
        text = self.ENABLED_TEXT if self.jukebox.is_playlist_enabled(index) else self.DISABLED_TEXT
        self.labels[index].set_markup(text)

    def update_play_pause_button_text(self):
        text = 'Pause' if self.jukebox.is_playing() else 'Play'
        self.play_pause_button.set_label(text)

    def toggle_playlist(self, button):
        index = self.buttons.index(button)
        self.jukebox.toggle_playlist(index)
        self.update_label_text(index)

    def play_pause(self, button):
        self.jukebox.toggle_play_pause()
        self.update_play_pause_button_text()

    def prev_song(self, button):
        self.jukebox.prev()
        self.update_play_pause_button_text()

    def next_song(self, button):
        self.jukebox.next()
        self.update_play_pause_button_text()

    def _create_labels(self):
        self.labels = []

        for i in range(self.jukebox.count_playlists()):
            label = Gtk.Label()
            self.labels.append(label)
            self.update_label_text(i)

    def _create_buttons(self):
        self.buttons = []

        for i in range(self.jukebox.count_playlists()):
            button = Gtk.Button(label='%s' % self.jukebox.playlist_name(i))
            button.connect('clicked', self.toggle_playlist)
            self.buttons.append(button)

    def _create_playback_buttons(self):
        self.play_pause_button = Gtk.Button(stock=Gtk.STOCK_MEDIA_PLAY)
        self.play_pause_button.connect('clicked', self.play_pause)
        self.update_play_pause_button_text()
        self.prev_button = Gtk.Button(label='<<')
        self.prev_button.connect('clicked', self.prev_song)
        self.next_button = Gtk.Button(label='>>')
        self.next_button.connect('clicked', self.next_song)

    def _create_layout(self):
        grid_layout = Gtk.Grid()
        self.add(grid_layout)

        for i in range(len(self.labels)):
            label = self.labels[i]
            grid_layout.attach(label, i, 0, 1, 1)

        for i in range(len(self.buttons)):
            button = self.buttons[i]
            grid_layout.attach(button, i, 1, 1, 1)

        grid_layout.attach(self.play_pause_button, 0, 2, 2, 1)
        grid_layout.attach(self.prev_button, 2, 2, 1, 1)
        grid_layout.attach(self.next_button, 3, 2, 1, 1)
