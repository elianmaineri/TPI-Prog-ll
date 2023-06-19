class Reserva:
    def __init__(self, dia, horaInicio, horaFin, seña):
        self.dia = dia
        self.horaInicio = horaInicio
        self.horaFin = horaFin
        self.seña = seña

    def get_dia(self):
        return self.dia
    
    def get_horaInicio(self):
        return self.horaInicio
    
    def get_horaFin(self):
        return self.horaFin
    
    def get_seña(self):
        return self.seña
    
    def set_dia(self, nuevo_dia):
        self.dia = nuevo_dia

    def set_horaInicio(self, nueva_horaInicio):
        self.horaInicio = nueva_horaInicio

    def set_horaFin(self, nueva_horaFin):
        self.horaFin = nueva_horaFin

    def set_seña(self, nueva_seña):
        self.seña = nueva_seña

    