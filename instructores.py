import json
import os

ARCHIVO_INSTRUCTORES = os.path.join("data", "instructores.json")

# Diccionario indexado por documento (clave única).
instructores = {}


def cargarInstructores():
    """Carga el diccionario de instructores desde el archivo JSON, si existe."""
    global instructores
    if os.path.exists(ARCHIVO_INSTRUCTORES):
        with open(ARCHIVO_INSTRUCTORES, "r", encoding="utf-8") as archivo:
            try:
                instructores = json.load(archivo)
            except json.JSONDecodeError:
                instructores = {}
    else:
        instructores = {}
    return instructores


def guardarInstructores():
    """Sobrescribe el archivo JSON con el diccionario completo de instructores."""
    os.makedirs("data", exist_ok=True)
    with open(ARCHIVO_INSTRUCTORES, "w", encoding="utf-8") as archivo:
        json.dump(instructores, archivo, indent=4, ensure_ascii=False)


def registroInstructor():
    """Pide los datos de un instructor por consola, los valida, los guarda
    en el diccionario 'instructores' (indexado por documento) y persiste
    el archivo. Devuelve el diccionario del instructor registrado."""

    while True:
        nombre = input("Digite el nombre completo del instructor: ").title().strip()
        if nombre.replace(" ", "").isalpha():
            break
        print("\nEl nombre no puede contener numeros ni caracteres especiales.")

    while True:
        documento = input("Digite el número de documento del instructor: ")
        if not (documento.isdigit() and 8 <= len(documento) <= 10):
            print("\nEl documento debe contener solo dígitos y tener entre 8 y 10 caracteres.")
            continue
        if documento in instructores:
            print("\nYa existe un instructor registrado con ese documento.")
            continue
        break

    while True:
        especialidad = input("¿La especialidad del instructor es carro? s/n: ").strip().lower()
        if especialidad in ("s", "n"):
            break
        print("\nRespuesta inválida. Debe ingresar 's' o 'n'.")

    if especialidad == "n":
        especialidad = "moto"
    else:
        while True:
            tambienMoto = input("¿El instructor también se especializa en moto? s/n: ").strip().lower()
            if tambienMoto in ("s", "n"):
                break
            print("\nRespuesta inválida. Debe ingresar 's' o 'n'.")
        especialidad = "carro y moto" if tambienMoto == "s" else "carro"

    while True:
        telefono = input("Digite el numero de telefono del instructor: ")
        if telefono.isdigit() and len(telefono) == 10:
            break
        print("\nEl numero de telefono no puede contener caracteres ni letras especiales (debe tener 10 digitos).")

    datos = {
        "nombre": nombre,
        "especialidad": especialidad,
        "telefono": "+57 " + telefono,
    }

    instructores[documento] = datos
    guardarInstructores()

    print(f"\nLos datos del Señor/señora {nombre} se han registrado con exito.")
    return datos


def buscarInstructor(documento):
    """Devuelve el diccionario del instructor con ese documento, o None si no existe."""
    return instructores.get(documento)


def listarInstructores():
    """Devuelve el diccionario completo de instructores."""
    return instructores


def menuRegistroInstructores():
    """Ciclo de registro: registra uno o varios instructores y, al terminar,
    regresa al menú principal (base.menu())."""
    cargarInstructores()
    while True:
        registroInstructor()
        while True:
            decision = input("¿Desea registrar un nuevo instructor? s/n: ").strip().lower()
            if decision in ("s", "n"):
                break
            print("\nRespuesta inválida. Debe ingresar 's' o 'n'.")
        if decision == "n":
            print(f"\nInstructores registrados en total: {len(instructores)}")
            break

    import base
    base.menu()


if __name__ == "__main__":
    menuRegistroInstructores()