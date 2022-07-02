#CUANDO TENEMOS UNA CLASE PADRE E HIJA

class Animales():

    def habla(self):
        print("Hola soy un animal")
    
    def descripcion(self):
        print("Yo soy un {}".format(self.animal))


class Perro(Animales): # se hereda en parentesis de animales
    pass

animal = Animales() #CREAMOS EL OBJETO A PARTIR DE LA CLASE ANIMAL
animal.habla()

class Abeja(Animales):
    def __init__(self,animal):
        self.animal = animal


#CREAMOS PERRO A PARTIR DE CLASE PERRO
perro = Perro()
perro.habla()

#CREAMOS UN OBJETO A PARTIR DE LA CLASE ABEJA
abeja = Abeja("Abeja")
abeja.descripcion()