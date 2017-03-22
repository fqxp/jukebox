import Adafruit_GPIO as GPIO
from . import event_loop


class ButtonArray:
    """ An array of buttons.
    """

    button_pins = (8, 9, 10, 11, 12, 13, 14, 15)

    def __init__(self, mcp, on_button_released=lambda: None):
        self._mcp = mcp
        self._setup_mcp()
        self._button_states = self._poll_button_states()
        self._on_button_released = on_button_released

    def poll(self):
        old_button_states = self._button_states
        self._button_states = self._poll_button_states()

        for index, pin_state in enumerate(self._button_states):
            if self._was_button_released(old_button_states[index], pin_state):
                self._on_button_released(index)

    def _poll_button_states(self):
        return self._mcp.input_pins(self.button_pins)

    def _was_button_released(self, old_state, new_state):
        return not old_state and new_state

    def _setup_mcp(self):
        for pin in self.button_pins:
            self._mcp.setup(pin, GPIO.IN)
            self._mcp.pullup(pin, True)
        event_loop.register_poll_func(self.poll)
