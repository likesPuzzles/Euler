from math import sqrt

"""K= # being tested to see if it is prime"""
K=11;
limit = sqrt(K);    #limit = Highest potential factor you need to test
j=2;                #j = potential factor
for (j in range(limit)):
    if (K%j==0):    #K is divisible by j)
        print ("K is not prime. " + str(j) + "is a factor")   
    elif (K%j !=0): #K is ot divisisble by j
        j=j+1  
print ("prime");
