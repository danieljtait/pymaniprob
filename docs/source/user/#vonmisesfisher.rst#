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


.. plot::

    >>> import numpy as np
    >>> import matplotlib.pyplot as plt
    >>> # Build a vector of 10000 normal deviates with variance 0.5^2 and mean 2
    >>> mu, sigma = 2, 0.5
    >>> v = np.random.normal(mu,sigma,10000)
    >>> # Plot a normalized histogram with 50 bins
    >>> plt.hist(v, bins=50, density=1)       # matplotlib version (plot)
    >>> plt.show()
    >>> # Compute the histogram with numpy and then plot it
    >>> (n, bins) = np.histogram(v, bins=50, density=True)  # NumPy version (no plot)
    >>> plt.plot(.5*(bins[1:]+bins[:-1]), n)
    >>> plt.show()
