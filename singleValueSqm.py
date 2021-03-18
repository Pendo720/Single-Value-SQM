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
   
    def showMap(self):
        '''Plots the set of values in dimValues on the four dimension
        Note: two of the values are negated for display purposes.    
        '''
        xs = [0 if i%2==0 else r for i, r in enumerate(self.dimValues)]
        xs[3] = -xs[3]
        ys = [r if i%2==0 else 0 for i, r in enumerate(self.dimValues)]
        ys[2] = -ys[2]
        
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
        plt.ylabel('Documentation/Specification', loc='center')
        plt.xlabel('Testing/Implementation', loc='center')
        plt.title('Single-Value-SQM')
        ticks = [m for m in np.arange(-4, 5, 1)]
        plt.xticks(ticks)
        plt.yticks(ticks)
        plt.tight_layout()
        plt.show()