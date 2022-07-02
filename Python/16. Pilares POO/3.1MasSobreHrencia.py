class Animales():

    def __init__(self, nombre):
        self.nombre = nombre

#EL problema de __init__ es que a veces se invoca mal


class Perro(Animales):
    
    def __init__(self,nombre, sonido):
        super().__init__(nombre)  # Super mas el metodo que queremos heredar
        self.sonido = sonido

perro = Perro("Norstty","Guauuuuuuuuu") #Cargamos la clase padre animales con el atributo nombre y sonido a una clase hija
print(perro.nombre)
print(perro.sonido)
