# Задача 1. В каждой группе учится от 20 до 30 студентов. По итогам экзамена все оценки
# заносятся в таблицу. Каждой группе отведена своя строка. Определите группу с
# наилучшим средним баллом.

import random

def GetRandomArray(M):
    RandomArray = [0]*M
    for i in range(len(RandomArray)):
        colum = random.randint(20, 30)
        RandomArray[i] = list(random.randint(1, 5) for _ in range(colum))
    return RandomArray

def GetBestGroup (group):
    rat = [0]*(len(group))
    for row in range(len(group)): 
        for colum in range(len(group[row])):
            rat[row] += group[row][colum]
        rat[row] = rat[row]/(len(group[row]))
    print(rat)
    print("Лучшая группа : ", (rat.index(max(rat)) + 1)) # +1 Because the numbering of groups starts from 1

N = int(input("Ведите количество групп:"))

rating = GetRandomArray(N)
print("Оценки по группам : ")
for row in rating: print(row)

GetBestGroup(rating)