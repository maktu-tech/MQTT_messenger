import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc != 0:
        print("Connect returned result code: " + str(rc))
    return

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    if (msg.topic == "c1send"):
        client.publish("c2listen", msg.payload.decode("utf-8"))
        print("yup  ",msg.payload.decode("utf-8"))
    elif (msg.topic == "c2send"):
        client.publish("c1listen", msg.payload.decode("utf-8"))
        print("puy")
# create the client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# enable TLS
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)

# set username and password
client.username_pw_set("example", "Example123")
# connect to HiveMQ Cloud on port 8883
client.connect("49d1a22e3af240efb207d443419e3257.s1.eu.hivemq.cloud", 8883)
client.subscribe("c1send")
client.subscribe("c2send")
client.loop_forever()