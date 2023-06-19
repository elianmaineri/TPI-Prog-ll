from Views.Vista import Vista
from Models.Cliente import Cliente

class controlador:
<<<<<<< HEAD
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

def fecha_dis(self):
    

=======
    def __init__(self, file, vista):
            try:
                self.cliente = []
                self.Vista = vista
                with open(file) as archivo:
                    for line in archivo:
                        data = line.strip().split(';')
                        self.cliente.append(Cliente(str(data[0]), int(data[1]), int(data[2]), str(data[3]), str(data[4])))
            except FileNotFoundError:
                print('No hay datos cargados')
>>>>>>> 44a6667357f1136f0065ca598dfbe679edb612b6


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
