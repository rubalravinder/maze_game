from re import X
import numpy as np


class Maze :

    def __init__(self, h, w):
        self.h = h
        self.w = w
        self.grid = np.full((h,w), -1)
        self.grid[np.random.randint(0, max(h))][np.random.randint(0, max(w))] = 100
        self.grid[np.random.randint(0, max(h))][np.random.randint(0, max(w))] = 100


    def elegibility(self):
        self.eligible_moves = np.full((10,10), 'UDLR')
        self.eligible_moves[0] = 'DLR'
        self.eligible_moves[:,0] = 'UDR'
        self.eligible_moves[max(self.h)] = 'DLR'
        self.eligible_moves[:,max(self.w)] = 'UDR'
        self.eligible_moves[0][0] = 'DR'
        self.eligible_moves[0][max(self.w)] = 'DL'
        self.eligible_moves[max(self.h)][max(self.w)] = 'UL'
        self.eligible_moves[max(self.h)][0] = 'UR'
        
    






    