import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient('mongodb+srv://arexihul:ICxOvgLgxsLw47up@cluster0.smc4esi.mongodb.net/test')

mydb = myclient["node-app"]
mycollection = mydb["products"]

# filter = {"name":"Samsung S5"}

# result = mycollection.find(filter)

# for i in result:
#     print(i)

# result = mycollection.find_one({'_id': ObjectId('635ed42dcb4118fa59135ca0')})
# print(result)

# result = mycollection.find({
#     "name": {
#         "$in": ["Samsung S5", "Samsung S6"]
#     }
# })
# for i in result:
#     print(i)

# result = mycollection.find({
#     "price": {
#         "$gt": 4000     # $gte -> greater and equal  $eq -> equal  $lt  $lte
#     }
# })
# for i in result:
#     print(i)

result = mycollection.find({
    "name": {
        "$regex": "^S"  # S ile başlayan
    }
})
for i in result:
    print(i)
