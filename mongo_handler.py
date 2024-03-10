# mongo_handler.py
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

# Load environment variables
mongo_uri = os.getenv("MONGO_URI")
mongo_database = os.getenv("MONGO_DATABASE")

# Initialize MongoDB client
client = MongoClient(mongo_uri)
db = client[mongo_database]
collection = db["tinymce_data"]

def store_data_in_mongo(content):
    # Store content in MongoDB
    collection.insert_one({"content": content})
    print("Content stored in MongoDB successfully!")
