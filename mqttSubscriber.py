import paho.mqtt.client as mqtt

from qgis._core import QgsTask


def on_connect(client, userdata, flags, rc):
    print("Connected With Result Code " + rc)

def on_message(client, userdata, message):
    result = message.payload.decode()
    result = result.split(' ')
    mqttSubscriber.radiation = result

def on_subscribe(client, obj, mid, granted_qos):
    client.subscribe("radiation - topic0", qos=0)

class mqttSubscriber(QgsTask):
    rc = 0
    radiation = list()
    def __init__(self):
        QgsTask.__init__(self)

    def run(self):
        print("I'm Subscriber")
        username = 'ubhhdpho'
        password = '7OEwDqtTAfec'
        server = 'tailor.cloudmqtt.com'
        port = 13662
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message
        client.on_subscribe = on_subscribe
        client.username_pw_set(username, password)
        client.connect(server, port)

        client.subscribe("radiation - topic0", qos=0)

        # Continue the network loop, exit when an error occurs
        while self.rc == 0:
            rc = client.loop()
        print("End Subscriber")

    def stopSub(self,stop):
        self.rc = stop

    def getRadiationList(self):
        return mqttSubscriber.radiation

    def flushRadiationList(self):
        mqttSubscriber.radiation = []