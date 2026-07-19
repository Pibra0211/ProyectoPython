#funcion registro
import json 
datosRegistro = {
    "nombre": "",
    "edad": "",
    "documento":"",
    "telefono":"",
    "tipo":"",

}

def registroCliente():
    nombre = input("\nDigite el nombre completo del cliente: ")
    while True:
        if nombre.isalpha():
            break
        else:
            print("\nEl nombre no puede contener numeros ni caracteres especiales")
            nombre = input("\nDigite el nombre completo del cliente nuevamente: ").capitalize().strip() 
    datosRegistro["nombre"] = nombre


    edad = input("Digite la edad del cliente: ")
    while True:
        if edad.isdigit() and len(edad) == 2:  
            break
        elif int(edad) < 16:
              edad = input(f"\nEl señor/señora {nombre} no puede ser menor de 16 años\nIngrese la edad nuevamente:")
        else: edad = input("\nLa edad no puede contener letras ni caracteres especiales y no puede ser mayor a 3 digitos \nIngresese la edad nuevamente: ")
    datosRegistro["edad"] = edad

    documento = int(input("Digite el numero de documento del cliente: "))
    datosRegistro["documento"] = documento
    telefono = int(input("Digite el numero de telefono del cliente: "))
    datosRegistro["telefono"] = telefono
    tipoVehiculo = input("¿El tipo de vehiculo al que aplica el cliente es carro? s/n ") 
    if tipoVehiculo == "n" or "tipoVehiculo" == "N":
        tipoVehiculo = "moto"
    elif tipoVehiculo == "s" or "tipoVehiculo" == "S":
        tipoVehiculo = "carro"
    datosRegistro["tipo"] = tipoVehiculo
    with open("clientess.json","a+") as archivoC:
        archivoC.write("\n" + json.dumps(datosRegistro))
    return(datosRegistro)
clientes = (registroCliente())
print(clientes)
print(f"\nSeñor/señora {clientes["nombre"]} sus datos se han registrado con exito")
desicion = input("¿Desea registrar un nuevo cliente? s/n: ")
if desicion == "s" or desicion == "S":
    registroCliente()
elif desicion == "n" or desicion == "N":
    import base 
    print (base.menu())
