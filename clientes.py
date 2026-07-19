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
    nombre = input("\nDigite el nombre completo del cliente: ").title().strip() 
    while True:
        if nombre.replace(" ","").isalpha():
            break
        else:
            print("\nEl nombre no puede contener numeros ni caracteres especiales.")
            nombre = input("\nDigite el nombre completo del cliente nuevamente: ").title().strip() 
    datosRegistro["nombre"] = nombre

    edad = (input("Digite la edad del cliente: "))
    while True:
        if edad.isdigit() and len(edad) == 2:  
            edad = int(edad)
            if (edad) < 16 or (edad) > 60:
                    edad = input(f"\nEl señor/señora {nombre} debe estar entre los 16 y 60 años\nIngrese la edad nuevamente: ")
                    continue
            break
        else: edad = input("\nLa edad no puede contener letras ni caracteres especiales y no puede ser mayor a 3 digitos \nIngresese la edad nuevamente: ")
    datosRegistro["edad"] = edad

    documento = (input("Digite el numero de documento del cliente: "))
    while True:
        if documento.isdigit() and len(documento) > 7:
            break
        elif documento.isdigit() and len(documento)  < 10:
            break
        else:
            documento = input("\nEl numero de documento no puede contener letras ni caracteres especiales\nDebe contener 10 digitos, ingreselo nuevamente: ")
    datosRegistro["documento"] = documento

    telefono = (input("Digite el numero de telefono del cliente: "))
    while True:
        if telefono.isdigit() and len(telefono) == 10:
            break
        else:
            telefono = input("\nEl numero de telefono no puede contener caracteres ni lestas especiales\nIngreselo nuevamente (debe tener 10d igitos): ")
    datosRegistro["telefono"] = "+57" + telefono

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
