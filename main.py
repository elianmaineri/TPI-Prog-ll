from Controller.Controlador import controlador
from Views.Vista import Vista

archivo = 'Servicios.txt'
vista = Vista()
Controlador = controlador(vista)

Controlador.menu()
