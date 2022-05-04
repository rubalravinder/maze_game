# déplacements selon le greedy par découverte de la carte
# 1er move au pif
# faut faire plusieurs parties où le maze est identique pour s'améliorer

# coder l'espérance selon l'éligibilité


# Imports
import numpy as np
import matplotlib.pyplot as plt
from maze import *
from vizualizer import *

class RandomAgent:

    def __init__(self, maze):
        self.maze = maze
        self.x = np.random.randint(maze.w)
        self.y = np.random.randint(maze.h)
        self.rewards = []

    def next_move(self):
        """
        Next move for the agent to do
        """
        possible_moves = self.maze.eligible_moves[self.x][self.y]
        possible_moves_list = [c for c in possible_moves]
        move = np.random.choice(possible_moves_list)
    
        if 'U' in move:
            self.y -= 1
        elif 'D' in move:
            self.y += 1
        elif 'L' in move:
            self.x -= 1
        elif 'R' in move:
            self.x += 1
    
    def get_reward(self):
        """
        Get reward for a (x,y) position
        """
        reward = self.maze.grid[self.x][self.y]
        self.rewards.append(reward)
        return reward
    
    def episode(self):
        self.next_move()
        self.get_reward()
    

        



class GreedyAgent:
    
    def __init__(self, maze):
        self.maze = maze
        pass




if __name__ == '__main__' :

    maze = Maze(10,10)
    dummy = RandomAgent(maze)
    visu = Visualizer(maze, dummy)

    dummy.episode()
    for i in range(5):
        while dummy.rewards[-1] < 0:
            print(dummy.x, dummy.y)
            dummy.episode()
        visu.plot_perf()
