num = 10

for i in range(2,num):
    if num%i == 0:
        print("Not prime")
        break
#control will come to else block when no condition matched in the if statement
else:
    print("Prime")


# Python Program to find prime numbers in a range 
import math 
import time 
def is_prime(n): 
    if n <= 1: 
        return False
  
    max_div = math.floor(math.sqrt(n)) 
    for i in range(2, 1 + max_div): 
        if n % i == 0: 
            return False
    return True
  
# Driver function 
t0 = time.time() 
c = 0 #for counting 
  
for n in range(1,100000): 
    x = is_prime(n)
    c += x
print("Total prime numbers in range :", c) 
  
t1 = time.time() 
print("Time required :", t1 - t0) 

# Python Program to find prime numbers in a range 
import math 
import time 
def is_prime(n): 
    if n <= 1: 
        return False
    if n == 2: 
        return True
    if n > 2 and n % 2 == 0: 
        return False
  
    max_div = math.floor(math.sqrt(n)) 
    for i in range(3, 1 + max_div, 2): #skipping the even numbers in the loop
        if n % i == 0: 
            return False
    return True
  
# Driver function 
t0 = time.time() 
c = 0 #for counting 
  
for n in range(1,100000): 
    x = is_prime(n) 
    c += x 
print("Total prime numbers in range :", c) 
  
t1 = time.time() 
print("Time required :", t1 - t0) 

# Seive method for finding a prime number in a range

# Python Program to find prime numbers in a range 
import time 
def SieveOfEratosthenes(n): 
       
    # Create a boolean array "prime[0..n]" and  
    # initialize all entries it as true. A value  
    # in prime[i] will finally be false if i is 
    # Not a prime, else true. 
    prime = [True for i in range(n+1)] 
      
    p = 2
    while(p * p <= n): 
           
        # If prime[p] is not changed, then it is  
       # a prime 
        if (prime[p] == True): 
               
            # Update all multiples of p 
            for i in range(p * 2, n + 1, p): 
                prime[i] = False
        p += 1
    c = 0
  
    # Print all prime numbers 
    for p in range(2, n): 
        if prime[p]: 
            c += 1
    return c 
  
# Driver function 
t0 = time.time() 
c = SieveOfEratosthenes(100000) 
print("Total prime numbers in range:", c) 
  
t1 = time.time() 
print("Time required:", t1 - t0) 
