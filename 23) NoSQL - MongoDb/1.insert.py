import pymongo

myclient = pymongo.MongoClient('mongodb+srv://arexihul:ICxOvgLgxsLw47up@cluster0.smc4esi.mongodb.net/test')


mydb = myclient["node-app"]
mycollection = mydb["products"]


# product = {"name":"Samsung S5", "price":2000}

# result = mycollection.insert_one(product)

# print(result)
# print(type(result))
# print(result.inserted_id)


# productList = [
#     {"name":"Samsung S6", "price":3000},
#     {"name":"Samsung S7", "price":4000},
#     {"name":"Samsung S8", "price":6000},
#     {"name":"Samsung S9", "price":7000},
#     {"name":"Samsung S10", "price":8000},
#     {"name":"Samsung S11", "price":9000}
# ]

# result = mycollection.insert_many(productList)
# print(result)
# print(type(result))
# print(result.inserted_ids)


# productList = [
#     {"_id":1, "name":"Samsung S6", "price":3000},
#     {"_id":2, "name":"Samsung S7", "price":4000},
#     {"_id":3, "name":"Samsung S8", "price":6000},
#     {"_id":4, "name":"Samsung S9", "price":7000},
#     {"_id":5, "name":"Samsung S10", "price":8000},
#     {"_id":6, "name":"Samsung S11", "price":9000}
# ]

# result = mycollection.insert_many(productList)
# print(result)
# print(type(result))
# print(result.inserted_ids)

productList = [
    {"name":"Samsung S6", "price":3000, "description":"good quality"},
    {"name":"Samsung S7", "price":4000, "categories": ['smartphone','electronics']}
]

result = mycollection.insert_many(productList)
