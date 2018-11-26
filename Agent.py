from __future__ import division
import random

#agent class that is used as each node in the network.
class Agent:
    boldness = 0
    vengefulness = 0
    name = 0

    DS = 0 #Defection score
    PS = 0 #Punishment score
    POS = 0 #punishment omission score
    TS = 0 #Total score

    def __init__(self, n):
        self.name = n
        self.boldness = random.randrange(8)/7
        self.vengefulness = random.randrange(8)/7

    def __call__(self, n):
        return self.name

    #agents need to reset their scores before interacting with other nodes for
    #that round.
    def reset_scores(self):
        self.DS = 0
        self.PS = 0
        self.POS = 0
        self.TS = 0

    def print_scores(self):
        # self.TS += self.DS + self.PS + self.POS
        print('id = ' + str(self.name))
        print('boldness: ', str(self.boldness))
        print('vengefulness: ', str(self.vengefulness))
        print('DS: ', str(self.DS))
        print('PS: ', str(self.PS))
        print('POS: ', str(self.POS))
        print('TS: ', str(self.TS))

    def explore(self):
        self.boldness = random.randrange(8)/7
        self.vengefulness = random.randrange(8)/7

    def total(self):
        self.TS += self.DS + self.PS + self.POS
