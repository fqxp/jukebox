#! /usr/bin/env python3

try:
    from jukebox.gtk.ui import GtkUserInterface
except ImportError:
    pass
from jukebox.hardware.ui import HardwareUserInterface
from jukebox.jukebox import Jukebox
import argparse


playlists = [
    'mamas',
    'laibach',
    'eels',
]

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description='Run jukebox')
    group = arg_parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        '--gtk',
        action='store_true',
        help='run Gtk user interface')
    group.add_argument(
        '--hardware',
        action='store_true',
        help='run hardware interface')
    arg_parser.add_argument(
        '--mpd-host',
        default='localhost',
        help='address of mpd server')
    arg_parser.add_argument(
        '--mpd-port',
        type=int,
        default=6600,
        help='port of mpd server')
    args = arg_parser.parse_args()

    jukebox = Jukebox(
        playlists=playlists,
        mpd_host=args.mpd_host,
        mpd_port=args.mpd_port)

    if args.gtk:
        jukebox_ui = GtkUserInterface(jukebox)
    elif args.hardware:
        jukebox_ui = HardwareUserInterface(jukebox)

    try:
        jukebox_ui.mainloop()
    except (KeyboardInterrupt, SystemExit):
        print('KEYBOARD INTERRUPT')
        jukebox_ui.stop()
