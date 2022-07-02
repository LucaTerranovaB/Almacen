# PARAMETRO: Es una variable que se va a utilizar cuando se crea la funcion
# ARGUMENTO: Es el valor que se la va a asignar a un parametro cuando llamamos a a una funcion

#METODO NORMAL VARIABLES INMUTABLES
def suma():
    num1 = 20
    num2 = 30
    suma = num1 + num2
    return suma

print(suma())

print("---------------------------------------------------------------------")
#CON PARAMETROS Y VARIABLES
def suma1(num1, num2):
    suma= num1 +num2
    return suma

print(suma1(10,35))
