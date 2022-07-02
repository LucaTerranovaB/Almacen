i = 0

num =int(input("Ingresar un numero para mostrar sus tablas de multiplicar :  "))

while i < 10 :
    i += 1
    print("{} * {}" .format(i,num))
    result = i * num
    print(" = ", result)
    print("-----------------------------------------------")