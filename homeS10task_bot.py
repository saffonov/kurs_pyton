# http://t.me/homeS10task_bot
# 5891238987:AAH9hH0lHJ2DsxeD70R8IhtGfhXaKa4bE7k

# Задача 1. Напишите бота для техподдержки. Бот должен записывать обращения
# пользователей в xml-файл.

# Задача 2. Добавьте боту модуль, который позволяет считывать из файла вопрос, отвечать
# на него и отправлять ответ обратно пользователю.


# {'content_type': 'text', 'id': 7, 'message_id': 7, 'from_user': 
# {'id': 463567608, 'is_bot': False, 'first_name': 'ivan', 'username': 
# None, 'last_name': None, 'language_code': 'en', 'can_join_groups': 
# None, 'can_read_all_group_messages': None, 'supports_inline_queries': 
# None, 'is_premium': None, 'added_to_attachment_menu': None}, 'date': 1670754519, 
# 'chat': {'id': 463567608, 'type': 'private', 'title': None, 'username': 
# None, 'first_name': 'ivan', 'last_name': None, 'is_forum': 
# None, 'photo': None, 'bio': None, 'join_to_send_messages': None, 'join_by_request': 
# None, 'has_private_forwards': None, 'has_restricted_voice_and_video_messages': 
# None, 'description': None, 'invite_link': None, 'pinned_message': 
# None, 'permissions': None, 'slow_mode_delay': None, 'message_auto_delete_time': 
# None, 'has_protected_content': None, 'sticker_set_name': None, 'can_set_sticker_set': 
# None, 'linked_chat_id': None, 'location': None, 'active_usernames': None, 'emoji_status_custom_emoji_id': None},
#  'sender_chat': None, 'forward_from': None, 'forward_from_chat': None, 'forward_from_message_id': 
#  None, 'forward_signature': None, 'forward_sender_name': None, 'forward_date': None, 'is_automatic_forward': None,}



import telebot
import requests
import webbrowser
import datetime

filename_xml = 'file_support.xml'
answer_file = 'answer_file.txt'


TOKEN = '5891238987:AAH9hH0lHJ2DsxeD70R8IhtGfhXaKa4bE7k'

bot = telebot.TeleBot(TOKEN, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

def CreateXML():
    pattern_xml = '''<?xml version="1.0" encoding="windows-1251"?>
    <support_line>
    '''
    output = open(filename_xml,"w")
    output.write(pattern_xml)
    output.close()

def CloseXML():
    output = open(filename_xml,"a")
    output.write('</support_line>')
    output.close()

def WriteXML(message):
    user_id = str(message.from_user.id)
    user_message = str(message.text)
    user_time = datetime.datetime.now() 

    p = "\n" + "<line>" + "\n" + \
        "\t" + "<user_id>%s</user_id>"%user_id + "\n"  +\
        "\t" + "<user_message>%s</user_message>"%user_message + "\n"  +\
        "\t" + "<user_time>%s</user_time>"%user_time + "\n" +\
        "</line>"

    output = open(filename_xml,"a")
    output.write(p)
    output.close()

def GetAnswer(message):
    output = open(answer_file,"r")
    question = str(message.text)
    question = question[:-2] # delete '??' in message
    for line in output:
        print(question)
        print(line)
        if question in line:
            answer = line.replace(question, ' ')
            break
        else: answer = 'Все ОК'
    return answer

@bot.message_handler(commands=['start'])
def start_command(message): 
    CreateXML()
    bot.reply_to(message, "START")

@bot.message_handler(commands=['help'])
def help_command(message):
    help_message = 'Запрос без ?? записывается в xml файл, запрос с ?? ищется в файле' 
    bot.reply_to(message, help_message)

@bot.message_handler(commands=['stop'])
def stop_command(message): 
    CloseXML()
    bot.reply_to(message, "STOP")


@bot.message_handler(func=lambda message: True)
def suppot_user(message):
    # First homework 
    if not'??' in message.text:
        bot.reply_to(message, 'принято ' + message.from_user.first_name)
        WriteXML(message)
    # Second homework
    elif '??' in message.text:
        answ = GetAnswer(message)
        bot.reply_to(message, answ)
    
bot.infinity_polling()
CloseXML()   
