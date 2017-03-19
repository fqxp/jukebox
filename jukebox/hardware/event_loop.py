import threading
import time


_running = False
_thread = None
_poll_functions = []
_interval = None


def start(interval=.01):
    global _interval, _thread
    _interval = interval
    _thread = threading.Thread(target=_loop)
    _thread.start()


def stop():
    global _running
    _running = False


def register_poll_func(poll_func):
    global _poll_functions
    _poll_functions.append(poll_func)


def _loop():
    global _interval, _running
    _running = True

    while _running:
        for poll_func in _poll_functions:
            poll_func()
        time.sleep(_interval)
