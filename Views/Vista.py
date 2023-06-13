class Vista:
    def mostrar_menu(self):
        print('MENÚ')
        print('0. ')
        print('1. ')
        print('2. ')
        print('3. ')
        print('4. Salir')
    
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