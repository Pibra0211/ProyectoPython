#registro vehiculos
import json


registroVehiculo = {
    "tipoVehiculo": "",
    "placa": "",
}



#validacion carro
def carro():
    while True:
        placa = input("\nIngrese la placa del carro: ").upper().strip()
        if len (placa) == 6 and placa[0:2].isalpha() and placa[3:5].isdigit():
            registroVehiculo["placa"] = placa
            print("")    
            print (registroVehiculo)
            print("\nPlaca registrada exitosamente. ")
            break
        print("\nPlaca inválida (ABC123).\nIntente nuevamente. ")
    with open("vehiculos.json","a+") as archivoC:
        archivoC.write("\n" + json.dumps(registroVehiculo))

# Validacion moto
def moto():
    while True:
        placa = input("\nIngrese la placa de la moto: ").upper().strip()
        if len (placa) == 6 and placa[0:2].isalpha() and placa[3:4].isdigit() and placa[5].isalpha:
            registroVehiculo["placa"] = placa    
            print("")
            print (registroVehiculo)
            print("\nPlaca registrada exitosamente. ")
            break
        print("\nPlaca inválida (ABC12D).\nIntente nuevamente. ")
    with open("vehiculos.json","a+") as archivoC:
        archivoC.write("\n" + json.dumps(registroVehiculo))

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