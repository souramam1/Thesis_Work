import machine
import utime


class Solar_Panels:
    
    def __init__(self,pin):
        self.potentiometer = machine.ADC(pin)
        self.curr_val = 0
        self.curr_volt = 0
        self.bounds = [1.4,1.8, 2.3,2.54,2.7,2.8,2.87,2.92,2.97]
        self.bound_id = 0
        self.solar_quant = 0
        self.solar_percent = 0
        self.solar_score = 0
        if pin == 28:
            self.bound_id = 4
        elif pin == 27:
            self.bound_id = 6
        elif pin == 26:
            self.bound_id = 8
        else:
            raise RunTimeError("Invalid pin number for the ADC")
        
    def read_potent(self):
        self.curr_val = self.potentiometer.read_u16()
        self.curr_volt = 3.3*(self.curr_val/65535)
    
    def solar_num(self):
        for i in range(self.bound_id+1):
            if self.curr_volt >= self.bounds[i]:
                pass
            else:
                self.solar_quant = i
                print(f"building id: {self.bound_id} has {self.solar_quant} sp attached")
                break
    
    def solar_percentage(self):
        self.solar_percent = (self.solar_quant/self.bound_id)*100
        print(self.solar_percent)
        return self.solar_percent
    

        
        
                
        
        
                   
if __name__ == "__main__":
    while True:
        my_solar_a = Solar_Panels(28)
        my_solar_y = Solar_Panels(27)
        my_solar_l = Solar_Panels(26)
        my_solar_a.read_potent()
        my_solar_a.solar_num()
        print(my_solar_a.curr_volt)
        print(my_solar_a.solar_percent)
        
        utime.sleep(1)
