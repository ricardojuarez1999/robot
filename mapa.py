class Mapa(object):
	def __init__(self, altura, ancho):
		self.altura = altura
		self.ancho = ancho
		self.fichas = []
		self.robot = None

	def dibujar(self):
		resultado = ""
		for y in range(self.altura):
			for x in range(self.ancho):
				if ficha.x == x and ficha.y == y:
					resultado += ficha
					self.agregar_ficha(ficha)
				elif robot.x == x and robot.y == y:
					resultado += robot
				else:
					resultado += " "
			resultado += "\n"

	def conteo_de_fichas(self, x, y):
		conteo = 0
		for f in fichas:
			if ficha.x == x and ficha.y == y:
				conteo += ficha
		return conteo

	def agregar_ficha(self,ficha):
		self.fichas.append(ficha)

	def asignar_robot(self, robot):
		self.robot = robot

	def hay_ficha(self, x, y):
		hay = False
		for f in fichas:
			if ficha.x == self.robot.x and ficha.y == self.robot.y:
				hay = True
				break
		return  hay

	def quitar_ficha(self,x,y):
		for f in fichas:
			if ficha.x == x and ficha.y == y:
				self.fichas.pop(ficha)
				break