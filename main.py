from Servicios import Servicios
from Cliente import Cliente
from Reserva import Reserva

evento1 = Servicios("No", "Si", "No", "Si", "No", "Si")

evento2 = Servicios(input("Quiere Dj? "), input("Quiere Decoracion? "), input("Quiere Cotillon? "), input("Quiere Maquina de humo? "), input("Quiere Maquillaje? "), input("Quiere Musica en vivo? ") )

print(f"Evento 1: {evento1}")
print(f"Evento 2: {evento2}")
