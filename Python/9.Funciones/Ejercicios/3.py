def numeros():

    num1 = input(print("Ingrese el primer numero"))
    num2 = input(print("Ingrese el segundo numero"))

    if num1 > num2:
        return 1
    elif num1 < num2:
        return -1
    elif num1 == num2:
        return 0

print(numeros())