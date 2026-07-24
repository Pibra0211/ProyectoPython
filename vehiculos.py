import json
import os

ARCHIVO_VEHICULOS = os.path.join("data", "vehiculos.json")

# Diccionario indexado por placa (clave única).
vehiculos = {}


def cargarVehiculos():
    #"""Carga el diccionario de vehiculos desde el archivo JSON, si existe."""
    global vehiculos
    if os.path.exists(ARCHIVO_VEHICULOS):
        with open(ARCHIVO_VEHICULOS, "r", encoding="utf-8") as archivo:
            try:
                vehiculos = json.load(archivo)
            except json.JSONDecodeError:
                vehiculos = {}
    else:
        vehiculos = {}
    return vehiculos

vehiculos = cargarVehiculos()

def guardarVehiculos():
    #"""Sobrescribe el archivo JSON con el diccionario completo de vehiculos."""
    os.makedirs("data", exist_ok=True)
    with open(ARCHIVO_VEHICULOS, "w", encoding="utf-8") as archivo:
        json.dump(vehiculos, archivo, indent=4, ensure_ascii=False)


def _placaValida(placa, tipo):
    #"""Valida el formato completo de la placa segun el tipo de vehiculo.
    #Carro: 3 letras + 3 digitos (ABC123). Moto: 3 letras + 2 digitos + 1 letra (ABC12D)."""
    if len(placa) != 6:
        return False
    if tipo == "carro":
        return placa[0:3].isalpha() and placa[3:6].isdigit()
    else:
        return placa[0:3].isalpha() and placa[3:5].isdigit() and placa[5].isalpha()


def registrarVehiculo():
    #"""Pide el tipo y la placa de un vehiculo por consola, los valida, los
    #guarda en el diccionario 'vehiculos' (indexado por placa) y persiste
    #el archivo. Devuelve el diccionario del vehiculo registrado."""

    while True:
        tipo = input("¿El tipo de vehiculo a registrar es carro? s/n: ").strip().lower()
        if tipo in ("s", "n"):
            break
        print("\nEl valor ingresado no es valido.")

    tipoVehiculo = "carro" if tipo == "s" else "moto"
    formato = "ABC123" if tipoVehiculo == "carro" else "ABC12D"

    while True:
        placa = input(f"\nIngrese la placa del {tipoVehiculo}: ").upper().strip()
        if not _placaValida(placa, tipoVehiculo):
            print(f"\nPlaca inválida ({formato}).\nIntente nuevamente.")
            continue
        if placa in vehiculos:
            print("\nYa existe un vehiculo registrado con esa placa.")
            continue
        break

    datos = {
        "tipoVehiculo": tipoVehiculo,
    }

    vehiculos[placa] = datos
    guardarVehiculos()

    print("")
    print({"placa": placa, **datos})
    print("\nPlaca registrada exitosamente.")
    return datos


def buscarVehiculo(placa):
    #"""Devuelve el diccionario del vehiculo con esa placa, o None si no existe."""
    return vehiculos.get(placa.upper().strip())


def listarVehiculos():
    #"""Devuelve el diccionario completo de vehiculos."""
    return vehiculos


def menuRegistroVehiculos():
    #"""Ciclo de registro: registra uno o varios vehiculos y, al terminar,
    #regresa al menú principal (base.menu())."""
    cargarVehiculos()
    while True:
        registrarVehiculo()
        while True:
            decision = input("¿Desea registrar un nuevo vehiculo? s/n: ").strip().lower()
            if decision in ("s", "n"):
                break
            print("\nRespuesta invalida. Debe ingresar 's' o 'n'.")
        if decision == "n":
            print(f"\nVehiculos registrados en total: {len(vehiculos)}")
            break

    import base
    base.menu()


if __name__ == "__main__":
    menuRegistroVehiculos()
