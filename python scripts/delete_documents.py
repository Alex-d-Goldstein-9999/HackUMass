import pymongo
from pymongo.server_api import ServerApi
import certifi
import sys

hall = sys.argv[1]


if sys.argv[2] == "1":
    meals = ["breakfast-scores", "lunch-scores", "dinner-scores", "grabngo-scores", "latenight-scores"]
else:
    meals = ["breakfast", "lunch", "dinner", "grabngo", "latenight"]



print(meals)
ca = certifi.where()
cluster0 = pymongo.MongoClient("mongodb+srv://Alex:AlexIsCool123@cluster0.wg76som.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca, server_api=ServerApi('1'))
db = cluster0[hall]

for meal in meals:
    collection = db[meal]

    query = {"name" : {"$exists" : "true"}}
    collection.delete_many(query)