from Views.Vista import Vista

class controlador:








    def menu(self):
        while True:
            self.Vista.mostrar_menu()
            choice = self.Vista.validar_entero(0, 4)
            match choice:
                case 0:
                    self.mostrar_mayores()
                case 1:
                    self.peso_actual()
                case 2:
                    self.calcular_peso_ideal()
                case 3:
                    self.calcular_diferencia()
                case 4:
                    break
