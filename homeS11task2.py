# Задача 2. Имеются данные о площади и стоимости 15 домов.
# Риелтору требуется узнать в каких домах стоимость квадратного метра меньше 50000
# рублей.
# Предоставьте ему графические данные о стоимость квадратного метра каждого дома и
# список подходящих ему домов, отсортированных по площади.
# Данные о домах сформируйте случайным образом. Площади от 100 до 300 кв. метров,
# цены от 3 до 20 млн.

import random
import matplotlib.pyplot as plt

def GenRNDhomeData(n):
    home_data = []*n
    for i in range(1, n+1):
        S = random.randint(100, 300)
        cost = random.randint(3, 20)
        one_home=[i, S, cost]
        home_data.insert(i, one_home)
    return home_data

def SortGoodHome(Home):
    Home.sort(key=custom_key)
    return Home

def custom_key(house):
    return house[2]


N = 15
Level = 0.05 # in million 50000 rub

# Home_Count = list(range(1, N+1))

Home_Data = GenRNDhomeData(N)

# for i in range (N): print(Home_Data[i])
# for i in range (N): print(Home_Data[i][0]) #N
# for i in range (N): print(Home_Data[i][1]) #S
# for i in range (N): print(Home_Data[i][2]) #cost

Home_N = []
for i in range (N): Home_N.append(Home_Data[i][0]) #N

Home_S = []
for i in range (N): Home_S.append(Home_Data[i][1]) #NS

Home_Cost = []
for i in range (N): Home_Cost.append(Home_Data[i][2]) #NS

Home_Cost_div_S = []
Good_level_Home =[]
for i in range (N):
    C_div_S = Home_Data[i][2] / Home_Data[i][1] 
    Home_Cost_div_S.append(C_div_S) #NS
    if C_div_S <= Level: Good_level_Home.append([i+1, C_div_S, Home_Data[i][1]] )


# print(Good_level_Home)
# print('Сортровка:')
# print(SortGoodHome(Good_level_Home))

Good_level_Home = SortGoodHome(Good_level_Home)
# print(Good_level_Home)




fig , ax = plt.subplots(nrows = 4)

ax[0].bar(Home_N, Home_S)
ax[0].set_title("Площадь дома")

ax[1].bar(Home_N, Home_Cost)
ax[1].set_title("Стоимость дома ")

ax[2].bar(Home_N, Home_Cost_div_S)
ax[2].set_title("Стоимость кв.м.")
str_label = '50000 за кв.м'
ax[2].hlines(Level, 0, N, color = 'r', linestyles = 'dashed', label = str_label)

column_labels=["Номер дома", "стоимость кв.м", "Площадь"]
ax[3].axis('tight')
ax[3].axis('off')
ax[3].table(cellText = Good_level_Home, colLabels = column_labels, loc="center")


plt.show()
