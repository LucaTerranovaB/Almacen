class A():

    def __init__(self,contador,cuenta):
        self._contador = 0 #EL GUION BAJO AVISA AL PROGRAMADOR QUE NO CAMBIA EL VALOR DEL ATRIBUTO (SE LLAMA CON GET O SET)
    
    def incrementar(self):
        self.__contador += 1 #CON EL BOBLE __ NO PERMITE PRINTEAR NI CAMBIAR EL ATRIBUTO

    def cuenta(self):
        return self._contador
        
