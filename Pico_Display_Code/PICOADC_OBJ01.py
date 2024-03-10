import machine
import utime


class Solar_Panels:
    
    def __init__(self):
        self.potentiometer = machine.ADC(26)
        self.curr_val = 0
        self.curr_volt = 0
        
    def read_potent(self):
        self.curr_val = self.potentiometer.read_u16()
        self.curr_volt = 3.3*(self.curr_val/65535)
        utime.sleep(2)
        


        
if __name__ == "__main__":
    my_solar = Solar_Panels()
    my_solar.read_potent()
    print(my_solar.curr_volt)
