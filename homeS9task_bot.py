# http://t.me/homeS9task_bot
# 5865989269:AAFQGkO5AdlcQEyvb_0GozTjbOjMzP6p8aY

# Задача 1. Добавьте telegram-боту возможность вычислять выражения:
# 1 + 4 * 2 -> 9
# Задача 2. Добавьте в бота игру «Угадай числа». Бот загадывает число от 1 до 1000. Когда
# игрок угадывает его, бот выводит количество сделанных ходов.

import telebot
import requests
import random

TOKEN = '5865989269:AAFQGkO5AdlcQEyvb_0GozTjbOjMzP6p8aY'

def BotGameRNDnum(message):
    #num = random.randint(0, 1000)
    num = 10
    answer = 1
    i = 0
   
    while num != answer :
        @bot.message_handler(func=lambda message: True)
        def get_num(message):
            bot.reply_to(message, 'Готов?')
            answer = int(message.text)
            print(answer, i)    
            i += 1
            bot.reply_to(message, str(i) + ' : ' + str(answer))
    return i


bot = telebot.TeleBot(TOKEN, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN


@bot.message_handler(commands=['start'])
def start_command(message): 
    bot.reply_to(message, "START")

@bot.message_handler(commands=['help'])
def help_command(message):
    help_message = 'Может считать, может играть' 
    bot.reply_to(message, help_message)

@bot.message_handler(commands=['stop'])
def stop_command(message): 
    bot.reply_to(message, "STOP")

@bot.message_handler(commands=['game'])
def stop_command(message):
    bot.reply_to(message, "GAME")
    BotGameRNDnum(message)



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
    # Homework 1
    elif 'вычислить' in message.text:
        a = message.text
        a = a.replace('вычислить', ' ')
        i = eval(str(a))
        bot.reply_to(message, 'Ответ = ' + str(i))



	# bot.reply_to(message, message.from_user.first_name)
    data = open('user_message.txt', 'a+', encoding ='utf-8' )
    data.writelines(str(message.from_user.id) + ' ' + message.text + '\n')
    data.close



bot.infinity_polling()