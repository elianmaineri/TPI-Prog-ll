from Views.Vista import Vista
from Models.Cliente import Cliente
from Models.Reserva import Reserva
from Models.Servicios import Servicios

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
                    self.reservas.append(Reserva(str(data[0]), str(data[1]), int(data[2]), str(data[3])))
        except FileNotFoundError:
                print('No hay datos cargados')

    def servicio(self,file):   
        self.servicios=[]
        try:
            with open(file) as archivo:
                for line in archivo:
                    data = line.strip().split(';')
                    self.servicios.append(Servicios(str(data[0]), str(data[1]), str(data[2]), str(data[3]), str(data[4]), str(data[5])))
        except FileNotFoundError:
                print('No hay datos cargados')

    def chek_fecha(self,dia,mes,ano,):
        a = True
        for x,y in enumerate(self.reservas):
            if (dia == y.get_dia()) and (y.get_mes()==mes) and (y.get_ano()==ano):
                vst.mostrar("Esta fecha ya esta reservada ")
                a = False
            else:
                pass
        
        if a :
            return (dia,mes,ano) 
        else:
            vst.mostrar("dias disponibles ")
            for i in range(-5,5,1):
                b = dia+i
                if b==0:
                    dia += 30 
                    mes -= 1
                else:
                    pass
                for x,y in enumerate(self.reservas):
                    if (dia == y.get_dia()) and (y.get_mes()==mes) and (y.get_ano()==ano):
                        pass
                    else:
                        vst.mostrar(f"{dia}/{mes}/{ano}")
    



    def solicitar_servicios(self):
        for i,j in enumerate(self.servicio):
            vst.confirmar_servicios()

    def cancelar_reserva(self):
        for x,y in enumerate(self.reservas):
            #sacar duda
            if self.reservas[x].get_fecha() >= 15:
                devolver = (self.reserva.get_seña()/1.2)
                self.vista.devolver_dinero(devolver)
            else:
                self.vista.no_devolver()

    
    def menu(self):
        while True:
            self.vista.mostrar_menu()
            choice = self.vista.validar_entero(0, 4)
            match choice:
                case 0:
                    pass
                case 1:
                    pass
                case 2:
                    self.cancelar_reserva()
                case 3:
                    break
