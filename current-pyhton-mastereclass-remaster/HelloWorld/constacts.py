import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name, phone, email) VALUES('Tim'' 1234, 'brian@gmail.com')")
db.execute("INSERT INTO contacts VALUES('Brian', 1234, 'tim@gmail.com')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

#print(cursor.fetchall())

for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)

cursor.close()
db.commit()
db.close()