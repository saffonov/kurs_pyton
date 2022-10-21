# Задача 2. В файле находятся названия фруктов.Выведите все фрукты, 
# названия которых начинаются на заданную букву.
# а–>абрикос,авокадо, апельсин, айва.

import os
FileDataName = 'frukt.txt'

def PrintFruct(Letter):
    with open (FileDataName , 'r', encoding='UTF-8') as data:
        for line in data:
            if (str(line[0]) == Letter):
            # print(str(line[0]))
                print(str(line))
    data.close()

print('START')
L = str(input("Введите букву : "))


if not(os.path.isfile(FileDataName)):
    print('ERROR: file NOT exsist')
else : PrintFruct(L)
