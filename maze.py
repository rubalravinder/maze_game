from re import X
import numpy as np


class Maze :

    def __init__(self, h, w):
        self.h = h
        self.w = w
        self.grid = np.full((h,w), -1)
        self.grid[np.random.randint(0, h)][np.random.randint(0, w)] = 100
        self.grid[np.random.randint(0, h)][np.random.randint(0, w)] = 100

        self.eligible_moves = np.full((10,10), 'UDLR')
        self.eligible_moves[0] = 'DLR'
        self.eligible_moves[:,0] = 'UDR'
        self.eligible_moves[self.h - 1] = 'ULR'
        self.eligible_moves[:,self.w - 1] = 'UDL'
        self.eligible_moves[0][0] = 'DR'
        self.eligible_moves[0][self.w - 1] = 'DL'
        self.eligible_moves[self.h - 1][self.w - 1] = 'UL'
        self.eligible_moves[self.h - 1][0] = 'UR'
        
    


if __name__ == '__main__':
    maze = Maze(10,10)
    print(maze.eligible_moves)



    