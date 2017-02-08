from navegador import Navegador
from tab import Tab
No = 1
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
a = 0
while a != 7:
	a = int(input("opcion: "))
	if a == 1 :
		nomb = input("nombre del tab: ")
		url = input("ingrese la url: ")
		nave.agregar_tab(No, nomb,url,)
		No += 1
	elif a == 2:
		print ("que url desea cambiar?")
		nave.mostrar_tab()
	elif a == 5:
		nave.mostrar_tab()

