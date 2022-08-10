#def my_function(prime) 
from math import sqrt

#Find 10001st prime;
#Euler 7
#Prime is Boolean variable.  If Prime is False, the number is not prime
#find_Prime is a function that tests for prime.  It passes,(N and Prime) 
#N is the number being tested
#N_Primes is the number of primes found

  #main body of code      
           
N_Primes=2      #start at 4 because my code does not work with 2 and 3
N=4
Prime = False



def find_Prime (N,Prime):     # function to deterine if N is Prime.  Returns Boolean value Prime=True is N is Prime
    limit=sqrt(N)               #Max value that needs to be tested as a factor
    limit=int(limit)+1          # wild guess
    j=2
    
    for j in range (2,limit):
        if (N%j==0 and j!=N):
            Prime = False
            return Prime
        else:
             Prime=True
    print ( N, j, Prime, limit)  #Print to see that all variables are as intended.  Looks good. 
    return Prime  



for N_Primes in range(0,25):
    print (N_Primes)
    find_Prime (N, Prime)   #call function
    print(Prime)            #this statement does not print if Prime is true
    if Prime:
        print(N_Primes, "is number of primes")
        N_Primes=N_Primes+1
        
    N=N+1                   # this statment executes












