


class Estudiante():

    def __init__(self,nombre,nota):
        self._nombre = 'Franco'
        self._nota = 8
    
    
    @property      
    def nombre(self):
        print (self._nombre)

    @nombre.setter
    def nombre(self,nombre): 
        self._nombre = nombre

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self,nota):
        self._nota = nota


a = Estudiante("franco","3")
print(a.nombre)
print(a.nota)