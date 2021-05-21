from os import renames
import pymongo

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# mydb = myclient["mydatabase"]
# mycol = mydb['customers']


# ddic = {"password":"ayush_pass"}
# mycol.insert_one(ddic)
# ddic = {'tsub': 'ayush_sr'}
# mycol.insert_one(ddic)
# ddic = {'tsub':'anime_sr'}
# mycol.insert_one(ddic)
# ddic = {'tpub': 'ayush'}
# mycol.insert_one(ddic)
# ddic = {'tpub':'anime'}
# mycol.insert_one(ddic)
# # tpub: ayush,anime,


# x = mycol.insert_one(ddic)
# y = mycol.find_one()
# print(y)
# res = mycol.find({'name':'Ayush'})
# print(list(res))
# print(type(res))
# ls = []
# for d in res:
#     del(d['_id'])
#     ls.append(d)

# print(ls)
# print(myclient.list_database_names())
# print(mydb.list_collection_names())
# print(x.inserted_id)


class Db:
    
    def __init__(self,dbname):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client[dbname]
        
    def s_table(self,tname):
        self.col = self.db[tname]

    def inData(self,data):
        self.col.insert_one(data)

    def outData(self,query = None):
        res = []
        for d in self.col.find(query):
            del(d['_id'])
            res.append(d)
        return res

class Serdb:

    def __init__(self):
        self.db = Db("msgapp")

    def addMsg(self,topic,sender,msg,tme):
        self.db.s_table(topic)
        self.db.inData({'sender':sender,'msg':msg, 'time':tme})
    
    def getMsg(self,topic):
        self.db.s_table(topic)
        return self.db.outData()

    def addTU(self,topic,user):
        self.db.s_table('topic_user')
        self.db.inData({'topic':topic,'user':user})

    def getTU(self,topic):
        self.db.s_table('topic_user')
        res = []
        for d in self.db.outData({'topic':topic}):
            res.append(d['user'])
        return res

    def getTUu(self,field):
        self.db.s_table('topic_user')
        res = {}
        for d in self.db.outData():
            res.add(d[field])
        return list(res)

    def addPass(self,topic,password):
        self.db.s_table('topic_pass')
        self.db.inData({'topic':topic,'password':password})

    def getPass(self,topic):
        self.db.s_table('topic_pass')
        for d in self.db.outData({'topic':topic}):
            return d['password']

class Clidb:

    def __init__(self):
        self.db = Db("cmsgapp")

    def addData(self,user,field,value):
        self.db.s_table(user)
        self.db.inData({'field':field,'value':value})

    def getData(self,user,field):
        res = []
        self.db.s_table(user)
        for d in self.db.outData({'field':field}):
            res.append(d['value'])
        return res
    



    def userE(self,name):
        return name in self.db.db.list_collection_names()


