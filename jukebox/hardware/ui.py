from Adafruit_GPIO.MCP230xx import MCP23017
import Adafruit_GPIO as GPIO
from .button import Button
from .button_array import ButtonArray
from .led_array import LedArray
from .led import Led
from . import config
from . import event_loop
import signal


class HardwareUserInterface:

    def __init__(self, jukebox):
        self.jukebox = jukebox
        mcp = MCP23017(address=0x20)
        self.button_array = ButtonArray(
            mcp,
            self.on_playlist_button_released,
            config.PLAYLIST_BUTTON_PINS
        )
        self.led_array = LedArray(mcp, config.PLAYLIST_BUTTON_LED_PINS)

        gpio = GPIO.get_platform_gpio()
        self.play_button = Button(
            gpio,
            config.PLAY_BUTTON_PIN,
            self.on_play_button_released)
        self.forward_button = Button(
            gpio,
            config.FORWARD_BUTTON_PIN,
            self.on_forward_button_released)
        self.backward_button = Button(
            gpio,
            config.BACKWARD_BUTTON_PIN,
            self.on_backward_button_released)

        self.led = Led(gpio, config.LED_PIN)

    def mainloop(self):
        event_loop.start()
        self.led.on()
        signal.pause()

    def stop(self):
        event_loop.stop()
        self.led.off()
        self.led_array.reset()

    def on_playlist_button_released(self, index):
        self.jukebox.toggle_playlist(index)
        self._update_led(index)

    def on_play_button_released(self):
        self.jukebox.toggle_play_pause()

    def on_backward_button_released(self):
        self.jukebox.prev()

    def on_forward_button_released(self):
        self.jukebox.next()

    def _update_led(self, index):
        state = self.jukebox.is_playlist_enabled(index)
        self.led_array.set(index, state)
