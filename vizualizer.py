import matplotlib.pyplot as plt
from maze import *
from agent import *

class Visualizer:

    def __init__(self, maze, agent):
        self.maze = maze
        self.agent = agent
    
    def plot_perf(self):
        """
        Plot a 2D map representing the gain that were found.
        historic : DataFrame with columns x,y,gain for each trial.
        """
        plt.plot(np.cumsum(self.agent.rewards), linestyle='', marker='*')
        plt.grid()
        plt.show()