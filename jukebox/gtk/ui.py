import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from .main_window import MainWindow


class GtkUserInterface(object):

    def __init__(self, jukebox):
        self.window = MainWindow(jukebox)
        self.window.connect('delete-event', Gtk.main_quit)
        self.window.show_all()

    def mainloop(self):
        Gtk.main()

    def stop(self):
        Gtk.main_quit()
