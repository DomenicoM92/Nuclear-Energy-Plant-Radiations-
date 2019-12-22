import paho.mqtt.client as mqtt
import time
import random

from qgis._core import QgsTask

class mqttPublisher(QgsTask):
    activator = 1

    def __init__(self):
        QgsTask.__init__(self)

    def on_connect(client, userdata, flags, rc):
        print("Connected With Result Code " + rc)

    def run(self):
        username = 'ubhhdpho'
        password = '7OEwDqtTAfec'
        server = 'tailor.cloudmqtt.com'
        port = 13662
        client = mqtt.Client()
        client.on_connect = self.on_connect

        client.username_pw_set(username, password)
        client.connect(server, port)

        while self.activator:
            time.sleep(5)
            randomRadiation = random.randint(1,200)
            client.publish(topic="radiation - topic0", payload=str(randomRadiation), qos=0, retain=False)
        print("End Publisher")


    def stopPub(self,act):
        self.activator = act