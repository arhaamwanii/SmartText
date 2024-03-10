import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson import json_util
import json

load_dotenv()

class MongoDBConnection:
    def __init__(self):
        self.db_uri = os.getenv("MONGODB_URI")
        self.db_name = os.getenv("DB_NAME")
        self.client = None
        self.db = None

    def connect(self):
        """Establish a connection to the MongoDB database."""
        try:
            self.client = MongoClient(self.db_uri)
            self.db = self.client[self.db_name]
            # Perform a quick check to see if the connection was successful
            self.client.admin.command('ping')
            print("MongoDB connection successful.")
        except ConnectionFailure:
            print("MongoDB connection failed.")
            self.client = None
            self.db = None

    def get_database(self):
        """Return the connected database."""
        if self.client and self.db:
            return self.db
        else:
            print("Database not connected. Call the connect method first.")
            return None

    def insert_data(self, collection_name, data):
        """Insert data into a specified collection within the database."""
        if not self.db:
            print("Database not connected. Call the connect method first.")
            return False
        
        try:
            collection = self.db[collection_name]
            result = collection.insert_one(json.loads(json_util.dumps(data)))
            print(f"Data inserted with record id {result.inserted_id}")
            return True
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
