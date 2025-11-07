from pymongo import MongoClient

mongoDbUrl=""
port=8000
client = MongoClient(mongoDbUrl, port)
db = client["autism_spectrum"]

