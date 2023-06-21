from Views.Vista import Vista
from Models.Cliente import Cliente
from Models.Reserva import Reserva
from Models.Servicios import Servicios
from datetime import date
gastosadm= (5000)
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
    
    def servselecs(self,file): 
        lista = []  
        self.servselec=[]
        co = 0
        try:
            with open(file) as archivo:
                for line in archivo:
                    data = line.strip().split(';')
                    for i,j in enumerate(data):
                        if i>1:
                            lista.append(data[i])
                        else:
                            pass
                    self.servselec.append(Servicios(str(data[0]), str(data[1] , lista)))
        except FileNotFoundError:
                print('No hay datos cargados')


    def chek_fecha(self,dia,mes,ano,):
        serv=[]
        a = True
        for x,y in enumerate(self.reservas):
            if (dia == y.get_dia()) and (y.get_mes()==mes) and (y.get_ano()==ano):
                vst.mostrar("Esta fecha ya esta reservada ")
                a = False
            else:
                pass
        if a :
            serv.append(dia)
            serv.append(mes)
            serv.append(ano)
            return (serv) 
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
    
    def seleccion_servicios(self):
        while True:
            serv_sel=[]
            vst.menu_ser()
            op=vst.validar_entero(1,2)
            if op == 1 :
                for i,j in enumerate(self.servicios):
                    vst.mostrar(f"{i+1} - {j[i].get_nombre()}")
                a=vst.validar_entero(1,len(self.servicios))
                serv_sel.append(self.servicios[i-1])
            else:
                break

        return serv_sel
    
    def calcular_pago(self,list,res):
        a=0 
        for i,j in enumerate(list):
            a += (j.get_precio()*res.get_duracion())
            a += (gastosadm)
            a = (a*1.21)
        return a 
    
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
            choice = self.vista.validar_entero(0, 5)
            match choice:
                case 0:
                    aux=self.chek_fecha()
    
                case 1:
                    self.consultar_fechas()
                case 2:
                    self.cancelar_reserva()
                case 4:
                    break
