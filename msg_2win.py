import paho.mqtt.client as mqtt
import threading
from tkinter import *

def on_connect(client, userdata, flags, rc):
    if rc != 0:
        print("Connect returned result code: " + str(rc))
    return
def eventNews(client, userdata, msg):
    print("<Event> "+msg.payload.decode("utf-8"))
    return
def authsend(tpub,pasw):
    client.publish("auth_to_ser",name+','+tpub+','+pasw)
    print("ok till")
    return
def authrec(client, userdata, msg):
    #tpub,tsub
    auth_ret=msg.payload.decode("utf-8").split(",")
    if(len(auth_ret)>0):
        tpub.append(auth_ret[0])
        tsub.append(auth_ret[1])
    return
def subFunc(client, userdata, msg):
    print("how")
    print(msg.payload.decode("utf-8"))
    return
def pubFunc(msgs,pub_topic):
    client.publish(pub_topic,msgs)
    return
# def lis(client, userdata, msg):
#     global msg_string
#     msg_string+=msg.payload.decode("utf-8")
#     msg_label.configure(text=msg_string)

# def add_emoji(m):
#     m1=msg_entry.get()
#     msg_entry.delete(0,'end')
#     msg_entry.insert(0,m1+m)
#     return
# def send():
#     global msg_string
#     global topic_name
#     if(msg_entry.get()==""):
#         return
#     client.publish(topic_name,"\n <"+ name+"> " + msg_entry.get())
#     msg_entry.delete(0,'end')
#     msg_label.configure(text=msg_string)
#     return
# def subscribe_all():
#     client.subscribe(topic_name)
#    return
def add_topic():
    flg = input("Do you want to enter topic(Y/N): ")
    if(flg == 'Y'):
        t_p_name = input("Enter Topic Name: ")
        t_p_pass = input("Enter Topic Password: ")
        authsend(t_p_name, t_p_pass)
        add_topic()
    elif(flg == 'N'):
        print(msg_rep)
        return
    else:
        add_topic()

# -- .ps file ---
topic_names = []
pws=""
tsub=[]
tpub=[]
msg_rep=""

name = input("Enter User Name: ")
fk = open(name+".ps","a+")
fk.seek(0,0)
pws=input("Enter Pass.: ")

# client creation
client = mqtt.Client()
client.on_connect = on_connect
client.message_callback_add("auth_ser@"+name, authrec)
client.message_callback_add("serv@"+name, eventNews)
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
client.username_pw_set("example", "Example123")
client.connect("49d1a22e3af240efb207d443419e3257.s1.eu.hivemq.cloud", 8883)

if(fk.readlines() == []):
    fk.write("name: "+name+'\n')//6
    fk.write("pass: "+pws+'\n')
else:
    fk.seek(0,0)
    data = fk.readlines()
    pws_ret=data[1][6:-1]
    if(pws!=pws_ret):
        print("Wrong Password")
        exit()
    if(len(data)>2):
        tsub.extend(data[2][6:-2].split(","))
        tpub.extend(data[3][6:-2].split(","))
#--- to enter topic ---
t1 = threading.Thread(target=add_topic)
t1.start()
if(len(tsub)==0):
    print("No, topic present exiting......")
    exit()
#--- if no topic exit --
for sb in tpub:
    client.message_callback_add(sb, subFunc)

client.subscribe("auth_ser@"+name)
client.subscribe("serv@"+name)
for sb in tpub:
    client.subscribe(sb)
pubFunc("mayank<@>Hello",tsub[0])
client.loop_forever()
# subscribe_all()

# msg_string=""

# root =Tk()
# root.geometry('304x500')
# root.title('lolChat>>> Topic: '+topic_name+' User: '+name)
# frame1=Frame(root, width=304, height=420, background="#ededed")
# frame1_5=Frame(root, width= 304, height=29,background="#ededed")
# frame2=Frame(root, width=304, height=50, background="#d4ffd4")


# frame1.pack(side=TOP, fill=X)
# msg_label=Label(frame1,text=msg_string, justify=LEFT,font=("Times Roman",12),anchor=W)
# msg_label.place(x=5, y=5,width=294, height = 300 )


# frame2.pack(side=BOTTOM, fill=X)
# msg_entry = Entry(frame2,justify=LEFT, font=("", 14))
# msg_button = Button(frame2, text=">>>",command=send)
# msg_entry.place(x=5, y= 5, width=240, height = 40)
# msg_button.place(x=254, y= 5, width=40, height = 40)

# frame1_5.pack(side=BOTTOM, fill=X)
# e_1 = Button(frame1_5, text="\U0001F606" ,font=("",12), command=lambda: add_emoji("\U0001F606"))
# e_1.place(x=2, y= 2, width=25, height = 25)
# e_2 = Button(frame1_5, text="\U0001F923" ,font=("",12), command=lambda: add_emoji("\U0001F923"))
# e_2.place(x=27, y= 2, width=25, height = 25)
# e_3 = Button(frame1_5, text="\U0001F643" ,font=("",12), command=lambda: add_emoji("\U0001F643"))
# e_3.place(x=52, y= 2, width=25, height = 25)
# e_4 = Button(frame1_5, text="\U0001F605" ,font=("",12), command=lambda: add_emoji("\U0001F605"))
# e_4.place(x=77, y= 2, width=25, height = 25)
# e_5 = Button(frame1_5, text="\U0001F607" ,font=("",12), command=lambda: add_emoji("\U0001F607"))
# e_5.place(x=102, y= 2, width=25, height = 25)
# e_6 = Button(frame1_5, text="\U0001F611" ,font=("",12), command=lambda: add_emoji("\U0001F611"))
# e_6.place(x=127, y= 2, width=25, height = 25)
# e_7 = Button(frame1_5, text="\U0001F60F" ,font=("",12), command=lambda: add_emoji("\U0001F60F"))
# e_7.place(x=152, y= 2, width=25, height = 25)
# e_8 = Button(frame1_5, text="\U0001F612" ,font=("",12), command=lambda: add_emoji("\U0001F612"))
# e_8.place(x=177, y= 2, width=25, height = 25)
# e_9 = Button(frame1_5, text="\U0001F44C" ,font=("",12), command=lambda: add_emoji("\U0001F44C"))
# e_9.place(x=202, y= 2, width=25, height = 25)
# e_10 = Button(frame1_5, text="\U0001F918" ,font=("",12), command=lambda: add_emoji("\U0001F918"))
# e_10.place(x=227, y= 2, width=25, height = 25)
# e_11 = Button(frame1_5, text="\U0001F44D" ,font=("",12), command=lambda: add_emoji("\U0001F44D"))
# e_11.place(x=252, y= 2, width=25, height = 25)
# e_12 = Button(frame1_5, text="\U0001F64F" ,font=("",12), command=lambda: add_emoji("\U0001F64F"))
# e_12.place(x=277, y= 2, width=25, height = 25)

# t1=threading.Thread(target=root.mainloop())
# t1.start()
# fk.close()
# exit()
