import threading
import sys
from tkinter import *

def pubFunc():
    print(msg_entry.get())
    return
def addT():
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    
    label_msg.configure(text="Enter Topic Cred.")
    #configure topic
    button_ok.configure(command=lambda: print(text_name.get(),text_pass.get()))
    frame0.pack()
    return
def check(n1, p1):
    if(name==n1 and pws==p1):
        frame0.pack_forget()
    else:
        label_msg.configure(text="Wrong Credentials")
    return
def serV():
    #server msg
    msg_string="21312"
    return
msg_string=""
name="1"
pws="1"
tpub=["t1","t2"]
tpub_btn=[]
root =Tk()
root.geometry('354x500')
root.title('lolChat>>> User: '+name)

#root.protocol("WM_DELETE_WINDOW", close_butt)
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

frame1=Frame(root, width=304, height=420, background="#ededed")
#frame1_5=Frame(root, width= 304, height=29,background="#ededed")
frame2=Frame(root, width=304, height=50, background="#d4ffd4")
frame3=Frame(root, width=50, height=500,background="#d1dfea")
for i in range(len(tpub)):
    tpub_btn.append(Button(frame3, text=tpub[i], command=lambda: print("hoho")))
    tpub_btn[i].place(x=5,y=5+50*i,width=40, height=40)
button_serv=Button(frame3, text="SERV", command=serV)
button_addt=Button(frame3, text="addT", command= addT)
button_serv.place(x=5, y=405, width=40, height=40)
button_addt.place(x=5, y=455, width=40, height=40)
frame3.pack(side=RIGHT, fill=X)
frame1.pack(side=TOP, fill=X)
msg_label=Label(frame1,text=msg_string, justify=LEFT,font=("Times Roman",12),anchor=W)
msg_label.place(x=5, y=5,width=294, height = 300 )



frame2.pack(side=BOTTOM, fill=X)
msg_entry = Entry(frame2,justify=LEFT, font=("", 14))
msg_button = Button(frame2, text=">>>",command=pubFunc)
msg_entry.place(x=5, y= 5, width=240, height = 40)
msg_button.place(x=254, y= 5, width=40, height = 40)


t2=threading.Thread(target=root.mainloop())
t2.daemon = True
t2.start()
