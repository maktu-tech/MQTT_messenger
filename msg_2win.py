from collections import namedtuple
import paho.mqtt.client as mqtt
import threading
from tkinter import *
from tkinter import simpledialog
def on_connect(client, userdata, flags, rc):
    if rc != 0:
        print("Connect returned result code: " + str(rc))
    return
def lis(client, userdata, msg):
    global msg_string
    msg_string+=msg.payload.decode("utf-8")
    msg_label.configure(text=msg_string)

def add_emoji(m):
    m1=msg_entry.get()
    msg_entry.delete(0,'end')
    msg_entry.insert(0,m1+m)
    return
def send():
    global msg_string
    global topic_name
    if(msg_entry.get()==""):
        return
    client.publish(topic_name,"\n <"+ name+"> " + msg_entry.get())
    msg_entry.delete(0,'end')
    msg_label.configure(text=msg_string)
    return
def extract():
    global topic_name, name
    topic_name=msg_en_top.get()
    if(msg_en_nam.get()==""):
        name="anonymous"
    else:
        name=msg_en_nam.get()
    root1.destroy()

topic_name, name = "", ""
root1 = Tk()
root1.geometry('400x180')
root1.title('Join Win')
frame1=Frame(root1, width= 400, height=180, background='#ededed')
frame1.pack(side=TOP, fill=X)
msg_lab_top = Label(frame1, text="Enter Topic: ", font=("", 11))
msg_en_top = Entry(frame1,justify=LEFT, font=("", 11))
msg_lab_nam = Label(frame1, text="Enter UserID: ", font=("", 11))
msg_en_nam = Entry(frame1,justify=LEFT, font=("", 11))
msg_button = Button(frame1, text="Ok",command=extract)

msg_lab_nam.place(x=10, y= 60, width=150, height = 20)
msg_lab_top.place(x=10, y= 20, width=150, height = 20)
msg_en_nam.place(x=200, y= 60, width=150, height = 20)
msg_en_top.place(x=200, y= 20, width=150, height = 20)
msg_button.place(x=162.5, y= 120, width=75, height = 30)
root1.mainloop()

client = mqtt.Client()
client.on_connect = on_connect
client.message_callback_add(topic_name, lis)
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
client.username_pw_set("example", "Example123")
client.connect("49d1a22e3af240efb207d443419e3257.s1.eu.hivemq.cloud", 8883)

client.loop_start()
client.subscribe(topic_name)

msg_string=""

root =Tk()
root.geometry('304x500')
root.title('lolChat>>> Topic: '+topic_name+' User: '+name)
frame1=Frame(root, width=304, height=420, background="#ededed")
frame1_5=Frame(root, width= 304, height=29,background="#ededed")
frame2=Frame(root, width=304, height=50, background="#d4ffd4")


frame1.pack(side=TOP, fill=X)
msg_label=Label(frame1,text=msg_string, justify=LEFT,font=("Times Roman",12),anchor=W)
msg_label.place(x=5, y=5,width=294, height = 300 )



frame2.pack(side=BOTTOM, fill=X)
msg_entry = Entry(frame2,justify=LEFT, font=("", 14))
msg_button = Button(frame2, text=">>>",command=send)
msg_entry.place(x=5, y= 5, width=240, height = 40)
msg_button.place(x=254, y= 5, width=40, height = 40)

frame1_5.pack(side=BOTTOM, fill=X)
e_1 = Button(frame1_5, text="\U0001F606" ,font=("",12), command=lambda: add_emoji("\U0001F606"))
e_1.place(x=2, y= 2, width=25, height = 25)
e_2 = Button(frame1_5, text="\U0001F923" ,font=("",12), command=lambda: add_emoji("\U0001F923"))
e_2.place(x=27, y= 2, width=25, height = 25)
e_3 = Button(frame1_5, text="\U0001F643" ,font=("",12), command=lambda: add_emoji("\U0001F643"))
e_3.place(x=52, y= 2, width=25, height = 25)
e_4 = Button(frame1_5, text="\U0001F605" ,font=("",12), command=lambda: add_emoji("\U0001F605"))
e_4.place(x=77, y= 2, width=25, height = 25)
e_5 = Button(frame1_5, text="\U0001F607" ,font=("",12), command=lambda: add_emoji("\U0001F607"))
e_5.place(x=102, y= 2, width=25, height = 25)
e_6 = Button(frame1_5, text="\U0001F611" ,font=("",12), command=lambda: add_emoji("\U0001F611"))
e_6.place(x=127, y= 2, width=25, height = 25)
e_7 = Button(frame1_5, text="\U0001F60F" ,font=("",12), command=lambda: add_emoji("\U0001F60F"))
e_7.place(x=152, y= 2, width=25, height = 25)
e_8 = Button(frame1_5, text="\U0001F612" ,font=("",12), command=lambda: add_emoji("\U0001F612"))
e_8.place(x=177, y= 2, width=25, height = 25)
e_9 = Button(frame1_5, text="\U0001F44C" ,font=("",12), command=lambda: add_emoji("\U0001F44C"))
e_9.place(x=202, y= 2, width=25, height = 25)
e_10 = Button(frame1_5, text="\U0001F918" ,font=("",12), command=lambda: add_emoji("\U0001F918"))
e_10.place(x=227, y= 2, width=25, height = 25)
e_11 = Button(frame1_5, text="\U0001F44D" ,font=("",12), command=lambda: add_emoji("\U0001F44D"))
e_11.place(x=252, y= 2, width=25, height = 25)
e_12 = Button(frame1_5, text="\U0001F64F" ,font=("",12), command=lambda: add_emoji("\U0001F64F"))
e_12.place(x=277, y= 2, width=25, height = 25)

t1=threading.Thread(target=root.mainloop())
t1.start()
exit()
