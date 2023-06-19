class Vista:
    def mostrar_menu(self):
        print('MENÚ')
        print('0. Reservar fecha')
        print('1. Consultar fechas reservadas')
        print('2. Cancelar reserva')
        print('3. Salir')
    
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