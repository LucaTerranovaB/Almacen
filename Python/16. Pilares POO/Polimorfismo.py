#Modificacion de metodos cuando se heredan de otra clase

class Animales():
    def __init__(self,mensaje):
        self.mensaje = mensaje

    def hablar(self):
        print(self.mensaje)

class Perro(Animales):
    def hablar(self):
        print("Yo no hablo, hago Guauuuuu")

#MODIFICAR METODOS HEREDADOS QUE ESTAN EN UNA CLASE PADRE, Y MODIFICAR EN LA CLASE HIJA

class Pez(Animales):
    def hablar(self):
        print("Yo nado")

perro = Perro("Guauuuu")
perro.hablar()

animal = Animales("Miau")
animal.hablar()

pez = Pez("Nada")
pez.hablar()
