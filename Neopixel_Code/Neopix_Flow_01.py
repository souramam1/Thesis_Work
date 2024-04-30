from neopixel import Neopixel
import utime

class NeoPixel:
    
    def __init__(self, num, data_pin):
        
        self.numpix = num
        self.strip = Neopixel(self.numpix, 0, data_pin, "RGB")

        self.delay = 0.008
        self.strip.brightness(42)
        self.blank = (0,0,0)
        
        self.green = (200, 40, 20)
        self.orange = (80, 255, 0)
        self.yellow = (150,200, 0)
        self.red = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.indigo = (0, 75, 130)
        self.violet = (0, 200, 100)
        self.colors_rgb = [self.red, self.orange, self.yellow, self.green, self.blue, self.indigo, self.violet]
#         self.trace_1_ix = 3
#         self.trace_2_ix = 11
        self.traces_end_index = [27,38,59,72,79,103]
        self.traces_to_show =  []
        self.set_delay = [0.004,0.008,0.012,0.016,0.020,0.024]
    
    
    
        
    
    
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
        
        if tr_choice == 0 :
            flow_init = 0
        else:
            flow_init = self.traces_end_index[tr_choice-1]
            
        if tr_dir == 0:
            self.l_to_r(flow_init,tr_choice,tr_colour,tr_speed)
        elif tr_dir == 1:
            self.r_to_l(flow_init,tr_choice,tr_colour,tr_speed)
        else:
            raise ValueError(f"The value for direction is invalid at : {tr_dir}") 
          
        
        
         
    def l_to_r(self,fl_init,tr_num, tr_col, tr_del):

        for x in range(fl_init,self.traces_end_index[tr_num]-2):
            self.strip.set_pixel(x+1,self.colors_rgb[tr_col])
            self.strip.show()
            utime.sleep(self.set_delay[tr_del])
            self.strip.set_pixel(x, self.colors_rgb[tr_col])
            self.strip.show()
            utime.sleep(self.set_delay[tr_del])
            self.strip.set_pixel(x+2, self.colors_rgb[tr_col])
            self.strip.show()
            utime.sleep(self.set_delay[tr_del])
            self.strip.set_pixel(x, self.blank)
            utime.sleep(self.set_delay[tr_del])
            self.strip.set_pixel(x+1, self.blank)
            utime.sleep(self.set_delay[tr_del])
            self.strip.set_pixel(x+2, self.blank)
            self.strip.show()
            
    def r_to_l(self,fl_init,tr_num, tr_col, tr_del):
        
        for x in reversed(range(fl_init,self.traces_end_index[tr_num]-2)):
            self.strip.set_pixel(x+1,self.colors_rgb[tr_col])
            self.strip.show()
            utime.sleep(self.set_delay[tr_del])
            self.strip.set_pixel(x, self.colors_rgb[tr_col])
            self.strip.show()
            utime.sleep(self.set_delay[tr_del])
            self.strip.set_pixel(x+2, self.colors_rgb[tr_col])
            self.strip.show()
            utime.sleep(self.set_delay[tr_del])
            self.strip.set_pixel(x, self.blank)
            utime.sleep(self.set_delay[tr_del])
            self.strip.set_pixel(x+1, self.blank)
            utime.sleep(self.set_delay[tr_del])
            self.strip.set_pixel(x+2, self.blank)
            self.strip.show()
            
    #def pulse_l_r(self):
        
               
        
if __name__ == "__main__":
    my_pix_1 = NeoPixel(103,22)
    #b = NeoPixel(7,21)
    

    while True:
        my_pix_1.strip.show()
        #b.strip.show()
        utime.sleep(0.5)
        trace_1 = [0,3,1,1]
        trace_2 = [1,0,5,0]
        curr_list = [trace_1,trace_2]
        my_pix_1.iter_traces(curr_list)

        
          
