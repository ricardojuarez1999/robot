import codigo_robot
def cargar_mapa(nombre):
	lista_menor = open(nombre, "r")
	lista = []
	v = ""
	for linea in lista_menor:
		lista.append(list(linea))
	for i in range(len(lista)):
		for j in range(len(lista[i])):
			if lista[i][j] == "0":
				v += " "
			elif lista[i][j] == "\n":
				v += "\n"
			elif lista[i][j] == "*":
				v += codigo_robot.rotar()
			else:
				v += lista[i][j]
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