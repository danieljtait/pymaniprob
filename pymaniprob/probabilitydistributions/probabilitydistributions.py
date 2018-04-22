"""
Definition of the base classes

- ProbabilityDistribution
- MultivariateProbabilityDistribution

"""


class ProbabilityDistribution:
    def __init__(self, **kwargs):

        for key, item in kwargs.items():
            setattr(self, key, item)

        # logical for if the pdf behaves like a numpy
        # ufunc
        self._pdf_is_vec = False


    def pdf(self, x, **kwargs):
        try:
            return self._pdf(x, **kwargs)
        except:
            # ToDo - Catch that properly 
            raise NotImplementedError


class MultivariateProbabilityDistribution(ProbabilityDistribution):
    def __init__(self, dim=1, **kwargs):
        # dimension of the embedding space
        self.dim = dim
        self.is_vectorised = False

        super(MultivariateProbabilityDistribution, self).__init__(**kwargs)


    def pdf(self, x):
        return _handle_muldim_input(x, self._pdf, self.dim, self._pdf_is_vec)
            

    def logpdf(self, x):
        if hasattr(self, '_logpdf'):
            return _handle_muldim_input(x, self._logpdf, self.dim, self._pdf_is_vec)
        else:
            return np.log(self.pdf(x))
