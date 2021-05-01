import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    if rc != 0:
        print("Connect returned result code: " + str(rc))
    return

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print("C1: -> " + msg.payload.decode("utf-8"))



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

# subscribe to the topic "my/test/topic"
# client.subscribe("trial")

# publish "Hello" to the topic "my/test/topic"
#client.subscribe("c2listen")
while True:
    client.publish("c2send",input())
# Blocking call that processes network traffic, dispatches callbacks and handles reconnecting.
client.loop_forever()