class Navegador(object):
	def __init__(self, nombre, version):
		self.nombre = nombre
		self.version = version
		self.tab = {}

	def agregar_tab(self, nombre, url):
		self.tab[nombre] = url

	def cambiar_url(self,tab):


	def mostrar_tab(self):
		print(self.tab)
