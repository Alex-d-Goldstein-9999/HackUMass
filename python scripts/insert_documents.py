import pymongo
from pymongo.server_api import ServerApi
import json
import certifi
import subprocess
import sys

ca = certifi.where()
cluster0 = pymongo.MongoClient("mongodb+srv://Alex:AlexIsCool123@cluster0.wg76som.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca, server_api=ServerApi('1'))

# halls = ["Berk", "Frank", "Woo", "Hamp"]
# hallsProperName = ["berkshire", "franklin", "worcester", "hampshire"]
meals = ["breakfast", "lunch", "dinner", "grabngo", "latenight"]

hall = sys.argv[1]
db=cluster0[hall]



for meal in meals:
    print(meal)
    collection_meal = meal
    collection = db[collection_meal]

    process = subprocess.Popen(['/usr/local/bin/node', '../Scrape scripts/%sScrape.js' % (meal), hall], stdout=subprocess.PIPE)
    document = process.stdout.read()

    print(document)


    jsonString = ""

    #query = {meal: {'$type' : 'array'}}
    
    with open('../Scrape data/%s/%s_%s.json' % (hall,hall,meal), 'r', encoding='utf-8') as json_data:
        for line in json_data:
            jsonString += line
            
        if (len(jsonString) > 15):
            objString = ""
            jsonString = jsonString[jsonString.index("[") + 1:]

            while True:
                try:
                    start = jsonString.index("{")
                    end = jsonString.index("}") + 1
                    objString = jsonString[start:end]

                    #load and upload
                    replace = json.loads(objString)
                    result = collection.insert_one(replace)

                    jsonString = jsonString[len(objString):]
                    jsonString = jsonString[jsonString.index("{"):]
                    objString =""
                except ValueError:
                    break




