from io import open

archivo = open("clientess.json", "r")
contenido = archivo.readlines()
print(contenido)
dict(contenido)
# for cliente in contenido:

#     elemento1 = dict(cliente)

#     print(elemento1)

#     print(type(elemento1))
#     #print(elemento1["nombre"])