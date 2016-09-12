class Mapa(object):
	def __init__(self, altura, ancho):
		self.altura = altura
		self.ancho = ancho
		self.fichas = []
		self.robot = None

	def conteo_de_fichas(self, x, y):
		conteo = 0
		for f in self.fichas:
			if f.x == x and f.y == y:
				conteo += 1
		return conteo

	def dibujar(self):
		resultado = ""
		for y in range(self.altura):
			for x in range(self.ancho):
				if self.robot.x == x and self.robot.y == y:
					resultado += self.robot.dibujar()
				elif self.conteo_de_fichas(x,y) > 0:
					resultado += str(self.conteo_de_fichas(x,y))
				else:
					resultado += " "
			resultado += "\n"
		return resultado

	def agregar_ficha(self,ficha):
		self.fichas.append(ficha)

	def asignar_robot(self, robot):
		self.robot = robot

	def hay_ficha(self, x, y):
		hay = False
		for f in self.fichas:
			if f.x == self.robot.x and f.y == self.robot.y:
				hay = True
				break
		return  hay

	def quitar_ficha(self,x,y):
		for f in fichas:
			if ficha.x == x and ficha.y == y:
				self.fichas.pop(ficha)
				break