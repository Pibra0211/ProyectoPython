import json
datosInstructor={
    "nombre":"",
    "documento":"",
    "especialidad":"",
    "telefono":""
}

def registroInstructor():
  nombre = input("Digite el nombre completo del instructor: ")
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
      tambien_moto = input("¿El instructor también se especializa en moto? s/n: ").strip().lower()
      while True:
          if tambien_moto == "s" or tambien_moto == "n":
              break
          else:
              tambien_moto = input("\nRespuesta inválida. Debe ingresar 's' o 'n': ").strip().lower()
      especialidad = "carro y moto" if tambien_moto == "s" else "carro"
  datosInstructor["especialidad"] = especialidad
  telefono = (input("Digite el numero de telefono del instructor: "))
  while True:
        if telefono.isdigit() and len(telefono) == 10:
            break
        else:
            telefono = input("\nEl numero de telefono no puede contener caracteres ni lestas especiales\nIngreselo nuevamente (debe tener 10d igitos): ")
  datosInstructor["telefono"] = "+57 " + telefono
  with open("instructoress.json","a+") as archivoI:
        archivoI.write("\n" + json.dumps(datosInstructor))
  return(datosInstructor)
instructores = (registroInstructor())
print(instructores)
print(f"\nLos datos del Señor/señora {instructores["nombre"]} se han registrado con exito")
desicion = input("¿Desea registrar un nuevo instructor? s/n: ")
if desicion == "s" or desicion == "S":
    registroInstructor()
elif desicion == "n" or desicion == "N":
    import base
    print (base.menu())
    