"""
This code is designed to implement a Retrieval-Augmented Generation system using Large Language Models.
It uses the Gemini model from Google Generative AI and LangChain for processing and generating responses based on the Nvidia 10-K report.
"""

# Importing necessary libraries
# from google.colab import drive
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from Loader.loader import *
from Retriever.retriever import *
from GPT.gpt import *
# Constants
GOOGLE_API_KEY = 'AIzaSyC02h1AJhpEL5whQQBYzdbHdgNStdZU2ko'  # Replace with your actual Google API key
DATA_PDF_PATH = "docs/pdfs/data.pdf"
GEMINI_MODEL_NAME = "gemini-pro"
EMBEDDING_MODEL_NAME = "models/embedding-001"
TEMPERATURE = 0.1
CHUNK_SIZE = 700
CHUNK_OVERLAP = 300
# #
# #
# # # Function to mount Google Drive
# # from itertools import product
# #
# #
#
# #
# # user = User("aba", "12346578")
# # user2 = User("awa", '333')
# # a = []
# # a.append(user)
# # a.append(user2)
# # for elem in a:
# #
# #     print(elem.get_description())
# #
# # # ans = 0
# # # cnt2 = 0
# # # for num in product('0123456789ABC', repeat=6):
# # #     if num[0] == '0':
# # #         continue
# # #     cnt_fives = 0
# # #     cnt2 += 1
# # #     for elem in num:
# # #         if elem == '5':
# # #             cnt_fives += 1
# # #     ok = True
# # #     for i in range(len(num) - 1):
# # #         value = 0
# # #
# # #         if '0' <= num[i] <= '9':
# # #             value = int(num[i])
# # #         if num[i] == 'A':
# # #             value = 10
# # #         if num[i] == 'B':
# # #             value = 11
# # #         if num[i] == 'C':
# # #             value = 12
# # #         value2 = 0
# # #         if '0' <= num[i + 1] <= '9':
# # #             value2 = int(num[i + 1])
# # #         if num[i + 1] == 'A':
# # #             value2 = 10
# # #         if num[i + 1] == 'B':
# # #             value2 = 11
# # #         if num[i + 1] == 'C':
# # #             value2 = 12
# # #         if value % 2 == 1 and value2 % 2 == 1:
# # #             ok = False
# # #
# # #     if cnt_fives <= 1 and ok == True:
# # #         ans += 1
# # # print(cnt2)
# # # print(ans)
# # #
model = genai.GenerativeModel(model_name='gemini-1.0-pro')
genai.configure(api_key='AIzaSyC02h1AJhpEL5whQQBYzdbHdgNStdZU2ko')
info = "Меня зовут Саша, мне 23 года, я мастер спорта по плаваиню, женат, воспитываю дочь. Закончил университет ИТМО. Живу в Волгограде, люблю салат с помидорами и хрустящими баклажанами"
while True:
    message = input()
    str = f'''сгенерируй ответ на вопрос: {message}'''
    # str = f'''Информация о человеке находится в поле КОНТЕКСТ.
    #         КОНТЕКСТ:{info}
    #         Твоя задача ответить на вопросы пользователей по этому человеку. Вопрос находится в поле ВОПРОС:
    #         ВОПРОС: {message}
    #         '''


    response = model.generate_content(str)

    answer = ""
    for chunk in response:
        answer += chunk.text
    print(answer)
# # # #
# #
# #
# # # class Player:
# # #     def init(self, name, email):
# # #         self.name = name
# # #         self.email = email
# # #         self.level = 0
# # # something = Player("Ivan", "ivanchik@bestmail.com")
# # # print(f"Привет,{something.name}! Тебе на почту {something.email} пришло письмо. Перейди по нему и подтверди регистрацию")
# #
# #
# # # class Player:
# # #     def init(self, name, email):
# # #         self.name = name
# # #         self.email = email
# # #         self.level = 0
# # #
# # # player1 = Player(name="Иван", email="ivan2010@mail.ru")
# # # print(player1.name)
# # # print(player1.email
# #
# #
# # # class Player:
# # #     def init(self, name, email):
# # #         self.name = name
# # #         self.email = email
# # #         self.level = 0  # уровень нового игрока по умолчанию 0
# # #
# # #     # метод, который возвращает значение
# # #     def get_data(self):
# # #         return f"Имя: {self.name}, почта: {self.email}, уровень: {self.level}"
# # # player1 = Player(name="Иван", email="ivan2010@mail.ru")
# # # print(player1.get_data())
# #
# # #
# # # class Player:
# # #     def init(self, name, email):
# # #         self.name = name
# # #         self.email = email
# # #         self.level = 0  # уровень нового игрока по умолчанию 0
# # #
# # #     # метод, который возвращает значение
# # #     def get_data(self):
# # #         return f"Имя: {self.name}, почта: {self.email}, уровень: {self.level}"
# # #
# # #     # метод, который ничего не возвращает, но изменяет атрибуты
# # #     def level_up(self):
# # #         self.level += 1
# # #         print(f"Уровень игрока {self.name} повышен до {self.level}")
# # # player1 = Player(name="Иван", email="ivan2010@mail.ru")
# # # print(player1.get_data())
# # # player1.level_up()
# # # print(player1.get_data())
# #
# #
# # class Person:
# #     def __init__(self, name, character, sex, height, weight):
# #         self.name = name
# #         self.character = character
# #         self.sex = sex
# #         self.height = height
# #         self.weight = weight
# #
# #     def change_height(self, new_height):
# #         self.height = new_height
# #
# #     def change_name(self, new_name):
# #         self.name = new_name
# #     def change_weigh(self, new_weight):
# #         self.weight = new_weight
# #     def print_description(self):
# #         print(f"Персонаж {self.name} имеет рост {self.height} и вес {self.weight}")
# # # vasya = Person("Vasya", "kind", "male", 160, 90)
# # # vasya.print_description()
# # # vasya.change_height(165)
# # # vasya.change_weigh(70)
# # # vasya.change_name("German")
# # # vasya.print_description()
# #
# #
# #
# # password = input()
# # if len(password) < 8:
# #     print("Bad password")
# #     print("Think of another one:((((")
# #
# # elif password.count("@") == 0:
# #     print("Nice try")
# #     print("Try again! You can do better, my friend")
# #
# # else:
# #     print("Good password")
# #     print("Accepted:)")
# #
# # # база данных
# # # vasya = 1
# # # petya = 2
# # # vanya = 3
# # # german = 4
# # # robert = 5
#
#
# # for elem in example_users_list: #in - перебор
# #     print(elem)
# # 1) уметь пробегаться по массиву
# # 2) добалять в массив
# # 3) массив своих классов(person, car)
#
# # интерактив на сайте
#
# class User:
#     def __init__(self, login, password):
#         self.login = login
#         self.password = password
#     def get_description(self):
#         print(self.login + " " + self.password)
# users = [] # пустой маcсив
#
#
# while True:
#     remember = False # логическая переменная которая показывает есть ли такой логи в базе
#     print("Enter login:")
#     login = input()
#     for user in users: # перебирает все пользователей в базе по очереди
#         if user.login == login:
#             remember = True
#             print("Enter password:")
#             password = input()
#             if password == user.password:
#                 print("Nice to see you again, my friend")
#                 break
#             else:
#                 print("incorrect password")
#     if remember == False:
#         print("Hi, we did not see you before, my friend")
#         print("Lets register you")
#         print("Enter your name:")
#         name = input()
#         print("Enter your password")
#         password = input()
#         # проверка правильности пароля
#         new_user = User(name, password)
#         users.append(new_user)
#         print("You were register")
#
#
#
#
# # if user == vasya:
# #     print("Welcome, vasya")
# # elif user == petya:
# #     print("Welcome, petya")
# # elif user == vanya:
# #     print("Welcome, vanya")
# # elif user == german:
# #     print("Welcome, german")
# # elif user == robert:
# #     print("Welcome, robert")
# # else:
# #     print("Good bye my unknown friend")
#

# a = []
# x = int(input())
# while x != 0:
#     a.append(x)
#     x = int(input())
# print(a)


# n = int(input())
# a = list(map(int, input().split()))
# print(min(a[]))
#
#
# for i in range(n):
#     b = b + a[i]
# print(b)
