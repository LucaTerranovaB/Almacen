#PARA DIVICION POR CERO
while True:
    try:
        num1 = int(input("Ingrese un numero :"))
        resultado = 100/ num1
        print(resultado)
        break
    except ZeroDivisionError:
        print("No se puede dividir por cero")
    finally:
        print("Division terminada")

print("--------------------------------------------------------")
#OTRO EJEMPLO
#PARA VALORES ERRONEOS
while True:
    try:
        edad = int(input(print("Ingresa tu edad: ")))
        print("Tu edad es : ",edad)
        break
    except ValueError:
        print("Has colocado un valor erroneo")
    finally:
        print("Al fin ")

print("-----------------------------------------------------")
#INTERRUPCION DEL PROGRAMA POR TECLADO

while True:
    try:
        edad = int(input(print("Ingrese su edad")))
        print("Tu edad es: ",edad)
        break
    except KeyboardInterrupt:
        print("\nHas cancelado la ejecucion")
        break