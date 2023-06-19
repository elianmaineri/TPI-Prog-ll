class Reserva:
    def __init__(self, dia, hora, seña):
        self.dia = dia
        self.hora = hora
        self.seña = seña

    def get_dia(self):
        return self.dia
    
    def get_hora(self):
        return self.hora
    
    def get_seña(self):
        return self.seña
    
    def set_dia(self, nuevo_dia):
        self.dia = nuevo_dia

    def set_hora(self, nueva_hora):
        self.hora = nueva_hora

    def set_seña(self, nueva_seña):
        self.seña = nueva_seña

    