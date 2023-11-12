import pymongo
from pymongo.server_api import ServerApi
import certifi
import sys

hall = sys.argv[1]
meals = ["breakfast", "lunch", "dinner", "grabngo", "latenight"]

ca = certifi.where()
cluster0 = pymongo.MongoClient("mongodb+srv://Alex:AlexIsCool123@cluster0.wg76som.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca, server_api=ServerApi('1'))
db = cluster0[hall]

for meal in meals:
    collection = db[meal]

    query = {"name" : {"$exists" : "true"}}

    collection.delete_many(query)