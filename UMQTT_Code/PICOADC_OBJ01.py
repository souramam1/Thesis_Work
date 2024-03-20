import machine
import utime
import time


class Solar_Panels:
    
    def __init__(self):
        self.potentiometer = machine.ADC(26)
        self.curr_val = 0
        self.curr_volt = 0
        self.band_choice = [0,1.8,2.3,2.55,2.9,3.3]
        self.solar_number = 0
        
    def read_potent(self):
        self.curr_val = self.potentiometer.read_u16()
        self.curr_volt = 3.3*(self.curr_val/65535)
        for i in range(1,len(self.band_choice)):
            if self.curr_volt <= self.band_choice[i]:
                if i == 5:
                    self.solar_number = 0
                else:
                    self.solar_number = i
                print("solar number is:")
                print(self.solar_number)
                break
        
                
            
        utime.sleep(2)
        


        
if __name__ == "__main__":
    while True:
        my_solar = Solar_Panels()
        my_solar.read_potent()
        print(my_solar.curr_volt)
        time.sleep(1)
