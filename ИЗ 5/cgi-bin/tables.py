import cgi
import sqlite3

dic = {"1": "Patient", "2": "Doctors", "3": "Qualification", "4": "Visit_Log"}
dic_rus = {"Patient": "Пациенты", "Doctors": "Врачи", "Qualification": "Должности врачей", "Visit_Log": "Визиты"}
val = None
form = cgi.FieldStorage()
text1 = form.getfirst("table", "None")

for i, j in dic.items():
    if i == text1:
        val = j

for i, j in dic_rus.items():
    if i == val:
        val_rus = j

con = sqlite3.connect('mydatabase.db')
cursor = con.cursor()

if val is not None:
 sqlite_select_query = """SELECT * from """+val
 cursor.execute(sqlite_select_query)
 result = cursor.fetchall()

 print("Content-type: text/html\n")
 print("""<!DOCTYPE HTML>
    <html>
    <head>")
      <meta charset="utf-8">
      <title>База данных</title>
    </head>
    <body><a href='#' onclick='history.back();return false;'>Вернуться назад</a>""")
 print('<h3>Таблица "%s"</h3> <table>' %val_rus)
 for row in result:
    print("<tr > ")
    for i in row:
     print("<td> %s   </td>" %i)
    print("</tr>")
 print(" </table> ")
 print(""" </body>
    </html>""")
else:
   print("Content-type: text/html\n")
   print("""<!DOCTYPE HTML>
    <html>
    <head>")
      <meta charset="utf-8">
      <title>База данных</title>
    </head>
    <body><a href='#' onclick='history.back();return false;'>Вернуться назад</a>""")
   print('<h3>Ошибка при выполнении запроса</h3>')
   print(""" </body>
    </html>""")

cursor.close()
con.close()
