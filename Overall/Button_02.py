import machine
from machine import Pin
import utime

class Button:
    def __init__(self, pin_num,handler_func):
        self.pin_num = pin_num
        self.pin = Pin(pin_num, Pin.IN, Pin.PULL_DOWN)

        
        # Configure interrupt
        self.pin.irq(trigger=Pin.IRQ_RISING, handler=handler_func)

    

def main():
    button_0 = Button(0)
    button_1 = Button(1)
    button_2 = Button(2)
    button_3 = Button(3)
    #print(f"button value is currently {button.pin.value()}")

if __name__ == "__main__":
    while True:
        main()
        utime.sleep(1)
        
