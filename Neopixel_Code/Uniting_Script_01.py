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
        self.button2 = Button(2,self.button2_pressed)
        self.button3 = Button(3,self.button3_pressed)
        

        self.neo = NeoStrip(204,22)
        self.status = 8 # --> there will be 6 of these 1,2,3,4,5,6 (0 is for when nothing is shown yet)
        self.slider = Slider(4,11)
        self.last_interrupt_time = 0
        self.debounce_delay = 1000  # Can be adjusted
        self.prosumption_to_add = -20
        self.times_added = 0
        
    
    def button0_pressed(self, pin):
        current_time = utime.ticks_ms()
        if current_time - self.last_interrupt_time > self.debounce_delay:
            print(f"BUTTON 0 PRESSED")
            if self.status < 8:
                self.status += 1
            else:
                self.status = 0
            print(self.status)
            
            self.last_interrupt_time = current_time
            
    def button1_pressed(self, pin):
        current_time = utime.ticks_ms()
        if current_time - self.last_interrupt_time > self.debounce_delay:
            if self.status == 8:
                # button 1 will be for the car --> WILMA
                print(f"BUTTON 1 PRESSED")
                self.last_interrupt_time = current_time
                car_hash_map = [1,4,-4,-6,0,6,5]
                self.translate_slider(car_hash_map)
                self.times_added += 1
                self.activities()
                
            
    def button2_pressed(self, pin):
        current_time = utime.ticks_ms()
        if current_time - self.last_interrupt_time > self.debounce_delay:
            if self.status == 8:
                print(f"BUTTON 2 PRESSED")
                self.last_interrupt_time = current_time
                # button 2 will be for the bath --> ELLEN
                bath_hash_map = [1,3,-2,-3,0,4,3]
                self.translate_slider(bath_hash_map)
                self.times_added += 1
                print(f"the value of prosumption to be added is {self.prosumption_to_add}")
                print(f"the value of prosumption times added is {self.prosumption_to_add}")
                self.activities()
            
    def button3_pressed(self, pin):
        current_time = utime.ticks_ms()
        if current_time - self.last_interrupt_time > self.debounce_delay:
            if self.status == 8:
                print(f"BUTTON 3 PRESSED")
                self.last_interrupt_time = current_time
                # button 3 will be for the tv --> OSCAR
                tv_hash_map = [-1,3,-1,-3,1,3,3]
                self.translate_slider(tv_hash_map)
                self.times_added += 1
                self.activities()
            

    def l_consuming(self):
        
        if self.status == 1:
            self.slider.consumption_score()
            self.neo.solar_light([8],self.slider.sli_consum_score/10,0)
            self.neo.show_trace([4,0,self.slider.sli_consum_score,0,6])
            
            
    def l_with_solar(self):
        
        # aim: the amount of green vs red in the building represents IN THAT TIME PERIOD what fraction of the
        # consumed energy is coming from the sun and what from the grid
        if self.status == 2:
            self.slider.update_prosump()
            self.slider.sun_score()
            self.slider.consumption_score()
            if self.slider.sli_sun_score == 0:
                print("in the sun is")
                fractional_prosump = 0
            else:
                relative_prosump = self.slider.max_prosump - self.slider.curr_prosump
                fractional_prosump = relative_prosump/self.slider.prosumption_range
            proportion_green = fractional_prosump
            a = self.slider.sli_consum_score/10
            print("the consumption proportion is {self.slider.sli_consum_score/10}")
            print("the green proportion is {proportion_green}")
            self.neo.solar_light([8],self.slider.sli_consum_score/10,proportion_green)
            if self.slider.curr_prosump <= 0:
                prosumption_value = 0
            elif self.slider.curr_prosump > 10:
                prosumption_value = 10
            else:
                prosumption_value = self.slider.curr_prosump
                #This means that if prosumption is negative we do not show a trace --> because that would mean we are depending not on the grid
                self.neo.show_trace([4,0,int(prosumption_value),0,3])
            
            print(f"slider prosumption is: {prosumption_value}")
            print(f"slider consumption score is : {self.slider.sli_consum_score}")
            print(f"slider sun score is : {self.slider.sli_sun_score}")
            
            
    def show_consumption_mode_all(self):
        if self.status == 3:
            self.slider.consumption_score()
            print(f"slider consumption score is : {self.slider.sli_consum_score}")
            self.neo.solar_light([4,6,8],self.slider.sli_consum_score/10,0)
            self.neo.consumption_flow(0,self.slider.sli_consum_score,3)
            


    def l_sharing(self):
      
# 		  tr_choice = trace_obj[0]
#         tr_colour = trace_obj[1]
#         tr_speed = trace_obj[2]
#         tr_dir = trace_obj[3]
#         tr_num_on = trace_obj[4]
#         tr_green_frac = trace_obj[5] --> this will be the solar score from the slider object from the adc object within
#         tr_bd_ix = trace_obj[6] --> this will also be from the adc object within the slider object

        if self.status == 4:
            #program this
            trace_list = []
            self.slider.update_prosump()
            self.slider.sun_score()
            self.slider.consumption_score()
            
            if self.slider.sli_sun_score == 0:
                print("in the sun is")
                fractional_prosump = 0
            else:
                relative_prosump = self.slider.max_prosump - self.slider.curr_prosump
                fractional_prosump = relative_prosump/self.slider.prosumption_range
            proportion_green = fractional_prosump
            self.neo.solar_light([8],self.slider.sli_consum_score/10,proportion_green)
            
            if fractional_prosump == 1:
                self.neo.solar_light([4,6],self.slider.sli_consum_score/10,0.1*proportion_green)
            else:
                print("FRACITONAL PROSUMP IS NOT 1")
                self.neo.solar_light([4,6],self.slider.sli_consum_score/10,0)
            
        
            if self.slider.curr_prosump <= 0:
                if self.slider.curr_prosump == 0:
                    self.slider.curr_prosump = 1
                b = int(10/abs(self.slider.curr_prosump))
                print(f"the value from the delay list that is being selected is {b}")
                prosumption_value = 10/abs(self.slider.curr_prosump)
                if fractional_prosump == 1:
                    trace_1 = [1,3,10 - int(10/abs(self.slider.curr_prosump)),1,3]
                    trace_2 = [2,3,10 - int(10/abs(self.slider.curr_prosump)),0,3]
                    trace_list.append(trace_1)
                    trace_list.append(trace_2)
                
                    
                trace_3 = [0,0,int(prosumption_value),0,3]
                trace_list.append(trace_3)
                self.neo.iter_traces(trace_list)
                trace_list = []   
            elif self.slider.curr_prosump > 10:
                prosumption_value = 10
            else:
                prosumption_value = self.slider.curr_prosump
                self.neo.consumption_flow(0,int(prosumption_value),3)

            
            
        
    def all_solar(self):
        if self.status == 5:
            #program this
            trace_list = []
            self.slider.update_prosump()
            self.slider.sun_score()
            self.slider.consumption_score()
            
            if self.slider.sli_sun_score == 0:
                print("in the sun is")
                fractional_prosump = 0
            else:
                relative_prosump = self.slider.max_prosump - self.slider.curr_prosump
                fractional_prosump = relative_prosump/self.slider.prosumption_range
            proportion_green = fractional_prosump
            self.neo.solar_light([8,4,6],self.slider.sli_consum_score/10,proportion_green+0.1*proportion_green)
            
        
            if self.slider.curr_prosump <= 0:
                if self.slider.curr_prosump == 0:
                    self.slider.curr_prosump = 1
                b = int(10/abs(self.slider.curr_prosump))
                print(f"the value from the delay list that is being selected is {b}")
                prosumption_value = 10/abs(self.slider.curr_prosump)
                if fractional_prosump == 1:
                    direction = random.randint(0,1)
                    trace_1 = [1,3,10 - int(10/abs(self.slider.curr_prosump)),direction,3]
                    direction = random.randint(0,1)
                    trace_2 = [2,3,10 - int(10/abs(self.slider.curr_prosump)),direction,3]
                    direction = random.randint(0,1)
                    trace_3 = [3,3,10 - int(10/abs(self.slider.curr_prosump)),direction,3]
                    trace_list.append(trace_1)
                    trace_list.append(trace_2)
                    trace_list.append(trace_3)
                    print(f"traces list is {trace_list}")
                    self.neo.iter_traces(trace_list)
                trace_list = []   
            elif self.slider.curr_prosump > 10:
                prosumption_value = 10
            else:
                prosumption_value = self.slider.curr_prosump
                self.neo.consumption_flow(0,int(prosumption_value),3)
            
        

    
    def prosumption_slider(self):
        if self.status == 6:
            self.neo.strip.fill(self.neo.blank)
            self.neo.strip.show()
            # program this
            for i in range(-6,7):
                self.neo.pro_val = i
                print(f"value of pro_val is {self.neo.pro_val}")
                self.neo.show_prosumption()
                utime.sleep(2)
                self.neo.strip.fill(self.neo.blank)
            pass

        
    def residents(self):
        if self.status == 7:
            wilma_slider = [0,4,0,0,0,10,0]
            oscar_slider = [4,0,0,5,0,6,6]
            ellen_slider = [0,3,2,2,0,6,1]
            persona_sliders = [wilma_slider,oscar_slider,ellen_slider]
            self.neo.strip.fill(self.neo.blank)
            wilma_led = 182
            oscar_led = 139
            ellen_led = 108
            persona_leds = [wilma_led,oscar_led,ellen_led]
            self.slider.check_status()
            self.slider.consumption_score()
            dweller_consumption = 0
            for i in range(len(persona_leds)):
                tally = 0
                for pin in self.slider.high_pins:
                    tally += persona_sliders[i][pin]
                #print(f"score is {score}")
                if len(self.slider.high_pins) == 0:
                    print("")
                    pass
                else:
                    dweller_consumption = int(tally/len(self.slider.high_pins))
                brightness = 255*dweller_consumption/10
                self.neo.strip.set_pixel(persona_leds[i],(0,brightness,0))
                
            #comment out this for loop to isolate red lights
            for i in range(103,191):
                if i not in persona_leds:
                    brightness_1 = 100*self.slider.sli_consum_score/10
                    brightness_2 = 210*self.slider.sli_consum_score/10
                    self.neo.strip.set_pixel(i,(brightness_1,brightness_2,0))
                    
 
            self.neo.strip.show()

            
            #program this
            pass
        
    def activities(self):
        if self.status == 8:
            self.neo.strip.fill(self.neo.blank)
            self.neo.strip.show()
            if self.prosumption_to_add != -20:
                if self.times_added <= 3:
                    print(f"in the self.times_added is less than 3 section")
                    self.neo.pro_val = int((self.neo.pro_val + self.prosumption_to_add)/self.times_added)
                    self.neo.show_prosumption()
                    self.neo.strip.show()
                else:
                    self.prosumption_to_add = -20
                    self.times_added = 0
                    self.neo.pro_val = 0
                    self.neo.show_prosumption()
                    self.neo.strip.show()
                
            
            #program this
            pass
        

   
    def reset(self):
        if self.status == 0:
            print("in status is 0")
            self.neo.strip.fill(self.neo.blank)
            self.neo.strip.show()
            
    def translate_slider(self,list):
        tally = 0
        self.slider.check_status()
        prosumption_to_add = 0
        for pin in self.slider.high_pins:
            tally += list[pin]
            #print(f"score is {score}")
        if len(self.slider.high_pins) == 0:
            print("")
            pass
        else:
            self.prosumption_to_add = int(tally/len(self.slider.high_pins))
            
            
            
        
        
        
    def main(self):
        hammarby.l_consuming()
        hammarby.show_consumption_mode_all()
        hammarby.l_with_solar()
        hammarby.l_sharing()
        hammarby.all_solar()
        hammarby.prosumption_slider()
        hammarby.residents()
        #hammarby.activities()
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


    
        
