class Coche:
    def __init__(self, marca, modelo, color, dueno):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.dueno = dueno
        
        
    def conducir(self):
        print(f"Conduciendo el coche {self.marca} {self.modelo} de color {self.color}")


    def hacer_mantenimiento(self):
        if self.marca == "Toyota":
            print("El mantenimiento es cada 5 años")
        else:
            print("El mantenimiento es cada 3 años")

    
    def vender_auto(self, dueno):
        self.dueno = dueno
        print(f"Auto vendido a {self.dueno}")

mi_coche = Coche("Toyota", "Corola", "Negro", "Joshua")

tu_coche = Coche("Chevrolet", "Onix", "Plomo", "Karly")

mi_coche.conducir()
tu_coche.conducir()

mi_coche.hacer_mantenimiento()
tu_coche.hacer_mantenimiento()

mi_coche.vender_auto("Jayden")