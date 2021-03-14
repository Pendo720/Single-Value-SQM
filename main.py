import matplotlib
import numpy as np
import random

from matplotlib import pyplot as plt
from matplotlib.patches import PathPatch
from matplotlib.path import Path

import singlValueSqm

def main():
    vals = [random.uniform(0, 4) for x in range(4)]
    plotValues(vals)      

def plotValues(vals):
    '''Plots the set of values in vals on the four dimension of quality
    Note: two of the values are negated for display purposes.    
    '''
    xs = [0, vals[1], 0, -vals[3]]
    ys = [vals[0], 0, -vals[2], 0]
    plt.style.use('fivethirtyeight')    
    _, ax = plt.subplots()    
    # ax.figsize=(15,9)
    ax.dpi = 70
    codes = []
    vertices = [x for x in zip(xs, ys)]
    vertices.append((xs[0], ys[0]))

    codes = [Path.MOVETO] + [Path.LINETO]*3 + [Path.CLOSEPOLY]
    path = Path(vertices, codes)
    pathPatch = PathPatch(path, facecolor='None', edgecolor='blue')
    
    ax.add_patch(pathPatch)    
    ax.autoscale_view()
    plt.ylabel('Documentation/Specification')
    plt.xlabel('Testing/Implementation')
    plt.title('Single-Value-SQM Graph')
    ticks = [m for m in np.arange(-4, 5, 1)]
    plt.xticks(ticks)
    plt.yticks(ticks)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()