import pymongo
from pymongo.server_api import ServerApi
import certifi
import sys
import re
import json
# from firebase_admin import credentials
# from firebase_admin import firestore

regexStipLetters = re.compile(r'[^\d.]+')


def makeNum(expr):
    try:
        if "mg" in expr:
            num = float(regexStipLetters.sub('', expr)) 
            return num * 0.001
        return float(regexStipLetters.sub('', expr)) 
    except ValueError:
        return 0

# cred = credentials.Certificate("./unutrition-d9755-firebase-adminsdk-cbryz-71439ab5f4.json")
# default_app = firebase_admin.initialize_app(cred)


meal = sys.argv[1]
hall = sys.argv[2]

ca = certifi.where()
cluster0 = pymongo.MongoClient("mongodb+srv://Alex:AlexIsCool123@cluster0.wg76som.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca, server_api=ServerApi('1'))
db = cluster0[hall]
dbToUpload = cluster0[hall + "-scores"]
collection = db[meal]
collectionToUpload = dbToUpload[meal + "-scores"]

foods = collection.find({})



#indexes for keys
# 1: name 
# 2: serving size 
# 3: calories
# 4: total_fat
# 5: total_carbohydrates
# 6: cholesterol
# 7: sodium
# 8: sugar
# 9: fiber
# 10: protein


bodyweight = float(sys.argv[3]) * 2.20462

#grams
dailyRecommendedValues = {"calories":2000.0, "fat":75.0, "carbohydrates":275.0, "sugar":30.0, "Fiber":30.0, "Cholesterol":0.3, "sodium":2.3, "protein":(0.75 * bodyweight)}



for m in foods:

    
    #determine how good the serving is for calories
    recommendedServingCalories = dailyRecommendedValues['calories'] / 9.0
    servingCalories = m['calories']
    percentDiff_Cal = (abs(makeNum(servingCalories) - recommendedServingCalories)) / (recommendedServingCalories)
    calorieScore = float(min(1, percentDiff_Cal))

    #determine how good the serving is for fats
    recommendedServingFat = dailyRecommendedValues['fat'] / 9.0
    servingFat = m['total_fat']
    diff_Fat = makeNum(servingFat) / recommendedServingFat
    fatScore = float(min(1,diff_Fat))

    #determine how good the serving is for carbohydrates
    recommendedCarbohydrates = dailyRecommendedValues["carbohydrates"] / 9.0
    servingCarbohydrates = m['total_carbohydrates']
    percentDiff_Carb = (abs(makeNum(servingCarbohydrates) - recommendedCarbohydrates)) / (recommendedCarbohydrates)
    carbScore = float(min(1,percentDiff_Carb))
    
    #determine how good the serving is for sugar
    recommendedServingSugar = dailyRecommendedValues["sugar"] / 9.0
    servingSugar = m['sugar'] 
    diff_sugar = (makeNum(servingSugar) / recommendedServingSugar)
    sugarScore = float(min(1, diff_sugar))

    #determine how good the serving is for fiber
    recommendedServingFiber = dailyRecommendedValues["Fiber"] / 9.0
    servingFiber = m['fiber']
    percentDiff_Fiber = (abs(makeNum(servingFiber) - recommendedServingFiber)) / (recommendedServingFiber)
    fiberScore = float(min(1, percentDiff_Fiber))

    #cholersterol 
    recommendedServingCholesterol = dailyRecommendedValues["Cholesterol"] / 9.0
    servingCholesterol = m['cholesterol']
    diff_Cholesterol = (makeNum(servingCholesterol) / recommendedServingCholesterol)
    cholesterolScore = float(min(1, diff_Cholesterol))

    #sodium 
    recommendedServingSodium = dailyRecommendedValues["sodium"] / 9.0
    servingSodium = m['sodium']
    diff_Sodium = (makeNum(servingSodium) / recommendedServingSodium)
    sodiumScore = float(min(1, diff_Sodium))

    #protein
    recommendedServingProtein = dailyRecommendedValues["protein"] / 9.0
    servingProtein = m['protein']
    percentDiff_Protein = (abs(makeNum(servingProtein) - recommendedServingProtein)) / (recommendedServingProtein)
    proteinScore = float(min(1, percentDiff_Protein))
    

    name = m['name']


    object = {
        "name" : name,
        "calorie score" : calorieScore,
        "fat score" : fatScore,
        "carbohydrate score" : carbScore,
        "cholesterol score" : cholesterolScore,
        "sodium score" : sodiumScore,
        "sugar score" : sugarScore,
        "fiber score" : fiberScore,
        "protein score" : proteinScore
    }

    jsonObject = json.dumps(object, indent=4)

    result = collectionToUpload.insert_one(object)
    print(result)

    # db = firestore.client()
    # db.collection("%s_%s" % (hall, meal)).document(name.replace("/", "_")).set(object)
    





        
    









