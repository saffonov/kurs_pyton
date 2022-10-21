# Задача 1. Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи.
# 6 –>1 1 2 3 5 8

import os

def Fibonachchi(NN):
    if NN in [1, 2]:
        return 1
    else:
        return Fibonachchi(NN-1) + Fibonachchi(NN-2)
    
   
FileDataName = 'file.txt'
N = 6 # Number of Fibonachchi

if (os.path.isfile(FileDataName)):
    os.remove(FileDataName)

with open (FileDataName , 'w') as data:
    for i in range(N):
        # print(Fibonachchi(i+1))
        data.write(str(Fibonachchi(i+1)))
        data.write(" ")
    data.close()




