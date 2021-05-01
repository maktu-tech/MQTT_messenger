import paho.mqtt.client as mqtt
import threading
import os
import time
msgs=[]
def on_connect(client, userdata, flags, rc):
    if rc != 0:
        print("Connect returned result code: " + str(rc))
    return
def c1lis(client, userdata, msg):
    msgs.append(msg.payload.decode("utf-8"))
    return
def c1sen(m1):
    print("C1: -> " + m1)
    client.publish("c1send",m1)
    return
def c1show():
    for i in msgs:
        print("Msg Res.: "+i)
    msgs.clear()
    return
client = mqtt.Client()
client.on_connect = on_connect
client.message_callback_add("c1listen",c1lis)
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
client.username_pw_set("example", "Example123")
client.connect("49d1a22e3af240efb207d443419e3257.s1.eu.hivemq.cloud", 8883)
client.loop_start()
client.subscribe("c1listen")
print("Format: send -> message....")
print("Format: show")
while True:
    a=input()
    if(a[0:4]=="send"):
        c1sen(a[8:])
    elif(a[0:4]=="show"):
        c1show()




