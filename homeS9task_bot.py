# http://t.me/homeS9task_bot
# 5865989269:AAFQGkO5AdlcQEyvb_0GozTjbOjMzP6p8aY

import telebot
import requests
import random

TOKEN = '5865989269:AAFQGkO5AdlcQEyvb_0GozTjbOjMzP6p8aY'

# def BotGameRNDnum(message):
#     #num = random.randint(0, 1000)
#     num = 10
#     i = 0
#     bot.reply_to(message, 'Готов?')
#     a = message.text
#     print(str(a))
#     print('br1')
#     # while not(num == answer):
#     #     bot.reply_to(message, 'угадай число от 0 до 1000?')
#     #     answer = int(message.text)
#     #     i += 1
#     #     bot.reply_to(message, i)
#     return i


bot = telebot.TeleBot(TOKEN, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#     bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def hello_user(message):
    if 'привет' in message.text:
        bot.reply_to(message, 'привет тебе' + message.from_user.first_name)
    elif message.text == 'играть':
        bot.reply_to(message, 'хочешь поиграть?')
    elif message.text == 'погода':
        r = requests.get('https://wttr.in/?0T')
        # print(r.text)
        bot.reply_to(message, r.text)
    # Homework
    elif 'вычислить' in message.text:
        a = message.text
        a = a.replace('вычислить', ' ')
        i = eval(str(a))
        bot.reply_to(message, 'Ответ = ' + str(i))
    elif message.text == 'игра': 
        #num = random.randint(0, 1000)
        num = 10
        i = 0
        answer = 0
        bot.reply_to(message, 'угадай число от 0 до 1000')
        @bot.message_handler(content_types=['text'])
        def input_data(message):
            answer = int(message.text)
            print(answer)
            bot.reply_to(message, 'INPUT')

        # while num != answer :
        #     a = message.text
        #     print(str(a))
        #     bot.reply_to(message, 'ввели ' + a)





	# bot.reply_to(message, message.from_user.first_name)
    data = open('user_message.txt', 'a+', encoding ='utf-8' )
    data.writelines(str(message.from_user.id) + ' ' + message.text + '\n')
    data.close



bot.infinity_polling()