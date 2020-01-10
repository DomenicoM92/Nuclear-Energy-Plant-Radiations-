from .paho.mqtt import client as mqtt
import time
import random

from qgis._core import QgsTask


class mqttPublisher(QgsTask):
    activator = 1
    timeRate = 5

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

            messagge = ""
            i = 1
            while i < 200:
                messagge += str(random.randint(1, 200)) + str(',')
                if i == 199:
                    messagge += str(random.randint(1, 200))
                i += 1
            client.publish(topic="radiation - topic0", payload=messagge, qos=0, retain=False)
            time.sleep(self.timeRate)

        print("End Publisher")

    def stopPub(self, act):
        self.activator = act

    def setTimeRatePub(self, newTime):
        self.timeRate = newTime
        print("New Publisher time rate:" + str(newTime))
