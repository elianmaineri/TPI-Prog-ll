class Servicios:
    def __init__(self, dj, decoracion, cotillon, maquinaDeHumo, maquillaje, musicaEnVivo):
        self.dj = str(dj)
        self.decoracion = str(decoracion)
        self.cotillon = str(cotillon)
        self.maquinaDeHumo = str(maquinaDeHumo)
        self.maquillaje = str(maquillaje)
        self.musicaEnVivo = str(musicaEnVivo)

    def __str__(self) -> str:
        return f"Servicios:\n - Dj: {self.dj} \n - Decoracion: {self.decoracion} \n - Cotillon: {self.cotillon} \n - Maquina de Humo: {self.maquinaDeHumo} \n - Maquillaje: {self.maquillaje} \n - Musica en vivo: {self.musicaEnVivo} \n"
    

    