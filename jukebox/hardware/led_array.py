import Adafruit_GPIO as GPIO


class LedArray:

    led_pins = (0, 1, 2, 3, 4, 5, 6, 7)

    def __init__(self, mcp):
        self._mcp = mcp
        self._setup_mcp()
        self.reset()

    def reset(self):
        for led_pin in self.led_pins:
            self._mcp.output(led_pin, False)

    def set(self, index, state):
        self._mcp.output(self.led_pins[index], state)

    def _setup_mcp(self):
        for pin in self.led_pins:
            self._mcp.setup(pin, GPIO.OUT)
