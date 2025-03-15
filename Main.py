import os
import logging
from flask import Flask, request
import openai
import telebot

# Telegram va OpenAI API kalitlarini olish
TELEGRAM_TOKEN = os.getenv("7672420157:AAFEuXNxT13dzBJws9CBE5iYBPqwaCnSeNM")
OPENAI_API_KEY = os.getenv("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")

# Kutubxonalarni sozlash
bot = telebot.TeleBot(TELEGRAM_TOKEN)
openai.api_key = OPENAI_API_KEY

# Flask serverini yaratish
app = Flask(__name__)

# Telegram webhook uchun endpoint
@app.route("/webhook", methods=["POST"])
def webhook():
    json_str = request.get_data().decode("UTF-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "!", 200

# Botga kelgan xabarlarni OpenAI bilan qayta ishlash
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        response = openai.Chat.create(
            model="gpt-4",
            messages=[{"role": "user", "content": message.text}]
        )
        bot.reply_to(message, response.choices[0].message["content"])
    except Exception as e:
        bot.reply_to(message, "Xatolik yuz berdi. Keyinroq urinib ko‘ring.")
        logging.error(f"OpenAI xatosi: {e}")

# Flask serverini ishga tushirish
if name == "main":
    bot.remove_webhook()
    bot.set_webhook(url="https://your-render-app-url.com/webhook")
    app.run(host="0.0.0.0", port=5000)
