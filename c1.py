import paho.mqtt.client as mqtt
import threading
import os
import time
def on_connect(client, userdata, flags, rc):
    if rc != 0:
        print("Connect returned result code: " + str(rc))
    return
def on_message(client, userdata, msg):
    print("C2: -> " + msg.payload.decode("utf-8"))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
client.username_pw_set("example", "Example123")
client.connect("49d1a22e3af240efb207d443419e3257.s1.eu.hivemq.cloud", 8883)
client.loop_start()
client.subscribe("c1listen")
client.publish("c1send",input())

t1 =thre

