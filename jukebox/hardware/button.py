import Adafruit_GPIO as GPIO
from . import event_loop


class Button:

    def __init__(self, gpio, pin, on_button_released=lambda: None):
        self._gpio = gpio
        self._pin = pin
        self._on_button_released = on_button_released
        self._setup()
        self._button_state = self._poll_button_state()

    def poll(self):
        old_button_state = self._button_state
        self._button_state = self._poll_button_state()

        if self._was_button_released(old_button_state, self._button_state):
            self._on_button_released()

    def _poll_button_state(self):
        return self._gpio.input(self._pin)

    def _was_button_released(self, old_state, new_state):
        return not old_state and new_state

    def _setup(self):
        self._gpio.setup(self._pin, GPIO.IN, GPIO.PUD_UP)
        event_loop.register_poll_func(self.poll)
