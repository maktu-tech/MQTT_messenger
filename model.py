import paho.mqtt.client as mqtt
import threading
import time
from tkinter import *
import sys

def on_connect(client, userdata, flags, rc):
    if rc != 0:
        print("Connect returned result code: " + str(rc))
    return
def subFunc(client, userdata, msg):
    global cur_tpub
    msg_dict[msg.topic]+=msg.payload.decode("utf-8")
    if(cur_tpub==msg.topic[:-3]):
        msg_label.configure(text=msg_dict[msg.topic])
    return
def sub_imp():
    client.message_callback_add("auth_ser@"+name, authrec)
    client.message_callback_add("serv@"+name, eventNews)
    client.subscribe("auth_ser@"+name)
    client.subscribe("serv@"+name)
    return
def check(n1, p1):
    global name, fk, pws
    name = n1
    root.title('User: '+name)
    fk = open(n1+".ps","a+")
    fk.seek(0,0)
    if(fk.readlines() == []):
        pws=p1
        fk.write("name: "+n1+'\n')//6
        fk.write("pass: "+p1+'\n')
        info(" Welcome, SignUp Success..\n")
        sub_imp()
        frame0.pack_forget()
    else:
        fk.seek(0,0)
        data = fk.readlines()
        pws_ret=data[1][6:-1]
        pws=pws_ret
        if(p1==pws_ret):
            if(len(data)>2):
                info(" Welcome, Login Success..\n")
                sub_imp()
                if(len(data[2])<8):
                    frame0.pack_forget()
                    return()        
                tsub.extend(data[2][6:-2].split(","))
                tpub.extend(data[3][6:-2].split(","))
                
            for i in range(len(tsub)):
                client.message_callback_add(tsub[i], subFunc)
                client.subscribe(tsub[i])
                tsub_btn.append(Button(frame3, text=tpub[i], command=lambda c=i: topD(c)))
                tsub_btn[i].place(x=5,y=5+50*i,width=40, height=40)
                msg_dict[tsub[i]]=""
            frame0.pack_forget()
        else:
            label_msg.configure(text=" Wrong Password, Try again")
    return

def topD(index):
    global cur_tpub
    frame2.pack(side=BOTTOM, fill=X)
    cur_tpub=tpub[index]
    msg_label.configure(text=msg_dict[tsub[index]])
    return
def info(m1=""):
    global cur_tpub
    cur_tpub=""
    frame2.pack_forget()
    global msg_info
    if(m1!=""):
        t1=time.localtime()
        msg_info+=str(time.strftime("%H:%M:%S",t1))+" :"+m1+"\n"
    msg_label.configure(text=msg_info)
    return

def eventNews(client, userdata, msg):
    info("<SerEv> "+msg.payload.decode("utf-8"))
    return
def authsend(tpub,pasw):
    client.publish("auth_to_ser",name+','+tpub+','+pasw)
    frame0.pack_forget()
    frame3.pack(side=RIGHT, fill=X)
    frame1.pack(side=TOP, fill=X)
    frame2.pack(side=BOTTOM, fill=X)
        
    return
def authrec(client, userdata, msg):
    #auth_ser@
    #tpub,tsub
    auth_ret=msg.payload.decode("utf-8").split(",")
    if(len(auth_ret)>0):
        tpub.append(auth_ret[0])
        tsub.append(auth_ret[1])
        i=(len(tsub)-1)
        client.message_callback_add(tsub[-1], subFunc)
        client.subscribe(tsub[-1])
        tsub_btn.append(Button(frame3, text=tpub[-1], command=lambda c=i: topD(c)))
        tsub_btn[-1].place(x=5,y=5+50*i,width=40, height=40)
        msg_dict[tsub[i]]=""
    return
def pubFunc():
    global msg_string
    global cur_tpub
    if(msg_entry.get()==""):
        return
    client.publish(cur_tpub,name+"<@>"+ msg_entry.get()+"\n")
    msg_entry.delete(0,'end')
    return
def addT():
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    
    label_msg.configure(text="Enter Topic Cred.")
    #configure topic
    button_ok.configure(command=lambda: authsend(text_name.get(), text_pass.get()))
    frame0.pack()
    return

def close_butt():
    if(fk==None):
        root.destroy()
        sys.exit()
    fk.truncate(0)
    #print("tsub",tsub)
    fk.write("name: "+name+"\n")
    fk.write("pass: "+pws+'\n')
    tmp=""
    for i in tsub:
        tmp+=i+","
    fk.write("tsub: "+tmp+'\n')
    tmp=""
    for i in tpub:
        tmp+=i+","
    fk.write("tpub: "+tmp+'\n')
    fk.close()
    root.destroy()
    sys.exit()

# -- .ps file ---
topic_names = []
cur_tpub=""
pws=""
tsub=[]
tpub=[]
tsub_btn=[]
msg_dict={}
msg_info=""
name =""
fk=None
#---frame 0--
root =Tk()
root.geometry('354x500')
root.title('lolChat>>>')
root.protocol("WM_DELETE_WINDOW", close_butt)
frame0=Frame(root, width=354, height=500, background='#ededed')
frame0.pack(side=TOP, fill=X)
label_msg=Label(frame0,text="Hello,\n Enter Your Credentials", font=("Times Roman",12),anchor=CENTER)
label_msg.place(x=105, y=120)
label_name=Label(frame0, text="Name: ",  font=("Times Roman",12))
label_name.place(x=55, y=180)
text_name=Entry(frame0, justify=LEFT, font=("", 12))
text_name.place(x=125, y=180, width=150)
label_pass=Label(frame0, text="Pass: ",  font=("Times Roman",12))
label_pass.place(x=55, y=230)
text_pass=Entry(frame0, justify=LEFT, font=("", 12))
text_pass.place(x=125, y=230, width=150)
button_ok=Button(frame0, text="Ok", command=lambda: check(text_name.get(), text_pass.get()) ,font=("", 12))
button_ok.place(x=150, y=270,width=50)



# client creation
client = mqtt.Client()
client.on_connect = on_connect
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
client.username_pw_set("example", "Example123")
client.connect("49d1a22e3af240efb207d443419e3257.s1.eu.hivemq.cloud", 8883)

   
t3=threading.Thread(target=client.loop_forever)
t3.daemon = True
t3.start()


frame1=Frame(root, width=304, height=420, background="#ededed")
#frame1_5=Frame(root, width= 304, height=29,background="#ededed")
frame2=Frame(root, width=304, height=50, background="#d4ffd4")
frame3=Frame(root, width=50, height=500,background="#d1dfea")
button_serv=Button(frame3, text="info", command=info)
button_addt=Button(frame3, text="+", command= addT)
button_serv.place(x=5, y=405, width=40, height=40)
button_addt.place(x=5, y=455, width=40, height=40)
frame3.pack(side=RIGHT, fill=X)
frame1.pack(side=TOP, fill=X)
msg_label=Label(frame1,text=msg_info, justify=LEFT,font=("Times Roman",12),anchor=W)
msg_label.place(x=5, y=5,width=294, height = 300 )



frame2.pack(side=BOTTOM, fill=X)
msg_entry = Entry(frame2,justify=LEFT, font=("", 14))
msg_button = Button(frame2, text=">>>",command=pubFunc)
msg_entry.place(x=5, y= 5, width=240, height = 40)
msg_button.place(x=254, y= 5, width=40, height = 40)


t2=threading.Thread(target=root.mainloop())
t2.daemon = True
t2.start()

