from msilib.schema import Property


class A():

    def __init__(self):
        self._cuenta = 0 #con 1 _ son atributos encapsulados
        self._contador = 0

    @property       #SE AGREGAR ESA PALABRA RESERVADA AL METODO PARA DECIRLE QUE VA A SER TOMADO COMO ATRIBUTO EL METODO
    def cuenta(self):
        return self._cuenta

    @property
    def contador(self):
        return self._contador

a = A()
print(a.cuenta)
print(a.contador)