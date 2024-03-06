#--------------------------------------- EXPLANATION ---------------------------------------------------------
# Varies value of green bar based on availability of light - red bar is fixed to 11, every 3 secs
#-------------------------------------------------------------------------------------------------------------
import time
from pimoroni import Button
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY, PEN_P4
import random
import machine


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
RED = display.create_pen(255,000,000)
GREEN = display.create_pen(000,255,000)

delay = 3
#--------------------------------NON DISPLAY FUNCTIon -----------------------------------------
potentiometer = machine.ADC(26)

#-------------------------------- FUNCTIONS ---------------------------------------------------

def clear():                   #Function called to clear the screen
    display.set_pen(BLACK)     #Assuming we want a black background
    display.clear()		       #Clears the screen setting it all to black - this is the pico graphics clear option
    display.update()
    
def Animate_Graph(bar,level):
    seg_num = 20
    B_height = int(200/seg_num)
    if(bar==1):
        display.set_pen(BLACK)             # Erase the text at the top
        display.rectangle(0,0,X_max,30)    #
    
    
    
    if (bar==1):
        display.set_pen(RED)
        level_s = str(level) + "kWh"             # making the level a string so it can be printed
        display.text(level_s, 5,0, 135, 2.5) #display the value 1 through 10 at that location and scale
    elif(bar==2):
        display.set_pen(GREEN)
        level_s = str(level) + "kWh"             # making the level a string so it can be printed
        display.text(level_s, 70, 0, 135, 2.5) #display the value 1 through 10 at that location and scale
    else:
        pass
    
                         #Each segment of the Bar chart has height 2
    Y_POS = Y_max - B_height           #Y_position base point is the 
    for b in range(0,seg_num):
        if (b <= level):
            if(bar == 1):
                display.set_pen(RED)
            elif(bar==2):
                display.set_pen(GREEN)       
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
        

            
        
def show_level(bar,val):
    seg_num = 20
    if(bar==1):
        a = 11
    else:
        a = round((val-0.3)/2*20)
    Animate_Graph(bar,a)
    print(a)
    

    
    
#------------------------- MAIN CODE --------------------------------

while True:
    curr_val = potentiometer.read_u16()
    curr_volt = 3.3*(curr_val/65535)
    print("CURR VOLT")
    print(curr_volt)
    show_level(1,0)
    show_level(2,curr_volt)
    time.sleep(delay)
    clear()
    
    
    



