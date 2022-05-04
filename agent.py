# déplacements selon le greedy par découverte de la carte
# 1er move au pif
# faut faire plusieurs parties où le maze est identique pour s'améliorer

# coder l'espérance selon l'éligibilité


# Imports
import numpy as np
import matplotlib.pyplot as plt
from maze import *
from vizualizer import *

class Agent:

    def __init__(self, maze):
        self.maze = maze
        self.x = np.random.randint(0,maze.w)
        self.y = np.random.randint(0,maze.h)
        self.rewards = []

    def random_move(self, possible_moves_list):
        return np.random.choice(possible_moves_list)

    def get_possible_moves(self):
        possible_moves = self.maze.eligible_moves[self.x][self.y]
        return [c for c in possible_moves]

    def next_move(self, move_func, moves):
        """
        Next move for the agent to do
        """
        
        move = move_func(moves)
    
        if 'U' in move:
            self.x -= 1
        elif 'D' in move:
            self.x += 1
        elif 'L' in move:
            self.y -= 1
        elif 'R' in move:
            self.y += 1
    
    def get_reward(self):
        """
        Get reward for a (x,y) position
        """
        reward = self.maze.grid[self.x][self.y]
        self.rewards[-1].append(reward)
        return reward
    
    def move(self):
        self.next_move()
        self.get_reward()
    

        
    def new_position(self):
        self.x = np.random.randint(0,maze.w)
        self.y = np.random.randint(0,maze.h)

class RandomAgent(Agent):
    def __init__(self, maze):
        super().__init__(maze)
    
    def next_move(self):
        super().next_move(self.random_move)
    



class GreedyAgent(Agent):
    
    def __init__(self, maze):
        super().__init__(maze)
        self.gamma = 0.9
        self.alpha = 0.1
        self.epsilon = 0.2

        # Initializing the Q-matrix
        self.Q = np.full((self.maze.w, self.maze.h),fill_value = {'U' : 0, 'D' : 0, 'L': 0, 'R':0 })
    

    
    def next_move(self):
        d = np.random.random()
        if self.epsilon < d :
            max_index = np.argmax(self.Q[self.x, self.y].values())
            move = list(self.Q[self.x, self.y].keys())[max_index]
        else :
            super().next_move(self.random_move)
        self.update()



    def update(state, state2, reward, action, action2):
        predict = self.Q[state][action]
        target = reward + gamma * Q[state2, action2]
        Q[state, action] = Q[state, action] + alpha * (target - predict)

if __name__ == '__main__' :

    maze = Maze(10,10)
    dummy = GreedyAgent(maze)
    visu = Visualizer(maze, dummy)

    nb_episode = 5
    max_step   = 150

    for i in range(nb_episode):
        dummy.rewards.append([])

        for it_step in range(max_step):
            print(dummy.x, dummy.y)
            dummy.move()
            if len(dummy.rewards[-1]) != 0 and dummy.rewards[-1][-1] > 0:
                break

        dummy.new_position()

    visu.plot_perf()
