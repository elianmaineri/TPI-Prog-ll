class Servicios:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self) -> str:
        return f" - Servicios:\n - Nombre: {self.nombre} \n - Precio: {self.precio} \n"
    
    def get_nombre(self):
        return self.nombre
    
    def get_precio(self):
        return self.precio
    
    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def set_precio(self, nueva_precio):
        self.precio = nueva_precio
