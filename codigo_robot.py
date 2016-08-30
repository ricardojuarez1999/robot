class Robot(object):
	def __init__(self, posicion_x, posicion_y):
		self.posicion_x	= posicion_x
		self.pocicion_y = posicion_y
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

	def recoger_fichas(self,x,y):
		