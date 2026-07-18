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

def main():

    while (True):

        menu()
        opcion = input("Selecciona la opción que deseas ejecutar: ")

main()

