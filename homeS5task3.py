# Задача 3. Задайте список случайных чисел от 1 до 10.
# Посчитайте, сколько всего совпадающих элементов есть в
# списке. Удалите все повторяющиеся элементы.

# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента
# совпадают
# Список уникальных элементов
# [1, 4, 2, 3, 6, 7]

import random

def GetRandomList(N):
    RandomList = []
    for i in range(N):
        RandomList.insert(i, random.randint(1, 10))
    return RandomList


# def FindEqual(List):
#     if List in List: return False
#     else: return True    

ListIn = GetRandomList(10)
print(ListIn)
ListOut = list(set(ListIn))
print(ListOut)

print(2*(len(ListIn) - len(ListOut)))

