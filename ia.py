from random import randint

class IA:
    def __init__(self, level):
        self.level = level
    
    def playLevel0(self, morpion):
        l = randint(1,3)
        c = randint(1,3)
        while(morpion.play(2,l,c) == False):
            l = randint(1,3)
            c = randint(1,3)
    

