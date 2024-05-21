#Native libs
import network
import time
import random
import machine
from pimoroni import Button
from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY, PEN_P4

from PICODISP_OBJ_04 import Display
from pub_sub_oop import InternetConnector
from pub_sub_oop import MQTTConnector


class Model:
    disp: Display
    mqtatoe: MQTTConnector
    inter: InternetConnector
    
    def __init__(self):
        self.disp = Display()
        
        self.inter = InternetConnector("maiahotspot", "12345678")
        self.inter.connect()
        
        self.mqtatoe = MQTTConnector(
            client_id=b"maia_com7",
            server="e46309c1b7584d2387038d16668324ea.s1.eu.hivemq.cloud",
            port=0,
            user="",
            password=""                             
        )
        self.mqtatoe.connect()
        self.mqtatoe.subscribe('Sent over COM 6', self.my_callback)
        
    def my_callback(self,topic, response):
        print("Received message on topic:", topic)
        print("Response:", int(response))  # Integerifying the response is valid
        int_resp = int(response)
        if(int_resp == 1):
            print("CHANGE GRAPH")
        else:
            print("NOT ONE")
        
        

    
if __name__ == '__main__':
    my_pico = Model()
    while True:
        time.sleep(5)
        my_pico.mqtatoe.client.check_msg()
        my_pico.mqtatoe.publish('Sent over COM 7', 'bonjour et bonsoir')
    
        
        


