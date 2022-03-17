class Light(Environment):
    def __init__(self):
        self.activate()
    
    def activate(self):
        self.activated=True
 
    def deactivate(self):
        self.activated=False

    def update(self):
        lum = self.environment.get_lum()
        if lum < 40:
            self.activate()
        else:
            self.deactivate()

    
    def __str__(self):
        lum = self.get_lum()
        status = "Nivel de luminosidad: " + str(lum)
        return status