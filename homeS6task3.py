# Задача 3. Найдите все простые несократимые дроби, лежащие между 0 и 1, 
# знаменатель которых не превышает 11.

num = [i+1 for i in range(11)]


for i in range(11):
    for j in range(i):
        if((num[i]%2 == 0) and (num[j]%2 == 0)) or ((num[i]%3 == 0) and (num[j]%3 == 0)): flag = False
        else: 
            #flag = True  
            #print(num[j] ,"/", num[i], flag)
            print(num[j] ,"/", num[i])
