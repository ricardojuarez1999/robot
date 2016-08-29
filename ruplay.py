from codigo_robot import Robot
from mapa import Mapa
def cargar_mapa(nombre):
	lista_menor = open(nombre, "r")
	lista = []
	v = ""
	robot = Robot(0,0)
	for linea in lista_menor:
		lista.append(list(linea))
	for i in range(len(lista)):
		for j in range(len(lista[i])):
			if lista[i][j] == "0":
				v += " "
			elif lista[i][j] == "\n":
				v += "\n"
			elif lista[i][j] == "*":
				v += robot.rotar()
			else:
				v += lista[i][j]
	return v
def cargar_instrucciones(nombre):
	instrucciones = open(nombre, "r")
	lista_2 = []
	for linea in instrucciones:
		lista_2.append(linea.strip())
	return lista_2
inst = "instrucciones/instruccion1.txt"
print (cargar_instrucciones(inst))

mapa = "mapas/mapa1.txt"
print (cargar_mapa(mapa))