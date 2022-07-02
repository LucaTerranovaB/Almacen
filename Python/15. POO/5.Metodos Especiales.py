class FabricaTelefonos():
    #CONSTRUCTOR
    def __init__(self,marca,color):
        self.marca = marca
        self.color = color
        print("El objeto {} ha sido creado". format(self.marca))
    #DESTRUCTOR
    def __del__(self):
        print("El objeto {} ha sido destruido". format(self.marca))

    def __str__(self):
        return "El objeto es {}".format(self.marca)

telefono = FabricaTelefonos("Apple","Rojo")
print(telefono.marca)

#SALE CODIGO MAQUINA (ARREGLADO EN __STR__)
print(telefono)