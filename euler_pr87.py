#problem statement: https://projecteuler.net/problem=87
#DISCLAIMER: don't read the solution until you try the problem.
#you will lose the joy if doing that.

import time
import math

t = time.time()

#an efficient way to sieve primes 
bound1 = 50000000
p4 = int(math.pow(bound1,0.25))
p2 = int(math.sqrt(bound1))
p3 = int(math.pow(bound1, 1/float(3)))

bound = p2
prime_list = [True] * bound
prime_list[0] = False
prime_list[1] = False
for i in range(2, int(bound ** 0.5)):
        if prime_list[i]:
            for j in range(i ** 2, bound, i):
                prime_list[j] = False

listprime2 = [k for k, v in enumerate(prime_list) if v]

listprime4 = [k for k in listprime2 if k <= p4]
#done sieving primes

#construct the set of prime power triples
S = set()

for x in listprime4:
    x4 = x**4
    temp1 = bound1 - x4
    
    listprime3 = [k for k in listprime2 if k<=int(math.pow(temp1, 1/float(3)))]
    for y in listprime3:
        y3 = y**3
        temp2 = temp1 - y3
        listprime21 = [k for k in listprime2 if k<=int(math.sqrt(temp2))]
        for z in listprime21:
            S.add(x4 + y3 + z**2)
    
print len(S)
print("Time: " + str(time.time()-t) + "\n")
