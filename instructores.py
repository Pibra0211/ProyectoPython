import json
import os

ARCHIVO_INSTRUCTORES = "instructoress.json"

datosInstructor={
    "nombre":"",
    "documento":"",
    "especialidad":"",
    "telefono":""
}
contadorInstructores = 1

def cargarInstructores():
    if os.path.exists(ARCHIVO_INSTRUCTORES):
        try:
            with open(ARCHIVO_INSTRUCTORES, "r") as archivoI:
                contenido = archivoI.read().strip()
                if contenido:
                    return json.loads(contenido)
        except json.JSONDecodeError:
            print(f"\nAviso: {ARCHIVO_INSTRUCTORES} no tiene un formato JSON válido, se iniciará vacío.")
    return {}

instructores = cargarInstructores()

def guardarInstructores():
    with open(ARCHIVO_INSTRUCTORES, "w") as archivoI:
        json.dump(instructores, archivoI, indent=4)

def obtenerInstructor(documento):
    return instructores.get(documento)

def registroInstructor():
  nombre = input("Digite el nombre completo del instructor: ").title().strip()
  while True:
      if nombre.replace(" ","").isalpha():
          break
      else:
          print("\nEl nombre no puede contener numeros ni caracteres especiales.")
          nombre = input("\nDigite el nombre completo del instructor nuevamente: ").title().strip()
  datosInstructor["nombre"] = nombre
  documento = input("Digite el número de documento del instructor: ")
  while not (documento.isdigit() and 8 <= len(documento) <= 10):
    documento = input("\nEl documento debe contener solo dígitos y tener entre 8 y 10 caracteres. Ingréselo nuevamente: ")
  datosInstructor["documento"] = documento

  especialidad = input("¿La especialidad del instructor es carro? s/n: ").strip().lower()
  while True:
    if especialidad == "s" or especialidad == "n":
        break
    else:
        especialidad = input("\nRespuesta inválida. Debe ingresar 's' o 'n': ").strip().lower()

  if especialidad == "n":
      especialidad = "moto"
  else:
      tambienMoto = input("¿El instructor también se especializa en moto? s/n: ").strip().lower()
      while True:
          if tambienMoto == "s" or tambienMoto == "n":
              break
          else:
              tambienMoto = input("\nRespuesta inválida. Debe ingresar 's' o 'n': ").strip().lower()
      especialidad = "carro y moto" if tambienMoto == "s" else "carro"
  datosInstructor["especialidad"] = especialidad
  telefono = (input("Digite el numero de telefono del instructor: "))
  while True:
        if telefono.isdigit() and len(telefono) == 10:
            break
        else:
            telefono = input("\nEl numero de telefono no puede contener caracteres ni letras especiales\nIngreselo nuevamente (debe tener 10 digitos): ")
  datosInstructor["telefono"] = "+57 " + telefono

  instructores[documento] = datosInstructor.copy()
  guardarInstructores()
  return(datosInstructor)

while True:
    datosDelInstructor = (registroInstructor())
    print(f"\nLos datos del Señor/señora {datosDelInstructor['nombre']} se han registrado con exito")
    decision = input("¿Desea registrar un nuevo instructor? s/n: ").lower()

    if decision == "s":
        contadorInstructores += 1
        continue
    elif decision == "n":
        print(f"\nInstructores registrados {contadorInstructores}")
        import base
        print (base.menu())
        break
    else:
        decision = input("\nRespuesta inválida. Debe ingresar 's' o 'n': ").lower()