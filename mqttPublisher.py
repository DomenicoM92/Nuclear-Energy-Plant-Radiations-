import paho.mqtt.client as mqtt
import time
import random


def on_connect(client, userdata, flags, rc):
    print("Connected With Result Code " + rc)

username = 'ubhhdpho'
password = '7OEwDqtTAfec'
server = 'tailor.cloudmqtt.com'
port = 13662
client = mqtt.Client()
client.on_connect = on_connect

client.username_pw_set(username, password)
client.connect(server, port)

while 1:
    time.sleep(5)
    randomRadiation = random.randint(1,200)
    client.publish(topic="radiation - topic0", payload=str(randomRadiation), qos=0, retain=False)


