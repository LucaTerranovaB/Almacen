#Es una secuencia de sentencias que realizan operaciones y reciben nombre.
#Se puede reciclar y llamar en cualquier parte del codigo

def Funcion():
    print("Holamundo")

Funcion()
#La funcion se llama fuera del contenedor

#PARAMETROS

def Funcion2(mensaje):
    mensaje = 'Hola carita'
    print(mensaje)

Funcion2(print)
