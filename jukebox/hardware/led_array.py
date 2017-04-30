import Adafruit_GPIO as GPIO


class LedArray:

    def __init__(self, mcp, pins):
        self._mcp = mcp
        self._pins = pins
        self._setup_mcp()
        self.reset()

    def reset(self):
        for led_pin in self._pins:
            self._mcp.output(led_pin, False)

    def set(self, index, state):
        self._mcp.output(self._pins[index], state)

    def _setup_mcp(self):
        for pin in self._pins:
            self._mcp.setup(pin, GPIO.OUT)
