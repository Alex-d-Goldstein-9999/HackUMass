import pymongo
from pymongo.server_api import ServerApi
import certifi


ca = certifi.where()
cluster0 = pymongo.MongoClient("mongodb+srv://Alex:AlexIsCool123@cluster0.wg76som.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca, server_api=ServerApi('1'))
