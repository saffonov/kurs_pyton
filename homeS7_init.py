import sqlite3

def InitContact():
    cx = sqlite3.connect("contact.db") 
    cur = cx.cursor()

    cur.execute( 'DROP TABLE IF EXISTS Contact ')

    cur.execute('''CREATE TABLE Contact
                                    (
                                        ItemID INTEGER PRIМARY КЕУ,
                                        ItemFIO TEXT,
                                        ItemName TEXT,
                                        ItemSname TEXT,
                                        ItemTel TEXT  
                                    )
                ''')   
    cx.commit()
    cx.close()

def InitBd():
    cx = sqlite3.connect("contact.db") 
    cur = cx.cursor()
    cur.execute('''INSERT INTO Contact (ItemFIO, ItemName, ItemSname, ItemTel) 
                    VALUES('Иванов', 'Иван', 'Иванович' , '811111111' )''')

    cur.execute('''INSERT INTO Contact (ItemFIO, ItemName, ItemSname, ItemTel) 
                    VALUES('Сидоров', 'Сидор', 'Сидорович' , '83333333' )''')
             

    cx.commit()
    cx.close()