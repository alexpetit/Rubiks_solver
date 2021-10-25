from rubik.cube import Cube
import matplotlib.pyplot as plt
import numpy as np

# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D, art3d


# prepare some coordinates
x, y, z = np.indices((3, 3, 3))

cube1 = (x < 3) & (y < 3) & (z < 3)

# set the colors of each object
colors = np.empty(cube1.shape, dtype=object)
colors[cube1] = ['red']

# and plot everything
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.set_aspect("auto")
ax.set_autoscale_on(True)



ax.voxels(cube1, facecolors=colors, edgecolor='k')

plt.show()

#c = Cube("OOOOOOOOOYYYWWWGGGBBBYYYWWWGGGBBBYYYWWWGGGBBBRRRRRRRRR")
