import machine
import time

# Importing machine module directly into namespace
from machine import Pin
from ADC_01 import Solar_Panels

class Slider:
    
    def __init__(self,lower,upper):
        self.pins = [Pin(i, Pin.IN, Pin.PULL_DOWN) for i in range(lower,upper)]
        self.high_pins = []
        self.consum_score_table = {0:1,1:6,2:5,3:2,4:5,5:10,6:1}
        self.sun_strength = {0:0,1:2,2:5,3:10,4:5,5:2,6:0}
        self.sli_consum_score = 0
        self.sli_sun_score = 0
        

    def check_status(self):
        self.high_pins = [i for i, pin in enumerate(self.pins) if pin.value() == 0]
        if self.high_pins:
            print("High pins:", self.high_pins)
        else:
            print("No pins are currently high.")
        
    def consumption_score(self):
        self.check_status()
        tally = 0
        for pin in self.high_pins:
            tally += self.consum_score_table[pin]
        #print(f"score is {score}")
        if len(self.high_pins) == 0:
            print("")
            pass
        else:
            self.sli_consum_score = int(tally/len(self.high_pins))
            print(f"consumption score is {self.sli_consum_score}")
            #return int(self.sli_consum_score)
            #return score/len(self.high_pins)
                   
    def sun_score(self):
        self.check_status()
        tally = 0
        for pin in self.high_pins:
            tally += self.sun_strength[pin]
        if len(self.high_pins) == 0:
            pass
        else:
            self.sli_sun_score = tally/len(self.high_pins)
            print(f"curr sun score = {self.sli_sun_score}")
            
            
   
if __name__ == "__main__":
    slider = Slider(4,11)
    while True:

        slider.consumption_score()
        slider.sun_score()
        time.sleep(1)
