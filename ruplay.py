def cargar_mapa(nombre):
	lista_menor = open(nombre, "r")
	lista = []
	v = ""
	for linea in lista_menor:
		lista.append(list(linea))
	for i in lista:
		for i2 in len(lista[i]):
			if lista[i][i2] == 0:
				v += " "
			elif lista[i][i2] == "\n":
				v += "\n"
			else:
				v += lista[i][i2]
	return v
mapa = "mapas/mapa1.txt"
print (cargar_mapa(mapa))

def cargar_instrucciones(nombre):
	instrucciones = open(nombre, "r")
	lista_2 = []
	for linea in instrucciones:
		lista_2.append(linea.strip())
	return lista_2
inst = "instrucciones/instruccion1.txt"
print (cargar_instrucciones(inst))