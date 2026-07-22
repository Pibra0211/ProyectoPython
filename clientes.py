#funcion registro
import json
import os

ARCHIVO_CLIENTES = "clientess.json"

datosRegistro = {
    "nombre": "",
    "edad": "",
    "documento":"",
    "telefono":"",
    "tipo":"",
}
contadorInstructores = 1

def cargarClientes():
    if os.path.exists(ARCHIVO_CLIENTES):
        try:
            with open(ARCHIVO_CLIENTES, "r") as archivoC:
                contenido = archivoC.read().strip()
                if contenido:
                    return json.loads(contenido)
        except json.JSONDecodeError:
            print(f"\nAviso: {ARCHIVO_CLIENTES} no tiene un formato JSON válido, se iniciará vacío.")
    return {}

clientes = cargarClientes()

def guardarClientes():
    with open(ARCHIVO_CLIENTES, "w") as archivoC:
        json.dump(clientes, archivoC, indent=4)

def obtenerCliente(documento):
    return clientes.get(documento)

def registroCliente():
    while True:
        nombre = input("\nDigite el nombre completo del cliente: ").title().strip() 
        if nombre.replace(" ","").isalpha():
            break
        else:
            print("\nEl nombre no puede contener numeros ni caracteres especiales.")
            nombre = input("\nDigite el nombre completo del cliente nuevamente: ").title()
    datosRegistro["nombre"] = nombre

    while True:
        edad = (input("Digite la edad del cliente: "))
        if edad.isdigit() and len(edad) == 2:  
            edad = int(edad)
            if (edad) < 16 or (edad) > 60:
                    edad = input(f"\nEl señor/señora {nombre} debe estar entre los 16 y 60 años\nIngrese la edad nuevamente: ")
                    continue
            break
        else: edad = input("\nLa edad no puede contener letras ni caracteres especiales y no puede ser mayor a 3 digitos \nIngresese la edad nuevamente: ")
    datosRegistro["edad"] = edad

    while True:
        documento = input("Digite el numero de documento del cliente: ")
        if documento.isdigit() and len(documento) >= 7 and len(documento) <= 10:
            break
        else:
            print("\nEl documento debe contener solo digitos y tener entre 7 y 10 digitos")
    datosRegistro["documento"] = documento

    while True:
        telefono = (input("Digite el numero de telefono del cliente: "))

        if telefono.isdigit() and len(telefono) == 10:
            break
        else:
            telefono = input("\nEl numero de telefono no puede contener caracteres ni letras especiales\nIngreselo nuevamente (debe tener 10 digitos): ")
    datosRegistro["telefono"] = "+57 " + telefono

    while True:
        tipoVehiculo = input("¿El tipo de vehiculo al que aplica el cliente es carro? s/n: ")
        if tipoVehiculo not in ("s", "S", "n", "N"):
            print("\nEl valor ingresado no es valido. ")
            continue
        break

    if tipoVehiculo in ("n", "N"):
        tipoVehiculo = "moto"
    else:
        if tipoVehiculo in ("s", "S"):
            tipoVehiculo = "carro"
            while True:
                tipoVehiculo = input("¿El cliente aplica para moto? s/n: ")
                if tipoVehiculo not in ("s", "S", "n", "N"):
                    print("\nEl valor ingresado no es valido. ")
                    continue
                break

    if tipoVehiculo in ("s", "S"):
        tipoVehiculo = "carro y moto"
    else:
       if tipoVehiculo in ("n", "N"):
        tipoVehiculo = "carro"

    datosRegistro["tipo"] = tipoVehiculo

    clientes[documento] = datosRegistro.copy()
    guardarClientes()
    return(datosRegistro)

while True:
    datosDelCliente = (registroCliente())
    print(datosDelCliente)
    print(f"\nSeñor/señora {datosDelCliente['nombre']} sus datos se han registrado con exito")
    decision = input("¿Desea registrar un nuevo cliente? s/n: ")
    if decision == "s" or decision == "S":
        contadorInstructores += 1
        continue
    elif decision == "n" or decision == "N":
        print(f"\nclientes registrados {contadorInstructores}")
        import base 
        print (base.menu())
        break
    else:
        decision = input("\nRespuesta inválida. Debe ingresar 's' o 'n': ")