class Factura:
    def __init__(self, seña, imptotal, gastosAdm, iva):
        self.seña = float(seña)
        self.imptotal = float(imptotal)
        self.gastosAdm = float(gastosAdm)
        self.iva = int(iva)

    def get_seña(self):
        if ((self.imptotal * 30)/100) == self.seña:
            return self.seña
        else:
            print("¡¡¡¡¡Error debe abonar el 30% del total del importe!!!!")

    