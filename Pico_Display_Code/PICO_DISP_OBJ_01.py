# Testing making the DISPLAY CODE OOP TO CLEAN IT UP FOR Display 07.

import time
from pimoroni import Button
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY, PEN_P4
import random
import machine


class Display:
    
    def __init__(self):
        self.display = PicoGraphics(display=DISPLAY_PICO_DISPLAY, pen_type=PEN_P4, rotate=0)  #Create display object in horizontal orientation
        self.X_max = 240                    #Helpful variables that define the graphic bounds
        self.Y_max = 135
        
        self.display.set_backlight(1.0)             #set backlight to max so display is very bright
        self.display.set_font("bitmap8")            #easy to use and see font

        self.RED = self.display.create_pen(255,000,000)
        self.BLACK = self.display.create_pen(000,000,000)
        
    def clear(self):
        self.display.set_pen(self.BLACK)     #Assuming we want a black background
        self.display.clear()		       #Clears the screen setting it all to black - this is the pico graphics clear option
        self.display.update()
    
    
    def draw_polygon(self):
        self.display.set_pen(self.RED)
        self.display.polygon([(25,25),(60,45),(60,90),(25,110)])
        self.display.update()
        
        
if __name__ == "__main__":
    my_disp = Display()
    my_disp.clear()
    my_disp.draw_polygon()


        