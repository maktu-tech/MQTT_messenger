import paho.mqtt.client as mqtt
import threading
import os
import time
from tkinter import *

def on_connect(client, userdata, flags, rc):
    if rc != 0:
        print("Connect returned result code: " + str(rc))
    return
# The callback for when a PUBLISH message is received from the server.
def c2lis(client, userdata, msg):
    global msg_string
    msg_string+="\n <C1> "
    msg_string+=msg.payload.decode("utf-8")
    msg_label.configure(text=msg_string)

def send():
    global msg_string
    client.publish("c2send",msg_entry.get())
    msg_string+="\n <me> "
    msg_string+=msg_entry.get()
    msg_entry.delete(0,'end')
    msg_label.configure(text=msg_string)
    return

client = mqtt.Client()
client.on_connect = on_connect
client.message_callback_add("c2listen", c2lis)
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
client.username_pw_set("example", "Example123")
client.connect("49d1a22e3af240efb207d443419e3257.s1.eu.hivemq.cloud", 8883)

client.loop_start()
client.subscribe("c2listen")

msg_string=""
root =Tk()
root.geometry('300x500')
root.title('lolChat')
frame1=Frame(root, width=300, height=450, background="#ededed")
frame2=Frame(root, width=300, height=50, background="#d4ffd4")

frame1.pack(side=TOP, fill=X)
msg_label=Label(frame1,text=msg_string, justify=LEFT,font=("Times Roman",12),anchor=W)
msg_label.place(x=5, y=5,width=290, height = 400 )
frame2.pack(side=BOTTOM, fill=X)
msg_entry = Entry(frame2,justify=LEFT, font=("", 14))
msg_button = Button(frame2, text=">>>",command=send)
msg_entry.place(x=5, y= 5, width=240, height = 40)
msg_button.place(x=250, y= 5, width=40, height = 40)

t1=threading.Thread(target=root.mainloop())

t1.start()
t1.stop()

