import telebot
import key
from telebot import types

bot = telebot.TeleBot(key.token)


@bot.message_handler(commands=["start"])
def keyboard_start(message):
    startKBoard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    Raspisanya = types.KeyboardButton(text="Как дела?")
    startKBoard.add(Raspisanya)
    bot.send_message(message.chat.id, "Привет", reply_markup=startKBoard)


@bot.message_handler(func=lambda m: m.text == 'Как дела?')
def echo_all(message):
    startKBoard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    e1 = types.KeyboardButton(text="Кот")
    e2 = types.KeyboardButton(text="Девочка")
    e3 = types.KeyboardButton(text="Улыбка")
    startKBoard.add(e1, e2, e3)
    bot.send_message(message.chat.id, "Что хочешь увидеть сегодня?", reply_markup=startKBoard)


@bot.message_handler(func=lambda m: m.text == 'Чёрный перец горошком')
def echo_all(message):
    photo = open('tmp/Девочка.jpg', 'rb')
    bot.send_photo(message.chat.id, photo, "Состав: чёрный перец горошком.")


@bot.message_handler(func=lambda m: m.text == 'Припава Тоскана')
def echo_all(message):
    photo = open('tmp/Кот.jfif', 'rb')
    bot.send_photo(message.chat.id, photo, "Состав: Хлопья томатов( томатная паста, кукурузный крахмал) соль йодированая, базилик,чеснок,орегано,лук,петрушка." )

@bot.message_handler(func=lambda m: m.text == 'Чёрный перец молотый')
def echo_all(message):
    photo = open('tmp/котомем.jpeg', 'rb')
    bot.send_photo(message.chat.id, photo, "Состав: перец черный молотый.")

@bot.message_handler(func=lambda m: m.text == 'Карри')
def echo_all(message):
    photo = open()
    bot.send_photo(message.chat.id, photo, "Состав: кориандр, куркума, фенугрек, перец чёрный молотый,кумин, имбирь, корица, гвоздика, чили, мускатный орех, фенхель, горчица,кардамон.")

@bot.message_handler(func=lambda m: m.text == 'Универсальная смесь специй')
def echo_all(message):
    photo = open()
    bot.send_photo(message.chat.id, photo, "Состав: кориандр, красный перец чили, кумин, куркума, имбирь, черный перец, горчица, фенхель, листья пажитника, чеснок, лук, мускусная дыня, черный кардамон, корица, гвоздика, мускатный цвет, мускатный орех, зеленый кардамон, асафетида.")

@bot.message_handler(func=lambda m: m.text == 'Корица молотая')
def echo_all(message):
    photo = open()
    bot.send_photo(message.chat.id, photo, "Состав: корица молотая.")

@bot.message_handler(func=lambda m: m.text == 'Паприка')
def echo_all(message):
    photo = open()
    bot.send_photo(message.chat.id, photo, "Состав: паприка красная.")

@bot.message_handler(func=lambda m: m.text == 'Тимьян')
def echo_all(message):
    photo = open()
    bot.send_photo(message.chat.id, photo, "Состав: тимьян сушёный")

@bot.message_handler(func=lambda m: m.text == 'Ваниль')
def echo_all(message):
    photo = open()
    bot.send_photo(message.chat.id, photo, "Состав: ваньль сушёная.")

@bot.message_handler(func=lambda m: m.text == 'Базилик')
def echo_all(message):
    photo = open()
    bot.send_photo(message.chat.id, photo, "Состав: базилик сушёный.")

@bot.message_handler(func=lambda m: m.text == 'Красный перец')
def echo_all(message):
    photo = open()
    bot.send_photo(message.chat.id, photo, "Состав: перец красный горошком.")

@bot.message_handler(func=lambda m: m.text == 'Белый перец')
def echo_all(message):
    photo = open()
    bot.send_photo(message.chat.id, photo, "Состав: перец белый горошком.")

@bot.message_handler(func=lambda m: m.text == 'Зеленый перец')
def echo_all(message):
    photo = open()
    bot.send_photo(message.chat.id, photo, "Состав: перец зелёный горошком.")

@bot.message_handler(func=lambda m: m.text == 'Хмели-сунели')
def echo_all(message):
    photo = open()
    bot.send_photo(message.chat.id, photo, "Состав: чеснок, горчица, майоран, розмарин, соль, кориандр, базилик, тмин, тимьян, морковь, перец чили, паприка сладкая, мята, шалфей, лавровый лист")

bot.polling()
