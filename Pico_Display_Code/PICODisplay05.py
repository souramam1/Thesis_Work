import time
from pimoroni import Button
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY, PEN_P4
import random

# Configure PICO Display, create variables needed for displaying bar graph
# Since only using a few colors, we can use a 4 bit/16 colour palette.

display = PicoGraphics(display=DISPLAY_PICO_DISPLAY, pen_type=PEN_P4, rotate=270) #270 means vertical display
X_max = 134
Y_max = 239
X_Bar_Width = 40 #set weidth for the bars - smaller = faster
X1_Bar_Start = round(((X_max / 4) - (X_Bar_Width / 2))) # find start point so bar is centred
X2_Bar_Start = round(((3*(X_max / 4)) - (X_Bar_Width / 2))) # find start point so bar is centred

display.set_backlight(1.0)
display.set_font("bitmap8")

# DEFINE bar graph segment colors
BLACK = display.create_pen(0,0,0)
txt_clr = display.create_pen(255,255,255)  #white
b_colour = []
b_colour.append(display.create_pen(255,255,255)) #white
b_colour.append(display.create_pen(210,210,210)) #grey
b_colour.append(display.create_pen(000,255,255)) #cyan
b_colour.append(display.create_pen(000,200,200)) #cyan
b_colour.append(display.create_pen(100,100,255)) #blue
b_colour.append(display.create_pen(000,000,255)) #blue
b_colour.append(display.create_pen(155,155,000)) #yellow
b_colour.append(display.create_pen(255,255,000)) #yellow
b_colour.append(display.create_pen(255,255,255)) #white
b_colour.append(display.create_pen(255,125,255)) #orange
b_colour.append(display.create_pen(255,000,000)) #white

delay = 3

#-------------------------------- FUNCTIONS ---------------------------------------------------

def clear():                   #Function called to clear the screen
    display.set_pen(BLACK)     #Assuming we want a black background
    display.clear()		       #Clears the screen setting it all to black - this is the pico graphics clear option
    display.update()
    
def Animate_Graph(bar,level):
    if(bar==1):
        display.set_pen(BLACK)             # Erase the text at the top
        display.rectangle(0,0,X_max,30)    #
    
    
    display.set_pen(txt_clr)
    if (bar==1):
        level_s = str(level)               # making the level a string so it can be printed
        display.text(level_s, 40, 0, 135, 2) #display the value 1 through 10 at that location and scale
    elif(bar==2):
        level_s = str(level)               # making the level a string so it can be printed
        display.text(level_s, 94, 0, 135, 2) #display the value 1 through 10 at that location and scale
    else:
        pass
    
    B_height = 20                      #Each segment of the Bar chart has height 2
    Y_POS = Y_max - B_height           #Y_position base point is the 
    for b in range(0,10):
        if (b <= level):
            display.set_pen(b_colour[b])
        else:
            display.set_pen(BLACK)
            
        if(bar==1):
            display.rectangle(X1_Bar_Start, Y_POS,X_Bar_Width,B_height)
            display.update()
            Y_POS -= B_height
        elif(bar==2):
            display.rectangle(X2_Bar_Start, Y_POS,X_Bar_Width,B_height)
            display.update()
            Y_POS -= B_height
        else:
            pass
            
        
def show_level(bar):
    a = random.randint(0,10)
    Animate_Graph(bar,a)
    print(a)
    
#------------------------- MAIN CODE --------------------------------

while True:
    show_level(1)
    show_level(2)
    time.sleep(delay)
    
    
    

