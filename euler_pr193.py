#problem statement: https://projecteuler.net/problem=193
#

import numpy as np
import time

t = time.time()
#N=2**50 gives 684465067343069
#2**49 gives 342232533672922
#2**48 gives 171116266836708
#2**40 gives 668422917419  
#2**25 = 33554432
N = 2**50

#an efficient way to sieve primes
bound = long(N**0.5)+1

primality = np.full(bound,True)
primality[0] = False
primality[1] = False

primality[4::2] = False
for i in xrange(3, long(bound ** 0.5)+1, 2):
        if primality[i]:
            primality[i**2::2*i] = False

print("Sieving prime time: " + str(time.time()-t) + "\n")
listprime = np.nonzero(primality)[0]
l = len(listprime)
#DONE sieving primes




#We use inclusion-exclusion principle.
# Num of square frees = N - sum_{x primes} #{n: x**2 divides n}
# + sum_{x, y different primes} #{n: x**2 y**2 divides n} - ...
#this sums stop after 7 primes since
# (2*3*5*7*11*13*17*19) **2 > 2**50
count = N

bound  = N**0.5
bound2 = bound**0.5
bound3 = bound** (1/float(3))
bound4 = bound** 0.25
bound5 = bound** 0.2 #which is 32
bound6 = bound** (1/float(6)) 
bound7 = bound** (1/float(7))

for x in listprime:
    # subtracting the number of n such that x**2 divides n
    # use bound instead of N because of the calculation speed problem
    count -= long((bound/float(x))**2)
    
 
for i1 in xrange(0,l):
    x1 = listprime[i1]
    if x1> bound2:
        break
    for i2 in xrange(i1+1,l):
        x2 = listprime[i2]
        x12 = x1*x2
        if x12>bound:
            break
        
        count += long((bound/float(x12))**2)
    
#688,510,164,099,596 in 34s
#print("Two terms: " + str(count) + " in " + str(time.time()-t))

for i1 in xrange(0,l):
    x1 = listprime[i1]
    if x1> bound3:
        break
    x2bound = bound2/ x1**0.5
    for i2 in xrange(i1+1,l):
        x2 = listprime[i2]
        if x2> x2bound:
            break
        x12 = x1 *x2
        for i3 in xrange(i2+1,l):
            x3 = listprime[i3]
            x123= x12*x3
            if x123> bound:
                break
            
            count -= int((bound/float(x123))**2)
#fact check    
#print("Three terms: " + str(count) + " in " + str(time.time()-t))

for i1 in xrange(0,l):
    x1 = listprime[i1]
    if x1> bound4:
        break
    x2bound = bound3/ x1**(1/float(3))
    for i2 in xrange(i1+1,l):
        x2 = listprime[i2]
        if x2 > x2bound:
            break
        x12 = x1 *x2
        x3bound = bound2/x12**0.5
        for i3 in xrange(i2+1,l):
            x3 = listprime[i3]
            if x3> x3bound:
                break
            x123 = x12 * x3
            for i4 in xrange(i3+1,l):
                x4 = listprime[i4]
                x1234 = x123*x4
                if x1234>bound:
                    break
                count += long((bound/float(x1234))**2)
                
#fact check
#print("Four terms: " + str(count) + " in " + str(time.time()-t))


for i1 in xrange(0,l):
    x1 = listprime[i1]
    if x1> bound5:
        break
    x2bound = bound4/ x1**(1/float(4))
    for i2 in xrange(i1+1,l):
        x2 = listprime[i2]
        if x2 > x2bound:
            break
        x12 = x1 *x2
        x3bound = bound3/x12**(1/float(3))
        for i3 in xrange(i2+1,l):
            x3 = listprime[i3]
            if x3> x3bound:
                break
            x123 = x12 * x3
            x4bound = bound2/x123 **0.5
            for i4 in xrange(i3+1,l):
                x4 = listprime[i4]
                if x4 > x4bound:
                    break
                x1234 = x123*x4
                for i5 in xrange(i4+1, l):
                    x5 = listprime[i5]
                    x12345 = x1234*x5
                    if x12345>bound:
                        break
                    count -= long((bound/float(x12345))**2)
#fact check
#print("Five terms: " + str(count) + " in "+ str(time.time()-t))


for i1 in xrange(0,l):
    x1 = listprime[i1]
    if x1> bound6:
        break
    x2bound = bound5/ x1**(1/float(5))
    for i2 in xrange(i1+1,l):
        x2 = listprime[i2]
        if x2 > x2bound:
            break
        x12 = x1 *x2
        x3bound = bound4/x12**(1/float(4))
        for i3 in xrange(i2+1,l):
            x3 = listprime[i3]
            if x3> x3bound:
                break
            x123 = x12 * x3
            x4bound = bound3/x123 **(1/float(3))
            for i4 in xrange(i3+1,l):
                x4 = listprime[i4]
                if x4 > x4bound:
                    break
                x1234 = x123*x4
                x5bound = bound2/x1234 **(1/float(2))
                for i5 in xrange(i4+1, l):
                    x5 = listprime[i5]
                    if x5>x5bound:
                        break
                    
                    x12345 = x1234*x5
                    x6bound = bound/x12345
                    for i6 in xrange(i5+1, l):
                        x6  = listprime[i6]
                        if x6>x6bound:
                            break
                        x123456=x12345*x6
                        count += long((bound/float(x123456))**2)
#fact check
#684,465,067,437,982 in 99.6s
#print("Six terms: " + str(count) + " in "+ str(time.time()-t))


for i1 in xrange(0,l):
    x1 = listprime[i1]
    if x1> bound7:
        break
    x2bound = bound6/ x1**(1/float(6))
    for i2 in xrange(i1+1,l):
        x2 = listprime[i2]
        if x2 > x2bound:
            break
        x12 = x1 *x2
        x3bound = bound5/x12**(1/float(5))
        for i3 in xrange(i2+1,l):
            x3 = listprime[i3]
            if x3> x3bound:
                break
            x123 = x12 * x3
            x4bound = bound4/x123 **(1/float(4))
            for i4 in xrange(i3+1,l):
                x4 = listprime[i4]
                if x4 > x4bound:
                    break
                x1234 = x123*x4
                x5bound = bound3/x1234 **(1/float(3))
                for i5 in xrange(i4+1, l):
                    x5 = listprime[i5]
                    if x5>x5bound:
                        break
                    x12345 = x1234*x5
                    x6bound = bound2/x12345**(1/float(2))
                    for i6 in xrange(i5+1, l):
                        x6  = listprime[i6]
                        if x6>x6bound:
                            break
                        x123456 = x12345*x6
                        x7bound = bound/x123456
                        for i7 in range(i6+1,l):
                            x7 = listprime[i7]
                            if x7>x7bound:
                                break
                          #  print x1, x2, x3, x4, x5, x6, x7
                            count -= long((bound/float(x123456*x7))**2)
    
#684,465,067,342,977 in 99.6s
#print("Seven terms: " + str(count) + " in "+ str(time.time()-t))

x1 = 2
x2 = 3
i2 = 1
x12 = x1 *x2
x3bound = bound6/x12**(1/float(6))
for i3 in xrange(i2+1,l):
    x3 = listprime[i3]
    if x3> x3bound:
        break
    x123 = x12 * x3
    x4bound = bound5/x123 **(1/float(5))
    for i4 in xrange(i3+1,l):
        x4 = listprime[i4]
        if x4 > x4bound:
            break
        x1234 = x123*x4
        x5bound = bound4/x1234 **(1/float(4))
        for i5 in xrange(i4+1, l):
            x5 = listprime[i5]
            if x5>x5bound:
                break
            x12345 = x1234*x5
            x6bound = bound3/x12345**(1/float(3))
            for i6 in xrange(i5+1, l):
                x6  = listprime[i6]
                if x6>x6bound:
                    break
                x123456 = x12345*x6
                x7bound = bound2/x123456**(1/float(2))
                for i7 in range(i6+1,l):
                    x7 = listprime[i7]
                    if x7>x7bound:
                        break
                    x1234567 = x123456*x7
                    x8bound = bound/x1234567
                    for i8 in range(i7+1,l):
                        x8 = listprime[i8]
                        if x8>x8bound:
                            break
                        count += long((bound/float(x1234567*x8))**2)
##fact check
#print("Eight terms: " + str(count) + " in "+ str(time.time()-t))


print ("The number of free square that is less than " + str(N) + " is " + str(count))
print ("Calculation time " + str(time.time()-t))

#one can use Mobius function. But that's boring.
#all solutions use inclusion-exclusion principle
