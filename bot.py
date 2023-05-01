import telebot
import sqlite3


API_bot = '6045868714:AAEnu6Hly8dLhoGhajvueCnaZ0E7xdkJ-XU'
bot = telebot.TeleBot(API_bot)

#по этой команде пользователь будет добавлен в базу данных
@bot.message_handler(commands=['start'])
def start(massage):
    conect = sqlite3.connect('Users.db')
    cursor = conect.cursor()#нужен что бы с БД взаимодействовать

    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
        id INTEGER, date DATE 
    )""")#если таблица не создана в папке Users.db, то она создаётся с полями, которые указал

    conect.commit()# сохраняет изменения

    #теперь добавим данные пользователя в таблицу
    user = [massage.chat.id, ]




@bot.message_handler(commands=['delete'])
def start(massage):
    pass









bot.polling()