class Servicios:
    def __init__(self, dj, decoracion, cotillon, maquinaDeHumo, maquillaje, musicaEnVivo):
        self.dj = str(dj)
        self.decoracion = str(decoracion)
        self.cotillon = str(cotillon)
        self.maquinaDeHumo = str(maquinaDeHumo)
        self.maquillaje = str(maquillaje)
        self.musicaEnVivo = str(musicaEnVivo)

    def __str__(self) -> str:
        return f" - Servicios:\n - Dj: {self.dj} \n - Decoracion: {self.decoracion} \n - Cotillon: {self.cotillon} \n - Maquina de Humo: {self.maquinaDeHumo} \n - Maquillaje: {self.maquillaje} \n - Musica en vivo: {self.musicaEnVivo} \n"
    
    def get_dj(self):
        return self.dj
    
    def get_decoracion(self):
        return self.decoracion
    
    def get_cotillon(self):
        return self.cotillon
    
    def get_maquinaDeHumo(self):
        return self.maquinaDeHumo
    
    def get_maquillaje(self):
        return self.maquillaje

    def get_musicaEnVivo(self):
        return self.musicaEnVivo
    
    def set_dj(self, nuevo_dj):
        self.dj = nuevo_dj

    def set_decoracion(self, nueva_decoracion):
        self.decoracion = nueva_decoracion

    def set_cotillon(self, nuevo_cotillon):
        self.cotillon = nuevo_cotillon

    def set_maquinaDeHumo(self, nueva_maquinaDeHumo):
        self.maquinaDeHumo = nueva_maquinaDeHumo

    def set_maquillaje(self, nuevo_maquillaje):
        self.maquillaje = nuevo_maquillaje

    def set_musicaEnVivo(self, nueva_musicaEnVivo):
        self.musicaEnVivo = nueva_musicaEnVivo
    