class Reserva:
    def __init__(self, dia, mes, año, horaInicio,duracion,idc,ids,paga):
        self.dia = dia
        self.mes = mes
        self.año = año
        self.horaInicio = horaInicio
        self.duracion = duracion
        self.id_Cliente  = idc 
        self.id_servicios = ids
        self.paga = paga

    def __str__(self) -> str:
        return f" - Dia: {self.dia}\n - Mes: {self.mes}\n  - Año: {self.año}\n - Hora Inicio: {self.horaInicio}\n - Hora Fin: {self.horaFin}\n - Seña: {self.seña}\n"

    def get_dia(self):
        return self.dia
    
    def get_mes(self):
        return self.mes
    
    def get_año(self):
        return self.año
    
    def get_horaInicio(self):
        return self.horaInicio
    
    def get_horaFin(self):
        return self.horaFin
    
    def get_seña(self):
        return self.seña
    
    def set_dia(self, nuevo_dia):
        self.dia = nuevo_dia

    def set_mes(self, nuevo_mes):
        self.mes = nuevo_mes

    def set_año(self, nuevo_año):
        self.año = nuevo_año

    def set_horaInicio(self, nueva_horaInicio):
        self.horaInicio = nueva_horaInicio

    def set_horaFin(self, nueva_horaFin):
        self.horaFin = nueva_horaFin

    def set_seña(self, nueva_seña):
        self.seña = nueva_seña

    