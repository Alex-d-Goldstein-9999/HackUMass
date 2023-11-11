import pymongo
from pymongo.server_api import ServerApi
import json
import certifi
import sys
import subprocess


ca = certifi.where()
cluster0 = pymongo.MongoClient("mongodb+srv://Alex:AlexIsCool123@cluster0.wg76som.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca, server_api=ServerApi('1'))

db=cluster0["Halls"]

collection_hall = sys.argv[1]
hall = sys.argv[2]
collection = db[collection_hall]

meals = ["breakfast", "lunch", "dinner", "grabngo", "latenight"]

for meal in meals:
    process = subprocess.Popen(['/usr/local/bin/node', '../dining scrape (using cmdline args)/%sScrape.js' % (meal), hall], stdout=subprocess.PIPE)
    document = process.stdout.read()



for meal in meals:
    jsonString = ""

    query = {meal: {'$type' : 'array'}}

    with open('../dining scrape/%s/%s_%s.json' % (hall,hall,meal), 'r', encoding='utf-8') as json_data:
        # iterate over the _io.TextIOWrapper returned by open() using enumerate()
        for i, line in enumerate(json_data):
            # append the parsed IO string to the JSON string
            jsonString += line
    
    if (jsonString != '{}'):
        replacement_doc = json.loads(jsonString)
        result = collection.replace_one(query,replacement_doc)



