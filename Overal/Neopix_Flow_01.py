from neopixel import Neopixel
import utime

class NeoStrip:
    
    def __init__(self, num, data_pin):
        
        self.numpix = num
        self.strip = Neopixel(self.numpix, 0, data_pin, "RGB")
        self.total = num
        self.delay = 0.008
        self.strip.brightness(42)
        self.blank = (0,0,0)
        self.green = (255, 0, 0)
        self.orange = (60, 255, 0)
        self.yellow = (100,210, 0)
        self.red = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.indigo = (0, 75, 130)
        self.magenta = (0, 200, 100)
        self.colors_rgb = [self.red, self.orange, self.yellow, self.green, self.blue, self.indigo, self.magenta]
        self.pro_col = [(0, 255, 0),(20, 255, 0),(40, 255, 0),(60, 255, 0),(80, 245, 0),(90, 230, 0),(100, 210, 0),(130, 190, 0),(160, 160, 0),(190, 100, 0),(200, 60, 0),(230, 30, 0),(255, 0, 0)]
        self.pro_val = 6 # ranges from -6 to +6 this is a value that will be calculated on the basis of the patches that are in operation and buttons pressed
        self.prev_pro_val = 0
        self.traces_end_index = [27,38,59,72,79,103,135,157,181,194]
        self.traces_to_show =  []
        self.set_delay = [0.035, 0.030, 0.028, 0.024, 0.020, 0.016, 0.012, 0.008, 0.004, 0.001]
        self.b_id_mapping = {4:24,6:32,8:32}
        
    
    
    
        
    
    
    def iter_traces(self,curr_trace_choice):
        for trace in curr_trace_choice:
            print(f"curr trace number is {trace[0]}")
            self.show_trace(trace)
            
            
            
        # the updated self.traces_to_show list will be sent here as curr_trace_choice
        # take tr_choice as list of lists in this  [trace_number,colour_index,speed_inxed,direction(0 or 1 0--> left, 1 --> right)]
        # because there can be several traces that want to be high at once
    def show_trace(self, trace_obj):
        tr_choice = trace_obj[0]
        tr_colour = trace_obj[1]
        tr_speed = trace_obj[2]
        tr_dir = trace_obj[3]
        tr_num_on = trace_obj[4]
        tr_green_frac = trace_obj[5]
        tr_bd_ix = trace_obj[6]
        
        
        if tr_choice == 0 :
            flow_init = 0
        else:
            flow_init = self.traces_end_index[tr_choice-1]
            
        if tr_dir == 0:
            self.l_to_r(flow_init,tr_choice,tr_colour,tr_speed,tr_num_on)
        elif tr_dir == 1:
            self.r_to_l(flow_init,tr_choice,tr_colour,tr_speed)
        elif tr_dir == 2:
             self.full_light(flow_init,tr_choice,tr_colour,tr_green_frac,tr_bd_ix)
        elif tr_dir == 3:
            self.show_prosumption()
        else:
            raise ValueError(f"The value for direction is invalid at : {tr_dir}") 
          
        
         
    def l_to_r(self,fl_init,tr_num, tr_col, tr_del,same_on):
        
        for x in range(fl_init,self.traces_end_index[tr_num]-(same_on-1)):
            for j in range(same_on):
                self.strip.set_pixel(x+j,self.colors_rgb[tr_col])
                self.strip.show()
                utime.sleep(self.set_delay[tr_del])
            for j in range(same_on):
                self.strip.set_pixel(x+j,self.blank)
                utime.sleep(self.set_delay[tr_del])
            self.strip.show()

    def r_to_l(self,fl_init,tr_num, tr_col, tr_del,same_on):
        same_on = 5
        for x in reversed(range(fl_init,self.traces_end_index[tr_num]-2)):
            for j in range(same_on):
                self.strip.set_pixel(x+j,self.colors_rgb[tr_col])
                self.strip.show()
                utime.sleep(self.set_delay[tr_del])
            for j in range(same_on):
                self.strip.set_pixel(x+j,self.blank)
                utime.sleep(self.set_delay[tr_del])
            self.strip.show()
            
    def full_light(self,fl_init,tr_num,tr_col,fraction_green,building_id):
        for i in range(fl_init,self.traces_end_index[tr_num]):
            #print("in full light")
            num_green = int(fraction_green/100*self.b_id_mapping[building_id]) #0.28 represents the maximum of solar production is around 28%
            print(num_green)
            max_green_ix = fl_init + num_green
            #print(f"the MAX Green number will be!")
            if i < max_green_ix:
                self.strip.set_pixel(i,self.green)
            else:
                self.strip.set_pixel(i, self.colors_rgb[tr_col])
                
            
        self.strip.show()
        
    def show_prosumption(self): # CHANGE THE BOUNDS OF THIS SO THAT IT CAN BE APPENDED TO THE WHOLE LED STRIP
        if self.pro_val < 0:
            for i in range(6-abs(self.pro_val),7):
                self.strip.set_pixel(i, self.pro_col[i])
        elif self.pro_val >= 0:
            for i in range(6,6+self.pro_val+1):
                self.strip.set_pixel(i, self.pro_col[i])
        else:
            pass
        self.strip.show()
        self.prev_pro_val = self.pro_val
            
        
                           
        
if __name__ == "__main__":
    my_pix_1 = NeoStrip(103,22)
    #b = NeoPixel(7,21)
    

    while True:
        my_pix_1.strip.show()
        utime.sleep(0.5)
        trace_1 = [0,0,0,0]
        trace_2 = [1,0,0,0]
        trace_3 = [2,0,0,0]
        trace_4 = [3,0,0,0]
        trace_5 = [4,0,0,0]
        trace_6 = [5,0,0,0]
        trace_7 = [6,]
        #WHAT NEEDS TO HAPPEN IS THAT THE LIST OF TRACES TO SHOW UPDATES AUTOMATICALLY WHEN THE SLIDER IS MOVED - AND THAT WE INTERRUPT WHAT IS CURRENTLY SHOWING WHEN THE BUTTON IS PRESSED TO SHOW THE UPDATED FLOW
#         trace_3 = [5,0,0,0]
        curr_list = [trace_1,trace_2]
        my_pix_1.iter_traces(curr_list)

        
          
