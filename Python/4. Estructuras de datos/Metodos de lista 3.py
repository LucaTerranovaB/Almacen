# MOdificacion de datos dentro de una lista

lista = ["Hola", 24, 25, "Luca"]

#Modificamos dato 3 de la lista = 25

lista[3] = "Bellachao"
print(lista[3])


#Eliminar elementos de unba lista (POP Y REEMOVE)

# POP elimina el ultimo
lista.pop()
print(lista)
#Reemove elimina el que elijas

lista.remove("Hola")
print(lista)