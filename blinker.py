# Blinker position (pos attribute)
BLINKER_FRONT = 1
BLINKER_REAR = 2

class Blinker:
    def __init__(self,pos):
        self.pos=pos
        self.deactivate()

    def activate(self):
        self.activated=True
 
    def deactivate(self):
        self.activated=False
 
    def get_activated(self):
        return self.activated

    def change(self):
        # self.activated = not self.activated
        if self.activated:  # if self.activated==True, pero al ser booleano lo capta 
            self.deactivate()
        else:  # if self.activated==False:
            self.activate()
            
    def __str__(self):
        if self.activated:
            status = 'A'
        else:
            status = 'D'
        return status

