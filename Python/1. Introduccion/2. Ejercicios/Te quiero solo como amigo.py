cadena = 'Te quiero solo como amigo'

print(cadena[0 : 3])
print("************************************************")
print(cadena[-3])
print("************************************************")
for i in range(0, 24, 2) :
    print(cadena[i])
print("************************************************")

print(cadena[: : -1])
print("*************************************************")

print(cadena[: : 1] + cadena [: : -1])