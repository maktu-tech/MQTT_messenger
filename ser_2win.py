import time
import threading
import paho.mqtt.client as mqtt
def on_connect(client, userdata, flags, rc):
    if rc != 0:
        print("Connect returned result code: " + str(rc))
    return
def auth(client, userdata, msg):
    global ser
    # _sr is "ser to user" => user subscribe it
    tmp = msg.payload.decode("utf-8").split(",")

    if(tmp[1] in ser):
        if(tmp[2]==ser[tmp[1]][0]):
            if(tmp[0] not in ser[tmp[1]][1:]):
                ser[tmp[1]].append(tmp[0])
                client.publish("serv@"+tmp[0],"Added to topic\n")
                client.publish("auth_ser@"+tmp[0],tmp[1]+","+tmp[1]+'_sr')
                print(ser)
                print("ok tillif")
            else:
                client.publish("serv@"+tmp[0],"Already added!\n")    
        else:
            client.publish("serv@"+tmp[0],"Wrong Password\n")
    else:
        ser[tmp[1]]=[tmp[2],tmp[0]]
        client.publish("serv@"+tmp[0],"Topic Created\n")
        client.publish("auth_ser@"+tmp[0],tmp[1]+","+tmp[1]+'_sr')
        client.message_callback_add(tmp[1],ser_pub)
        client.subscribe(tmp[1])
        print(ser)
        print("ok tillelse")
    return
def ser_pub(client, userdata, msg):
    global ser
    # message
    # user<@>message will be .....
    tmp=msg.payload.decode("utf-8").split("<@>")
    for key in ser:
        if(key==msg.topic and  tmp[0] in ser[key][1:]):
            if(len(tmp)>2):
                for i in range(2,len(tmp),1):
                    tmp[1]+="<@>"
                    tmp[1]+=tmp[i]
            client.publish(key+'_sr',""+tmp[0]+"$"+tmp[1])
            return
    client.publish("serv@"+tmp[0],"Not added to topic "+tmp[0]+"\n")
    return
def time_pass():
    #server active time
    time.sleep(600)
    client.disconnect()
    fs.truncate(0)
    for key in ser:
        tmp=""
        for i in ser[key]:
            tmp+=i+','
        fs.write(key+":"+ tmp+'\n')
    fs.close()
    return
start_time=time.time()
ser={}
fs = open("server.ps", 'a+')
fs.seek(0,0)
ser_list=fs.readlines()
# topic_name:paswd,member1,member2,\n
# topic_name_sr
# TODO: auth for unique name is not added now
if(ser_list!=[]):
    for i in ser_list:
        tmp = i[0:-2].split(":")
        ser[tmp[0]]=tmp[1].split(",")

client = mqtt.Client()
client.on_connect = on_connect
for key in ser:
    client.message_callback_add(key,ser_pub)
client.message_callback_add("auth_to_ser",auth)

client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
client.username_pw_set("example", "Example123")
client.connect("49d1a22e3af240efb207d443419e3257.s1.eu.hivemq.cloud", 8883)
client.subscribe("auth_to_ser")
for key in ser:
    client.subscribe(key)
#client.publish("serv@1")
t1 = threading.Thread(target=client.loop_forever)
t2 = threading.Thread(target=time_pass)
t2.start()
t1.start() 


