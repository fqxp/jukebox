#!/usr/bin/env python3

import Adafruit_GPIO as GPIO
import time

PINS = [18, 17, 27, 23, 24]
BUTTONS = {
    'play': 'PLAY_BUTTON_PIN',
    'backward': 'BACKWARD_BUTTON_PIN',
    'forward': 'FORWARD_BUTTON_PIN',
    'question': 'QUESTION_BUTTON_PIN',
}

gpio = GPIO.get_platform_gpio()


def setup():
    for pin in PINS:
        gpio.setup(pin, GPIO.IN, GPIO.PUD_UP)


def wait_until_no_button_is_pressed():
    while any(not gpio.input(pin) for pin in PINS):
        time.sleep(.005)


def find_button(name, timeout=5):
    wait_until_no_button_is_pressed()

    print('Press button %s' % name)

    start_time = time.monotonic()
    state = True
    while start_time + timeout > time.monotonic():
        time.sleep(.005)
        states = [not gpio.input(pin) for pin in PINS]
        if any(states):
            index = states.index(True)
            return PINS[index]

    print('timeout detecting button press')


def find_buttons():
    return dict(
        (config_var, find_button(name))
        for (name, config_var) in BUTTONS.items())


def print_config():
    mapping = find_buttons()
    for (config_var, pin) in mapping.items():
        print('%s = %d' % (config_var, pin))


if __name__ == '__main__':
    setup()
    print_config()
