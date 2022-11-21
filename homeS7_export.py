import sqlite3
import webbrowser
import homeS7_view as view

filename_html = 'file.html'
filename_xml = 'file.xml'

pattern_html = '''
<html>
<head>
    <meta content="text/html; charset=Win-1251"
    http-equiv="content-type">
    <title>Телефоный справочник</title>
</head>
<body>
    <table>
    <tr><th>Фамилия</th><th>Имя</th><th>Отчество</th><th>Телефон</th></tr>
    %s
    </table>
</body>
</html>
'''

pattern_xml = '''<?xml version="1.0" encoding="windows-1251"?>
<phonebook>
    %s
</phonebook>
'''


def get_all_data(flag):
    cx = sqlite3.connect("contact.db") 
    cur = cx.cursor()
    cur.execute('SELECT ItemFIO, ItemName, ItemSname, ItemTel FROM Contact')
    results = cur.fetchall()
    # print(results)

    # p = "<tr><th>Фамилия</th><th>Имя</th><th>Отчество</th><th>Телефон</th></tr>"
    p = ""
    for row in results:
        if flag == "html":
            p = p + "<tr><td>%s</td>"%row[0] + "<td>%s</td>"%row[1] + "<td>%s</td>"%row[2] + "<td>%s</td></tr>"%row[3]
        elif flag == "xml":
            p = p + "\n" + "<men>" + "\n" + \
                "\t" + "<fio>%s</fio>"%row[0] + "\n"  +\
                "\t" + "<name>%s</name>"%row[1] + "\n"  +\
                "\t" + "<sname>%s</sname>"%row[2] + "\n" +\
                "\t" + "<tel>%s</tel>"%row[3] + "\n" +\
                "</men>" 

  
    cx.close()
    # return pattern_html%(p)
    return p

def CreateHtml():
    output = open(filename_html,"w")
    output.write(pattern_html%(get_all_data("html")))
    output.close()
    webbrowser.open(filename_html)

def CreateXml():
    output = open(filename_xml,"w")
    output.write(pattern_xml%(get_all_data("xml")))
    output.close()
    webbrowser.open(filename_xml)




# CreateHtml(filename)    
# webbrowser.open(filename)