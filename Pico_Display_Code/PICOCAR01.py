from machine import Pin
import time


button = Pin(22, Pin.IN, Pin.PULL_DOWN)

while True:
    print(button.value())
    time.sleep(1)
