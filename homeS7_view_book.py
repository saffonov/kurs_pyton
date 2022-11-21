import tkinter
import tkinter.messagebox


def convert():
# Получить значение, введенное пользователем в виджет kilo_entry.
    kilo = float(kilo_entry.get())
    miles = kilo * 0.6214
# Показать результаты в информационном диалоговом окне.
    tkinter.messagebox.showinfo ('Результаты', str(kilo) + ' километров эквивалентно ' + str(miles) + ' милям.')

main_window = tkinter.Tk()

top_frame = tkinter.Frame(main_window)
bottom_frame = tkinter.Frame(main_window)

# Создать две рамки, чтобы сгруппировать виджеты.
top_frame = tkinter.Frame(main_window)
bottom_frame = tkinter.Frame(main_window)

# Создать виджеты для верхней рамки.
prompt_label = tkinter.Label(top_frame, text = "Введите расстояние в километрах:")
kilo_entry = tkinter.Entry(top_frame, width = 10)

# Упаковать виджеты верхней рамки.
prompt_label.pack(side='left')
kilo_entry.pack(side='left')

# Создать виджеты Button для нижней рамки.
calc_button = tkinter.Button(bottom_frame, text = "Преобразовать", command = convert)
quit_button = tkinter.Button(bottom_frame, text = " Выйти " , command = main_window.destroy)

# Упаковать кнопки.
calc_button.pack(side='left')
quit_button.pack(side='left')

# Упаковать рамки.
top_frame.pack()
bottom_frame.pack()

# Войти в главный цикл tkinter.
tkinter.mainloop()

# Метод convert является функцией обратного вызова
#для кнопки 'Преобразовать'.










# MainWindow = None
# TopFrame = None

# def CreateMenu():
#     global MainWindow
#     global TopFrame
#     MainWindow=Tk()
#     TopFrame = ttk.Frame(MainWindow, padding=30)
#     TopFrame.grid()
#     ttk.Label(TopFrame, text = "Hello word!").grid(column=0, row=0)
#     # ttk.Button(TopFrame, text = "Result", command=PrintResult).grid(column=0, row=1)
#     EnterUserData("Фамилия")
#     ttk.Button(TopFrame, text = "Quit", command=MainWindow.destroy).grid(column=1, row=0)
#     UserData =  ttk.Entry(TopFrame, width=10)
#     data = UserData.get()

#     MainWindow.mainloop()

# def PrintResult():
#     global MainWindow
#     global frm
#     ttk.Label(frm, text = "Here result").grid(column=1, row=1)

# def EnterUserData(DataLabel):
#     global MainWindow
#     global TopFrame
#     # DataFrame = Frame(MainWindow)
#     DataFrame = TopFrame
#     ttk.Label(DataFrame, text = DataLabel).grid(column=0, row=1)
#     UserData =  ttk.Entry(DataFrame, width=100)
#     return UserData

