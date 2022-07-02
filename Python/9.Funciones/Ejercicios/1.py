lista = []
num = 0

def agregar():
    i = 0
    while i <= 5:
        num= int((input(print("Ingrese elementos a la lista"))))
        lista.append(num)
        i += 1
        print(lista)

agregar()

def ordenar():
    lista.sort()
    listaimp = [] 
    listapar = []
    i = 0
    while i <= 5:
        if lista[i] % 2 == 0:
            listapar.append(lista[i])
        else:
            listaimp.append(lista[i])
        i += 1
    print(lista)
    print(listaimp)
    print(listapar)

ordenar()