# Задача 1. Напишите программу, которая принимает на вход число N 
# и выдает список факториалов для чисел от 1 до N.
# пусть N = 4->[ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

print('START')
N = int(input("Введите число : "))

mult = 1

for i in range (N):
    mult *= i+1
    print(mult)

print('FINISH')