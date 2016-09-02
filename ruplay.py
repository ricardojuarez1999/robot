from codigo_robot import Robot
from mapa import Mapa
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

inst = "instrucciones/instruccion1.txt"
print (cargar_instrucciones(inst))

mapa = "mapas/mapa1.txt"
print (Mapa.dibujar(cargar_mapa(mapa)))
