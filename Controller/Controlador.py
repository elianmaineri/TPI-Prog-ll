from Views.Vista import Vista
from Models.Cliente import Cliente
from Models.Reserva import Reserva
vst = Vista

class controlador:
    def __init__(self, vista):
        self.vista = vista
    
    def cliente(self,file):   
        self.cliente=[]
        try:
            with open(file) as archivo:
                for line in archivo:
                    data = line.strip().split(';')
                    self.cliente.append(Cliente(str(data[0]), int(data[1]), int(data[2]), str(data[3]), str(data[4])))
        except FileNotFoundError:
                print('No hay datos cargados')

    def reserva(self,file):   
        self.reservas=[]
        try:
            with open(file) as archivo:
                for line in archivo:
                    data = line.strip().split(';')
                    self.reservas.append(Reserva(str(data[0]), str(data[1]), int(data[2]), str(data[3]),))
        except FileNotFoundError:
                print('No hay datos cargados')

    def fecha_dis(self,fecha):
        for x,y in enumerate(self.reservas):
            if (fecha == y.get_dia()):
                vst.mostrar("Esta fecha ya esta reservada ")
                




        
    
    def menu(self):
        while True:
            self.Vista.mostrar_menu()
            choice = self.Vista.validar_entero(0, 4)
            match choice:
                case 0:
                    pass
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    break
