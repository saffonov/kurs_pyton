# Задача 3. Создайте скрипт бота, который находит ответы на фразы по ключу в словаре. 
# Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут». 
# Если фраза ему неизвестна, он выводит соответствующую фразу.
# «как тебя зовут?»–>меня зовут Анатолий

BotDict = {
    'Привет' : "Привет! Я бот",
    'зовут' : "Меня зовут бот Анатолий",
    'дела' : "Дела у меня хорошо! А у Вас как дела?"

}

print("Начнем диалог")
print("Для завершения диалога введите Пока " )
NotAnswer = True

UserPhrase = input()

while not(UserPhrase == 'Пока'):
    UserWord = UserPhrase.split()
    print(UserWord)
    for UW in UserWord: 
        if (UW in BotDict):
            print(BotDict.get(UW))
            NotAnswer = False
    if NotAnswer :
        print('Я Вас не понимаю')      
    UserPhrase = input("? :")
else : print('Всего хорошего!')     




