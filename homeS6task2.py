# Задача 2. Задан массив из случайных цифр на 15 элементов. 
# На вход подаётся трёхзначное натуральное число. 
# Напишите программу, которая определяет, есть в массиве последовательность из трёх элементов, 
# совпадающая с введённым числом.
# {0, 5, 6, 2, 7, 7, 8, 1, 1, 9} -277 -> да
# {4, 4, 3, 6, 7, 0, 8, 5, 1, 2} -812 -> нет

from pickle import FALSE, TRUE
import random

def GetRandomList(N):
    RandomList = []
    for i in range(N):
        RandomList.insert(i, random.randint(0, 9))
    return RandomList


LengthList = 15
N = input("ведите трехзначное натуральное число :")

ListShablon = [N[0], N[1], N[2]]
ListN = GetRandomList(LengthList)

# #######################################
# ##for Debug:
# ListN += ListShablon; ListN
# LengthList = LengthList + 3
# #######################################

print(ListN)

answer = False

for i in range(LengthList-2):
    # print((ListN[i:i+3:1]))
    if (ListN[i:i+3:1] == ListShablon): answer = True

if answer: print("Да")
else: print("Нет")
