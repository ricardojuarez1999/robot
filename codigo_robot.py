class Robot(object):
	def __init__(self, posicion_x, posicion_y):
		self.posicion_x	= posicion_x
		self.pocicion_y = posicion_y
		self.rotacion = 1
		self.mapa = mapa
		self.fichas = 0
	def sumar_en_X(self):
		if rotacion == 2:
			self.posicion_x += 1
		elif rotacion == 4:
			self.posicion_x -= 1
	def sumar_en_Y(self):
		if rotacion == 1:
			self.posicion_y -= 1
		elif rotacion == 3:
			self.posicion_y += 1
	def rotar(self):
		self.rotacion += 1
		if self.rotacion == 5:
			self.rotacion = 1
		if self.rotacion == 1:
			return "▲"
		elif self.rotacion == 2:
			return "►"
		elif self.rotacion == 3:
			return "▼"
		elif self.rotacion == 4:
			return "◄"
	def pickear(self):
		if Hay_ficha(self.posicion_x, self.posicion_y):
			mapa.quitar_ficha(self.x,self.y)
			self.fichas += 1