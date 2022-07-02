class FabricaTelefonos():

    def __init__(self,marca, *colores, **modelos):            # ** DICCIONARIO
        self.marca = marca
        self.colores = colores
        self.modelos = modelos

telefono = FabricaTelefonos("Nokia","Negro","Azul",m1=500,m2=505)    #Llave y valor para que reconozca diccionarios
print(telefono.marca)
print(telefono.colores)
print(telefono.modelos)