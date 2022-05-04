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
        plt.figure(1)
        for i in range(len(self.agent.rewards)):
            plt.plot(np.cumsum(self.agent.rewards[i]), "+-", label="traj_{}".format(i))
        plt.grid()
        plt.legend()
        plt.show()