# mongo_handler.py
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

mongo_uri=your_mongo_connection_uri
mongo_database=your_database_name


# Load environment variables
mongo_uri = os.getenv("mongo_uri")

# Initialize MongoDB client
client = MongoClient(mongo_uri)
db = client[os.getenv("mongo_database")]  # Load the database name from environment variables
collection = db["tinymce_data"]  # Collection to store TinyMCE data

def store_data_in_mongo(content):
    # Store content in MongoDB
    collection.insert_one({"content": content})
    print("Content stored in MongoDB successfully!")
