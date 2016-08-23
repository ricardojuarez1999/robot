class Robot(object):
	def __init__(self, posicion_x, posicion_y, rotacion, pick, mapa):
		self.posicion_x	= 0
		self.pocicion_y = 0
		self.rotacion = 1
		self.pick = False
		self.mapa = mapa
		self.fichas = 0
	def Sumar_en_X(self):
		if rotacion == 2:
			self.posicion_x += 1
		elif rotacion == 4:
			self.posicion_x -= 1
	def Sumar_en_Y(self):
		if rotacion == 1:
			self.posicion_y -= 1
		elif rotacion == 3:
			self.posicion_y += 1
	def Rotar(self):
		self.rotacion += 1
		if self.rotacion == 5:
			self.rotacion = 1
	def Pickear(self):
		if Hay_ficha(self.x, self.y):
			mapa.quitar_ficha(self.x,self.y)
			self.fichas += 1