import machine
from machine import Pin
import utime

class Button:
    def __init__(self, pin_num):
        self.pin_num = pin_num
        self.pin = Pin(pin_num, Pin.IN, Pin.PULL_DOWN)
        self.last_interrupt_time = 0
        self.debounce_delay = 1000  # Can be adjusted 
        
        # Configure interrupt
        self.pin.irq(trigger=Pin.IRQ_RISING, handler=self.button_pressed)

    def button_pressed(self, pin):
        current_time = utime.ticks_ms()
        if current_time - self.last_interrupt_time > self.debounce_delay:
            print(f"HEY {self.pin_num}")
            # Here call function that will change the value of the prosumption bar in accordance to THE SLIDER
            # And what patches are connected --> mega slay.
            
            
            #Reset the interrupt time so that it can restart the debounce timer.
            self.last_interrupt_time = current_time

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
        