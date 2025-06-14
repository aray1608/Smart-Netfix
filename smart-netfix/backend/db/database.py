from pymongo import MongoClient
import os

# MongoDB connection URI (default localhost)
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

# Initialize MongoDB client
client = MongoClient(MONGO_URI)

# Access your DB (create if doesn't exist)
db = client["smart_netfix"]
