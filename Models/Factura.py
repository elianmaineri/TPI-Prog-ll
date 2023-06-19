class Factura:
    def __init__(self, seña, imptotal, gastosAdm, iva):
        self.seña = float(seña)
        self.imptotal = float(imptotal)
        self.gastosAdm = float(gastosAdm)
        self.iva = int(iva)

    def __str__(self) -> str:
        return f"Seña: {self.seña}\n - Importe Total: {self.imptotal}\n - Gastos Administrativos: {self.gastosAdm}\n - IVA: {self.iva}\n" 

    def get_seña(self):
        return self.seña
    
    def get_imptotal(self):
        return self.imptotal
    
    def get_gastosAdm(self):
        return self.gastosAdm
    
    def get_iva(self):
        return self.iva
    
    def set_seña(self, nueva_seña):
        self.seña = nueva_seña

    def set_imptotal(self, nuevo_imptotal):
        self.imptotal = nuevo_imptotal

    def set_gastosAdm(self, nuevo_gastosAdm):
        self.gastosAdm = nuevo_gastosAdm

    def set_iva(self, nuevo_iva):
        self.iva = nuevo_iva

        