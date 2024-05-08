import machine
import time

# Importing machine module directly into namespace
from machine import Pin
from ADC_01 import Solar_Panels

class Slider:
    
    def __init__(self,lower,upper):
        self.pins = [Pin(i, Pin.IN, Pin.PULL_DOWN) for i in range(lower,upper)]
        self.high_pins = []
        #CHANGED
        self.consum_score_table = [1,6,5,2,6,10,1]
        #self.consum_score_table = {0:1,1:6,2:5,3:2,4:5,5:10,6:1}
        self.sun_strength = [0,2,5,10,5,2,0]
        self.prosumption_table = [None]*len(self.consum_score_table)
        #self.sun_strength = {0:0,1:2,2:5,3:10,4:5,5:2,6:0}
        for i in range(len(self.consum_score_table)):
            self.prosumption_table[i] = self.consum_score_table[i] - self.sun_strength[i]
        self.min_prosump = min(self.prosumption_table)
        self.max_prosump = max(self.prosumption_table)
        self.prosumption_range = self.max_prosump - self.min_prosump
        self.curr_prosump = 0
        self.sli_consum_score = 0
        self.sli_sun_score = 0
        

    def update_prosump(self):
        self.check_status()
        tally = 0
        for pin in self.high_pins:
            tally += self.prosumption_table[pin]
        if len(self.high_pins)== 0:
            pass
        else:
            self.curr_prosump = int(tally/len(self.high_pins))
            print(f"prosumption score is {self.curr_prosump}")
            
        
    
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
        slider.update_prosump()
#         print(f"slider prosumption table is: {slider.prosumption_table}")
#         print(f"lowest prosumptio is {slider.min_prosump}")
#         print(f"max prosump is {slider.max_prosump}")
#         print(f"prosump range is {slider.prosumption_range}")
        time.sleep(1)
        
