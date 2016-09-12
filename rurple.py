from codigo_robot import Robot
from mapa import Mapa
from ficha import Ficha
import utilidades
import time

inst = "instrucciones/instruccion1.txt"
instrucciones = utilidades.cargar_instrucciones(inst)

mapa = "mapas/mapa1.txt"
tamano_mapa = utilidades.cargar_mapa(mapa)

el_mapa = Mapa(utilidades.calcular_dimension_y(mapa), utilidades.calcular_dimension_x(mapa))

for y in range(el_mapa.altura):
	for x in range(el_mapa.ancho):
		if tamano_mapa[y][x] == "*":
			el_robot = Robot(x,y)
			el_mapa.asignar_robot(el_robot)
			el_robot.colocar_en_mapa(el_mapa)
		else:
			cantidad_fichas = int(tamano_mapa[y][x])

			for i in range(cantidad_fichas):
				la_ficha = Ficha(y,x)
				el_mapa.agregar_ficha(la_ficha)
print (el_mapa.dibujar())
for i in instrucciones:
	if i == "MOVER":
		el_robot.mover()
	elif i == "ROTAR":
		el_robot.rotar()
	else:
		el_robot.recoger_fichas(el_robot.x, el_robot.y)
	print (el_mapa.dibujar())
	print (el_robot.x)
	print (el_robot.y)
	time.sleep(1)
