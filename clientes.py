#funcion registro
import json 
datosRegistro = {
    "nombre": "",
    "edad": "",
    "documento":"",
    "tipo":"",
}

def registroCliente():
    nombre = input("Digite el nombre completo del cliente: ")
    datosRegistro["nombre"] = nombre
    edad = int(input("Digite la edad del cliente: "))
    datosRegistro["edad"] = edad
    documento = int(input("Digite el numero de documento del cliente: "))
    datosRegistro["documento"] = documento
    tipoVehiculo = input("¿El tipo de vehiculo al que aplica el cliente es carro? s/n ") 
    if tipoVehiculo == "n" or "tipoVehiculo" == "N":
        tipoVehiculo = "moto"
    elif tipoVehiculo == "s" or "tipoVehiculo" == "S":
        tipoVehiculo = "carro"
    datosRegistro["tipo"] = tipoVehiculo
    with open("clientess.json","a+") as archivoC:
        archivoC.write("\n" + json.dumps(datosRegistro))
    return(datosRegistro)
print(registroCliente())
