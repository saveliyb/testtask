from pymongo import MongoClient
from models import Message
import os

client = MongoClient(os.getenv('MONGO_URI'))
db = client["messages_db"]
collection = db["messages"]


async def get_all_messages():
    return list(collection.find({}, {"_id": 0}))


async def create_message(message: Message):
    result = collection.insert_one(message.dict())
    return {"inserted_id": str(result.inserted_id)}
