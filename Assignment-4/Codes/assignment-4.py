import numpy as np
import random as rd
from scipy.stats import binom
#setting of values
#of n and p
n=4
#here, n=5 because we know that there are already 3 black balls and now we have to have 2 black balls in the other 5 balls with equal probability of having the colour blue or black
p=0.5
#defining the list of r values
r_values=list(range(n+1))
dist=binom.pmf(2,n,p)
print("probability that there are 5 black balls is "+ str(dist))
sample_space=50000
new=0.0
arr=[-1,-1,-1,-1]
for i in range(sample_space):
    count=0
    for k in range(4):
        arr[k]=rd.randint(0,1)
        if(arr[k]==0):
            count+=1
    if count==2:
        new+=1
pr=float(new/sample_space)
print(pr)