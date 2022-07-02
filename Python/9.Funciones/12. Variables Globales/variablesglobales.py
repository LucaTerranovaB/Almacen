#funciones estaticas, indiferencia ante el cambio de valor

def valores():
    global num1
    global num2
    '''Con global lee las variables fuera del contenedor de la funcion'''
    '''Primero se declara global num y luego num= 5, nunca global num = 5'''
    num1 = 100
    num2 = 50
    resultado = num1 + num2
    return resultado
#Siempre da lo mismo
print(valores())
print(valores())
print(valores())

#ACCEDER A LAS VARIABLES DE UNA FUNCION POR FUERA(GLOBAL)
resta = num1 - num2
print(resta)
