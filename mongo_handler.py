# mongo_handler.py
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

# Load environment variables
mongo_uri = os.getenv("mongo_uri")

# Initialize MongoDB client
client = MongoClient(mongo_uri)
db = client["your_database_name"]  # Change "your_database_name" to your desired database name
collection = db["tinymce_data"]  # Collection to store TinyMCE data

def store_data_in_mongo(content):
    # Store content in MongoDB
    collection.insert_one({"content": content})
    print("Content stored in MongoDB successfully!")
load_dotenv()

# Load environment variables
tinymce_key = os.getenv("tiny")
openai_key = os.getenv("openai")
mongo_uri = os.getenv("mongo_uri")

# Initialize MongoDB client
client = MongoClient(mongo_uri)
db = client["your_database_name"]  # Change "your_database_name" to your desired database name
collection = db["tinymce_data"]  # Collection to store TinyMCE data

tinymce_ai_html = f"""
<!-- Your existing TinyMCE initialization code -->
"""

def store_data_in_mongo(content):
    # Store content in MongoDB
    collection.insert_one({"content": content})
    st.success("Content stored in MongoDB successfully!")

def main():
    st.title("Streamlit with TinyMCE AI Assistant")

    # Use the `components.html` method to embed the TinyMCE with AI Assistant feature
    components.html(tinymce_ai_html, height=500, scrolling=True)

    if st.button("Save Content to MongoDB"):
        editor_content = st.execute_js("tinymce.activeEditor.getContent();")
        store_data_in_mongo(editor_content)

if __name__ == "__main__":
    main()


tinymce_ai_html = """
<!-- Your existing TinyMCE initialization code -->
"""

def main():
    st.title("Streamlit with TinyMCE AI Assistant")

    # Use the `components.html` method to embed the TinyMCE with AI Assistant feature
    components.html(tinymce_ai_html, height=500, scrolling=True)

    if st.button("Save Content to MongoDB"):
        editor_content = st.execute_js("tinymce.activeEditor.getContent();")
        store_data_in_mongo(editor_content)

if __name__ == "__main__":
    main()
