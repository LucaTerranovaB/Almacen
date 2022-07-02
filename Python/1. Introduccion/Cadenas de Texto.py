# String

from re import T


cadena = "texto"
print(cadena)


#comillas dentro de comillas (usar simples por fuera y dobles por dentro)

cadena2 = 'texto con "comillas"'
print(cadena2)

# Union de cadena (concatenacion)

cadena = "hola"
cadena1 = "luca" 

cadena3 = cadena + cadena1
print(cadena3)
# o tambien


print(cadena + cadena1)

# multiplicacion de cadenas

cadena4 = cadena1 * 5
print(cadena4)

#concatenar 2

print("Hola usuario!!: ", cadena1)

#convertir numeros a cadena de texto

numero = 5

print((type(str(numero))))