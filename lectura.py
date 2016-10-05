import sqlite3

f = sqlite3.connect('personas.db')

resultados = f.execute("SELECT * FROM persona ORDER BY id DESC")
for resultado in resultados:
	print (resultado)

f.commit()

f.close()