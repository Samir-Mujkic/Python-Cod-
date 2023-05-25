import sqlite3

db = sqlite3.connect("contacts.sqlite")

update_sql = "UPDATE contacts SET email = "update@update.com" WHERE phone = 1234"
update_cursor = db.cursor()
update_cursor.execute(update_sql)
print("{} rows updates".format(update_cursor.rowcount))

update_cursor.connection.commit()#abdetujemo novo sto smo odradili u tabelu

update_cursor.close() # od 5 do 10 smo ubacili email a da ide poslije WHERE phone is 1234
#zamjenili bi smo na tome mjestu dje je taj broj sa emailom.

for row in db.execute("SELECT * FROM contacts"):
    print(row)

db.close()