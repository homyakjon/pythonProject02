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

URL = 'https://megapanopticum.info/tags/анекдоты%20про%20рыбалку/'


def parser_bonus(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    bon = soup.find_all('div', class_='text')
    return [c.text for c in bon]


bonus = parser_bonus(URL)
random.shuffle(bonus)


URL = 'https://megapanoptikum.info/tags/анекдоты%20про%20дальнобойщиков/'


def parser_two(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    a_three = soup.find_all('div', class_='text')
    return [c.text for c in a_three]


li_three = parser_two(URL)
random.shuffle(li_three)

d = "Других тем пока нет!)"


@bot.message_handler(commands=['hello'])
def hello(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeybordButton('🍺Анекдоты про алкашей')
    item2 = types.KeybordButton('🚑Анекдоты про врачей')
    item3 = types.KeybordButton('🚚Анекдоты про дальнобойщиков')
    item4 = types.KeybordButton('🐟Анекдоты про рыбалку')
    item5 = types.KeybordButton('🛞Другое')

    markup.add(item1, item2, item3, item4, item5)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}!'.format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == '🍺Анекдоты про алкашей':
            bot.send_message(message.chat.id, 'Ваш Анекдот:' + str(li_one[0]))

    elif message.chat.type == 'private':
        if message.text == '🚑Анекдоты про врачей':
            bot.send_message(message.chat.id, 'Ваш анекдот:' + str(li_two[0]))

    elif message.chat.type == 'private':
        if message.text == '🚚Анекдоты про дальнобойщиков':
            bot.send_message(message.chat.id, 'Ваш Анекдот:' + str(li_three[0]))

    elif message.chat.type == 'private':
        if message.text == '🐟Анекдоты про рыбалку':
            bot.send_message(message.chat.id, 'Ваш Анекдот:' + str(bonus[0]))

    elif message.chat.type == 'private':
        if message.text == '🛞Другое':
            bot.send_message(message.chat.id, d)


bot.polling(none_stop=True)