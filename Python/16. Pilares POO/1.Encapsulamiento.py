# PILARES DE POO --> ENCAPSULAMIENTO-ABSTRACCION-HERENCIA-POLIMORFISMO

'''Aplicar sobre los atributos cierto alcance parq que ese atributo solo sea utilizado dentro de la clase'''

class A():

    def __init__(self):
        self.contador = 0
        
    def incrementar(self):
        self.contador += 1

    def cuenta(self):
        return self.contador


class B():
    def __init__(self):
        self.__contador = 0
        
    def incrementar(self):
        self.__contador += 1

    def cuenta(self):
        return self.__contador


a = A()
print(a.cuenta())
#Objeto.metodo
a.incrementar()
print(a.cuenta())
print("----------------------------------------------------------")
b = B()
print(b.cuenta())
b.incrementar()
print(b.cuenta())

print("-------------------------------")
print(b.__contador) #CON LA DOBLE GUION BAJO SE ENCAPSULA EL ATRIBUTO, NO PUDIENDO ACCEDER A EL POR FUERA DE LA CLASE