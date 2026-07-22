#registro vehiculos
import json
import os

ARCHIVO_VEHICULOS = "vehiculos.json"

registroVehiculo = {
    "tipoVehiculo": "",
    "placa": "",
}

def cargarVehiculos():
    if os.path.exists(ARCHIVO_VEHICULOS):
        try:
            with open(ARCHIVO_VEHICULOS, "r") as archivoC:
                contenido = archivoC.read().strip()
                if contenido:
                    return json.loads(contenido)
        except json.JSONDecodeError:
            print(f"\nAviso: {ARCHIVO_VEHICULOS} no tiene un formato JSON válido, se iniciará vacío.")
    return {}

vehiculos = cargarVehiculos()

def guardarVehiculos():
    with open(ARCHIVO_VEHICULOS, "w") as archivoC:
        json.dump(vehiculos, archivoC, indent=4)

def obtenerVehiculo(placa):
    return vehiculos.get(placa)

#validacion carro
contadorCarro = 0
contadorMoto = 0
def carro():
    global contadorCarro
    while True:
        placa = input("\nIngrese la placa del carro: ").upper().strip()
        if len (placa) == 6 and placa[0:2].isalpha() and placa[3:5].isdigit():
            registroVehiculo["placa"] = placa
            print("")    
            print (registroVehiculo)
            print("\nPlaca registrada exitosamente. ")
            contadorCarro +=1
            print (f"\ncarros registrados {contadorCarro}")
            vehiculos[placa] = registroVehiculo.copy()
            guardarVehiculos()
            break
        print("\nPlaca inválida (ABC123).\nIntente nuevamente. ")

# Validacion moto
def moto():
    global contadorMoto
    while True:
        placa = input("\nIngrese la placa de la moto: ").upper().strip()
        if len (placa) == 6 and placa[0:2].isalpha() and placa[3:4].isdigit() and placa[5].isalpha:
            registroVehiculo["placa"] = placa    
            print("")
            print (registroVehiculo)
            print("\nPlaca registrada exitosamente. ")
            contadorMoto +=1
            print(f"\nmotos registradas{contadorMoto}")
            vehiculos[placa] = registroVehiculo.copy()
            guardarVehiculos()
            break
        print("\nPlaca inválida (ABC12D).\nIntente nuevamente. ")

#menu
def menu(): 

    print("""---Vehiculo a registrar---

    1. carro  
    2. moto
    3. salir
        """)

def main():


    while (True):
        menu()
        opcion = input("\nSelecciona la opción que deseas ejecutar: ")
        if opcion == "1":
            registroVehiculo["tipoVehiculo"] = "carro"
            carro()
        if opcion == "2":
            registroVehiculo["tipoVehiculo"] = "moto"
            moto()
        if opcion == "3":
            import base
            base.mainBase()
            break
main()