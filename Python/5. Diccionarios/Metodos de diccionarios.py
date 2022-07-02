diccionario = {1 : 2, 2 : 3, 3 : 4}

print(diccionario)


#Eliminar elemento numero .....

diccionario.pop(3)

print(diccionario)

#Limpiar diccionario

diccionario.clear()

print(diccionario)

# Devuelve el valor de la clave
diccionario = {1 : 2, 2 : 3, 3 : 4}

print(diccionario.get(3))

# Asignacion

diccionario.setdefault(4,5)

print(diccionario)

#Actualizar valores, concatenacion de diccionarios

diccionario2 = {4 : 5, 6 : 100}

diccionario.update(diccionario2)

print(diccionario)

#Sacar una copia del diccionario

diccionario.copy()

print(diccionario)
