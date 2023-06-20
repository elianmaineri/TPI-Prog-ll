from Views.Vista import Vista
from Models.Cliente import Cliente
from Models.Reserva import Reserva
from Models.Servicios import Servicios
from datetime import date

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
                    self.reservas.append(Reserva(int(data[0]), int(data[1]), int(data[2]), int(data[3]), int(data[4]),  int(data[5])))
        except FileNotFoundError:
                print('No hay datos cargados')

    def servicio(self,file):   
        self.servicios=[]
        try:
            with open(file) as archivo:
                for line in archivo:
                    data = line.strip().split(';')
                    self.servicios.append(Servicios(str(data[0]), str(data[1])))
        except FileNotFoundError:
                print('No hay datos cargados')

    def fecha_dis(self,fecha):
        for x,y in enumerate(self.reservas):
            if (fecha == y.get_dia()):
                vst.mostrar("Esta fecha ya esta reservada ")
            else:
                pass

    def solicitar_servicios(self):
        for i,j in enumerate(self.servicio):
            vst.confirmar_servicios()

    def consultar_fechas(self):
        for line,j in enumerate(self.reservas):
            self.vista.mostrar_reserva((f'{self.reservas[line].get_dia()} - {self.reservas[line].get_mes()} - {self.reservas[line].get_año()} - {self.reservas[line].get_horaInicio()} - {self.reservas[line].get_horaFin()}'))


    def cancelar_reserva(self):
        dia_hoy = date.today()
        mes_hoy = date.today()
        año_hoy = date.today()
        dia_hoy = int(dia_hoy.strftime('%d'))
        mes_hoy = int(mes_hoy.strftime('%m'))
        año_hoy = int(año_hoy.strftime('%Y'))
        for x,y in enumerate(self.reservas):
            diferencia += ((self.reservas[x].get_año() - año_hoy)*365)
            diferencia += ((self.reservas[x].get_mes() - mes_hoy)*30)
            diferencia += (self.reservas[x].get_dia() - dia_hoy)
            if diferencia >= 15:
                devolver = (self.reservas.get_seña()/1.2)
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
                    self.consultar_fechas()
                case 2:
                    self.cancelar_reserva()
                case 3:
                    break
