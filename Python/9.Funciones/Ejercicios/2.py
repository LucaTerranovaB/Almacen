'''Ejercicio 2

Escribir una función que reciba un número entero positivo y devuelva su factorial.'''

def factorial():
    num= int(input(print("Ingrese un numero")))
    if num > 0 :
        i = 1
        fact = 0
        rta = 0
        num2 = 0
        while i <= num+1:
       
            if i != 0:
                num2 = num - 1
                fact= (num*num2) 
                rta= fact +rta
            i += 1     
                
        print(rta)
    else:
        print("Numeros mayores a cero porfavor")

factorial()