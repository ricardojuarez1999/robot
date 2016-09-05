from codigo_robot import Robot
from mapa import Mapa
from ficha import Ficha
import utilidades

inst = "instrucciones/instruccion1.txt"
instrucciones = utilidades.cargar_instrucciones(inst)

mapa = "mapas/mapa1.txt"
tamaño_mapa = utilidades.cargar_mapa(mapa)

el_mapa = Mapa(utilidades.calcular_dimension_y(mapa), utilidades.calcular_dimension_x(mapa))

for y in tamaño_mapa:
	for x in tamaño_mapa[y]:
		if tamaño_mapa[y][x] == "*":
			print ("hola")
		else:
			print ("*")
