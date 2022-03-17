from blinker import *

class Vehicle:
    def __init__(self):
        self.blinker_front = Blinker(BLINKER_FRONT)
        self.blinker_rear = Blinker(BLINKER_REAR)

    def __str__(self):
        status = str(self.blinker_front) + ' ' + str(self.blinker_rear)
        return status


    def do_work(self):

        while True:            
            print(self)

            key = input('next action (q quit): ')
            if key == 's':
                self.blinker_front.change()
            if key == 'a':
                self.blinker_rear.change()
            #if key == 'w':
            #    self.engine.modify_rpm(100)
            #if key == 'z':
            #    self.engine.modify_rpm(-100)
            #if key == 'e':
            #    self.engine.modify_gear(1)
            #if key == 'd':
            #    self.engine.modify_gear(-1)
            #if key == 'r':
            #    self.environment.modify_lum(10)
            #if key == 'f':
            #    self.environment.modify_lum(-10)

            if key == 'q':
                exit()
            
            #self.light.update()
            #self.fuel.update()


if __name__ == "__main__":
    vehicle1 = Vehicle()
    vehicle1.do_work()

