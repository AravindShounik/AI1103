from scipy.stats import rv_discrete
import numpy as np
xk = (1,2,3)
pk = (0.3,0.6,0.1)
custm = rv_discrete(name='custm', values=(xk, pk))
variance=rv_discrete.var(custm)
print("The variance of the given discrete random variable is "+ str(variance))
print("The theoretical variance of the discrete random variable is 0.36")