# Задача 2. Дана квадратная матрица, заполненная случайными числами. Определите,
# сумма элементов каких строк превосходит сумму главной диагонали матрицы.

import random

def GetRandomArray(M):
    RandomArray = [0]*M
    for i in range(len(RandomArray)):
        RandomArray[i] = list(random.randint(0, 10) for _ in range(M))
    return RandomArray

def GetMaxLine(matrix):
    SumGeneralDiag = 0
    for i in range(len(matrix)): SumGeneralDiag += matrix[i][i]
    
    print("Сумма главной диагонали: ",SumGeneralDiag)

    for i in range(len(matrix)):
        if SumGeneralDiag < sum(matrix[i]): print("Строка № :", i)


N = int(input("Ведите размерность квадратной матрицы:"))

Matrix = GetRandomArray(N)

for row in Matrix: print(row , ":", sum(row))

GetMaxLine(Matrix)

