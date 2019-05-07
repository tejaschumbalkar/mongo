import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["ml"]
#mycol = mydb["attack"]
mycol = mydb["output"]
'''
mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]
'''
for x in mycol.find():
  print(x)

#x = mycol.insert_many(mylist)
'''
myquery = { "src_ip": "10.0.2.3" }

mydoc = mycol.find(myquery)
print(mydoc.count())
for x in mydoc:
  print(x)
for i in mycol.find():
    print(i)
'''
