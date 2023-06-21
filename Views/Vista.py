class Vista:
    def mostrar_menu(self):
        print('MENÚ')
        print('0. Reservar fecha')
        print('1. Consultar fechas reservadas')
        print('2. Cancelar reserva')
        print("3. calcular costos totales ")
        print("4. registrar pago seña ")
    
        print('4. Salir')
    
    def menu_ser():
        print ("MENU")
        print("1-Agregar otro servicio")
        print("2- salir al menu ")


    def validar_entero(self, lim_inf, lim_sup):
        while True:
            try:
                choice = int(input(f'Ingrese una opción entre {lim_inf} y {lim_sup}\n'))
            except ValueError:
                print('Opción inválida. Intente nuevamente:')
                continue
            else:
                if choice < lim_inf or choice > lim_sup:
                    print('Opción inválida. Intente de nuevo:')
                    continue
                else:
                    return choice
        
    def mostrar(self,dato):
        print(dato)

    def pedir(pedido):
        a = input(pedido)
        return a
    
    def confirmar_servicios(self):
        j = input("Quiere el siguiente servicio ")
        return j
    
    def devolver_dinero(self, dinero):
        print(f"Se devulve el 20% de su dinero: ${dinero}")

    def mostras_reserva(self,):
        pass
    def no_devolver(self):
        print("No se reintegra nada de dinero, ya que paso el tiempo limite")
    
