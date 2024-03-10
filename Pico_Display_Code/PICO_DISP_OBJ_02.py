# Testing making the DISPLAY CODE OOP TO CLEAN IT UP FOR Display 07.
# Display functions of DISP07 but OOP (i.e this does not include potentiometer functions etc.
import time
from pimoroni import Button
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY, PEN_P4
import random
import machine


class Display:
    
    def __init__(self):
    
        self.display = PicoGraphics(display=DISPLAY_PICO_DISPLAY, pen_type=PEN_P4, rotate=270) #270 means vertical display
        self.X_max = 134
        self.Y_max = 239
        self.X_Bar_Width = 40 #set weidth for the bars - smaller = faster
        self.X1_Bar_Start = round(((self.X_max / 4) - (self.X_Bar_Width / 2))) # find start point so bar is centred
        self.X2_Bar_Start = round(((3*(self.X_max / 4)) - (self.X_Bar_Width / 2))) # find start point so bar is centred
        # INITIALISE THE DISPLAY
        self.display.set_backlight(1.0)
        self.display.set_font("bitmap8")
        # DEFINE bar graph segment colors
        self.BLACK = self.display.create_pen(0,0,0)
        self.txt_clr = self.display.create_pen(255,255,255)  #white
        self.RED = self.display.create_pen(255,000,000)
        self.GREEN = self.display.create_pen(000,255,000)
        #DELAYS
        self.delay = 3

    
    def clear(self):
        self.display.set_pen(self.BLACK)     #Assuming we want a black background
        self.display.clear()		       #Clears the screen setting it all to black - this is the pico graphics clear option
        self.display.update()
        
        
        
    def animate_graph(self,bar,level):
        seg_num = 20
        B_height = int(200/seg_num)
        if(bar==1):
            self.display.set_pen(self.BLACK)             # Erase the text at the top
            self.display.rectangle(0,0,self.X_max,30)    
        
        
        
        if (bar==1):
            self.display.set_pen(self.RED)
            level_s = str(level) + "kWh"             # making the level a string so it can be printed
            self.display.text(level_s, 5,0, 135, 2.5) #display the value 1 through 10 at that location and scale
        elif(bar==2):
            self.display.set_pen(self.GREEN)
            level_s = str(level) + "kWh"             # making the level a string so it can be printed
            self.display.text(level_s, 70, 0, 135, 2.5) #display the value 1 through 10 at that location and scale
        else:
            pass
                                               #Each segment of the Bar chart has height 2
        Y_POS = self.Y_max - B_height           #Y_position base point is the 
        for b in range(0,seg_num):
            if (b <= level):
                if(bar == 1):
                    self.display.set_pen(self.RED)
                elif(bar==2):
                    self.display.set_pen(self.GREEN)       
            else:
                self.display.set_pen(self.BLACK)
                
      
            if(bar==1):
                self.display.rectangle(self.X1_Bar_Start, Y_POS,self.X_Bar_Width,B_height)
                self.display.update()
                Y_POS -= B_height
            elif(bar==2):
                self.display.rectangle(self.X2_Bar_Start, Y_POS,self.X_Bar_Width,B_height)
                self.display.update()
                Y_POS -= B_height
            else:
                pass
            
            
    def show_level(self,bar,val):
        seg_num = 20
        if(bar==1):
            a = 11
        else:
            a = round((val-0.3)/2*20)
        self.animate_graph(bar,a)
        print(a)
            
    

        
        
if __name__ == "__main__":
    my_disp = Display()
    my_disp.clear()
    my_disp.show_level(1,11)                   
    my_disp.show_level(2,1)


        
