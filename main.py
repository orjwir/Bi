import telebot
from telebot import types

bot = telebot.TeleBot("5294719040:AAGtJmFRvTZSloq1tfRoqvyErPVur0vX5Z0")


@bot.message_handler(commands=["start"])
def keyboard_start(message):
    startKBoard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    ramm = types.KeyboardButton(text="Привет!")
    startKBoard.add(ramm)
    bot.send_message(message.chat.id, "Привет", reply_markup=startKBoard)


@bot.message_handler(func=lambda m: m.text == 'Привет!')
def echo_all(message):
    startKBoard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    e1 = types.KeyboardButton(text="Ваниль")
    e2 = types.KeyboardButton(text="Чёрный перец горошком")
    e3 = types.KeyboardButton(text="Приправа Тоскана")
    e4 = types.KeyboardButton(text="Чёрный перец молотый")
    e5 = types.KeyboardButton(text="Карри")
    e6 = types.KeyboardButton(text="Универсальная смесь специй")
    e7 = types.KeyboardButton(text="Корица молотая")
    e8 = types.KeyboardButton(text="Паприка")
    e9 = types.KeyboardButton(text="Тимьян")
    e10 = types.KeyboardButton(text="Базилик")
    e11 = types.KeyboardButton(text="Красный перец")
    e12 = types.KeyboardButton(text="Белый перец")
    e13 = types.KeyboardButton(text="Зеленый перец")
    e14 = types.KeyboardButton(text="Хмели-сунели")
    startKBoard.add(e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14)
    bot.send_message(message.chat.id, "Что хочешь увидеть сегодня?", reply_markup=startKBoard)


@bot.message_handler(func=lambda m: m.text == 'Чёрный перец горошком')
def echo_all(message):
    photo = open('черн.горох.jpg', 'rb')
    bot.send_photo(message.chat.id, photo, "Состав: чёрный перец горошком.")

@bot.message_handler(func=lambda m: m.text == 'Приправа Тоскана')
def echo_all(message):
    photo = open('тоскана.jpg', 'rb')
    bot.send_photo(message.chat.id, photo, "Состав: Хлопья томатов(томатная паста, кукурузный крахмал) соль йодированая,"
                                           " базилик,чеснок,орегано,лук,петрушка." )

@bot.message_handler(func=lambda m: m.text == 'Чёрный перец молотый')
def echo_all(message):
    photo = open('черн.молот.jpg', 'rb')
    bot.send_photo(message.chat.id, photo, "Состав: перец черный молотый.")

@bot.message_handler(func=lambda m: m.text == 'Карри')
def echo_all(message):
    photo = open('карри.jpg', 'rb')
    bot.send_photo(message.chat.id, photo, "Состав: кориандр, куркума, фенугрек, перец чёрный молотый,кумин, имбирь, "
                                           "корица, гвоздика, чили, мускатный орех, фенхель, горчица,кардамон.")

@bot.message_handler(func=lambda m: m.text == 'Универсальная смесь специй')
def echo_all(message):
    photo = open('индия.jpg', 'rb')
    bot.send_photo(message.chat.id, photo, "Состав: кориандр, красный перец чили, кумин, куркума, имбирь, черный перец,"
                                           " горчица, фенхель, листья пажитника, чеснок, лук, мускусная дыня, черный кардамон, корица, гвоздика, мускатный цвет, мускатный орех, зеленый кардамон, асафетида.")

@bot.message_handler(func=lambda m: m.text == 'Корица молотая')
def echo_all(message):
    photo = open('корица.jpg', 'rb')
    bot.send_photo(message.chat.id, photo, "Состав: корица молотая.")

@bot.message_handler(func=lambda m: m.text == 'Паприка')
def echo_all(message):
    photo = open('паприка.jpg', 'rb')
    bot.send_photo(message.chat.id, photo, "Состав: паприка красная.")

@bot.message_handler(func=lambda m: m.text == 'Тимьян')
def echo_all(message):
    photo = open('тимьян.webp', 'rb')
    bot.send_photo(message.chat.id, photo, "Состав: тимьян сушёный")

@bot.message_handler(func=lambda m: m.text == 'Ваниль')
def echo_all(message):
    photo = open('ваниль.jpg', 'rb')
    bot.send_photo(message.chat.id, photo, "Состав: ваниль сушёная.")

@bot.message_handler(func=lambda m: m.text == 'Базилик')
def echo_all(message):
    photo = open('базилик.jpg', 'rb')
    bot.send_photo(message.chat.id, photo, "Состав: базилик сушёный.")

@bot.message_handler(func=lambda m: m.text == 'Красный перец')
def echo_all(message):
    photo = open('перец.красн.jpg', 'rb')
    bot.send_photo(message.chat.id, photo, "Состав: перец красный горошком.")

@bot.message_handler(func=lambda m: m.text == 'Белый перец')
def echo_all(message):
    photo = open('бел.перец.jpg', 'rb')
    bot.send_photo(message.chat.id, photo, "Состав: перец белый горошком.")

@bot.message_handler(func=lambda m: m.text == 'Зеленый перец')
def echo_all(message):
    photo = open('зел.перец.jpg', 'rb')
    bot.send_photo(message.chat.id, photo, "Состав: перец зелёный горошком.")

@bot.message_handler(func=lambda m: m.text == 'Хмели-сунели')
def echo_all(message):
    photo = open('хмели сунели.jpg', 'rb')
    bot.send_photo(message.chat.id, photo, "Состав: чеснок, горчица, майоран, розмарин, соль, кориандр, базилик, тмин, "
                                           "тимьян, морковь, перец чили, паприка сладкая, мята, шалфей, лавровый лист")

bot.polling()
