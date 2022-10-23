# Задача 1. Задайте натуральное число N. Напишите 
# программу, которая составит список простых множителей 
# числа N
# 60 -> 2, 2, 3, 5

def GetSimpleMultFactor(n):
    result = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            result.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        result.append(n)
    return result

print('START')
N = int(input("Введите число : "))

print(GetSimpleMultFactor(N))