import openai
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command

# Tokenlarni shu yerga qo‘ying
TELEGRAM_BOT_TOKEN = "7672420157:AAFEuXNxT13dzBJws9CBE5iYBPqwaCnSeNM"
OPENAI_API_KEY = "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"

# OpenAI API sozlamalari
openai.api_key = OPENAI_API_KEY

# Aiogram bot va dispatcher
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

# Start buyrug'iga javob
@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Salom! Men OpenAI bilan bog‘langan Telegram botiman. Savollaringizni yozing!")

# Foydalanuvchi xabariga javob
@dp.message()
async def chat_with_ai(message: Message):
    user_text = message.text
    
    # OpenAI orqali javob olish
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content": user_text}]
    )

    # ChatGPT javobi
    bot_reply = response["choices"][0]["message"]["content"]
    
    await message.answer(bot_reply)

# Botni ishga tushirish
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
