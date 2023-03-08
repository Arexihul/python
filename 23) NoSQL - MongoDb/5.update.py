import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient('mongodb+srv://arexihul:ICxOvgLgxsLw47up@cluster0.smc4esi.mongodb.net/test')

mydb = myclient["node-app"]
mycollection = mydb["products"]

# mycollection.update_one(
#     {"name": "Samsung S6"},
#     {"$set": {
#         "name": "Iphone 6"
#     }}
# )
# for i in mycollection.find():
#     print(i)

# mycollection.update_many(
#     {"name": "Samsung S7"},
#     {"$set": {
#         "name": "Iphone 7", "price": 5000
#     }}
# )
# for i in mycollection.find():
#     print(i)


query = {"name": "Samsung S8"}
newvalues = {"$set": {"name": "Iphone 8", "price": 7500}}
result = mycollection.update_many(query, newvalues)
print(f"{result.modified_count} record updated")
for i in mycollection.find():
    print(i)

