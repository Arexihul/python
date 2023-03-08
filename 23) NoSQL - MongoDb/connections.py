import pymongo

# myclient = pymongo.MongoClient('mongodb://localhost:27017')
myclient = pymongo.MongoClient('mongodb+srv://arexihul:ICxOvgLgxsLw47up@cluster0.smc4esi.mongodb.net/test')


mydb = myclient["node-app"]

print(mydb.list_collection_names())
