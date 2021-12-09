import sqlite3
sqlite_connection = sqlite3.connect('mydatabase.db')
cursor = sqlite_connection.cursor()

query1 = '''CREATE TABLE IF NOT EXISTS "Qualification" (
	"ID_Qualification"	INTEGER,
	"Qualification"	TEXT,
	PRIMARY KEY("ID_Qualification" AUTOINCREMENT)
);'''
query2 = '''CREATE TABLE IF NOT EXISTS "Visit_Log" (
	"ID_Visit"	INTEGER,
	"Date_Of_Visit"	TEXT NOT NULL,
	"ID_Patient"	INTEGER,
	"ID_Doctor"	INTEGER,
	FOREIGN KEY("ID_Doctor") REFERENCES "Doctors"("ID_Doctor"),
	FOREIGN KEY("ID_Patient") REFERENCES "Patient"("ID_Patient"),
	PRIMARY KEY("ID_Visit" AUTOINCREMENT)
);'''
query3 = '''CREATE TABLE IF NOT EXISTS "Patient" (
	"ID_Patient"	INTEGER,
	"FIO_Patient"	TEXT NOT NULL,
	"Birth_Date"	TEXT NOT NULL,
	"Place_Of_Living"	TEXT,
	"Blood_Type"	INTEGER NOT NULL,
	"Diagnosis"	TEXT,
	PRIMARY KEY("ID_Patient")
);'''
query4 = '''CREATE TABLE IF NOT EXISTS "Doctors" (
	"ID_Doctor"	INTEGER,
	"FIO_Doctor"	TEXT NOT NULL,
	"ID_Qualification"	INTEGER UNIQUE,
	PRIMARY KEY("ID_Doctor" AUTOINCREMENT),
	FOREIGN KEY("ID_Qualification") REFERENCES "Qualification"("ID_Qualification")
);'''
cursor.execute(query1)
cursor.execute(query3)
cursor.execute(query4)
cursor.execute(query2)

sqlite_insert_query1 = """INSERT INTO Qualification
                          (ID_Qualification, Qualification)  VALUES (NULL, ?)"""


sql_delete_query1 = """DELETE from Qualification where ID_Qualification > 10"""
cursor.execute(sql_delete_query1)

sql_select_query1 = """SELECT * from Qualification where ID_Qualification > 5"""
cursor.execute(sql_select_query1)
rows = cursor.fetchall()

print(rows)

query1_list = [["Психотерапевт"], ["Иммунолог"]]
for i in query1_list:
 cursor.execute(sqlite_insert_query1,  (i))

sqlite_connection.commit()
cursor.close()
sqlite_connection.close()
