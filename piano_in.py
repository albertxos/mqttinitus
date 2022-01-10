import time
import paho.mqtt.client as paho
from paho import mqtt

# setting callbacks
def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)

# print subsription topics
def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

# print received tone
def on_tone(client, userdata, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

# client_id is the given name of the client
client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect

# enable TLS for secure connection
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
# set username and password
client.username_pw_set("conti", "your_password")
# connect to HiveMQ Cloud on port 8883 (default for MQTT)
client.connect("7dc97497c5fa41d58ce193bf064f9a73.s1.eu.hivemq.cloud", 8883)

# setting callbacks
client.on_subscribe = on_subscribe
client.on_message = on_tone

# subscribe to all topics of encyclopedia by using the wildcard "#"
client.subscribe("pianist/#", qos=1)

# loop_forever
# you can also use loop_start and loop_stop
client.loop_forever()
