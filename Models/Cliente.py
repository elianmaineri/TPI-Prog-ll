class Cliente:
    def __init__(self,nombre,apellido,telefono,direccion,dni):
        self.nombre = nombre 
        self.apellido = apellido 
        self.telefono = telefono
        self.direccion = direccion 
        self.id = dni  

    def __str__(self) -> str:
        return f" - Nombre: {self.nombre}\n - Apellido: {self.apellido}\n - Telefono: {self.telefono}\n - Direccion: {self.direccion}\n"

    def get_nombre(self):
        return self.nombre
    
    def get_apellico(self):
        return self.apellido
    
    def get_telefono(self):
        return self.telefono
    
    def get_direccion(self):
        return self.direccion
    
    def get_id(self):
        return self.id
    
    def set_nombre(self,nombre):
        self.nombre = nombre

    def set_apellido(self,apellido):
        self.apellido = apellido
    
    def set_telefono(self,telefono):
        self.telefono = telefono 

    def set_direccion(self,direccion):
        self.direccion = direccion 
    
    def set_id(self,id):
        self.id = id 
        
    

