import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient('mongodb+srv://arexihul:ICxOvgLgxsLw47up@cluster0.smc4esi.mongodb.net/test')

mydb = myclient["node-app"]
mycollection = mydb["products"]

# mycollection.delete_one({"name": "Samsung S10"})
# for i in mycollection.find():
#     print(i)

# mycollection.delete_many({"name": "Samsung S11"})
# for i in mycollection.find():
#     print(i)

# result = mycollection.delete_many({"name": {"$regex": "^S"}})
# print(f"{result.deleted_count} records deleted")
# for i in mycollection.find():
#     print(i)

result = mycollection.delete_many({})
print(f"{result.deleted_count} records deleted")
for i in mycollection.find():
    print(i)

