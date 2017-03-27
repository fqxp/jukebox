#! /usr/bin/env python
import Adafruit_GPIO as GPIO
import sys
import time

def test_pins(pins):
    print('testing pins %r' % pins)
    gpio = GPIO.get_platform_gpio()
    for pin in pins:
        gpio.setup(pin, GPIO.IN, GPIO.PUD_UP)

    i=0
    while True:
        results = [pin
                   for pin in pins
                   if gpio.input(pin) == 0]
        print('%04d: %r' % (i, results))
        time.sleep(.01)
        i += 1


if __name__ == '__main__':
    pins = list(int(arg) for arg in sys.argv[1:])
    test_pins(pins)
