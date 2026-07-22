print("")



def menu(): 

    print("""---Bienvenido a DriveSafe---

    1. Registrar cliente
    2. Registrar instructor
    3. Registrar vehículo 
    4. Programar cita 
    5. Consultar citas programadas 
    6. Registrar asistencia y observaciones
    7. Consultar historial de prácticas
    8. Salir      
        """)

def mainBase():

    while (True):
        menu()
        opcion = input("Selecciona la opción que deseas ejecutar: ").strip()
        if opcion == "1":
            import clientes
            clientes.registroCliente()    
        elif opcion == "2":
            import instructores
            instructores.registroInstructor()
        elif opcion == "3":
            import vehiculos
            vehiculos.registrarVehiculo()
        elif opcion == "4":
            import programarCitas
            programarCitas.ProgramarCita()
        elif opcion == "5":
            import programarCitas
            programarCitas.buscarCita()
        #elif opcion == "6":
        elif opcion == "7":
            import programarCitas
            programarCitas.historialCliente()
        elif opcion == "8":
            print("\nGracias por usar DriveSafe, vuelva pronto.")
        break        
mainBase()

