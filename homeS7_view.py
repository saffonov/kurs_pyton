# from tkinter import *
# from tkinter import ttk

import tkinter
import tkinter.messagebox

import homeS7_controler as controler
import homeS7_export as export



def CreateMenu():
    global fio_entry
    global name_entry
    global sname_entry
    global tel_entry

    main_window = tkinter.Tk()
    top_frame = tkinter.Frame(main_window) # Frame for enter data
    middle_frame = tkinter.Frame(main_window) # Frame for screach data
    bottom_frame = tkinter.Frame(main_window) #Frame for menu button

    fio_label = tkinter.Label(top_frame, text = "Фамилия:")
    fio_entry = tkinter.Entry(top_frame, width = 10)

    name_label = tkinter.Label(top_frame, text = "Имя:")
    name_entry = tkinter.Entry(top_frame, width = 10)

    sname_label = tkinter.Label(top_frame, text = "Отчество:")
    sname_entry = tkinter.Entry(top_frame, width = 10)

    tel_label = tkinter.Label(top_frame, text = "Телефон:")
    tel_entry = tkinter.Entry(top_frame, width = 10)

    # Packed frame for data.
    fio_label.pack(side='left')
    fio_entry.pack(side='left')

    name_label.pack(side='left')
    name_entry.pack(side='left')

    sname_label.pack(side='left')
    sname_entry.pack(side='left')

    tel_label.pack(side='left')
    tel_entry.pack(side='left')

    # Menu.
    record_button = tkinter.Button(bottom_frame, text = "Записать", command = controler.data_record)
    search_button = tkinter.Button(bottom_frame, text = "Поиск", command = controler.data_search)
    view_all_button = tkinter.Button(bottom_frame, text = "Показать все", command = controler.view_all)

    export2html_button = tkinter.Button(bottom_frame, text = "Экспорт в html", command = export.CreateHtml)
    export2xml_button = tkinter.Button(bottom_frame, text = "Экспорт в xml]", command = export.CreateXml)

    quit_button = tkinter.Button(bottom_frame, text = " Выйти " , command = main_window.destroy)

    # Packed button.
    record_button.pack(side='left')
    search_button.pack(side='left')
    view_all_button.pack(side='left')
    export2html_button.pack(side='left')
    export2xml_button.pack(side='left')
    quit_button.pack(side='left')

    # Packed frame.
    top_frame.pack()
    middle_frame.pack()
    bottom_frame.pack()

    tkinter.mainloop()


