import sqlite3
import cgi

form = cgi.FieldStorage()
text1 = form.getfirst("Qualification", "Не задано")

con = sqlite3.connect('mydatabase.db')
cursor = con.cursor()

cursor.execute('INSERT INTO Qualification VALUES (?,?)', (None, text1))
con.commit()
sqlite_select_query = """SELECT * from Qualification"""
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
print('<h3>Таблица "Должности врачей"</h3> <table>')
for row in result:
    print("<tr > ")
    for i in row:
     print("<td> %s   </td>" %i)
    print("</tr>")
print(" </table> ")
print(""" </body>
    </html>""")

cursor.close()
con.close()
