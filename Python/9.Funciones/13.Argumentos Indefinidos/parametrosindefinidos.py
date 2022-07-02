#COMO SE ALMACENAN LOS PARAMETROS EN TUPLAS O LISTA
#CUANDO NO SABEMOS CUANTOS Y QUE TIPOS DE DATOS VAN A ENTRAR EN ALGUNA PARTE DEL CODIGO

def argumento(num):
    return type(num)

print(argumento("Hola"))

#PARA QUE OBTENGA MAS DE UN VALOR USO DEL *
def argumento1(*num1):
    return type(num1)

print(argumento1(10,20,30,20,10))