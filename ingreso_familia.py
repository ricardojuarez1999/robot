import sqlite3

f = sqlite3.connect('personas.db')

f.execute("INSERT INTO familia(nombre) VALUES  ('Juarez')")
f.execute("INSERT INTO familia(nombre) VALUES  ('Juarez2')")
f.execute("INSERT INTO familia(nombre) VALUES  ('Juarez3')")
f.execute("INSERT INTO familia(nombre) VALUES  ('Juarez4')")
f.execute("INSERT INTO familia(nombre) VALUES  ('Juarez5')")

f.commit()

f.close