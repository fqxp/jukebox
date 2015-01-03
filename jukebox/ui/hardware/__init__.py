from mcp230xx import MCP230xx
import time


class UI(object):

    def __init__(self, jukebox):
        self.hardware_interface = HardwareInterface(jukebox)

    def run(self):
        self.hardware_interface.main()


class HardwareInterface(object):

    def __init__(self, jukebox):
        self.jukebox = jukebox
        self.mcp = self._setup_mcp()
        self.current_pin_state = self.mcp.input_state()

    def main(self):
        try:
            self._loop()
        except KeyboardInterrupt:
            self.cleanup()

    def toggle_playlist(self, index):
        self.update_led(index)
        self.jukebox.toggle_playlist(index)

    def update_led(self, index):
        value = 1 if self.jukebox.is_playlist_enabled(index) else 0
        self.mcp.output(index, value)

    def _loop(self):
        while True:
            pin_state = self.mcp.input_state()
            if pin_state != self.current_pin_state:
                self._trigger_events(pin_state)
                self.current_pin_state = pin_state
            time.sleep(.01)

    def _trigger_events(self, new_pin_state):
        changed_pins = self.current_pin_state ^ new_pin_state
        for pin in range(8, 16):
            if changed_pins & (1 << pin) & new_pin_state:
                self.toggle_playlist(pin - 8)

    def _setup_mcp(self):
        mcp = MCP230xx(busnum=1, address=0x20, num_gpios=16)

        for pin in range(0, 8):
            mcp.config(pin, mcp.OUTPUT)
        for pin in range(8, 16):
            mcp.pullup(pin, 1)

        return mcp

    def cleanup(self):
        self.mcp.cleanup()



