import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient('mongodb+srv://arexihul:ICxOvgLgxsLw47up@cluster0.smc4esi.mongodb.net/test')

mydb = myclient["node-app"]
mycollection = mydb["products"]

result = mycollection.find().sort("name")
result = mycollection.find().sort("name", -1)
result = mycollection.find().sort([("name", 1), ("price", -1)])

for i in result:
    print(i)