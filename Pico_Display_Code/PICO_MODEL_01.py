#First overall assembly of consituent classes

from machine import Pin
import time
from pimoroni import Button
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY, PEN_P4
import random
import machine

from PICO_CAR_OOP02 import Car_Bay
from PICO_DISP_OBJ_02 import Display
from PICOADC_OBJ01 import Solar_Panels


class Model:
    
    disp: Display
    solar: Solar_Panels
    charger: Car_Bay
    
    def __init__(self):
        self.disp = Display()
        self.solar = Solar_Panels()
        self.charger = Car_Bay()
        self.val = 0
        
        
        
        
        
if __name__ == "__main__":
    my_model = Model()
    my_model.disp.clear()
    my_model.disp.show_level(1,11)
    my_model.disp.show_level(2,1)
    
    while True:
        my_model.charger.check_cars()
        time.sleep(0.1)

    
        