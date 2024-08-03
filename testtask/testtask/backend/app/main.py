from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient

app = FastAPI()

client = MongoClient("mongodb://mongo:27017/")
db = client.messages_db
messages_collection = db.messages


class Message(BaseModel):
    text: str


@app.get("/api/v1/messages/")
async def get_messages():
    messages = list(messages_collection.find({}, {"_id": 0}))
    return messages


@app.post("/api/v1/message/")
async def create_message(message: Message):
    result = messages_collection.insert_one(message.dict())
    return {"inserted_id": str(result.inserted_id)}
