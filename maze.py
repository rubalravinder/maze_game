from re import X
import numpy as np


class Maze :

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.grid = np.full((x,y), -1)
        self.grid[4][6] = 100
        self.grid[9][2] = 100

    