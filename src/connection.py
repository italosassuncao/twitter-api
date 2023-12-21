from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://italosassuncao:**********@twitterapi.qdunzu2.mongodb.net/?retryWrites=true&w=majority")

db = client.tweeApi

users_collection = db.users
