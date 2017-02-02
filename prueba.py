from navegador import Navegador
from tab import Tab
nave = Navegador("nave", 1.0)
print ("""
	 _________________________
	|          MENU          |
	|1.Crear nuevo tab.      |
	|2.Cambiar url del tab.  |
	|3.Cerrar tab.           |
	|4.Carrar todos los tabs.|
	|5.Mostrar mis tabs.     |
	|6.Guardar mis tabs.     |
	|7.Salir.                |
	|________________________|
	""")
a = int(input("opcion: "))
while a != 7:
	if a == 1 :
		nomb = input("nombre del tab: ")
		url = input("ingrese la url: ")
		nave.agregar_tab(nomb,url)
	elif a == 2:
		print ("que url desea cambiar?")
		nave.mostrar_tab()