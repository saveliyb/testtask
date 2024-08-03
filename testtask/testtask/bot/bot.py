from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
import aiohttp
import os

API_URL = "http://web:8000/api/v1/messages/"

bot = Bot(token=os.getenv('TELEGRAM_BOT_TOKEN'))
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Привет! Я бот для работы с сообщениями.")


@dp.message(Command("get_messages"))
async def get_messages(message: types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.get(API_URL) as response:
            if response.status == 200:
                messages = await response.json()
                messages_text = "\n".join([msg.get('text', '') for msg in messages])
                await message.answer(messages_text)
            else:
                await message.answer("Не удалось получить сообщения")


@dp.message(Command("create_message"))
async def create_message(message: Message):
    text = message.text.split(" ", 1)[1]
    async with aiohttp.ClientSession() as session:
        async with session.post("http://web:8000/api/v1/message/", json={"text": text}) as response:
            if response.status == 200:
                await message.answer("Сообщение создано")
            else:
                await message.answer("Не удалось создать сообщение")


if __name__ == "__main__":
    dp.run_polling(bot)
