from pymaniprob.probabilitydistributions import MultivariateProbabilityDistribution


"""
Class definitions
"""
class BaseVonMisesFisher(MultivariateProbabilityDistribution):
    def __init__(self, m, k, p):
        pass


class FrozenVonMisesFisher(BaseVonMises):
    def __init__(self, **kwargs):
        super(FrozenVonMisesFisher, self).__init__(**kwargs)


class VonMisesFisher:

    def __new__(self, m=None, k=1, p=2):
        m, k, p = _handle_parameter_specification(m, k, p)
        return FrozenVonMisesFisher(m=m, k=k, p=p)


"""
Utility methods for setting up
"""
def _handle_parameter_specification(m, k, p):
    _norm_tol = 1e-5
    
    if m is None:
        m = np.zeros(p)
        m[0] = 1.
    else:
        m = np.asarray(m)
        try:
            assert( abs(np.linalg.norm(m) - 1.) < _norm_tol)
        except:
            raise ValueError("mean should be a unit vector")
        assert(m.size == p)

    return m, k, p
