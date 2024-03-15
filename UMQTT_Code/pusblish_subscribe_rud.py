#Native libs
import network
import time
import random

#Third Party
from umqtt.robust import MQTTClient

# Internal libs
#import constants


def connectMQTT():
    '''Connects to Broker'''
    # Client ID can be anything
    client = MQTTClient(
        client_id=b"maia_com7",
        server="e46309c1b7584d2387038d16668324ea.s1.eu.hivemq.cloud",
        port=0,
        user="souramam1",
        password="Cia25yow",
        keepalive=7200,
        ssl=True,
        ssl_params={'server_hostname': "e46309c1b7584d2387038d16668324ea.s1.eu.hivemq.cloud"}
    )
    client.connect()
    return client


def connect_to_internet(ssid, password):
    # Pass in string arguments for ssid and password
    
    # Just making our internet connection
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
    # Wait for connect or fail
    max_wait = 10
    while max_wait > 0:
      if wlan.status() < 0 or wlan.status() >= 3:
        break
      max_wait -= 1
      print('waiting for connection...')
      time.sleep(1)
    # Handle connection error
    if wlan.status() != 3:
       print(wlan.status())
       raise RuntimeError('network connection failed')
    else:
      print('connected')
      print(wlan.status())
      status = wlan.ifconfig()

def make_connections():
    # Connect to internet and set MPU to start taking readings
    connect_to_internet("maiahotspot", "12345678")
    return connectMQTT()


def publish(topic, value, client):
    '''Sends data to the broker'''
    print(topic)
    print(value)
    client.publish(topic, value)
    print("Publish Done")
    
def my_callback(topic, response):
    # Perform desired actions based on the subscribed topic and response
    print("Received message on topic:", topic)
    print("Response:", int(respose)) #integerifying the response is valid
    
def subscribe(topic, client):
    '''Recieves data from the broker'''
    client.subscribe(topic)
    print("Subscribe Done")


client = make_connections()
client.set_callback(my_callback)
subscribe('Sent over COM 6', client)

while True:
    time.sleep(5)
    client.check_msg()
    publish('Sent over COM 7', 'bonjour et bonsoir', client)
    


