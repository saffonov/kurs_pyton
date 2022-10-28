# Задача 2. Дан список случайных чисел. Создайте список, в
# который попадают числа, описывающие возрастающую
# последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] =>
# [1, 2, 3] или [1, 7] или [1, 6, 7] и
# т.д.

import random

def GetRandomList(N):
    RandomList = []
    for i in range(N):
        RandomList.insert(i, random.randint(1, 10))
    return RandomList

def NewList(List):
    ListOut = []
    i = 0
    for Li in List:
        #print(Li, "<",  List[i])
        if List[i] < Li:
            i = i + 1
            ListOut.insert(i, Li)
           
    return ListOut

ListIn = GetRandomList(5)
print(ListIn)
# print(list(filter(BiggestNext, ListIn)))

N = len(ListIn)
print(N)
ListDump = ListIn

for i in range(N):
    print(NewList(ListDump))
    ListDump = ListIn[i:N]
