import sqlite3

f = sqlite3.connect('personas.db')

f.execute ("CREATE TABLE  familia (id integer primary key AUTOINCREMENT, nombre text)")

f.execute ("CREATE TABLE persona (id integer primary key AUTOINCREMENT, nombre text, apellido text, edad integer, familia_id integer, FOREING KEY (familia_id) REFERENCES familia(id))")

f.commit()

f.close()