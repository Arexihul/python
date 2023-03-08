import pymongo

myclient = pymongo.MongoClient('mongodb+srv://arexihul:ICxOvgLgxsLw47up@cluster0.smc4esi.mongodb.net/test')

mydb = myclient["node-app"]
mycollection = mydb["products"]

# result = mycollection.find_one()
# print(result)

# for i in mycollection.find():
#     print(i)

# for i in mycollection.find({},{"_id":0}):
#     print(i)

for i in mycollection.find({},{"name":0}):
    print(i)

# for i in mycollection.find({},{"_id":0, "name":1, "price":1}):
#     print(i)


