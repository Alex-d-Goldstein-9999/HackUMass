import pymongo
from pymongo.server_api import ServerApi
import json
import certifi
import subprocess
import sys

ca = certifi.where()
hall = sys.argv[1]
meal = sys.argv[2]

keyWords = {
    "low calories" : [0, False],
    "low fat" : [0, False],
    "low carb" : [0, False],
    "low cholesterol": [0, False],
    "low sodium" : [0, False],
    "low sugar": [0, False],
    "high fiber": [0, False],
    "high protein": [0, False]
}

wordAssociation = {
    "low calories" : "calorie score",
    "low fat" : "fat score",
    "low carb" : "carbohydrate score",
    "low cholesterol": "cholesterol score",
    "low sodium" : "sodium score",
    "low sugar": "sugar score",
    "high fiber": "fiber score",
    "high protein": "protein score"

}


def get_key(val, my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key
        
#assign ranked choices
prefs = 0
for index, arg in enumerate(sys.argv):
    if arg in keyWords.keys():
        keyWords[arg] = [index - 2, True]
        prefs += 1
    


cluster0 = pymongo.MongoClient("mongodb+srv://Alex:AlexIsCool123@cluster0.wg76som.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca, server_api=ServerApi('1'))
db = cluster0[hall + "-scores"]
collection = db[meal + "-scores"]

#possible_foods = list(collection.find({}))


query = {}

#generate all possible foods
for index in range(prefs):
    queryWord = wordAssociation[get_key([index + 1, True], keyWords)]
    boolean = (queryWord == "protein score" or queryWord == 'fiber score')

    if (queryWord == "protein score" or queryWord == 'fiber score' or queryWord == 'calorie score'):
        query[queryWord] =  {"$gt" : 0.75}
    else:
        query[queryWord] =  {"$lt" : 0.5}

    

result = collection.find(query)
suggested_foods = list(result)
final_foods = []

for food in suggested_foods:
    final_foods.append(food['name'])
    
print(final_foods)







    



