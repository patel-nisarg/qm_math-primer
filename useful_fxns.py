import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pylab
import matplotlib
import matplotlib.cm as mplcm
import matplotlib.colors as colors


NUM_COLORS = 10
plt.rc('text', usetex=True)
params = {'text.latex.preamble': [r'\usepackage{amsmath}', r'\usepackage{physics}']}
plt.rcParams.update(params)
cm = plt.get_cmap('tab10')
cNorm = colors.Normalize(vmin=0, vmax=NUM_COLORS - 1)
scalarMap = mplcm.ScalarMappable(norm=cNorm, cmap=cm)


# plot vectors
def plot_vec2d(vec, labels, x_given=False):
    """
    Plots vectors and their respective labels.
    vec: List of vectors to be plotted
    labels: List of labels corresponding to vectors
    x_given: Set to True of vec contains starting X, Y coordinates. Otherwise, [0,0] are assumed for all vectors.
    """
    if len(vec) != len(labels):
        print('Warning: Not all vectors contain labels!')
    vec = np.array(vec)
    if x_given:
        vec = np.array([np.concatenate(vec[i], axis=None) for i in range(len(vec))])
        X, Y, U, V = vec[:, 0], vec[:, 1], vec[:, 2], vec[:, 3]
    else:
        X, Y = (np.zeros(len(vec)), np.zeros(len(vec)))
        U, V = (vec[:, 0], vec[:, 1])
    plt.figure(figsize=(9, 5))
    ax = plt.gca()
    scale_factor = 1.3
    xmin, xmax = np.abs(np.min(U)-np.min(X)), np.abs(np.max(U)-np.max(X))
    ymin, ymax = np.abs(np.min(V)-np.min(Y)), np.abs(np.max(V)-np.max(Y))
    if xmin > 0:
        xmin = -0.5 * xmin
    if ymin > 0:
        ymin = -0.5 * ymin
    ax.grid(True, alpha=0.5)
    color = [scalarMap.to_rgba(i) for i in range(NUM_COLORS)]
    q = ax.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1, color=color[:len(X)])
    ax.set_xlim(xmin * scale_factor - 2, xmax * scale_factor + 2)
    ax.set_ylim(ymin * scale_factor - 2, ymax * scale_factor + 2)
    ax.set_axisbelow(True)
    # show legend with vector names
    xpos = 0.9
    ypos = 0.95
    for i, label in enumerate(labels):
        ax.quiverkey(q, xpos, ypos - i / 6, U=0.4, label=label, labelpos='S', labelcolor='black',
                     color=color[i], fontproperties={'size': 14, 'weight': 'semibold'})
    plt.draw()
    plt.show()

