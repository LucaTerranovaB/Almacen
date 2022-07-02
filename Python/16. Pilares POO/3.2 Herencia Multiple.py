#una herencua de mas de una clase

class A():
    def primera(self):
        return "Esta es la clase A"
    
class B():
    def segunda(self):
        return "Esta es la clase B"


class C(A,B):
    pass

c = C()
#Puedo llamar al metodo primera o segunda
print(c.primera())
print(c.segunda())