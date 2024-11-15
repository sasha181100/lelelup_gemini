import telebot

# token = "7351021789:AAH9yHi0SIF4nML52dSzlwkr43_b1EpW0nA"
token = "7958499973:AAEneo1pmqF0FeF-brNRHi3k2JMT7njOUY8"
bot = telebot.TeleBot(token=token)

# run = False
# users = {}
from GPT.gpt import *
# hello_txt = '''Привет! 👋 Я Иишка - Ваш помощник по миру Bigoland.
#
# У нас вы можете приобрести самые крутые конструкторы!
# Более 80 детских и взрослых транспортных средств от снегоката до электро-картинга из 1 коробки.
#
# Чем я могу Вам помочь? '''
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '''Привет, Вася!''')

# def check_password(password):
#     if '$' in password and len(password) > 8: # проверка на хорошесть пароля
#         return 1
#     else:
#         return 0

# функция - именованный блок кода
# функция используется для того чтобы не было повторений кода
# password = input()
# password2 = input()
# password3 = input()
# if check_password(password) == 1:
#     print("good pass")
# else:
#     print("bad pass")

#
#
#     bot.send_message(message.chat.id, hello_txt)
#
# @bot.message_handler(commands=['help'])
# def help(message):
#     bot.send_message(message.chat.id, '''У бота имеется несколько комманд:
#     /question - задать вопрос к базе.
#     /stop - останавливает программу.
#     ''')
# @bot.message_handler(commands=['clear'])
# def clear_history(message):
#     users[message.from_user.id]["chat_history"] = [f'''
#     Пользователь: ""
#     Менеджер: {hello_txt}''']
#
# @bot.message_handler(commands=['stop'])
# def exitos(message):
#     bot.stop_bot()
#
#
#
# chat_history = ""
#
flag = False
@bot.message_handler(content_types=['text'])
def answer(message):

    if flag:
        user_id = message.from_user.id
        if message.text:
            try:
                ans = generate_answer(message.text, users[user_id]["chat_history"])
                bot.send_message(message.chat.id, ans)
                users[user_id]["chat_history"].append(f"Пользователь: {message.text}")
                users[user_id]["chat_history"].append(f"Менеджер: {ans}")
            except Exception as e:
                bot.send_message(message.chat.id, "Упс :( У нас возникли неполадки, Решаем проблему" + e.args[0])
    else:
#         вывод того как обращаться
#
bot.polling()

class Tools:
    def __init__(self, name, durability, damage):
        self.name = name
        self.durability = durability
        self.damage = damage


pickaxe = Tools("pickaxe", 100, 7)
# создай два объекта: spade и sword


print(f"Инструмент {pickaxe.name} имеет прочность {pickaxe.durability} и наносит урон {pickaxe.damage}")
# выведи описание объектов spade и sword по шаблону из задания