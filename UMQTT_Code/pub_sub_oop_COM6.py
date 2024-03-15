#Native libs
import network
import time
import random
from umqtt.robust import MQTTClient

class InternetConnector:
    def __init__(self, ssid, password):
        self.ssid = ssid
        self.password = password

    def connect(self):
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(self.ssid, self.password)
        max_wait = 10
        while max_wait > 0:
            if wlan.status() < 0 or wlan.status() >= 3:
                break
            max_wait -= 1
            print('waiting for connection...')
            time.sleep(1)
        if wlan.status() != 3:
            print(wlan.status())
            raise RuntimeError('network connection failed')
        else:
            print('connected')
            print(wlan.status())
            return wlan.ifconfig()

class MQTTConnector:
    def __init__(self, client_id, server, user, password, ssl=True, port=0):
        self.client_id = client_id
        self.server = server
        self.port = port
        self.user = user
        self.password = password
        self.ssl = ssl
        self.ssl_params = {'server_hostname': server}
        self.client = None

    def connect(self):
        self.client = MQTTClient(
            client_id=self.client_id,
            server=self.server,
            port=self.port,
            user=self.user,
            password=self.password,
            keepalive=7200,
            ssl=self.ssl,
            ssl_params=self.ssl_params
        )
        self.client.connect()

    def publish(self, topic, value):
        if self.client is None:
            raise RuntimeError('MQTT client is not connected')
        self.client.publish(topic, value)
        print("Publish Done")

    def subscribe(self, topic, callback):
        if self.client is None:
            raise RuntimeError('MQTT client is not connected')
        self.client.set_callback(callback)
        self.client.subscribe(topic)
        print("Subscribe Done")

def my_callback(topic, response):
    print("Received message on topic:", topic)
    print("Response:", int(response))  # Integerifying the response is valid

def main():
    internet_connector = InternetConnector("maiahotspot", "12345678")
    internet_connector.connect()

    mqtt_connector = MQTTConnector(
        client_id=b"maia_com6",
        server="e46309c1b7584d2387038d16668324ea.s1.eu.hivemq.cloud",
        port=0,
        user="souramam1",
        password="Cia25yow"
    )
    mqtt_connector.connect()
    mqtt_connector.subscribe('Sent over COM 7', my_callback)

    while True:
        time.sleep(5)
        mqtt_connector.client.check_msg()
        mqtt_connector.publish('Sent over COM 6', '1')

if __name__ == "__main__":
    main()

