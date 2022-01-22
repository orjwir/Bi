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
    """photo = open('a', 'e2')
    photo = open('b', 'e1')
    photo = open('c', 'e3')

    bot.send_photo(message.chat_id, photo,"привет")"""
bot.polling()