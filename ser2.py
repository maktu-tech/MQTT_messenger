import paho.mqtt.client as mqtt
def on_connect(client, userdata, flags, rc):
    if rc != 0:
        print("Connect returned result code: " + str(rc))
    return
def fun(client, userdata, msg):
    global a, b
    for i in a:
        if(i==msg.topic):
            client.publish(b[i], msg.payload.decode("utf-8"))
a=["c1send","c2send"]
b={"c1send":"c2listen","c2send":"c1listen" }
client = mqtt.Client()
client.on_connect = on_connect
for i in a:
    client.message_callback_add(i,fun)
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
client.username_pw_set("example", "Example123")
client.connect("49d1a22e3af240efb207d443419e3257.s1.eu.hivemq.cloud", 8883)
for i in a:
    client.subscribe(i)
client.loop_forever()
