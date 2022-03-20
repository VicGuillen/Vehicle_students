class Light:
    def __init__(self,environment):
        self.activate()
        self.environment = environment
    
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

        status = "Luces: " 
        if self.activated:
            status += ' Activadas'
        else:
            status += ' Desactivadas'
        return status
        
        
        return status