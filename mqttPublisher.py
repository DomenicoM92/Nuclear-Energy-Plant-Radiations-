from .paho.mqtt import client as mqtt
import time
import random

from qgis._core import QgsTask


class mqttPublisher(QgsTask):
    activator = 1
    timeRate = 1
    initRadiation = [124.0, 82.0, 53.0, 134.0, 179.0, 151.0, 166.0, 54.0, 109.0, 45.0, 64.0, 115.0, 169.0, 94.0, 102.0, 43.0, 39.0, 83.0, 144.0, 72.0, 17.0, 193.0, 45.0, 173.0, 64.0, 43.0, 32.0, 69.0, 12.0, 150.0, 185.0, 179.0, 17.0, 139.0, 130.0, 196.0, 159.0, 120.0, 158.0, 58.0, 180.0, 81.0, 189.0, 119.0, 100.0, 1.0, 53.0, 59.0, 66.0, 103.0, 138.0, 179.0, 155.0, 121.0, 63.0, 48.0, 183.0, 151.0, 175.0, 152.0, 14.0, 24.0, 129.0, 132.0, 186.0, 3.0, 68.0, 75.0, 119.0, 164.0, 115.0, 152.0, 69.0, 178.0, 172.0, 77.0, 193.0, 36.0, 83.0, 139.0, 22.0, 66.0, 199.0, 22.0, 81.0, 136.0, 100.0, 18.0, 80.0, 81.0, 178.0, 126.0, 83.0, 180.0, 39.0, 21.0, 112.0, 115.0, 57.0, 14.0, 124.0, 65.0, 83.0, 161.0, 157.0, 169.0, 68.0, 40.0, 161.0, 193.0, 153.0, 39.0, 195.0, 87.0, 61.0, 146.0, 121.0, 74.0, 41.0, 66.0, 177.0, 179.0, 153.0, 108.0, 40.0, 103.0, 147.0, 96.0, 87.0, 99.0, 95.0, 78.0, 104.0, 186.0, 100.0, 61.0, 192.0, 144.0, 94.0, 164.0, 31.0, 119.0, 119.0, 25.0, 54.0, 61.0, 58.0, 128.0, 193.0, 64.0, 115.0, 197.0, 38.0, 126.0, 198.0, 150.0, 17.0, 95.0, 193.0, 44.0, 76.0, 55.0, 179.0, 137.0, 119.0, 187.0, 19.0, 55.0, 112.0, 138.0, 17.0, 108.0, 198.0, 195.0, 100.0, 74.0, 156.0, 67.0, 95.0, 6.0, 147.0, 139.0, 151.0, 150.0, 159.0, 111.0, 133.0, 127.0, 19.0, 141.0, 37.0, 10.0, 41.0, 43.0, 17.0, 47.0, 45.0, 104.0, 168.0, 97.0]

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
                messagge += str(random.randint(mqttPublisher.initRadiation[i -1], 200)) + str(',')
                if i == 199:
                    messagge += str(mqttPublisher.initRadiation[i -1])
                i += 1
            client.publish(topic="radiation - topic0", payload=messagge, qos=0, retain=False)
            time.sleep(self.timeRate)
        return True

    def finished(self, result):
        print("End Publisher")

    def cancel(self):
        super().cancel()

    def stopPub(self, act):
        self.activator = act

    def setTimeRatePub(self, newTime):
        self.timeRate = newTime
        #print("New Publisher time rate:" + str(newTime))
