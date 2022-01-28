import telebot
import key
from telebot import types

bot = telebot.TeleBot(key.token)
@bot.message_handler(commands=["start"])

def keyboard_start(message):
    startKBoard = types.ReplyKeyboardMarkup(row_width=1 , resize_keyboard=True)
    Raspisanya = types.KeyboardButton(text="Как дела?")
    startKBoard.add(Raspisanya)
    bot.send_message(message.chat.id, "Привет", reply_markup=startKBoard)

@bot.message_handler(func=lambda m: m.text == 'Как дела?')
def echo_all(message):
    startKBoard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    e1 = types.KeyboardButton(text="Прислать мем")
    e2 = types.KeyboardButton(text="Прислать кота")
    e3 = types.KeyboardButton(text="Прислать мем с котом")
    startKBoard.add(e1, e2, e3)
    bot.send_message(message.chat.id, "Что хочешь увидеть сегодня?", reply_markup=startKBoard)

photo1 = open('Девочка.jpg', 'e1')
bot.send_photo(chat_id, photo1)
photo2 = open('Кот.jfif', 'e2')
bot.send_photo(chat_id, photo2)
photo3 = open('котомем.jpeg', 'e3')
bot.send_photo(chat_id, photo3)


    bot.send_photo(message.chat_id, "привет")

bot.polling()
