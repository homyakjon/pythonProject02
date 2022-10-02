# from datetime import datetime
#
#
# class Developer:
#     def __init__(self, name, dob, employment_date, unit, profile, salary, work_day):
#         self.name = name
#         self.dob = self.transform_date(dob)
#         self.employment_date = self.transform_date(employment_date)
#         self.unit = unit
#         self.profile = profile
#         self.salary = salary
#         self.work_day = work_day
#
#     def transform_date(self, date_as_string: str) -> datetime:
#         date_as_object = datetime.strptime(date_as_string, "%d.%m.%Y")
#         return date_as_object
#
#     def check_work_experience(self):
#         today = datetime.today()
#         experience = today - self.employment_date
#         return experience
#
#     def increase_salary(self, amount, restrictions=True):
#         if amount == self.salary * 0.1 and restrictions:
#             print("You can increase salary more than 10%")
#             self.salary += amount
#             print(f"msg: new salary is {self.salary}")
#         else:
#             print(f"Not can increase salary")
#
#     def data_processing(self):
#         if self.check_work_experience() >= 24:
#             self.increase_salary(
#                 self.salary * 0.3,
#                 restrictions=False
#             )
#
#     def work_bonus(self, bonus=300):
#         if self.work_day > 8:
#             print(f"add bonus developer in size {bonus} dollars")
#             self.salary += bonus
#         else:
#             print("Sorry, developer not get bonus")
#
#
# class Junior(Developer):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#
#
# class Senior(Developer):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#
#
# junior = Junior(
#     name="Stan",
#     dob="11.05.1990",
#     employment_date="07.04.2021",
#     unit="B",
#     profile="Python",
#     salary=1000,
#     work_day=10
#
# )
#
#
# senior = Senior(
#     name="Billy",
#     dob="08.11.1989",
#     employment_date="05.02.2018",
#     unit="B",
#     profile="Python",
#     salary=4000,
#     work_day=10
#
# )


import random
import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup as b

TOKEN = "5757690615:AAG5TRPUax91V9c1u2b_b0dwpr2hqA0tuq4"

bot = telebot.Telebot(TOKEN)

URL = 'https://megapanoptikum.info/tags/анекдоты%20про%20алкашей/'


def parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    a_one = soup.find_all('div', class_='text')
    return [c.text for c in a_one]


li_one = parser(URL)
random.shuffle(li_one)

URL = 'https://megapanoptikum.info/tags/анекдоты%20про%20врачей/'


def parser_one(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    a_two = soup.find_all('div', class_='text')
    return [c.text for c in a_two]


li_two = parser_one(URL)
random.shuffle(li_two)

URL = 'https://megapanoptikum.info/tags/анекдоты%20про%20дальнобойщиков/'


def parser_two(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    a_three = soup.find_all('div', class_='text')
    return [c.text for c in a_three]


li_three = parser_two(URL)
random.shuffle(li_three)

d = "Пошел нахуй!)"


@bot.message_handler(commands=['hello'])
def hello(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeybordButton('🍺Анекдоты про алкашей')
    item2 = types.KeybordButton('🚑Анекдоты про врачей')
    item3 = types.KeybordButton('🚚Анекдоты про дальнобойщиков')
    item4 = types.KeybordButton('🛞Другое')

    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == '🍺Анекдоты про алкашей':
            bot.send_message(message.chat.id, 'Ваш Анекдот:' + str(li_one[0]))

    if message.chat.type == 'private':
        if message.text == '🚑Анекдоты про врачей':
            bot.send_message(message.chat.id, 'Ваш анекдот:' + str(li_two[0]))

        if message.chat.type == 'private':
            if message.text == '🚚Анекдоты про дальнобойщиков':
                bot.send_message(message.chat.id, 'Ваш Анекдот:' + str(li_three[0]))

        if message.chat.type == 'private':
            if message.text == '🛞Другое':
                bot.send_message(message.chat.id, d)


bot.polling(none_stop=True)
