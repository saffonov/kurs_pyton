# Задача 4. 
# Напишите программу, которая на вход принимает число (N), 
# а на выходе показывает все чётные числа от 1 до N.
# 5 -> 2, 4
# 8 -> 2, 4, 6, 8

print('START')
num = int(input("Введите число : "))

i = 1;

if (num >= 0):
    while i <= num:
        if not(i % 2) : print(i)
        i+=1
else: print("Введено отрицательное значение")

print('FINISH')
