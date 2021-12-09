import sqlite3
import cgi
form = cgi.FieldStorage()
text1 = form.getfirst("FIO_p", "Не задано")
text2 = form.getfirst("Birth_date", "Не задано")
text3 = form.getfirst("Place_of_living", "Не задано")
text4 = form.getfirst("Blood_type", "Не задано")
text5 = form.getfirst("Diagnosis", "Не задано")

con = sqlite3.connect('mydatabase.db')
cursor = con.cursor()

cursor.execute('INSERT INTO Patient VALUES (?,?,?,?,?,?)', (None, text1, text2, text3, text4, text5))
con.commit()
sqlite_select_query = """SELECT * from Patient"""
cursor.execute(sqlite_select_query)
result = cursor.fetchall()

# print(result)

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
    <html>
    <head>")
      <meta charset="utf-8">
      <title>База данных</title>
    </head>
    <body>  </table> <a href='#' onclick='history.back();return false;'>Вернуться назад</a>""")
print('<h3>Таблица "Пациенты"</h3> <table>')
for row in result:
    print("<tr > ")
    for i in row:
     print("<td> %s   </td>" %i)
    print("</tr>")
print("</table>")
print(""" </body>
    </html>""")

cursor.close()
con.close()
