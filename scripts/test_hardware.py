#!/usr/bin/env python3

from Adafruit_GPIO.MCP230xx import MCP23017
import Adafruit_GPIO as GPIO
import time

output_pins = (0, 1, 2, 3, 4, 5, 6, 7)
input_pins = (8, 9, 10, 11, 12, 13, 14, 15)

mcp = MCP23017(address=0x20)

# Set pin 3 to input with the pullup resistor enabled
# mcp.pullup(3, 1)
# Read pin 3 and display the results
# print "%d: %x" % (3, mcp.input(3) >> 3)

def wait_for_button_press(input_pin, timeout=5):
    start_time = time.monotonic()
    state = True
    print('press button %d now' % input_pin)
    while start_time + timeout > time.monotonic():
        time.sleep(.005)
        state = mcp.input(input_pin)
        if not state:
            print('OK')
            return
        # print('pin %d: %r' % (input_pin, state))
        # states = mcp.input_pins(input_pins)
        # print('%r' % states)

    print('timeout detecting button press on button %d' % input_pin)


def test_outputs():
    for output_pin in output_pins:
        print('flashing led %d' % output_pin)
        mcp.setup(output_pin, GPIO.OUT)
        mcp.output(output_pin, 1)
        time.sleep(.5)
        mcp.output(output_pin, 0)


def test_inputs():
    # for input_pin in input_pins:
    for input_pin in input_pins:
        mcp.setup(input_pin, GPIO.IN)
        mcp.pullup(input_pin, True)
        wait_for_button_press(input_pin)


if __name__ == '__main__':
    test_outputs()
    test_inputs()
