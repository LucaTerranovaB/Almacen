#retorna un valor de una funcion

def entero():
    print("Este es un dato entero: ")
    return 10

print(entero())

def decimal():
    print("Este es un dato decimal: ")
    return 20.5

print(decimal())

def frase():
    return 'Hola'

print(frase())

def asignacion():
    return 1,2,3,4,5

v1,v2,v3,v4,v5= asignacion()

print(v1)
print(asignacion())