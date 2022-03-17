class Engine:
    def __init__(self):
        self.rpm=0
        self.gear=0

    def modify_rpm(self,variation):
        self.rpm +=variation

    def modify_gear(self,variation):
        self.gear += variation
        if self.gear > 5:
            self.gear = 5
            print("Marcha máxima")
        if self.gear < -1:
            self.gear = -1
            print("Marcha mínima")
    
    def get_speed(self):
        if self.gear >= 0:
            speed = (self.rpm*self.gear/5)/10
        elif self.rpm > 0:
            speed = -10
        else:
            speed = 0
        return speed

    def __str__(self):
        speed=self.get_speed()
        status = str(self.rpm) + ' rpm, ' + str(self.gear) + ' marcha, ' + str(speed) + ' km/h'
        return status