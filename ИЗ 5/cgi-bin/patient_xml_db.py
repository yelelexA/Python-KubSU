#!/usr/bin/python
import sqlite3
import cgitb
import xml_func
from xml_func import patient_xml_get
cgitb.enable()

res_list = patient_xml_get()
print(res_list)
con = sqlite3.connect('mydatabase.db')
cursor = con.cursor()

# print(res_list)
for i in res_list:
    cursor.execute('INSERT INTO Patient VALUES (?,?,?,?,?,?)', (None, i[0], i[1], i[2], i[3], i[4]))
    con.commit()

cursor.close()
con.close()

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
    <html>
    <head>")
      <meta charset="utf-8">
      <title>База данных</title>
    </head>
    <body><a href='#' onclick='history.back();return false;'>Вернуться назад</a>""")
print('<h3>Успешно!</h3> ')
print(""" </body </html>""")
