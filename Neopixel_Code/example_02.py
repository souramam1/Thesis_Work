#Example 1 - Control individual LED

from neopixel import Neopixel
import utime
import random



class NeoPixel:
    
    def __init__(self, num, data_pin):
        
        self.numpix = num
        self.strip = Neopixel(self.numpix, 0, data_pin, "RGB")

        self.delay = 0.5
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


if __name__ == "__main__":
    my_pix = NeoPixel(16,22)

while True:
    
    for i in range(16):
        my_pix.strip.set_pixel(i, my_pix.red)

    print(my_pix.numpix)
    my_pix.strip.show()
    utime.sleep(my_pix.delay)
    my_pix.strip.fill((0,0,0))
    
    
        
          


