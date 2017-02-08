from tab import Tab
class Navegador(object):
	def __init__(self, nombre, version):
		self.nombre = nombre
		self.version = version
		self.tabs = {}

	def agregar_tab(self, No, nombre, url):
		tab = Tab(nombre,url)
		self.tabs[No] = tab 

	def cambiar_url(self):
			for i in self.tabs:
				print ()

	def mostrar_tab(self):
		for i in self.tabs:
			print(self.tabs[i].nombre, "\t", self.tabs[i].url)