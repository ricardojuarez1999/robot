def cargar_mapa(nombre):
	lista_menor = open(nombre, "r")
	lista = []
	for linea in lista_menor:
		lista.append(list(linea))
	return lista

def cargar_instrucciones(nombre):
	instrucciones = open(nombre, "r")
	lista_2 = []
	for linea in instrucciones:
		lista_2.append(linea.strip())
	return lista_2

def calcular_dimension_y(nombre):
	lista = cargar_mapa(nombre)
	return (len(lista))

def calcular_dimension_x(nombre):
	lista = cargar_mapa(nombre)
	return (len(lista[1])-1)