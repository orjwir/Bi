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
    startKBoard = types.ReplyKeyboardMarkup(row_width=1 , resize_keyboard=True)
    e1 = types.KeyboardButton(text="Кот")
    e2 = types.KeyboardButton(text="Девочка")
    e3 = types.KeyboardButton(text="Улыбка")
    startKBoard.add(e1,e2,e3)
    bot.send_message(message.chat.id, "Что хочешь увидеть сегодня?", reply_markup=startKBoard)

@bot.message_handler(func=lambda m: m.text == 'Мем')
def echo_all(message):
    photo = open('tmp/Девочка.jpg', 'rb')
    bot.send_photo(message.chat.id, photo, "Конечно")

@bot.message_handler(func=lambda m: m.text == 'Кот')
def echo_all(message):
    photo = open('tmp/Кот.jfif', 'rb')
    bot.send_photo(message.chat.id, photo, "Мило:З")

@bot.message_handler(func=lambda m: m.text == 'Улыбка')
def echo_all(message):
    photo = open('tmp/котомем.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo, "Получай")


bot.polling()
