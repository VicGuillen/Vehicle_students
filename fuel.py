class Fuel(Engine):
    def __init__(self):
        self.level = 1000

    def update(self):
        self.level = self.level - abs(self.engine.get_speed())*0.01

    def __str__(self):
        status = "Nivel de combustible: " + str(self.update()) + ' L'
        return status