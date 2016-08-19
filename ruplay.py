def cargar_mapa(nombre):
	lista_menor = open(nombre, "r")
	lista = []
	for linea in lista_menor:
		lista.append(list(linea))
	return lista
mapa = "mapas/mapa1.txt"
print (cargar_mapa(mapa))