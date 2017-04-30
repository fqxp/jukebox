import Adafruit_GPIO as GPIO


class Led:

    def __init__(self,  gpio, pin):
        self._gpio = gpio
        self._pin = pin
        gpio.setup(self._pin, GPIO.OUT)

    def on(self):
        self._gpio.output(self._pin, GPIO.HIGH)

    def off(self):
        self._gpio.output(self._pin, GPIO.LOW)
