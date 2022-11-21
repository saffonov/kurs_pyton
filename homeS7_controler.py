import tkinter
import tkinter.messagebox
import sqlite3
import homeS7_view as view

from tkinter import *
from tkinter import ttk



def data_record():
    fio = str(view.fio_entry.get())
    print(fio)
    name = str(view.name_entry.get())
    sname = str(view.sname_entry.get())
    tel = str(view.tel_entry.get())
    RecordToBase(fio, name, sname, tel)
    tkinter.messagebox.showinfo('Записано:', fio + "  " + name +"  " + sname + "  " + str(tel))

def RecordToBase(fio, name, sname, tel):
    cx = sqlite3.connect("contact.db") 
    cur = cx.cursor()
    cur.execute('''INSERT INTO Contact (ItemFIO, ItemName, ItemSname, ItemTel) 
                    VALUES(?, ?, ?, ?)''', (fio, name, sname, tel))   
    cx.commit()
    cx.close()

def view_all():
    cx = sqlite3.connect("contact.db") 
    cur = cx.cursor()
    cur.execute('SELECT ItemFIO, ItemName, ItemSname, ItemTel FROM Contact')
    results = cur.fetchall()
    tkinter.messagebox.showinfo('Справочник',results)
    cx.close()

def data_search():
    fio = str(view.fio_entry.get())
    name = str(view.name_entry.get())
    sname = str(view.sname_entry.get())
    tel = str(view.tel_entry.get())

    cx = sqlite3.connect("contact.db") 
    cur = cx.cursor()
    # cur.execute('''SELECT * FROM Contact WHERE ItemFIO = ?''', ('Иванов',))
    cur.execute('''SELECT * FROM Contact WHERE (ItemFIO = ?) 
                                            OR (ItemName = ?)
                                            OR (ItemSname = ?)
                                            OR (ItemTel = ?)                                           
                                            ''', (fio, name, sname, tel))

    results = cur.fetchall()
    # print(fio, results)
    tkinter.messagebox.showinfo('Справочник', results)
    cx.close()


