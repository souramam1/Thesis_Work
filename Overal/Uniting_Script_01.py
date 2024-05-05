#First overall assembly of consituent classes

from machine import Pin
import utime
import random
import machine
from Neopix_Flow_01 import NeoStrip
from Slider_First import Slider_And_Panels
from Button_01 import Button


class Model:
    
    button: Button
    neo: Neopixel
    slider: Slider_And_Panels
    
    def __init__(self):
        self.display_mode = 0
        self.button0 = Button(0)
        self.button1 = Button(1)
        self.button2 = Button(2)
        self.button3 = Button(3)
        self.neo = NeoStrip(135,22)
        self.slider = Slider_And_Panels(4,11)
        
    
    def building_lighting(self):
        #calling traces_iter with the adjusted building consitution that will be calculated here
        self.slider.production_score()
        trace_list = []
        for i in range(len(self.slider.buildings)):
            b_id = self.slider.buildings[i].bound_id
            print(b_id)
            num_green = self.slider.buildings[i].solar_score  # potentially can't return value from funciton and assign it at same time
            #print(num_green)
            trace = [6,0,0,2,0,num_green,b_id] # just 6 for now but will be 7 and 8 with the A and Y buildings too.
            trace_list.append(trace)
        self.neo.iter_traces(trace_list)
        
            
            
    
    def trace_lighting(self):
        pass
        # calling traces_iter withe the adjusted trace inputs that will be calced here
    
    def inst_pros_score(self):
        #instantaneous prosumption score this will calculate how much solar energy each building is using and the speed of its consumption as well as adjusting if it is giving energy to others
        #after this function the traces to show energy to other buildings will show.
        pass
        
        
        
        
        
        
if __name__ == "__main__":
    hammarby = Model()
#         tr_choice = trace_obj[0]
#         tr_colour = trace_obj[1]
#         tr_speed = trace_obj[2]
#         tr_dir = trace_obj[3]
#         tr_num_on = trace_obj[4]
#         tr_green_frac = trace_obj[5] --> this will be the solar score from the slider object from the adc object within
#         tr_bd_ix = trace_obj[6] --> this will also be from the adc object within the slider object
        

    while True:
        hammarby.slider.check_status()
        hammarby.slider.consumption_score()
        hammarby.slider.sun_score()
        hammarby.slider.production_score()
        print(hammarby.slider.sli_cons_score)
        hammarby.building_lighting()
        #curr_list = [[5,0,hammarby.slider.sli_cons_score-1,0,4,0,0],[6,0,0,2,0,100,8]]
        #hammarby.neo.iter_traces(curr_list)
        utime.sleep(0.001)

    
        
