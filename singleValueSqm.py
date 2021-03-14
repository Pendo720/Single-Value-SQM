# singleValueSqm

import matplotlib
import numpy as np
import random

from matplotlib import pyplot as plt
from matplotlib.patches import PathPatch
from matplotlib.path import Path

class singleValueSqm:
    
    def __init__(self, dimValues):
        '''Initialising quality values for the four dimensions    
        '''
        self.dimValues = dimValues   
   
    def plotValues(self):
        '''Plots the set of values in dimValues on the four dimension
        Note: two of the values are negated for display purposes.    
        '''
        xs = [0, self.dimValues[1], 0, -self.dimValues[3]]
        ys = [self.dimValues[0], 0, -self.dimValues[2], 0]
        plt.style.use('fivethirtyeight')    
        _, ax = plt.subplots()    
        ax.dpi = 70
        codes = []
        vertices = [x for x in zip(xs, ys)]
        vertices.append((xs[0], ys[0]))

        codes = [Path.MOVETO] + [Path.LINETO]*3 + [Path.CLOSEPOLY]
        path = Path(vertices, codes)
        pathPatch = PathPatch(path, facecolor='None', edgecolor='black')
        
        ax.add_patch(pathPatch)    
        ax.autoscale_view()
        plt.ylabel('Documentation/Specification')
        plt.xlabel('Testing/Implementation')
        plt.title('Single-Value-SQM')
        ticks = [m for m in np.arange(-4, 5, 1)]
        plt.xticks(ticks)
        plt.yticks(ticks)
        plt.tight_layout()
        plt.show()