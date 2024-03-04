from pimoroni import Button                      #Need this if using pimoroni buttons
from picographics import PicoGraphics            #Universal graphics library - part of the UF2 file
from picographics import DISPLAY_PICO_DISPLAY    #Class for this model display
from picographics import PEN_P4                  #Class for the "color depth" we want

display = PicoGraphics(display=DISPLAY_PICO_DISPLAY, pen_type=PEN_P4, rotate=0)  #Create display object in horizontal orientation
X_max = 240                    #Helpful variables that define the graphic bounds
Y_max = 135

#-------------------------------------------------------------------------------------------------

display.set_backlight(1.0)             #set backlight to max so display is very bright
display.set_font("bitmap8")            #easy to use and see font

RED = display.create_pen(255,000,000)    #Define some colors to use(R,G,B)
GREEN = display.create_pen(000,255,000)
BLUE = display.create_pen(000,000,255)
WHITE = display.create_pen(255,255,255)
BLACK = display.create_pen(0,0,0)

def clear():                   #Function called to clear the screen
    display.set_pen(BLACK)     #Assuming we want a black background
    display.clear()		       #Clears the screen setting it all to black - this is the pico graphics clear option
    display.update()           #Performs the actual screen update --> when we tell the display to do something, it goes into buffer, then when call update, contents of buffer on screen
    
#-------------------------------------------------------------------------------------------------
    
clear()

display.set_pen(RED)
#display.pixel(10,10)    #for plotting a pixel
#display.pixel_span(5,5,50) #projects line in the direction of the orientation from a defined starting point
#display.line(0,135,240,0) # line from p1 to p2 defined by x and y coords
#display.rectangle(20,20,200,95) # x, y, distance_y, distance_x
#display.circle(120,67,50) #x, y , radius of 50
#display.triangle(120,17,163,92,77,92)
display.polygon([(25,25),(60,45),(60,90),(25,110)])
display.update()   