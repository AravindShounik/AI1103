import numpy as np
import random as rd
from scipy.stats import binom
sample_space=50000
def check(arr):
    for i in range(5):
        j=i+1
        while j<5:
            if arr[i]==arr[j]:
                return True
            j+=1
    return False
arr=[-1,-1,-1,-1,-1]
num=0.0

for i in range(sample_space):
    for j in range(5):
        arr[j]=rd.randint(1,10)
    if check(arr)==True:
        num+=1
pr=num/sample_space
print("The probability that there are atleast 2 same type of chocolates is "+str(pr))
