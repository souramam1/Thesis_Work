#example of a simple non-interrupt way of reading Pico Display's buttons with a loop that checks to
import time
from pimoroni import Button
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY, PEN_P4
from pimoroni import RGBLED

#we're only using a few colours so we can use a 4 bit/16 colour palette and save RAM!
display = PicoGraphics(display=DISPLAY_PICO_DISPLAY, pen_type=PEN_P4, rotate=0)

#define led pins
led = RGBLED(6,7,8)

display.set_backlight(0.5)
display.set_font("bitmap8") #bitmap font reference point is the upper left hand point

#define button pins
button_a = Button(12)
button_b = Button(13)
button_x = Button(14)
button_y = Button(15)

#Define some colors to use(R,G,B)
WHITE = display.create_pen(255,255,255)
BLACK = display.create_pen(0,0,0)
RED = display.create_pen(255,000,000)
CYAN = display.create_pen(0,255,255)
YELLOW = display.create_pen(255,255,000)
MAGENTA = display.create_pen(255,000,255)
GREEN = display.create_pen(000,255,000)
BLUE = display.create_pen(000,000,255)

def clear():                   #Function called to clear the screen
    display.set_pen(BLACK)     #Assuming we want a black background
    display.clear()		       #Clears the screen setting it all to black - this is the pico graphics clear option
    display.update()           #Performs the actual screen update --> when we tell the display to do something, it goes into buffer, then when call update, contents of buffer on screen
    
#----------------------------------------------------------------------------------------------------------------------

clear()

# text(text,x,y,wordwrap,scale,angle,spacing)

while True:
    if button_a.read():
        clear()
        display.set_pen(WHITE)
        display.text("Button A pressed", 10,10,240,4) #x, y , wordwrap (num of pixels before word wraps to next line, 
        display.update()
        led.set_rgb(255,255,255)
        time.sleep(1)
        clear()
    elif button_b.read():
        clear()
        display.set_pen(CYAN)
        display.text("Button B pressed", 10,10,240,4)
        display.update()
        led.set_rgb(000,000,255)
        time.sleep(1)
        clear()
    elif button_x.read():
        clear()
        display.set_pen(MAGENTA)
        display.text("Button X pressed", 10,10,240,4)
        display.update()
        led.set_rgb(255,000,255)
        time.sleep(1)
        clear()
    elif button_y.read():
        clear()
        display.set_pen(YELLOW)
        display.text("Button Y pressed", 10,10,240,4)
        display.update()
        led.set_rgb(255,255,000)
        time.sleep(1)
        clear()
    else:
        display.set_pen(GREEN)
        led.set_rgb(000,255,000)
        display.text("Press any button!",10,10, 240,4)
        display.update()
    time.sleep(0.1) #frequency of checking for button pressing
