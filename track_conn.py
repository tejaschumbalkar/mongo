from kafka import KafkaConsumer
import pymongo
import json
from json import loads

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["ml"]
mycol = mydb["output"]
myattk = mydb["attack"]
mytrk = mydb["trackconn"]

count = 0
consumer = KafkaConsumer('test', bootstrap_servers='130.65.159.69:9092',value_deserializer=lambda v: json.loads(v.decode('utf-8')))
for message in consumer:
    print(message.value)
    mycol.insert_one(message.value)

    #update the trackconn 
    sid = message.value['src_ip']+"-"+message.value['dst_ip']
    print('sid ',sid)
    result = message.value['result']
    print('result ',result)

    myquery = {"id":sid}
    mydoc = mytrk.find(myquery)

    if mydoc.count() == 1:
        print('query update')
        for x in mydoc:

            cnt = x['count']

            if result == 0:
                print('query result update',0)
                mytrk.update({'id':sid},{'$set':{'count':0}})
            
            else:
                temp_cnt = cnt + 1
                print('temp_cnt',temp_cnt)
                if temp_cnt >= 100:
                    mytrk.update({'id':sid},{'$set':{'count':0}})
                else:
                    mytrk.update({'id':sid},{'$set':{'count':temp_cnt}})
    else:
        print('new')
        obj = {}
        obj['id'] = message.value['src_ip']+"-"+message.value['dst_ip']
        
        if result == 1:
            obj['count'] = 1
        else:
            obj['count'] = 0
        print('insert',obj)
        mytrk.insert_one(obj)




    
 

    
