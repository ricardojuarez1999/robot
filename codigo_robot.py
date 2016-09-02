class Robot(object):
	def __init__(self, posicion_x, posicion_y):
		self.x	= posicion_x
		self.y = posicion_y
		self.rotacion = 0
		self.mapa = None
		self.fichas = 0

	def rotar(self):
		self.rotacion = (self.rotacion + 1) % 4

	def dibujar(self):
		if self.rotacion == 0:
			return "^"
		elif self.rotacion == 1:
			return ">"
		elif self.rotacion == 2:
			return "v"
		return "<"

	def colocar_en_mapa(self,mapa):
		self.mapa = mapa

	def mover(self):
		if self.rotacion == 0:
			self.y -= 1
			if self.y < 0:
				self.y = 0
		elif self.rotacion == 1:
			self.x += 1
			if self.x > 79:
				self.x = 79
		if self.rotacion == 2:
			self.y += 1
			if self.y > 49:
				self.y = 49
		else:
			self.x -= 1
			if self.x < 0:
				self.x = 0

	def recoger_fichas(self, x, y):
		if self.mapa.hay_ficha():
			self.fichas += 1