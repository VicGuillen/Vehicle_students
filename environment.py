class Environment:
    def __init__(self):  # nivel luminosidad 0 - 99
        self.lum = 0

    def modify_lum(self,variacion):
        self.lum += variacion
    
    def set_lum(self):
        self.lum = input('Nivel de luminosidad (0-99): ')

    def get_lum(self):
        lum = self.lum
        return lum

    
    def __str__(self):
        lum = self.get_lum()
        status = "Nivel de luminosidad: " + str(lum)
        return status