class ServSelec:
    def __init__(self,id,duracion,list=[]):
        self.id = id
        self.list = []
        self.list = list
    
    def get_id(self):
        return self.id
    
    def get_list(self):
        return self.list
    
    def set_id(self,id):
        self.id=id
    
    def set_list(self,list):
        self.list = list
    

    def agregar_ser(self,serv):
        self.list.append(serv)
