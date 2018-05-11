from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

from pymaniprob.sphere import VonMisesFisher

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_aspect("equal")

# credit to https://stackoverflow.com/a/11156353/8828470
# for the sphere and vector plotting routines

# draw sphere
u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)
ax.plot_wireframe(x, y, z, color="k", alpha=0.2)


#m = np.random.normal(size=3)
#m/= np.linalg.norm(m)
#azi = 3*np.pi/2
#el = np.pi/4
#m = np.ones(3)
#m /= np.linalg.norm(m)
m = np.array([0., 0., 1.])

X = VonMisesFisher.rvs(m=m, p=3, k=2, size=100)

ax.scatter(*X.T)


#  draw a vector
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d


class Arrow3D(FancyArrowPatch):

    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        FancyArrowPatch.draw(self, renderer)



cm = 1.5*m # make the mean vector larger for visualisation
verts = [[0, x] for x in cm]

a = Arrow3D(*verts, mutation_scale=20,
            lw=1, arrowstyle="-|>", color="k")
#a = Arrow3D([0, 1], [0, 1], [0, 1], mutation_scale=20,
#            lw=1, arrowstyle="-|>", color="k")
#ax.add_artist(a)
ax.view_init(elev=60., azim=0.)
plt.axis('off')
plt.tight_layout()

fig2 = plt.figure()
fig2.suptitle("Von-Mises Fisher Random Variables")
for nt, k in enumerate([20, 100]):
    ax = fig2.add_subplot(1, 2, nt+1, projection='3d')
    ax.set_aspect("equal")    
    ax.plot_wireframe(x, y, z, color="k", alpha=0.2)

    X = VonMisesFisher.rvs(m=m, p=3, k=k, size=100)

    a = Arrow3D(*verts, mutation_scale=20,
                lw=1, arrowstyle="-|>", color="k")
    ax.add_artist(a)
    ax.scatter(*X.T)

    ax.view_init(elev=45., azim=0)

    ax.set_title(r"$\kappa ={}$".format(k))
    
    plt.axis('off')
    plt.tight_layout()    


plt.show()
