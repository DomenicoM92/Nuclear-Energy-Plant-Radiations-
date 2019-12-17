import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected With Result Code " + rc)

def on_message(client, userdata, message):
    print("Message Recieved: " + message.payload.decode())


def on_subscribe(client, obj, mid, granted_qos):
    client.subscribe("radiation - topic0", qos=0)

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
rc = 0
while rc == 0:
    rc = client.loop()
print("rc: " + str(rc))



