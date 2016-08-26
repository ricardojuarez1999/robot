class Mapa(object):
	def __init__(self, altura, ancho, fichas, robot):
		self.altura = altura
		self.ancho = ancho
		self.fichas = []
		self.robot = robot
	def quitar_richa(self):
		