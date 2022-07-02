#edad = int(input("Ingrese su edad : "))
#print("Tu edad es :" , edad)

#QUE PASAS SI METO UN STR???
#COMO HACERLE SABER AL USUSARIO DONDE Y COMO SE EQUIVOCO
while True:       #MIENTRAS ME EQUIVOQUE SE REPITE EL CICLO HASTA EL CORRECTO
    try:
        edad = int(input("Ingrese su edad: "))
        print("Tu edad es : ", edad)
        break
    except:
        print("Ingresaste un valor erroneo")
#FINALLY EJECUTO HAYA O NO HAYA ERROR
    finally:
        print("La ejecucion ha sido finalizada")