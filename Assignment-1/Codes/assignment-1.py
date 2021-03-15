import random as rd

sample_data=500000

bag=[-1,-1,-1,-1,-1,-1,-1,-1]
i=0
while i<3:
    temp=rd.randint(0,7)
    if(bag[temp]==-1):
        bag[temp]=0
        i+=1
i=0
while i<5:
    temp=rd.randint(0,7)
    if(bag[temp]==-1):
        bag[temp]=1
        i+=1
red=0
#0 is for red
#1 is for black
i=0
for i in range(sample_data):
    temp=rd.randint(0,7)
    if(bag[temp]==0):
        red+=1
prob_red=red / sample_data

print("The results from stimulations:")
print("The probability that the taken ball is red is {}" .format(prob_red))
print("The probability that the taken ball is not red is {}".format(1-prob_red))
print()
print("The results obtained theoretically :")
print("The probability that the taken ball is red is 0.375")
print("The probability that the taken ball is not red is 0.625")
print()
print("The errors while calculating the probabilities:")
print("The absolute error in calculating probability that the ball taken out is red is {}".format(abs(0.375-prob_red)))
print("The absolute error in calculating probability that the ball taken out is not red is {}".format(abs(0.625-1+prob_red)))
