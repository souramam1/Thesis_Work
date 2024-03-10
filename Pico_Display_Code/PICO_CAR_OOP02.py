# Turns on corresponding LED when car is in the bay

from machine import Pin
import time

class Car_Bay:
    
    def __init__(self):
        self.led1 = Pin(0, Pin.OUT)
        self.led2 = Pin(1, Pin.OUT)
        self.led3 = Pin(2, Pin.OUT)
        self.led4 = Pin(3, Pin.OUT)
        self.leds = [self.led1,self.led2,self.led3,self.led4]
        self.car1 = Pin(4, Pin.IN, Pin.PULL_DOWN)
        self.car2 = Pin(5, Pin.IN, Pin.PULL_DOWN)
        self.car3 = Pin(6, Pin.IN, Pin.PULL_DOWN)
        self.car4 = Pin(10, Pin.IN, Pin.PULL_DOWN)
        self.cars = [self.car1,self.car2,self.car3,self.car4]
        
        
    def check_cars(self):
        print(len(self.cars))
        for i in range(len(self.cars)):
            if(self.cars[i].value()):
                self.leds[i].value(1)
            else:
                self.leds[i].value(0)
            
            
            
if __name__ == "__main__":
    my_car_charger = Car_Bay()
    
    while True:
        my_car_charger.check_cars()
        time.sleep(0.1)
        
                
                
            
                
            
                
                
                
                
        
    
    
