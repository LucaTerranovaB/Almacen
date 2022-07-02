#A DIFERENCIA DE GET QUE ES PARA OBTENER EL GET ES PARA MODIFICAR
#PARA CADA ATRIBUTO SI QUEREMOS MODIFICARLO HAY QUE AGREGARLE EL METODO SET
class A():

    def __init__(self):
        self._cuenta = 0 
        self._contador = 0

    @property      
    def cuenta(self):
        return self._cuenta

    @cuenta.setter
    def cuenta(self,cuenta):  #como parametro self y atributo a modificar
        self._cuenta = cuenta


    @property
    def contador(self):
        return self._contador

    @contador.setter
    def contador(self,contador):
        self._contador = contador

a = A()
print(a.cuenta)
print(a.contador)

#LLamar a cuenta set
a.cuenta = 20
print(a.cuenta)

#Llamar a contador con set
a.contador =50
print(a.contador)