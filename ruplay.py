def cargar_mapa(nombre):
	lista_menor = open(nombre, "r")
	lista = []
	v = ""
	for linea in lista_menor:
		lista.append(list(linea))
	for i in lista:
		for e in lista[i]:
			if lista[i][e] == 0:
				v += " "
			else:
				v += lista[i,e]
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