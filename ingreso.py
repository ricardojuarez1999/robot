import sqlite3

f = sqlite3.connect('personas.db')

f.execute("INSERT INTO persona(nombre, apellido, edad, familia_id) VALUES  ('erick', 'lopez', 12, 1)")
f.execute("INSERT INTO persona(nombre, apellido, edad, familia_id) VALUES  ('erika', 'mendez', 15, 1)")
f.execute("INSERT INTO persona(nombre, apellido, edad, familia_id) VALUES  ('rainer', 'escobar', 13, 2)")
f.execute("INSERT INTO persona(nombre, apellido, edad, familia_id) VALUES  ('adrian', 'gevara', 17, 2)")
f.execute("INSERT INTO persona(nombre, apellido, edad, familia_id) VALUES  ('diego', 'barrios', 18, 100)")
	
f.commit()

f.close()