# Задача 1. Задайте список случайных чисел от 1 до 10,
# выведите все элементы больше 5. Используйте для решения
# лямбда-функцию.
# 2, 3, 4, 6, 7, 8 -> 6, 7, 8

import random

def GetRandomList(N):
    RandomList = []
    for i in range(N):
        RandomList.insert(i, random.randint(1, 10))
    return RandomList

ListIn = GetRandomList(10)
print(ListIn)
print(list(filter(lambda x: (x > 5), ListIn)))




