from tab import Tab
class Navegador(object):
	def __init__(self, nombre, version):
		self.nombre = nombre
		self.version = version
		self.tabs = {}

	def agregar_tab(self, nombre, url):
		tab = Tab(nombre,url)
		self.tabs[nombre] = tab 

	def cambiar_url(self):
			for i in self.tabs:
				print ()

	def mostrar_tab(self):
		print(self.tabs)
