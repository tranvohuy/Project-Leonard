#problem statement: https://projecteuler.net/problem=229
#WARNING: Don't read solution until you try the problem.
#You will lose the joy if you do that.




#nothing to be proud of
#there should be a mathy way to solve
#instead of brute-forcing like this
#hk's solution runs in less than 10 secs

import numpy as np
import time

t = time.time()
N  =2*10**9

bound = N+1
#define a boolean array. Each element is True if it is a^2+b^2.
b2 = np.array(range(1,int((N-1)**0.5)+1))**2
S1 = np.full(bound,False)

for a in range(1,int((N-1)**0.5)+1):
    bbound = int((N-a**2)**0.5)
    a2= a**2
    S1[a2 +b2[:bbound]] = True
print time.time()-t


#define a boolean array. Each element is True if it is a^2 + 2 b^2
S2 = np.full(bound, False)

for a in range(1,int((N-1)**0.5)+1):
    a2= a**2
    bbound =  int(((N-a**2)*0.5)**0.5)
    S2[a2 + 2*b2[:bbound]] = True
print time.time()-t

#logical AND between S1 and S2. Each element is true if it is a^2 + b^2 and 
# is c^2 + 2*d^2
S1 = np.logical_and(S1,S2)
S2[:] = False
for a in range(1,int((N-1)**0.5)+1):
    a2= a**2
    bbound =  int(((N-a**2)/float(3))**0.5)
    S2[a2 + 3*b2[:bbound]] = True
print time.time()-t

S1 = np.logical_and(S1,S2)
S2[:] = False

for a in range(1,int((N-1)**0.5)+1):
    a2= a**2
    bbound =  int(((N-a**2)/float(7))**0.5)
    S2[a2 + 7*b2[:bbound]] = True
S1 = np.logical_and(S1,S2)
  
print len(np.nonzero(S1)[0])
print time.time()-t
