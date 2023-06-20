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
                
    def mostrar(self,dato):
        print(dato)

    def pedir(pedido):
        a = input(pedido)
        return a
    
    def confirmar_servicios(self):
        j = input("Quiere el siguiente servicio ")
        return j
    
    def pedir_fecha(self):
        return input("Ingrese la fecha del evento (DD-MM-AAAA): ")
    
    def mostrar_fecha_disponible(self, fecha_disponible):
        print(f"La fecha solicitada no está disponible. La fecha más próxima disponible es: {fecha_disponible}")
    
    def pedir_servicios(self):
        servicios = ["dj", "decoración", "cotillón", "máquina de humo", "maquillaje", "música en vivo"]
        print("Seleccione los servicios deseados:")
        for i, servicio in enumerate(servicios, 1):
            print(f"{i}. {servicio}")
        servicio_elegido = input("Ingrese los números correspondientes a los servicios separados por comas: ")
        servicio_elegido = [int(elegido) for elegido in servicio_elegido.split(",")]
        return servicio_elegido
    
    def mostrar_costo_total(self, costo_total):
        print(f"El costo total del evento es: ${costo_total}")
    
    def mostrar_seña(self, seña):
        print(f"El monto de la señal requerida es: ${seña}")
        
    def pedir_fecha_cancelacion(self):
        return input("Ingrese la fecha de cancelación (DD-MM-AAAA): ")
    
    def mostrar_monto_a_devolver(self, devolucion):
        print(f"El monto a devolver es: ${devolucion}")

    def mostras_reserva(self, nombre):
        print(nombre)

    def no_devolver(self):
        print("No se reintegra nada de dinero, ya que paso el tiempo limite")
    
