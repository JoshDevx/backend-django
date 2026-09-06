class A:
    def saludar(self):
        print("Hola desde la clase A")
    

class B:
    def saludar(self):
        print("Hola desde la clase B")


class C(A, B):
    pass


c = C()
c.saludar()

print(C.__mro__)  # Metodo de resolucion de orden