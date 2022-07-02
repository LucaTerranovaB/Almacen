palabra1 = input("Ingrese su primer palabra:   ")
palabra2 = input("Ingrese su segunda palabra:  ")

# Uso de len para tamaño de la cadena para ver si riman

if len(palabra1) < 3 or len(palabra2) < 3:
    print("No se puede rimar")

elif palabra1[-3 : ] == palabra2[-3 : ] :
    print("Las palabras riman")

elif palabra1[-2 : ] == palabra2[-2 : ] :
    print("Las palbras riman un poco")

else:
    print("Las palabras no riman")    