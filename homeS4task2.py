# Задача 2. В первой строке файла находится информация об 
# ассортименте мороженного, во второй - информация о том, 
# какое мороженное есть на складе. Выведите названия того 
# товара, который закончился.

# 1. «Сливочное», «Бурёнка»,
# «Вафелька», «Сладкоежка»
# 2. «Сливочное», «Вафелька», 
# «Сладкоежка»
# Закончилось: «Бурёнка»

import os

FileDataName = 'icecream.txt'

def PrintDefecit():
    # with open (FileDataName , 'r', encoding='UTF-8') as data:
    #     for n, line in enumerate(data, 1):
    #         line = line.rstrip('\n')       
    #         print(f"Вывод строки: {n}) - {line}")

    with open (FileDataName , 'r', encoding='UTF-8') as data:
         str1 = data.readline()
         str2 = data.readline()
         list1 = str1.split()
         list2 = str2.split()
         print('Закончилось: ' , list(set(list1) - set(list2)))                 
    data.close()

print('START')

if not(os.path.isfile(FileDataName)):
    print('ERROR: file NOT exsist')
else : PrintDefecit()


