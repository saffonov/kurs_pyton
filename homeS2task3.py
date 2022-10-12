# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one»«onetwonine»-o–2, n –3, e –3

print('START')
Sting1 = (input("Введите первую строку : "))
Sting2 = (input("Введите вторую строку : "))

for i in Sting1:
    k = 0
    for j in Sting2:
        if (i==j) : k +=1
    print (i, "встречается" , k, "раз")

print('FINISH')