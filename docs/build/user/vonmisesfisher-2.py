import numpy as np
import matplotlib.pyplot as plt
#from pymaniprob.sphere import VonMisesFisher
u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_aspect("equal")
ax.plot_wireframe(x, y, z, color="k", alpha=0.2)
plt.show()
