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
        if opcion.isalpha():
            print("Respuesta invalida, digite un numero.")
            mainBase()
        if opcion == "1":
            import clientes
            clientes.menuRegistroClientes()    
        elif opcion == "2":
            import instructores
            instructores.menuRegistroInstructores()
        elif opcion == "3":
            import vehiculos
            vehiculos.menuRegistroVehiculos()
        elif opcion == "4":
            import programarCitas
            programarCitas.menuProgramarCitas()
        elif opcion == "5":
            import programarCitas
            idCita = input("Digite el id de la cita (ej: CITA001): ").strip()
            cita = programarCitas.buscarCita(idCita)
            if cita:
                print(f"""
        --- Cita {idCita.upper()} ---
        Cliente: {cita['cliente']}
        Instructor: {cita['instructor']}
        Vehículo: {cita['vehiculo']}
        Fecha: {cita['fecha']} {cita['hora']}
        Duración: {cita['duracion']} minutos
        Asistencia: {cita['asistencia']}
        Observaciones: {cita['observaciones']}
        """)
            else:
                print("\nNo existe ninguna cita con ese id.")
                
        elif opcion == "6":
            import programarCitas
            programarCitas.menuRegistrarAsistencia()
        
        elif opcion == "7":
            import programarCitas
            documento = input("Digite el documento del cliente: ").strip()
            historial = programarCitas.historialCliente(documento)
            if historial:
                print(f"\n--- Historial de citas del cliente {documento} ---")
                for cita in historial:
                    print(f"{cita['id']} | Fecha: {cita['fecha']} {cita['hora']} | Asistencia: {cita['asistencia']}")
            else:
                print("\nEste cliente no tiene citas registradas.")
        elif opcion == "8":
            print("\nGracias por usar DriveSafe, vuelva pronto.")
            break   

mainBase()
__name__ = "__main__"

