from Adafruit_GPIO.MCP230xx import MCP23017
from .button_array import ButtonArray
from .led_array import LedArray
from . import event_loop
import signal


class HardwareUserInterface:

    def __init__(self, jukebox):
        self.jukebox = jukebox
        mcp = MCP23017(address=0x20)
        self.button_array = ButtonArray(mcp, self.on_playlist_button_released)
        event_loop.register_poll_func(self.button_array.poll)
        self.led_array = LedArray(mcp)

    def mainloop(self):
        event_loop.start()
        signal.pause()

    def stop(self):
        event_loop.stop()

    def on_playlist_button_released(self, index):
        self.jukebox.toggle_playlist(index)
        self._update_led(index)

    def _update_led(self, index):
        state = self.jukebox.is_playlist_enabled(index)
        self.led_array.set(index, state)
