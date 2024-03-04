## Crea una clase lamada vehiculo capaz de procesar la informacion basica de los mismos en una consencionaria. Debe tener constructor, los atributos del vahiculo son: patente, marca, kilometraje. Crear meodos getter y setter. mostar por pantalla al menos un atributo y mostrar kilometraje.

class Vehiculo:
    def __init__(self, patente, marca, kilometraje):
        self.patente = patente
        self.marca = marca
        self.kilometraje = kilometraje

    def get_patente(self):
        return self.patente

    def set_patente(self, patente):
        self.patente = patente

    def get_marca(self):
        return self.marca

    def set_marca(self, marca):
        self.marca = marca

    def get_kilometraje(self):
        return self.kilometraje

    def set_kilometraje(self, kilometraje):
        self.kilometraje = kilometraje

    def mostrar_kilometraje(self):
        print("El kilometraje del vehículo es:", self.kilometraje)


vehiculo = Vehiculo("CBM613", "Ferrari", 50000)
print("La marca del vehículo es:", vehiculo.get_marca())
vehiculo.mostrar_kilometraje()
