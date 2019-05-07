from kafka import KafkaProducer
import json
from json import dumps 
producer = KafkaProducer(bootstrap_servers='130.65.159.69:9092',value_serializer=lambda v: json.dumps(v).encode('utf-8'))
for i in range(100):
    data = {'number' : i}
    producer.send('test', data).get(timeout=30)
