conjunto = set((1, 1, 3, 3, 4, 4, 5))
lista = [1, 1 ,2 ,3 ,4 ,4]

#lista permite elementos repetidos , Conjuntos NO


print(conjunto)
print(lista)

conjunto2 = {1, 2, 3, 4, 5}

#Agregar elemento

conjunto2.add(20)
print(conjunto2)

# Quitar elemento

conjunto2.remove(1)
print(conjunto2)

conjunto2.discard(2)
print(conjunto2)
#Eliminar con pop (Elimina cualquier elemento a azar)

conjunto3 = {1, 2, 3, 4, 5}
conjunto3.pop()

print(conjunto3)

#Actualizar update()

conjunto4 ={1, 2, 3, 4, 5}
conjunto4.update([1, 2, 3, 6, 7 ])
print(conjunto4)

#Limpiar conjunto clear()

conjunto4.clear()
print(conjunto4)
