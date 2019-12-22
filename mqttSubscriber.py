import paho.mqtt.client as mqtt
import time
import random

from qgis._core import QgsTask


class mqttSubscriber(QgsTask):
    rc = 0

    def __init__(self):
        QgsTask.__init__(self)

    def on_connect(client, userdata, flags, rc):
        print("Connected With Result Code " + rc)

    def on_message(client, userdata, message):
        print("Message Recieved: " + message.payload.decode())

    def on_subscribe(client, obj, mid, granted_qos):
        client.subscribe("radiation - topic0", qos=0)

    def run(self):
        print("I'm Subscriber")
        username = 'ubhhdpho'
        password = '7OEwDqtTAfec'
        server = 'tailor.cloudmqtt.com'
        port = 13662
        client = mqtt.Client()
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        client.on_subscribe = self.on_subscribe
        client.username_pw_set(username, password)
        client.connect(server, port)

        client.subscribe("radiation - topic0", qos=0)

        # Continue the network loop, exit when an error occurs
        while self.rc == 0:
            print("hi")
            rc = client.loop()
        print("End Subscriber: " + str(rc))

    def stopSub(self,stop):
        self.rc = stop






























#import paho.mqtt.client as mqtt

#OLD CODE
# def on_connect(client, userdata, flags, rc):
#     print("Connected With Result Code " + rc)
#
# def on_message(client, userdata, message):
#     print("Message Recieved: " + message.payload.decode())
#
#
# def on_subscribe(client, obj, mid, granted_qos):
#     client.subscribe("radiation - topic0", qos=0)
#
# username = 'ubhhdpho'
# password = '7OEwDqtTAfec'
# server = 'tailor.cloudmqtt.com'
# port = 13662
# client = mqtt.Client()
# client.on_connect = on_connect
# client.on_message = on_message
# client.on_subscribe = on_subscribe
# client.username_pw_set(username, password)
# client.connect(server, port)
#
# client.subscribe("radiation - topic0", qos=0)
#
# # Continue the network loop, exit when an error occurs
# rc = 0
# while rc == 0:
#     rc = client.loop()
# print("rc: " + str(rc))