import paho.mqtt.client as mqtt
import threading
import time
from tkinter import *
from widgetstk import *
import sys
from dbMMongo import *

def on_connect(client, userdata, flags, rc):
    if rc != 0:
        print("Connect returned result code: " + str(rc))
    return
def loginevent(client, userdata, msg):
    global msg_card
    tmp =msg.payload.decode("utf-8").split('$')
    if tmp[0] not in msg_card:
        msg_card[tmp[0]] = []
    msg_card[tmp[0]].append(msgLbl(frame1,tmp[1],tmp[2]))
    #topic_name$sender_name$msg
    return 
def subFunc(client, userdata, msg):
    global cur_tpub,msg_card
    temp = msg.payload.decode("utf-8").split('$')
    print(temp)

    if msg.topic[:-3] not in msg_card:
        msg_card[msg.topic[:-3]] = []
    msg_card[msg.topic[:-3]].append(msgLbl(frame1,temp[0],temp[1]))

    if(cur_tpub==msg.topic[:-3]):
    # msg_label.configure(text=msg_dict[msg.topic])
        
        column = 1
        if temp[0] == name:
            column = 2

        msg_card[msg.topic[:-3]][-1][0].grid(column = column,row =len(msg_card[msg.topic[:-3]]))
        # msg_dict[msg.topic]+=temp
        print(len(msg_card[msg.topic[:-3]]))

    return
def sub_imp():
    client.message_callback_add("auth_ser@"+name, authrec)
    client.message_callback_add("serv@"+name, eventNews)
    client.message_callback_add("login@"+name, loginevent)
    client.subscribe("auth_ser@"+name)
    client.subscribe("serv@"+name)
    client.subscribe("login@"+name)
    return
def check(n1, p1):
    global name, pws , tpub , tsub
    name = n1
    root.title('User: '+name)
    # fk = open(n1+".ps","a+")
    datab = Clidb()
    # fk.seek(0,0)
    if(not datab.userE(n1)):
        #sign up 

        datab.addData(n1,'password',p1)
        pws=p1
        # fk.write("name: "+n1+'\n')//6
        # fk.write("pass: "+p1+'\n')
        info(" Welcome, SignUp Success..\n")
        sub_imp()
        switchmain()
    else:
        #login
        # fk.seek(0,0)
        # data = fk.readlines()
        # pws_ret=data[1][6:-1]
        pws_ret = datab.getData(n1,'password')[0]
        pws=pws_ret
        if(p1==pws_ret):
            # if(len(data)>2):
            client.publish('login_succ',name)
            info(" Welcome, Login Success..\n")
            sub_imp()
            tsub = datab.getData(n1,'tsub')
            tpub = datab.getData(n1,'tpub')

            if(len(tsub) == 0):
                switchmain()
                return()       
                #add values in tsub and tpub list 
            
            for i in range(len(tsub)):
                client.message_callback_add(tsub[i], subFunc)
                client.subscribe(tsub[i])
                tsub_btn.append(scrButton(frame3,tpub[i],lambda c=i: topD(c),i+3))
                # tsub_btn.append(Button(frame3, text=tpub[i], command=lambda c=i: topD(c)))
                # tsub_btn[i].place(x=5,y=5+50*i,width=40, height=40)
                msg_dict[tsub[i]]=""
            switchmain()
            # client.publish('login_succ',name)
        else:
            label_msg.configure(text="Try Again!")
    return

def topD(index):
    global cur_tpub, tsub_btn, cur_tpub_btn
    frame2.place(x = 230,y = 640,width=640,height=60)
    # msg_frm.pack_forget()
    if cur_tpub_btn != '':
        cur_tpub_btn.config(bg = secCol,fg = '#a7c0cd')
    tsub_btn[index].config(bg = whiteCol,fg = secCol)
    cur_tpub_btn = tsub_btn[index]
    if cur_tpub in msg_card:
        for card in msg_card[cur_tpub]:
            card[0].grid_forget()
    cur_tpub=tpub[index]
    if cur_tpub in msg_card:
        count = 1   
        for card in msg_card[cur_tpub]:
            clm = 1
            if card[1].cget("text") == name:
                clm = 2
            card[0].grid(row = count,column = clm)
            count+=1
    # msg_frm.pack_forget()
    return

def info(m1=""):
    global cur_tpub
    cur_tpub=""
    frame2.pack_forget()
    global msg_info
    if(m1!=""):
        t1=time.localtime()
        msg_info+=str(time.strftime("%H:%M:%S",t1))+" $"+m1+"\n"
    msg_data = msg_info.split('$')
    # msg_frm.pack(side = TOP)
    # msg_user.configure(text=msg_data[0])
    # msg_label.configure(text=msg_data[1])
    return

def eventNews(client, userdata, msg):
    info("<SerEv> "+msg.payload.decode("utf-8"))
    return


def authsend(tpub,pasw):
    client.publish("auth_to_ser",name+','+tpub+','+pasw)
    frame0.pack_forget()
    root.geometry('800x700') #dfg
    # canvasf3.pack(side=tk.LEFT)
    # sb_f3.pack(side=tk.LEFT, fill='y')
    # frame3.pack(side=LEFT, fill=X)
    scroll_f.pack(side=LEFT, fill="both")
    # frame1.pack(side=TOP, fill=X)
    sf_1.place(x=230,y = 0)
    frame2.place(x = 230,y = 640,width=640,height=60)

def authrec(client, userdata, msg):
    #auth_ser@
    #tpub,tsub
    global name
    auth_ret=msg.payload.decode("utf-8").split(",")
    if(len(auth_ret)>0):
        datab = Clidb()
        datab.addData(name,'tpub',auth_ret[0])
        datab.addData(name,'tsub',auth_ret[1])
        tpub.append(auth_ret[0])
        tsub.append(auth_ret[1])
        i=(len(tsub)-1)
        client.message_callback_add(tsub[-1], subFunc)
        client.subscribe(tsub[-1])
        # tsub_btn.append(Button(frame3, text=tpub[-1], command=lambda c=i: topD(c)))
        tsub_btn.append(scrButton(frame3,tpub[-1],lambda c=i: topD(c),i+3))
        # tsub_btn[-1].place(x=5,y=5+50*i,width=40, height=40) 0,5+50*i,350,60
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
    sf_1.place_forget()
    # frame1.pack_forget()
    frame2.pack_forget()
    # frame3.pack_forget()
    scroll_f.forget()
    root.geometry('600x500')
    # canvasf3.pack_forget()
    # sb_f3.pack_forget()
    label_msg.configure(text="Enter Topic Cred.")
    #configure topic
    
    button_ok.configure(command=lambda: authsend(name_field.get(), pass_field.get()),text='OK')
    frame0.pack()
    return

def close_butt():
    root.destroy()
    sys.exit()
    # fk.truncate(0)
    # #print("tsub",tsub)
    # fk.write("name: "+name+"\n")
    # fk.write("pass: "+pws+'\n')
    # tmp=""
    # for i in tsub:
    #     tmp+=i+","
    # fk.write("tsub: "+tmp+'\n')
    # tmp=""
    # for i in tpub:
    #     tmp+=i+","
    # fk.write("tpub: "+tmp+'\n')
    # fk.close()
    root.destroy()
    sys.exit()

def switchmain():
    frame0.pack_forget()
    root.geometry('800x700') #dfg
    sf_1.place(x=230,y = 0)


# -- .ps file ---
topic_names = []
cur_tpub=""
cur_tpub_btn = ''
pws=""
tsub=[]
tpub=[]
tsub_btn=[]
msg_dict={}
msg_card = {}
msg_info=""
name =""
# fk=None
#---frame 0--
root =Tk()
root.geometry('600x500')
root.title('lolChat>>>')
root.protocol("WM_DELETE_WINDOW", close_butt)
frame0=Frame(root, width=600, height=500, background=bkcolor)
frame0.pack(side=TOP, fill=X)
#root.resizable(width=False, height=False)
label_msg=createLbl(frame0,"USER LOGIN",CENTER)
label_msg.place(x=200, y=100)
text_name,name_field=tf(frame0,'Username')
text_name.place(x=150, y=180, width=300)
text_pass,pass_field=tf(frame0,'Password',passtf = True)
text_pass.place(x=150, y=230, width=300)
button_ok=Button(frame0, text="CONNECT", relief=tk.FLAT,borderwidth=0,command=lambda: check(name_field.get() ,pass_field.get()), bg = '#006064' , fg = whiteCol,font = ('Calibri',18,))
button_ok.place(x=150, y=300,width=300,height = 50)



# client creation
client = mqtt.Client()
client.on_connect = on_connect
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
client.username_pw_set("example", "Example123")
client.connect("49d1a22e3af240efb207d443419e3257.s1.eu.hivemq.cloud", 8883)

   
t3=threading.Thread(target=client.loop_forever)
t3.daemon = True
t3.start()

# frame1=Frame(root, width=500, height=500, background="#0000aa")
sf_1 = ScrolledFrame(root, width=550, height=634,scrollbars = 'vertical')
# sf_1.place(x=350,y = 0)
frame1 = sf_1.display_widget(Frame)
#frame1_5=Frame(root, width= 304, height=29,background="#ededed")s
frame2=Frame(root, width=304, height=50, background=bkcolor)

# canvasf3,sb_f3 = scrframe(root)
frame3,scroll_f = scrframe(root)
# frame3 = Frame(canvasf3, width=350, height=700,background="#00aa00")
# canvasf3.create_window((0,0), window=frame3, anchor='nw')

# button_serv = scrButton(frame3,'info',info,1)
button_addt=scrButton(frame3, "Add Topic", addT,2)
button_addt.config(bg="#a7c0cd", fg= "#000a12")
# frame3.pack(side=LEFT, fill=X)
# frame1.pack(side=TOP, fill=X)
# msg_frm,msg_user,msg_label=msgLbl(frame1,msg_info,msg_info)
# msg_label.pack(side= TOP)



# frame2.place(x = 360,y = 640,width=640,height=60)
msg_entry = Entry(frame2,justify=LEFT, font=("", 14),relief=FLAT,borderwidth=10)
msg_button = Button(frame2, text=">>>",command=pubFunc)
msg_entry.place(x = 15,y = 5, width=470,height= 45)
msg_button.place(x = 497,y = 5,width = 60,height=45)


t2=threading.Thread(target=root.mainloop())
t2.daemon = True
t2.start()

