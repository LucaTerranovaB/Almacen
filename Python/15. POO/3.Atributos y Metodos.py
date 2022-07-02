#Metodos y atributos
#OBJETO: TELEFONO
#ATRIBUTOS: MARCA-MEMORIA-PANTALLA
#COMPORTAMIENTOS: LLAMA- MENSAJEA - ALARMA-CALENDARIO     (ACCIONES)

'''METODOS: Son funciones que en POO , en una clase se llaman metodos, los cuales lo realizan los objetos
   ATRIBUTOS: caracteristicas, cualidades, descripciones que describen un objeto de la clase'''

#EN CODIGO

#DEFINICION DE CLASE
class FabricaTelefonos():
   marca = 'Apple'
   color = 'Negro'
   MemRam = 32
   Memsec = 256

#DEFINICION METODOS , CON ARGUMENTO SELF
   def llamar(self,mensaje):
      return mensaje

   def EscucharMusica(self):
      print("Estas escuchando musica")


#DEFINICION DE OBJETO 1 TARUBUTOS
telefono = FabricaTelefonos()
print(telefono.marca)
print(telefono.color)
print(telefono.MemRam)
print(telefono.Memsec)

#USAMOS METODO fuera de la clase
print(telefono.llamar("Hola bro"))
print(telefono.EscucharMusica())