from Controller.Controlador import controlador
from Views.Vista import Vista

archivo = 'Servicios.txt'
archivo2 = 'Reserva.txt'
archivo3 = 'Cliente.txt'
vista = Vista()
Controlador = controlador(vista)

Controlador.menu()
