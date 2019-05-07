from kafka import KafkaConsumer
import pymongo
import json
from json import loads

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["ml"]
mycol = mydb["messages"]
count = 0
consumer = KafkaConsumer('test', bootstrap_servers='130.65.159.69:9092',value_deserializer=lambda v: json.loads(v.decode('utf-8')))
for message in consumer:
    print(message.value)
    '''
    mycol.insert_one(message.value)
    count +=1
    if count == 10:
        mycol.insert_one({'attack':count})
        count = 0
    ''' 
