#!/usr/bin/python
import sqlite3
import cgitb
import xml_func
from xml_func import patient_xml_set

cgitb.enable()

con = sqlite3.connect('mydatabase.db')
cursor = con.cursor()

sqlite_select_query = """SELECT * from Patient"""
cursor.execute(sqlite_select_query)

res_list = cursor.fetchall()

for i in res_list:
        # i = list(i)
        # i.pop(0)
        patient_xml_set(i)

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
