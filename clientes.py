import json
import os

ARCHIVO_CLIENTES = os.path.join("data", "clientes.json")

# Diccionario indexado por documento (clave única).
clientes = {}


def cargarClientes():
    """Carga el diccionario de clientes desde el archivo JSON, si existe."""
    global clientes
    if os.path.exists(ARCHIVO_CLIENTES):
        with open(ARCHIVO_CLIENTES, "r", encoding="utf-8") as archivo:
            try:
                clientes = json.load(archivo)
            except json.JSONDecodeError:
                clientes = {}
    else:
        clientes = {}
    return clientes


def guardarClientes():
    """Sobrescribe el archivo JSON con el diccionario completo de clientes."""
    os.makedirs("data", exist_ok=True)
    with open(ARCHIVO_CLIENTES, "w", encoding="utf-8") as archivo:
        json.dump(clientes, archivo, indent=4, ensure_ascii=False)


def registroCliente():
    """Pide los datos de un cliente por consola, los valida, los guarda
    en el diccionario 'clientes' (indexado por documento) y persiste
    el archivo. Devuelve el diccionario del cliente registrado."""

    while True:
        nombre = input("\nDigite el nombre completo del cliente: ").title().strip()
        if nombre.replace(" ", "").isalpha():
            break
        print("\nEl nombre no puede contener numeros ni caracteres especiales.")

    while True:
        edad = input("Digite la edad del cliente: ")
        if edad.isdigit() and len(edad) <= 2:
            edad = int(edad)
            if 16 <= edad <= 60:
                break
            print(f"\nEl señor/señora {nombre} debe estar entre los 16 y 60 años.")
        else:
            print("\nLa edad no puede contener letras ni caracteres especiales y no puede tener mas de 2 digitos.")

    while True:
        documento = input("Digite el numero de documento del cliente: ")
        if not (documento.isdigit() and 7 <= len(documento) <= 10):
            print("\nEl documento debe contener solo digitos y tener entre 7 y 10 digitos.")
            continue
        if documento in clientes:
            print("\nYa existe un cliente registrado con ese documento.")
            continue
        break

    while True:
        telefono = input("Digite el numero de telefono del cliente: ")
        if telefono.isdigit() and len(telefono) == 10:
            break
        print("\nEl numero de telefono no puede contener caracteres ni letras especiales (debe tener 10 digitos).")

    while True:
        respuesta = input("¿El tipo de vehiculo al que aplica el cliente es carro? s/n: ").strip().lower()
        if respuesta in ("s", "n"):
            break
        print("\nEl valor ingresado no es valido.")

    if respuesta == "n":
        tipoVehiculo = "moto"
    else:
        while True:
            tambienMoto = input("¿El cliente aplica tambien para moto? s/n: ").strip().lower()
            if tambienMoto in ("s", "n"):
                break
            print("\nEl valor ingresado no es valido.")
        tipoVehiculo = "carro y moto" if tambienMoto == "s" else "carro"

    datos = {
        "nombre": nombre,
        "edad": edad,
        "telefono": "+57 " + telefono,
        "tipo": tipoVehiculo,
    }

    clientes[documento] = datos
    guardarClientes()

    print(f"\nSeñor/señora {nombre}, sus datos se han registrado con exito.")
    return datos


def buscarCliente(documento):
    """Devuelve el diccionario del cliente con ese documento, o None si no existe."""
    return clientes.get(documento)


def listarClientes():
    """Devuelve el diccionario completo de clientes."""
    return clientes


def menuRegistroClientes():
    """Ciclo de registro: registra uno o varios clientes y, al terminar,
    regresa al menú principal (base.menu())."""
    cargarClientes()
    while True:
        registroCliente()
        while True:
            decision = input("¿Desea registrar un nuevo cliente? s/n: ").strip().lower()
            if decision in ("s", "n"):
                break
            print("\nRespuesta invalida. Debe ingresar 's' o 'n'.")
        if decision == "n":
            print(f"\nClientes registrados en total: {len(clientes)}")
            break

    import base
    base.menu()


if __name__ == "__main__":
    menuRegistroClientes()