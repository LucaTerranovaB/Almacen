'''Ejercicio 1

Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular después la suma, resta, multiplicación y división.
 Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.'''

class Calculadora():

    def __init__(self,num1,num2):
        self._num1 = num1
        self._num2 = num2
     

    def suma(self,num1,num2):
        self._suma = num1 + num2
        return self._suma

    def resta(self,num1,num2):
        self._resta = num1 - num2
        return self._resta

    def multiplicacion(self,num1,num2):
        self._multiplicacion = num1 * num2
        return self._multiplicacion

    def division(self,num1,num2):
        self._division = num1 / num2
        return self._division

num1 = int(input(print("Ingrese el primer numero: ")))
num2 = int(input(print("Ingrese el segundo numero: ")))

s = Calculadora(num1,num2)
print("La suma es: ",s.suma(num1,num2))

r = Calculadora(num1,num2)
print("La resta es: ",r.resta(num1,num2))

m = Calculadora(num1,num2)
print("La multiplicacion es: ",m.multiplicacion(num1,num2))

d = Calculadora(num1,num2)
print("La division es : ",d.division(num1,num2))
