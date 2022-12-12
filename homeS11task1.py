# Задача 1. Постройте график функции
# 𝑓 𝑥 = 5𝑥^2 + 10𝑥 − 30
# По графику определите, при каких значения x значение функции отрицательно.

from math import sqrt
import numpy as np

import matplotlib.pyplot as plt

# y = (5*x*x + 10*x - 30)
# y = (a*x*x + b*x +c)
a = 5
b= 10
c = -30


def SolveSQRfunction(a, b, c):
    # ax^2 + bx + c
    # x1, 2 = (-b+-sqrt(b*b - 4ac))/2a
    D = b*b - 4*a*c
    if D >= 0:
        x2 = (-b + sqrt(D)) / (2*a)
        x1 = (-b - sqrt(D)) / (2*a)
        text = "The discriminant is: %s \n X1 is: %s \n X2 is: %s \n" % (D, x1, x2)       
    else:
        text = "The discriminant is: %s \n This equation has no solutions" % D
    print(text)
    return x1, x2, text

def Function(x):
    y = (a*x*x + b*x +c)
    return y



x = np.linspace(-5, 5, 100)
y = [Function(i) for i in x]

[x1, x2, message] = SolveSQRfunction(a, b, c)



# Построение графика
plt.title("Квадратичная зависимость зависимость y = 5х^2 + 10х − 30") # заголовок
plt.xlabel("x") 
plt.ylabel("y") 
plt.grid()      
plt.plot(x, y)
plt.plot(x1, 0, marker='v', color="red") 
plt.plot(x2, 0, marker='o', color="red")
plot_annot = "Между {0:5.2f} и {1:5.2f} функция отрицателmная".format(x1, x2)
plt.text(-4, 15, plot_annot)
plt.show()