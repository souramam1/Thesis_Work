#First overall assembly of consituent classes

from machine import Pin
import utime
import random
import machine
from Neopix_Flow_01 import NeoStrip
from Slider_02 import Slider
from Button_02 import Button


class Model:
    
    button: Button
    neo: Neopixel
    slider: Slider
    
    def __init__(self):
        self.display_mode = 0
        self.button0 = Button(0,self.button0_pressed)
        self.button1 = Button(1,self.button1_pressed)
        self.button2 = Button(2,self.button0_pressed)
        self.button3 = Button(3,self.button0_pressed)
        self.button4 = Button(4,self.button0_pressed)

        self.neo = NeoStrip(204,22)
        self.status = 0 # --> there will be 6 of these 1,2,3,4,5,6 (0 is for when nothing is shown yet)
        self.slider = Slider(4,11)
        self.last_interrupt_time = 0
        self.debounce_delay = 1000  # Can be adjusted 
        
    
    def button0_pressed(self, pin):
        current_time = utime.ticks_ms()
        if current_time - self.last_interrupt_time > self.debounce_delay:
            print(f"BUTTON 0 PRESSED")
            if self.status < 7:
                self.status += 1
            else:
                self.status = 0
            print(self.status)
            
            self.last_interrupt_time = current_time
            
    def button1_pressed(self, pin):
        current_time = utime.ticks_ms()
        if current_time - self.last_interrupt_time > self.debounce_delay:
            print(f"BUTTON 1 PRESSED")
            self.last_interrupt_time = current_time
            
    def button2_pressed(self, pin):
        current_time = utime.ticks_ms()
        if current_time - self.last_interrupt_time > self.debounce_delay:
            print(f"BUTTON 2 PRESSED")
            self.last_interrupt_time = current_time
            
    def button3_pressed(self, pin):
        current_time = utime.ticks_ms()
        if current_time - self.last_interrupt_time > self.debounce_delay:
            print(f"BUTTON 3 PRESSED")
            self.last_interrupt_time = current_time
            
    def button4_pressed(self, pin):
        current_time = utime.ticks_ms()
        if current_time - self.last_interrupt_time > self.debounce_delay:
            print(f"BUTTON 4 PRESSED")
            self.last_interrupt_time = current_time


    def l_consuming(self):
        self.neo.strip.fill(self.neo.blank)
        if self.status == 1:
            self.neo.strip.fill(self.neo.blank)
            self.slider.consumption_score()
            self.neo.consumption_buildings([8])
            self.neo.show_trace([4,0,self.slider.sli_consum_score,0,3])
            
            
    def l_with_solar(self):
        
        # aim: the amount of green vs red in the building represents IN THAT TIME PERIOD what fraction of the
        # consumed energy is coming from the sun and what from the grid
        if self.status == 2:
            self.neo.strip.fill(self.neo.blank)
            self.slider.update_prosump()
            relative_prosump = self.slider.max_prosump - self.slider.curr_prosum
            fractional_prosump = relative_prosump/self.slider.prosumption_range
            proportion_green = fractional_prosump
            self.neo.solar_light([8],proportion_green)
            if prosumption_value < 0:
                prosumption_value = 0
            elif prosumption_value > 10:
                prosumption_value = 10
            else:
                #This means that if prosumption is negative we do not show a trace --> because that would mean we are depending not on the grid
                self.neo.show_trace([4,0,int(prosumption_value),0,3])
            
            
            

            print(f"slider prosumption is: {prosumption_value}")
            print(f"slider consumption score is : {self.slider.sli_consum_score}")
            print(f"slider sun score is : {self.slider.sli_sun_score}")
            
            
    def show_consumption_mode_all(self):
        if self.status == 3:
            self.neo.strip.fill(self.neo.blank)
            self.slider.consumption_score()
            print(f"slider consumption score is : {self.slider.sli_consum_score}")
            self.neo.consumption_buildings([4,6,8])
            self.neo.consumption_flow(0,self.slider.sli_consum_score,3)
            


    def l_sharing(self):
#         self.consum_score_table = {0:1,1:6,2:5,3:2,4:5,5:10,6:1}
#         self.sun_strength = {0:0,1:2,2:5,3:10,4:5,5:2,6:0}
#         
        
        # tr_choice = trace_obj[0]
#         tr_colour = trace_obj[1]
#         tr_speed = trace_obj[2]
#         tr_dir = trace_obj[3]
#         tr_num_on = trace_obj[4]
#         tr_green_frac = trace_obj[5] --> this will be the solar score from the slider object from the adc object within
#         tr_bd_ix = trace_obj[6] --> this will also be from the adc object within the slider object
        if self.status == 4:
            self.neo.strip.fill(self.neo.blank)
            #program this
            trace_list = []
            trace_1 = []
            trace_2 = []
            
            sefl.slider.update_prosump()
            if self.slider.curr_prosum < 0:
                trace_1 = [1,3,int(10/abs(prosumption_value)),1,3]
                trace_2 = [2,3,int(10/abs(prosumption_value)),0,3]
                trace_list.append(trace_1)
                trace_list.append(trace_2)
            elif self.slider.curr_prosum > 10:
                prosumption_value = 10
            relative_prosump = self.slider.max_prosump - self.slider.curr_prosum
            fractional_prosump = relative_prosump/self.slider.prosumption_range
            proportion_green = fractional_prosump
            self.neo.solar_light([8],proportion_green)
            self.neo.iter_traces(trace_list)
            self.neo.solar_light([4,6], 0.1)
            self.neo.consumption_flow(0,int(prosumption_value),3)
            
            
        
    def all_solar(self):
        if self.status == 5:
            self.neo.strip.fill(self.neo.blank)
            # program this
            pass

    
    def prosumption_slider(self):
        if self.status == 6:
            self.neo.strip.fill(self.neo.blank)
            # program this
            pass

        
    def activities(self):
        if self.status == 7:
            self.neo.strip.fill(self.neo.blank)
            #program this
            pass

        
        
    def reset(self):
        if self.status == 0:
            print("in status is 0")
#             for i in range(204):
#                 print("in for loop")
#                 #self.neo.strip.set_pixel(i, self.neo.blank)
            self.neo.strip.fill(self.neo.blank)
            self.neo.strip.show()
            
                
            
            

        
        
        
        
        
    
    def trace_lighting(self):
        pass
        # calling traces_iter withe the adjusted trace inputs that will be calced here
    
    def inst_pros_score(self):
        #instantaneous prosumption score this will calculate how much solar energy each building is using and the speed of its consumption as well as adjusting if it is giving energy to others
        #afterthis function the traces to show energy to other buildings will show.
        pass
        
        
    def main(self):
        hammarby.l_consuming()
        hammarby.show_consumption_mode_all()
        hammarby.l_with_solar()
        hammarby.l_sharing()
        hammarby.all_solar()
        hammarby.prosumption_slider()
        hammarby.reset()
        
        
        
        
        
        
        
        
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
        hammarby.main()
        #print(hammarby.status)


    
        
