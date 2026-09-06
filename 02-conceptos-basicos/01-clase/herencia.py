class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    
    def comer(self):
        print(f"{self.nombre} esta comiendo...")


class Perro(Animal):
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza
    
    
    def ladrar(self):
        print("Wof Wof")


mi_perro = Perro("Dracko","Pitbul")
mi_perro.comer()
mi_perro.ladrar()