import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation
import pandas as pd
from pymaniprob.sphere import VonMisesFisher

N = 10

a = np.random.rand(2000, 3)*10
t = np.array([np.ones(100)*i for i in range(20)]).flatten()
df = pd.DataFrame({"time": t ,"x" : a[:,0], "y" : a[:,1], "z" : a[:,2]})

#kk = np.linspace(0.1, 100.1, 20)
kk = np.geomspace(1., 100, 10, endpoint=True)
rvs = [VonMisesFisher.rvs(p=3, size=100, k=k) for k in kk]

def update_graph(num):
#    data=df[df['time']==num]
    data = rvs[num]
    graph._offsets3d = (data[:, 0], data[:, 1], data[:, 2])    
#    graph._offsets3d = (data.x, data.y, data.z)
    title.set_text(r'$\kappa={:0.2g}$'.format(kk[num]))


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
title = ax.set_title('3D Test')

ax = fig.gca(projection='3d')
ax.set_aspect("equal")

u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
x = np.cos(u)*np.sin(v)
y = np.sin(u)*np.sin(v)
z = np.cos(v)
ax.plot_wireframe(x, y, z, color="k", alpha=0.2)

ax.view_init(elev=60., azim=0)


#data=df[df['time']==0]
#graph = ax.scatter(data.x, data.y, data.z)

data = rvs[0]
graph = ax.scatter(data[:, 0], data[:, 1], data[:, 2])



ani = matplotlib.animation.FuncAnimation(fig, update_graph, N-1, 
                               interval=1500, blit=False)

plt.axis('off')
plt.show()
