import machine
import utime
potentiometer = machine.ADC(26)
while True:
    curr_val = potentiometer.read_u16()
    curr_volt = 3.3*(curr_val/65535)
    print(curr_volt)
    utime.sleep(2)
