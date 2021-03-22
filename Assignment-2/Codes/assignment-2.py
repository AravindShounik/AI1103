import numpy as np
import random as rd
from scipy.stats import binom
#setting of values
#of n and p
n=10
p=0.6
#defining the list of r values
r_values=list(range(n+1))
dist=binom.pmf(6,n,p)
print("probability that there are 6 free throws is "+ str(dist))