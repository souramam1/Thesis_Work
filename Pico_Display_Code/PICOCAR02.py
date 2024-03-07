from machine import Pin
import time

led1 = Pin(0, Pin.OUT)
led2 = Pin(1, Pin.OUT)
led3 = Pin(2, Pin.OUT)
led4 = Pin(3, Pin.OUT)
car1 = Pin(4, Pin.IN, Pin.PULL_DOWN)
car2 = Pin(5, Pin.IN, Pin.PULL_DOWN)
car3 = Pin(6, Pin.IN, Pin.PULL_DOWN)
car4 = Pin(10, Pin.IN, Pin.PULL_DOWN)


while True:
    print("car1")
    print(car1.value())
    led1.value(car1.value())
    print("car2")
    print(car2.value())
    led2.value(car2.value())
    print("car3")
    print(car3.value())
    led3.value(car3.value())
    print("car4")
    print(car4.value())
    led4.value(car4.value())
    time.sleep(0.1)
