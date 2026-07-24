import json
import os
from datetime import datetime, timedelta

import clientes
import instructores
import vehiculos

ARCHIVO_CITAS = os.path.join("data", "citas.json")

# Diccionario indexado por id de cita (clave única).
citas = {}


def cargarCitas():
    """Carga el diccionario de citas desde el archivo JSON, si existe."""
    global citas
    if os.path.exists(ARCHIVO_CITAS):
        with open(ARCHIVO_CITAS, "r", encoding="utf-8") as archivo:
            try:
                citas = json.load(archivo)
            except json.JSONDecodeError:
                citas = {}
    else:
        citas = {}
    return citas

citas = cargarCitas()

def guardarCitas():
    """Sobrescribe el archivo JSON con el diccionario completo de citas."""
    os.makedirs("data", exist_ok=True)
    with open(ARCHIVO_CITAS, "w", encoding="utf-8") as archivo:
        json.dump(citas, archivo, indent=4, ensure_ascii=False)


# ---------- Funciones auxiliares (uso interno del módulo) ----------

def generarIdCita():
    """Genera un identificador único tipo CITA001, CITA002, etc."""
    numero = len(citas) + 1
    while f"CITA{numero:03d}" in citas:
        numero += 1
    return f"CITA{numero:03d}"


def validarFecha(fechaStr):
    """Valida formato DD/MM/AAAA y que sea una fecha real."""
    if len(fechaStr) != 10:
        return False
    if fechaStr[2] != "/" or fechaStr[5] != "/":
        return False
    try:
        datetime.strptime(fechaStr, "%d/%m/%Y")
        return True
    except ValueError:
        return False


def validarHora(horaStr):
    """Valida formato HH:MM en formato 24h."""
    if len(horaStr) != 5:
        return False
    if horaStr[2] != ":":
        return False
    try:
        datetime.strptime(horaStr, "%H:%M")
        return True
    except ValueError:
        return False


def validarDuracion(duracionStr):
    """Valida que sea un entero entre 30 y 240 minutos. Devuelve el int o None."""
    if not duracionStr.isdigit():
        return None
    minutos = int(duracionStr)
    if 30 <= minutos <= 240:
        return minutos
    return None


def validarRespuestaSiNo(respuesta):
    """Devuelve True solo si la respuesta es 's' o 'n'."""
    return respuesta in ("s", "n")


def fechaHoraADatetime(fechaStr, horaStr):
    """Convierte DD/MM/AAAA + HH:MM a un objeto datetime."""
    return datetime.strptime(f"{fechaStr} {horaStr}", "%d/%m/%Y %H:%M")


def haySolapamiento(fechaNueva, horaNueva, duracionNueva, citaExistente):
    """Dos citas se solapan si sus intervalos [inicio, fin] se intersectan."""
    try:
        inicioNuevo = fechaHoraADatetime(fechaNueva, horaNueva)
        finNuevo = inicioNuevo + timedelta(minutes=duracionNueva)

        inicioExistente = fechaHoraADatetime(
            citaExistente["fecha"], citaExistente["hora"]
        )
        finExistente = inicioExistente + timedelta(
            minutes=int(citaExistente["duracion"])
        )

        return inicioNuevo < finExistente and inicioExistente < finNuevo
    except (ValueError, KeyError):
        return False


def instructorOcupado(documentoInstructor, fecha, hora, duracion):
    """Revisa si el instructor ya tiene una cita que se solape con el horario."""
    for datos in citas.values():
        if datos["instructor"] == documentoInstructor:
            if haySolapamiento(fecha, hora, duracion, datos):
                return True
    return False


def vehiculoOcupado(placa, fecha, hora, duracion):
    """Revisa si el vehículo ya tiene una cita que se solape con el horario."""
    for datos in citas.values():
        if datos["vehiculo"] == placa:
            if haySolapamiento(fecha, hora, duracion, datos):
                return True
    return False


def esPasado(fechaStr, horaStr):
    """True si la fecha/hora ya pasó respecto al momento actual."""
    try:
        return fechaHoraADatetime(fechaStr, horaStr) < datetime.now()
    except ValueError:
        return True


def mostrarListaVehiculos():
    """Imprime de forma legible todos los vehículos registrados."""
    listaVehiculos = vehiculos.listarVehiculos()
    if not listaVehiculos:
        print("\nNo hay vehículos registrados en el sistema.")
        return False
    print("\n--- Vehículos registrados ---")
    for placa, datos in listaVehiculos.items():
        print(f"  Placa: {placa} | Tipo: {datos['tipoVehiculo']}")
    print("----------------------------\n")
    return True


def mostrarListaInstructores():
    """Imprime de forma legible todos los instructores registrados."""
    listaInstructores = instructores.listarInstructores()
    if not listaInstructores:
        print("\nNo hay instructores registrados en el sistema.")
        return False
    print("\n--- Instructores registrados ---")
    for documento, datos in listaInstructores.items():
        print(f"  Documento: {documento} | Nombre: {datos['nombre']} | Especialidad: {datos['especialidad']}")
    print("--------------------------------\n")
    return True


def mostrarListaClientes():
    """Imprime de forma legible todos los clientes registrados."""
    listaClientes = clientes.listarClientes()
    if not listaClientes:
        print("\nNo hay clientes registrados en el sistema.")
        return False
    print("\n--- Clientes registrados ---")
    for documento, datos in listaClientes.items():
        print(f"  Documento: {documento} | Nombre: {datos['nombre']} | Tipo: {datos['tipo']}")
    print("----------------------------\n")
    return True


# ---------- Función principal ----------

def programarCita():
    """Programa una nueva cita validando compatibilidad y disponibilidad."""
    cargarCitas()

    while True:
        mostrarListaClientes()
        documentoCliente = input("Digite el documento del cliente: ").strip()
        cliente = clientes.buscarCliente(documentoCliente)
        if cliente is None:
            print("\nNo existe un cliente registrado con ese documento.")
            continuar = input("¿Desea intentar con otro documento? s/n: ").strip().lower()
            while not validarRespuestaSiNo(continuar):
                print("\nRespuesta inválida. Debe ingresar 's' o 'n'.")
                continuar = input("¿Desea intentar con otro documento? s/n: ").strip().lower()
            if continuar == "n":
                print("Programación cancelada.")
                return None
            continue
        print(f"Cliente encontrado: {cliente['nombre']}")
        break

    while True:
        mostrarListaVehiculos()
        placa = input("Digite la placa del vehículo: ").upper().strip()
        vehiculo = vehiculos.buscarVehiculo(placa)
        if vehiculo is None:
            print("\nNo existe un vehículo registrado con esa placa.")
            continuar = input("¿Desea intentar con otra placa? s/n: ").strip().lower()
            while not validarRespuestaSiNo(continuar):
                print("\nRespuesta inválida. Debe ingresar 's' o 'n'.")
                continuar = input("¿Desea intentar con otra placa? s/n: ").strip().lower()
            if continuar == "n":
                print("Programación cancelada.")
                return None
            continue

        tipoVehiculo = vehiculo["tipoVehiculo"]
        tipoCliente = cliente["tipo"]

        if tipoVehiculo == "carro" and tipoCliente not in ("carro", "carro y moto"):
            print(f"\nEl cliente solo aplica para {tipoCliente}, no para carro.")
            continuar = input("¿Desea intentar con otro vehículo? s/n: ").strip().lower()
            while not validarRespuestaSiNo(continuar):
                print("\nRespuesta inválida. Debe ingresar 's' o 'n'.")
                continuar = input("¿Desea intentar con otro vehículo? s/n: ").strip().lower()
            if continuar == "n":
                print("Programación cancelada.")
                return None
            continue
        if tipoVehiculo == "moto" and tipoCliente not in ("moto", "carro y moto"):
            print(f"\nEl cliente solo aplica para {tipoCliente}, no para moto.")
            continuar = input("¿Desea intentar con otro vehículo? s/n: ").strip().lower()
            while not validarRespuestaSiNo(continuar):
                print("\nRespuesta inválida. Debe ingresar 's' o 'n'.")
                continuar = input("¿Desea intentar con otro vehículo? s/n: ").strip().lower()
            if continuar == "n":
                print("Programación cancelada.")
                return None
            continue

        print(f"Vehículo encontrado: {tipoVehiculo} con placa {placa}")
        break

    while True:
        mostrarListaInstructores()
        documentoInstructor = input("Digite el documento del instructor: ").strip()
        instructor = instructores.buscarInstructor(documentoInstructor)
        if instructor is None:
            print("\nNo existe un instructor registrado con ese documento.")
            continuar = input("¿Desea intentar con otro documento? s/n: ").strip().lower()
            while not validarRespuestaSiNo(continuar):
                print("\nRespuesta inválida. Debe ingresar 's' o 'n'.")
                continuar = input("¿Desea intentar con otro documento? s/n: ").strip().lower()
            if continuar == "n":
                print("Programación cancelada.")
                return None
            continue

        especialidad = instructor["especialidad"]

        if tipoVehiculo == "carro" and especialidad not in ("carro", "carro y moto"):
            print(f"\nEl instructor solo se especializa en {especialidad}, no en carro.")
            continuar = input("¿Desea intentar con otro instructor? s/n: ").strip().lower()
            while not validarRespuestaSiNo(continuar):
                print("\nRespuesta inválida. Debe ingresar 's' o 'n'.")
                continuar = input("¿Desea intentar con otro instructor? s/n: ").strip().lower()
            if continuar == "n":
                print("Programación cancelada.")
                return None
            continue
        if tipoVehiculo == "moto" and especialidad not in ("moto", "carro y moto"):
            print(f"\nEl instructor solo se especializa en {especialidad}, no en moto.")
            continuar = input("¿Desea intentar con otro instructor? s/n: ").strip().lower()
            while not validarRespuestaSiNo(continuar):
                print("\nRespuesta inválida. Debe ingresar 's' o 'n'.")
                continuar = input("¿Desea intentar con otro instructor? s/n: ").strip().lower()
            if continuar == "n":
                print("Programación cancelada.")
                return None
            continue

        print(f"Instructor encontrado: {instructor['nombre']}")
        break

    while True:
        while True:
            fecha = input("\nIngrese la fecha de la cita (DD/MM/AAAA): ").strip()
            if validarFecha(fecha):
                break
            print("\nFecha inválida. Use DD/MM/AAAA con una fecha real (ej: no 31/02/2026).")

        while True:
            hora = input("Ingrese la hora de inicio (HH:MM, formato 24h): ").strip()
            if not validarHora(hora):
                print("\nHora inválida. Use HH:MM (ej: 14:30).")
                continue
            horaPermitida = datetime.strptime(hora, "%H:%M").time()
            if horaPermitida < datetime.strptime("07:00", "%H:%M").time() or horaPermitida > datetime.strptime("18:00", "%H:%M").time():
                print("\nLa hora debe estar entre las 7:00 a.m. y las 6:00 p.m.")
                continue
            break
        while True:
            duracionStr = input("Digite la duración en minutos (30 a 240): ").strip()
            duracion = validarDuracion(duracionStr)
            if duracion is not None:
                break
            print("\nDuración inválida. Debe ser un número entre 30 y 240.")

        if esPasado(fecha, hora):
            print("\nNo se puede programar una cita en una fecha/hora que ya pasó.")
            reintentar = input("¿Desea intentar con otra fecha/hora? s/n: ").strip().lower()
            while not validarRespuestaSiNo(reintentar):
                print("\nRespuesta inválida. Debe ingresar 's' o 'n'.")
                reintentar = input("¿Desea intentar con otra fecha/hora? s/n: ").strip().lower()
            if reintentar == "s":
                continue
            print("Programación cancelada.")
            return None

        if instructorOcupado(documentoInstructor, fecha, hora, duracion):
            print("\nEl instructor ya tiene una cita programada en ese horario.")
            reintentar = input("¿Desea intentar con otra fecha/hora/duración? s/n: ").strip().lower()
            while not validarRespuestaSiNo(reintentar):
                print("\nRespuesta inválida. Debe ingresar 's' o 'n'.")
                reintentar = input("¿Desea intentar con otra fecha/hora/duración? s/n: ").strip().lower()
            if reintentar == "s":
                continue
            print("Programación cancelada.")
            return None

        if vehiculoOcupado(placa, fecha, hora, duracion):
            print("\nEl vehículo ya tiene una cita programada en ese horario.")
            reintentar = input("¿Desea intentar con otra fecha/hora/duración? s/n: ").strip().lower()
            while not validarRespuestaSiNo(reintentar):
                print("\nRespuesta inválida. Debe ingresar 's' o 'n'.")
                reintentar = input("¿Desea intentar con otra fecha/hora/duración? s/n: ").strip().lower()
            if reintentar == "s":
                continue
            print("Programación cancelada.")
            return None

        break

    idCita = generarIdCita()
    datos = {
        "cliente": documentoCliente,
        "instructor": documentoInstructor,
        "vehiculo": placa,
        "fecha": fecha,
        "hora": hora,
        "duracion": duracion,
        "asistencia": "Pendiente",
        "observaciones": "",
    }
    citas[idCita] = datos
    guardarCitas()

    print(f"\nCita {idCita} programada exitosamente.")
    print(datos)
    return datos


def buscarCita(idCita):
    """Devuelve el diccionario de la cita con ese id, o None si no existe."""
    return citas.get(idCita.upper().strip())


def listarCitas():
    """Devuelve el diccionario completo de citas."""
    return citas


def historialCliente(documentoCliente):
    """Devuelve una lista con todas las citas de un cliente dado."""
    return [
        {"id": idCita, **datos}
        for idCita, datos in citas.items()
        if datos["cliente"] == documentoCliente
    ]


def registrarAsistencia():
    """Pide el id de una cita ya existente y actualiza sus campos
    'asistencia' y 'observaciones'. No crea citas nuevas, solo modifica
    una que ya está guardada."""
    cargarCitas()

    idCita = input("Digite el id de la cita (ej: CITA001): ").upper().strip()
    cita = buscarCita(idCita)
    if cita is None:
        print("\nNo existe ninguna cita con ese id.")
        return None

    print(f"\nCita encontrada: cliente {cita['cliente']}, fecha {cita['fecha']} {cita['hora']}")

    while True:
        respuesta = input("¿El cliente asistió a la práctica? s/n: ").strip().lower()
        if validarRespuestaSiNo(respuesta):
            break
        print("\nRespuesta inválida. Debe ingresar 's' o 'n'.")

    cita["asistencia"] = "Asistió" if respuesta == "s" else "No asistió"
    cita["observaciones"] = input("Ingrese observaciones de la práctica: ").strip()

    guardarCitas()
    print(f"\nAsistencia y observaciones registradas para la cita {idCita}.")
    return cita


def menuRegistrarAsistencia():
    """Ciclo para registrar asistencia/observaciones de una o varias citas."""
    cargarCitas()
    while True:
        registrarAsistencia()
        while True:
            decision = input("\n¿Desea registrar asistencia de otra cita? s/n: ").strip().lower()
            if validarRespuestaSiNo(decision):
                break
            print("\nRespuesta inválida. Debe ingresar 's' o 'n'.")
        if decision == "n":
            break

    import base
    base.menu()


def menuProgramarCitas():
    """Ciclo de programación de citas."""
    cargarCitas()
    while True:
        programarCita()
        while True:
            decision = input("\n¿Desea programar otra cita? s/n: ").strip().lower()
            if validarRespuestaSiNo(decision):
                break
            print("\nRespuesta inválida. Debe ingresar 's' o 'n'.")
        if decision == "n":
            print(f"\nCitas registradas en total: {len(citas)}")
            break

    import base
    base.menu()


if __name__ == "__main__":
    menuProgramarCitas()