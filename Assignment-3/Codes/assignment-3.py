import numpy as np
def check(arr):
    for i in range(5):
        j=i+1
        while j<5:
            if arr[i]==arr[j]:
                return True
            j+=1
    return False
#atleast 2 chocolates are identical is the converse of no 2 are identical
sample_space=5000000.0
arr=[0,0,0,0,0]
k=0
num=0
while k<sample_space:
    for i in range(5):
        temp=np.random.randint(1,10)
        arr[i]=temp
    if check(arr)==True:
        num+=1
    k+=1

#probability of atleast 2 same chocolates is num/sample_space
probability=float(num/sample_space)
print("The probability is "+ str(probability))