#Metodo init y self
'''Init: Metodo contrusctor de otros lenguajes'''
'''self: forma de equiparar los objetos llamandolos a una instancia'''

class FabricaTelefonos():
    marca = 'Apple'

    def ElaborarHuawei(self):   #COMO ES METODO DE INSTANCIA CREADA POR NOSOTROS SE PONE SELF DE ARGUMENTO
        self.marca = 'Huawei'   #Sirve para englobar un atributo a toda una clase

telefono = FabricaTelefonos()
print(telefono.marca)

#PARA LLAMAR UN METODO

telefono.ElaborarHuawei()
print(telefono.marca)

print("---------------------------------------------------------------")
#METODO INIT

class FabricaTelefonos():

    def __init__(self,marca,color): #Se ejecutan automaticamente, poner argumentos
        print("Estoy ejecutando el metodo init por un nuevo objeto")

        self.marca = marca
        self.color = color

        #CUANDO SE EJECUTE EL CODIFO VA A PEDIR MARCA Y COLOR

    
telefono = FabricaTelefonos('Apple',"Negro")
print(telefono.marca)
print(telefono.color)









