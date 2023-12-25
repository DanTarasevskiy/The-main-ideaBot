import asyncio
import logging

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
from aiogram.filters import CommandStart, Command

from transformers import pipeline

summarizer = pipeline("summarization", model="Falconsai/text_summarization")

BOT_TOKEN = "6858437857:AAHa2dww9ZTYFdVtYHPAV7EUKsBDAMZgkaU"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message()
async def echo_message(message: types.Message):

    await bot.send_message(
        chat_id=message.chat.id,
        text=(str(summarizer(str(message), max_length=400, min_length=100, do_sample=False)).strip("[{'summary_text': '").rstrip("'}]")),
    )

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
