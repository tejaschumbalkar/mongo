from kafka import KafkaConsumer
import pymongo
import json
from json import loads

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["ml"]
mycol = mydb["openv"]

consumer = KafkaConsumer('openvswitch', bootstrap_servers='130.65.159.69:9092',value_deserializer=lambda v: json.loads(v.decode('utf-8')))
for message in consumer:
    print(message.value)
    mycol.insert_one(message.value)

