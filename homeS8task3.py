# Задача 3. В двумерном массиве хранятся средние дневные температуры с мая по сентябрь за
# прошлый год. Каждому месяцу соответствует своя строка. Определите самый жаркий и
# самый холодный 7-дневный промежуток этого периода. Выведите его даты.

import calendar
import random

from datetime import datetime, timedelta

def GeneratorCalendar(СurrentYear, StartMonth, StopMonth):
    # c = calendar.TextCalendar(calendar.THURSDAY)
    MyCalendar =[0]*(StopMonth+1 - StartMonth)
    for month in range(StartMonth, StopMonth+1):
        MyCalendar[month-StartMonth] = list(i+1 for i in range((calendar.monthrange(СurrentYear, month)[1])))
    return MyCalendar

def GetRandomTemperatureList(M):
    RandomArray = list(random.randint(0, 30) for _ in range(M))
    return RandomArray

def GetRandomTemperatureCalendarInLine(Calendar):
    TemperatureInLine = []
    for i in range (len(Calendar)):
        TemperatureInLine += GetRandomTemperatureList(len(Calendar[i]))
        # print(TemperatureInLine)
    return TemperatureInLine

def FindMaxAndMin_Index_in7Window(DataLine):
    IndexMax = 0
    IndexMin = 0
    Max = sum(DataLine[i] for i in range(6))
    Min = Max
    for i in range(1,(len(DataLine) - 6)):
        WindowSum = sum(DataLine[j] for j in range(i,(i+6)))
        if Min > WindowSum: IndexMin = i
        if Max < WindowSum: IndexMax = i
    return IndexMin, IndexMax

def DefineData(MyCalendar, Start_Month, day):
    CurrentMonth = 0
    currentDay = day
    while currentDay > len(MyCalendar[CurrentMonth]):
        currentDay -= len(MyCalendar[CurrentMonth])
        CurrentMonth += 1
    CurrentMonth = CurrentMonth + Start_Month
    return CurrentMonth, currentDay

def PrintData7Day(DataTime):
    for i in range(7):
        # print(DataTime.strftime('%A %d %B %Y'))
        print(DataTime)
        DataTime = DataTime + timedelta(days=1)

Сurrent_Year = 2021
Start_Month = 5
Stop_Month = 9

Calendar = GeneratorCalendar(Сurrent_Year, Start_Month, Stop_Month)
TemperatureDataLine = GetRandomTemperatureCalendarInLine(Calendar)
Index = list(FindMaxAndMin_Index_in7Window(TemperatureDataLine))
print(Index)
DataMin = DefineData(Calendar, Start_Month, Index[0])
DataMax = DefineData(Calendar, Start_Month, Index[1])

print("Дни минимума температуры:")
PrintData7Day(datetime(Сurrent_Year, DataMin[0], DataMin[1]))

print("Дни максимума температуры:")
PrintData7Day(datetime(Сurrent_Year, DataMax[0], DataMax[1]))




