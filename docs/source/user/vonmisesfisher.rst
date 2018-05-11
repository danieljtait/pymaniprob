#############################
Von-Mises Fisher Distribution
#############################

.. currentmodule:: numpy

Hello!

.. plot::

   >>> import numpy as np
   >>> from mpl_toolkits.mplot3d import Axes3D
   >>> import matplotlib.pyplot as plt
   >>> from pymaniprob.sphere import VonMisesFisher
   >>> u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
   >>> x = np.cos(u)*np.sin(v)
   >>> y = np.sin(u)*np.sin(v)
   >>> z = np.cos(v)
   >>> fig = plt.figure()
   >>> ax = fig.gca(projection='3d')
   >>> ax.set_aspect("equal")
   >>> ax.plot_wireframe(x, y, z, color="k", alpha=0.2)
   >>> X = VonMisesFisher.rvs(p=3, k=20, size=100)
   >>> ax.scatter(*X.T)
   >>> plt.axis('off')
   >>> plt.show()

Update please

.. plot:: pyplots/vmf_plot.py
