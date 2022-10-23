# Задача 4*. Даны два файла, в каждом из которых находится 
# запись многочлена. Найдите сумму данных многочленов.
# 1. 5x^2 + 3x
# 2. 3x^2 + x + 8
# Результат: 8x^2 + 4x + 8


import os
import re
FileEquation_1Name = 'fileS4t4_1.txt'
FileEquation_2Name = 'fileS4t4_2.txt'

def ParseEquation(Line):
    Line = Line.replace(' ', '')
    Line = Line.replace('x^2', ' ')
    Line = Line.replace('x', ' ')
    Coeff = [0, 0, 0]
    i = 0
    for s in Line.split():
        # print("i =", i , ":", s, ":", float(s))
        Coeff[i] = int(s)
        i += 1
    return Coeff


def JoinEquation():
    with open (FileEquation_1Name , 'r', encoding='UTF-8') as data1:
        Line1 = data1.readline()
        Coeff1 = ParseEquation(Line1)
    data1.close()
    with open (FileEquation_2Name , 'r', encoding='UTF-8') as data2:
        Line2 = data2.readline()
        Coeff2 = ParseEquation(Line2)
    data2.close()
    return list(map((lambda x: x[0]+x[1]),zip(Coeff1,Coeff2)))
    

    

print('START')

if not(os.path.isfile(FileEquation_1Name)  
    or  os.path.isfile(FileEquation_2Name)):
    print('ERROR: file NOT exsist')
else : 
    List = JoinEquation()
    print(List[0],"x^2 + ",List[1],"x +",List[2])
