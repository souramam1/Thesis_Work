import machine
import time

# Importing machine module directly into namespace
from machine import Pin
from ADC_01 import Solar_Panels

class Slider_And_Panels:
    
    def __init__(self,lower,upper):
        self.solar_a = Solar_Panels(28)
        self.solar_y = Solar_Panels(27)
        self.solar_l = Solar_Panels(26)
        self.buildings = [self.solar_a ,self.solar_y ,self.solar_l]
        self.solar_a_prod_score = 0
        self.solar_y_prod_score = 0
        self.solar_l_prod_score = 0
        self.solar__scores = [self.solar_a_prod_score,self.solar_y_prod_score,self.solar_l_prod_score]
        self.pins = [Pin(i, Pin.IN, Pin.PULL_DOWN) for i in range(lower,upper)]
        self.high_pins = []
        self.con_score_table = {0:1,1:6,2:5,3:2,4:5,5:10,6:1}
        self.sun_strength = {0:0,1:2,2:5,3:10,4:5,5:2,6:0}
        self.sli_cons_score = 0
        

    def check_status(self):
        self.high_pins = [i for i, pin in enumerate(self.pins) if pin.value() == 0]
        if self.high_pins:
            print("High pins:", self.high_pins)
        else:
            print("No pins are currently high.")
        
    def consumption_score(self):
        tally = 0
        for pin in self.high_pins:
            tally += self.con_score_table[pin]
        #print(f"score is {score}")
        if len(self.high_pins) == 0:
            pass
        else:
            self.sli_cons_score = int(tally/len(self.high_pins))
            print(self.sli_cons_score)
            #return score/len(self.high_pins)
                   
    def sun_score(self):
        tally = 0
        for pin in self.high_pins:
            tally += self.sun_strength[pin]
        #print(f"score is {score}")
        if len(self.high_pins) == 0:
            pass
        else:
            curr_sun_score = tally/len(self.high_pins)
            print(curr_sun_score)
            return curr_sun_score
            
        
    def production_score(self): #changes the solar score of each building based on the slider and the number of panels attached as a percentage
        for block in self.buildings:
            #block.solar_score = (block.solar_percentage())*(self.sun_score())/10 BYPASSING TO PRETEND ALL SP ARE ATTACHED --> solar_score is therefore a percentage
            block.solar_score = (self.sun_score())*10
            print(block.solar_score)
        
        
    
if __name__ == "__main__":
    slider = Slider_And_Panels(4,11)
    while True:
        slider.check_status()
        #slider.sun_score()
        slider.production_score()
        print(slider.solar_a.solar_score)
        time.sleep(1)