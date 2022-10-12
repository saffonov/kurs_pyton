# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧Y) ∨Z.

print('START')

for X in range(2):
    for Y in range(2):
        for Z in range(2):
            F = bool(not(X and Y) or Z)
            print(X, Y, Z, F)

print('FINISH')