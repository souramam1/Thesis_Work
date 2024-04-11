import machine
import time

# Importing machine module directly into namespace
from machine import Pin

class Slider:
    def __init__(self):
        self.pins = [Pin(i, Pin.IN, Pin.PULL_DOWN) for i in range(7)]

    def check_status(self):
        high_pins = [i for i, pin in enumerate(self.pins) if pin.value() == 1]
        if high_pins:
            print("High pins:", high_pins)
        else:
            print("No pins are currently high.")

if __name__ == "__main__":
    slider = Slider()
    while True:
        slider.check_status()
        time.sleep(1)