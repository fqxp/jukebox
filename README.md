jukebox
=======

A hardware-controlled simple jukebox for Raspberry Pi

## Setup
Create a virtual environment and activate it:

    $ virtualenv --system-site-packages venv
    $ . venv/bin/activate

Install required software:

    $ sudo aptitude install mpd
    $ pip install -r requirements.txt

Run jukebox:

    python main.py
