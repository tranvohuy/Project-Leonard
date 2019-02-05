#problem statement: https://projecteuler.net/problem=269
#DISCLAIMER: don't read the solution before trying the problem
#553 people solved it as of Jan 2019.





import os
clear = lambda: os.system('cls') #on Windows System
clear()

import time
import numpy as np

start_time = time.time()


# idea: 16 = (4+4) + (4+4)
# polynomial of degree 16 is the sum of two different polynomials.
# their values have to be mached nicely such that their sum is zero.
# compute possible values of these polynomials
# There are overlapses of cases since 6 = 2 *3, 4= 2*2 = 4*1, 9=3*3 = 9*1,etc
# have to use inclusion-exclusion principle.


##################
# global variables
p = 4
p2 = 2*p
bound1 = 10**p
count = 10**(4*p-1)
dvp = [None] * 10
dvpnot = [None] * 10
bound_sml = [0, 0, 6, 5, 4, 2, 2, 2, 2, 2]
for k in range(0,10):
    dvp[k] = {}
    dvpnot[k] = {}
    
P = np.zeros((bound1,10))


##############################

dv8 = [None] * 10
for k in range(0,10):
    dv8[k] = {}

####################################

def initialize_all_vp():
    v = np.zeros((1,10))
    Pk = np.zeros((p, 10))
    for i in xrange(0, p):
        for k in xrange(0,10):
            Pk[i,k] = (-k)**i
    for n in range(0, bound1):
        s = str(n)
        l = len(s)
        for i in range(0,p-l):
            s = '0' + s
        v = np.array([int(x) for x in s])
        P[n, :] = np.dot(v, Pk)
        v = P[n, :]
        for k in xrange(1,10):
            if v[k] not in dvp[k]:
                dvp[k][v[k]] = 1
            else:
                dvp[k][v[k]] +=1
            if v[0]!=0:
                if v[k] not in dvpnot[k] and v[0]!=0:
                    dvpnot[k][v[k]] = 1
                else:
                    dvpnot[k][v[k]] +=1    

#    for a in xrange(0,10):
#        for b in xrange(0,10):
#            for c in xrange(0,10):
#                for d in xrange(0,10):
#                    abcd = a*1000 + b*100 + c*10 + d
#                    P[abcd, :] = np.dot(np.array([d, c, b, a]),Pk)
#                    v  = P[abcd, :]
#                    for k in xrange(1,10):
#                        if v[k] not in dvp[k]:
#                            dvp[k][v[k]] = 1
#                        else:
#                            dvp[k][v[k]] +=1
#                        if v[0]!=0:
#                            if v[k] not in dvpnot[k] and v[0]!=0:
#                                dvpnot[k][v[k]] = 1
#                            else:
#                                dvpnot[k][v[k]] +=1    
#    
  
##################################
def data_structure1():
    global count
    # compute dv8[1], containing all values v such that P(abcdefgh,1)=v
    # and how many such abcdefgh.
    # P(abcdefgh,1)= v if P(abcd,1) + P(efgh,1)=v
    for v1 in dvp[1]:
        for v2 in dvp[1]:
            if v1 + v2 not in dv8[1]:
                dv8[1][v1+v2] = dvp[1][v1] * dvp[1][v2]
            else:
                dv8[1][v1+v2] += dvp[1][v1] * dvp[1][v2]
    # compute dv8not0, containing all values v such that P(abcdefgh,1)=v
    # and P(...,0) !=0 i.e. h !=0
    # That leads to compute dvpnot[1]
  
    # compute dv8not0, all values v s.t. there is A8: P(A8,1 ) =v
    # and P(A8,0)!=0
    # A8 = AB
    # P(A)+ P(B) = v and P(B)!=0
    dv8not  = {}
    for v1 in dvp[1]:
        for v2 in dvpnot[1]:
            if v1 + v2 not in dv8not:
                dv8not[v1 + v2] = dvp[1][v1] * dvpnot[1][v2]
            else:
                dv8not[v1 + v2] += dvp[1][v1] * dvpnot[1][v2]
                
    ####
    # Now count the number of good A16 = abcdefgh such that P(A16,1)=0 but
    # P(A16,0) != 0
    # Note that A8 = AB where A,B are 8-digit numbers.
    # So P(A) =- P(B) and P(B)!=0
    #
    count += sum (dv8[1][v] * dv8not[-v] for v in dv8[1] if -v in dv8not)
       
##################################
#
#
#
#
def data_structure2():
    global count
    ##compute dv8[2], containing all v such that P(A8,2) = v
    # A8 = A + B so P(A,2)*2**4 + P(B,2) = v
    # for v in dv8[2], we only care those |v|<6 and w = -2**8 *v
    pos_dv8_sml = range(-5,6)
    pos_dv8_big = [-2**p2 * v for v in pos_dv8_sml]
    pairp = {}
    # contains pairs (v1, v2) such that 2**4 *v1 + v2 in pos_dv8_sml
    # number of such pairs is much smaller than len(dvp[2])**2, save a lot of calculation
    for v1 in dvp[2]:
        for v2 in dvp[2]:
            if 2**p * v1 + v2 in pos_dv8_sml:
                pairp[(v1, v2)] = True
                temp = 2**p * v1 + v2
                if temp not in dv8[2]:
                    dv8[2][temp] = dvp[2][v1] * dvp[2][v2]
                else:
                    dv8[2][temp] += dvp[2][v1] * dvp[2][v2]
    # compute dv8not from dvpnot[2]
    # compute dv8not, all values v s.t. there is A8: P(A8,1 ) = v
    # and P(A8,0)!=0
    # A8 = AB
    # P(A)+ P(B) = v and P(B)!=0
    # only care v in pos_dv8_big
    dv8not  = {}
    pairpnot = {}
    for v1 in dvp[2]:
        for v2 in dvpnot[2]:
            if 2**p * v1 + v2 in pos_dv8_big:
                pairpnot[(v1, v2)] = True
                temp = 2**p * v1 + v2
                if temp not in dv8not:
                    dv8not[temp] = dvp[2][v1] * dvpnot[2][v2]
                else:
                    dv8not[temp] += dvp[2][v1] * dvpnot[2][v2]
    # this pair8 contains (v1, v2) such that there are 8-digit A and B s.t. P(A,2)=v1, P(B,2) = v2
    # and v1* 2** 8+ v2 = 0
    # v2 has to be in dv8not, that is P(B,0)!=0
    # |v1| <6, so there are at most 11 pairs.
    pair8 = {}
    pos_dv8_sml = [] # we also update pos_dv8_sml (saving some calculations later)
    pos_dv8_big = []
    for v1 in dv8[2]: #expect abs(v1) < 6, v1 in pos_dv8_sml
        if -2**p2 * v1 in dv8not: #expect  in pos_dv8_sml. So there is no repeat
            temp = -2**p2 * v1
            pos_dv8_sml.append(v1)
            pos_dv8_big.append(temp)
            pair8[(v1, temp)] = dv8[2][v1] * dv8not[temp]
    # update back pairp
    pairp_update = {}
    for (v1, v2) in pairp:
        if 2**p *v1 + v2 in pos_dv8_sml:
            pairp_update[(v1, v2)] = True
    # update back pairpnot_update
    pairpnot_update = {}
    for (v1, v2) in pairpnot:
        if 2**p *v1 + v2 in pos_dv8_big:
            pairpnot_update[(v1, v2)] = True
    # create val = pos_dv8_sml (almost = dv8[2]) and valnot = dv8not
    # but val[v] contains P(A8,1) for all A such that P(A8,2) = v
    # to do this, have to find valp and valpnot
    # val and valnot have more details than dv8[2] and dv8not
    # valp and valpnot have more details than dvp[2] and dvpnot[2]
    valp = {}
    for v in dvp[2]:
        valp[v] = {}
    valpnot = {}
    for v in dvpnot[2]:
        valpnot[v] = {}

    for n in range(0, bound1):
        if P[n,1] not in valp[P[n,2]]:
            valp[P[n,2]][P[n,1]] = 1
        else:
            valp[P[n,2]][P[n,1]] += 1
        if P[n, 0]!=0:
            if P[n,1] not in valpnot[P[n,2]]:
                valpnot[P[n,2]][P[n,1]] = 1
            else:
                valpnot[P[n,2]][P[n,1]] += 1            
    # use valp and valpnot to construct val and valnot
    # val = pos_dv8_sml (almost = dv8[2])
    # and valnot = pos_dv8_big (almost  = dv8not[2])
    # val and valnot have more details than dv8[2] and dv8not[2]
    # val[v] is a list of P(A8,1) with P(A8,2) = v.
    # Has to use valp
    val = {}
    valnot = {}
    for v in pos_dv8_sml:
        val[v] = {}
        valnot [-2**p2 *v] = {}
    #
    for (v1, v2) in pairp_update: # this pair combines to give pos_dv8_sml 
        temp = 2**p * v1 + v2 # surely in pos_dv8_sml_update
        # val[temp] contains w = P(A4,1) + P(B4,1) where P(A4,2) = v1, P(B4,2) = v2
        # so P(A4,1) is in valp[v1]
        for a in valp[v1]:
            for b in valp[v2]:
                w = a + b
                if w not in val[temp]:
                    val[temp][w] = valp[v1][a] * valp[v2][b]
                else:
                    val[temp][w] += valp[v1][a] * valp[v2][b]
           
    # now compute valnot, a bit more complicated, but almost same as above
    # again valnot[v] contains a list of w where P(B8,2) =v, P(B8,1) = w, and count
    for (v1, v2) in pairpnot_update:
        temp = 2**p * v1 + v2 # surely in pos_dv8_big_update
        # val[temp] contains w = P(A4,1) + P(B4,1) where P(A4,2) = v1, P(B4,2) = v2
        # so P(A4,1) is in valp[v1]
        for a in valp[v1]:
            for b in valpnot[v2]:
                w = a + b
                if w not in valnot[temp]:
                    valnot[temp][w] = valp[v1][a] * valpnot[v2][b]
                else:
                    valnot[temp][w] += valp[v1][a] * valpnot[v2][b]
    # 
    #
    #
   
  
    #count the number of good A16 = abcdefgh such that P(A16,2)=0 but
    # P(A16,1) != 0 and P(A16)!=0
    # Note that A8 = AB where A,B are 8-digit numbers.
    # So 2**8 P(A,2) =- P(B,2),
    # P(A,1)!= - P(B,1)
    # P(B,0)!=0
    #

    #dv8[2][v1] contains number of A8 such that P(A8, 2) = v1
    for (v1, v2) in pair8:
        count += pair8[(v1, v2)]
        ## subtract extra terms
        count -= sum( val[v1][w] *valnot[v2][-w] for w in val[v1] if -w in valnot[v2])
        ## subtract AB where P(A,1) = w = - P(B,1) and P(B,1)!=0
        ## val[v1] lists  all w s.t there is A: P(A,1) = w, P(A,2)= v1
        ## val[v1][w] counts number of such A
        ## valnot[v2] lists all w s.t. there is B: P(B,1) =w, P(B,2) = v2 and P(B,0) != 0
        ## valnot[v2][w] counts number of such B
        ## the answer is symmetric if one switch to "w in valnot[v2] if -w in val[v1]

        
#########################################
# P[n,3], P[n, 5], P[n, 7] are similar to P[n,2]. Since 2, 3, 5, and 7 are primes
# Just copied the code and changes appripriately. Mostly the range for pos_dv8_sml

def data_structure2357(k): #k=2, 3, 5, or 7
    global count
    pos_dv8_sml = [v for v in range(-10,10) if abs(v)<bound_sml[k]]
##    if k == 2:
##        pos_dv8_sml = range(-5,6)
##    elif k==3:
##        pos_dv8_sml = range(-3,4)
##    elif k==5 or k ==7:
##        pos_dv8_sml = [-1, 0, 1]
    pos_dv8_big = [-k**p2 * v for v in pos_dv8_sml]
    ## for k from 2 up, dvp[k] has  a lot of elements
    ## we only care specials dvp[k] (in pairp_update and pairpnot_update)
    dvpsml = [v for v in dvp[k] if abs(v)< bound_sml[k]]

    pairp = {}
    for v1 in dvpsml:
        for v2 in dvp[k]:
            if (-k)**p * v1 + v2 in pos_dv8_sml:
                pairp[(v1, v2)] = True
                temp = (-k)**p * v1 + v2
                if temp not in dv8[k]:
                    dv8[k][temp] = dvp[k][v1] * dvp[k][v2]
                else:
                    dv8[k][temp] += dvp[k][v1] * dvp[k][v2]

    dv8not  = {}
    ## we only care specials dvp[k] (in pairp_update and pairpnot_update)
    dvpbig = [v for v in dvpnot[k] if v% k**p==0]

    pairpnot = {}
    for v1 in dvp[k]:   
        for v2 in dvpbig:
            if (-k)**p * v1 + v2 in pos_dv8_big:
                ## here we see that v2 has to be divisible by k**4
                pairpnot[(v1, v2)] = True
                temp = (-k)**p * v1 + v2
                if temp not in dv8not:
                    dv8not[temp] = dvp[k][v1] * dvpnot[k][v2]
                else:
                    dv8not[temp] += dvp[k][v1] * dvpnot[k][v2]
    ######################################
    pair8 = {}
    pos_dv8_sml = [] # we also update pos_dv8_sml (saving some calculations later)
    pos_dv8_big = []
    for v1 in dv8[k]: #expect abs(v1) < 6, < 4, <1, or <1 depending k = 2, 3, 5, or 7, v1 in pos_dv8_sml
        if -k**p2 * v1 in dv8not: #expect  in pos_dv8_sml. So there is no repeat
            temp = -k**p2 * v1
            pos_dv8_sml.append(v1)
            pos_dv8_big.append(temp)
            pair8[(v1, temp)] = dv8[k][v1] * dv8not[temp]
    # update back pairp
    pairp_update = {}
    for (v1, v2) in pairp:
        if (-k)**p *v1 + v2 in pos_dv8_sml:
            pairp_update[(v1, v2)] = True
    # update back pairpnot_update
    pairpnot_update = {}
    for (v1, v2) in pairpnot:
        if (-k)**p *v1 + v2 in pos_dv8_big:
            pairpnot_update[(v1, v2)] = True
   
    valp = {}
    for v in dvp[k]:
        valp[v] = {}
    valpnot = {}
    for v in dvpnot[k]:
        valpnot[v] = {}

    for n in range(0,bound1):
        if P[n,1] not in valp[P[n,k]]:
            valp[P[n, k]][P[n,1]] = 1
        else:
            valp[P[n, k]][P[n,1]] += 1
        if P[n, 0]!=0:
            if P[n,1] not in valpnot[P[n, k]]:
                valpnot[P[n, k]][P[n,1]] = 1
            else:
                valpnot[P[n, k]][P[n,1]] += 1            
    val = {}
    valnot = {}
    for v in pos_dv8_sml:
        val[v] = {}
        valnot [-k**p2 *v] = {}
    #
    for (v1, v2) in pairp_update: 
        temp = (-k)**p * v1 + v2
        for a in valp[v1]:
            for b in valp[v2]:
                w = a + b
                if w not in val[temp]:
                    val[temp][w] = valp[v1][a] * valp[v2][b]
                else:
                    val[temp][w] += valp[v1][a] * valp[v2][b]
           
    for (v1, v2) in pairpnot_update:
        temp = (-k)**p * v1 + v2
        for a in valp[v1]:
            for b in valpnot[v2]:
                w = a + b
                if w not in valnot[temp]:
                    valnot[temp][w] = valp[v1][a] * valpnot[v2][b]
                else:
                    valnot[temp][w] += valp[v1][a] * valpnot[v2][b]
  
  
    for (v1, v2) in pair8:
        count += pair8[(v1, v2)]
        ## subtract extra terms
        
        count -= sum( val[v1][-w] *valnot[v2][w] for w in valnot[v2] if -w in val[v1])
        # 
####################################
# very similar to data_structure2
# read more commments in that function
#
#
#
############################################3
def data_structure49(k): #k = 4, or 9, or even 3
    global count
    pos_dv8_sml = [v for v in range(-10,10) if abs(v)<bound_sml[k]]
    if k== 2:
        [k1, k2] = [1, 3]
    if k == 3: # in this case 3 has to run after 2
        [k1, k2] = [1, 2]
    if k == 4:
        [k1, k2] = [1, 2]  #other two divisors of 4
    elif k  == 9:
        [k1, k2] = [1, 3]

    pos_dv8_big = [-k**p2 * v for v in pos_dv8_sml]
    pairp = {}
    dvpsml = [v for v in dvp[k] if abs(v)< bound_sml[k]]
    
    for v1 in dvpsml:
        for v2 in dvp[k]:
            if (-k)**p * v1 + v2 in pos_dv8_sml:
                pairp[(v1, v2)] = True
                temp = (-k)**p * v1 + v2
                if temp not in dv8[k]:
                    dv8[k][temp] = dvp[k][v1] * dvp[k][v2]
                else:
                    dv8[k][temp] += dvp[k][v1] * dvp[k][v2]
    dv8not  = {}
    pairpnot = {}
    dvpbig = [v for v in dvpnot[k] if v% k**p==0]

    for v1 in dvp[k]:
        for v2 in dvpbig:
            if (-k)**p * v1 + v2 in pos_dv8_big:
                pairpnot[(v1, v2)] = True
                temp = (-k)**p * v1 + v2
                if temp not in dv8not:
                    dv8not[temp] = dvp[k][v1] * dvpnot[k][v2]
                else:
                    dv8not[temp] += dvp[k][v1] * dvpnot[k][v2]

    ######################################
    pair8 = {}
    pos_dv8_sml = [] # we also update pos_dv8_sml (saving some calculations later)
    pos_dv8_big = []
    for v1 in dv8[k]: #expect abs(v1) < 6, < 4, <1, or <1 depending k = 2, 3, 5, or 7, v1 in pos_dv8_sml
        if -k**p2 * v1 in dv8not: #expect  in pos_dv8_sml. So there is no repeat
            temp = -k**p2 * v1
            pos_dv8_sml.append(v1)
            pos_dv8_big.append(temp)
            pair8[(v1, temp)] = dv8[k][v1] * dv8not[temp]
    #

    
    # update back pairp
    pairp_update = {}
    for (v1, v2) in pairp:
        if (-k)**p *v1 + v2 in pos_dv8_sml:
            pairp_update[(v1, v2)] = True
    # update back pairpnot_update
    pairpnot_update = {}
    for (v1, v2) in pairpnot:
        if (-k)**p *v1 + v2 in pos_dv8_big:
            pairpnot_update[(v1, v2)] = True
   
    valp = {}
    for v in dvp[k]:
        valp[v] = {}
    valpnot = {}
    for v in dvpnot[k]:
        valpnot[v] = {}
    ####
    #
    # one of the differences of k
    # depending on how many divisors of k
    # difference between {4, 9} and {2, 3, 5, 7}
    for n in range(0, bound1):
        if (P[n,k1], P[n, k2]) not in valp[P[n,k]]:
            valp[P[n, k]][(P[n,k1], P[n,k2])] = 1
        else:
            valp[P[n, k]][(P[n,k1], P[n,k2])] += 1
        if P[n, 0]!=0:
            if (P[n,k1], P[n,k2]) not in valpnot[P[n, k]]:
                valpnot[P[n, k]][(P[n,k1], P[n,k2])] = 1
            else:
                valpnot[P[n, k]][(P[n,k1], P[n,k2])] += 1            
    val = {}
    valnot = {}
    for v in pos_dv8_sml:
        val[v] = {}
        valnot [-k**p2 *v] = {}
    #
    #difference between {4, 9} and {2, 3, 5, 7}
    for (v1, v2) in pairp_update: 
        temp = (-k)**p * v1 + v2
        for (a1, a2) in valp[v1]:
            for (b1, b2) in valp[v2]:
                w = (a1* k1**p + b1, a2* k2**p + b2)
                if w not in val[temp]:
                    val[temp][w] = valp[v1][(a1, a2)] * valp[v2][(b1, b2)]
                else:
                    val[temp][w] += valp[v1][(a1, a2)] * valp[v2][(b1, b2)]
           
    for (v1, v2) in pairpnot_update:
        temp = (-k)**p * v1 + v2
        for (a1, a2) in valp[v1]:
            for (b1, b2) in valpnot[v2]:
                w = (a1* k1**p + b1, a2* k2**p + b2)
                if w not in valnot[temp]:
                    valnot[temp][w] = valp[v1][(a1, a2)] * valpnot[v2][(b1, b2)]
                else:
                    valnot[temp][w] += valp[v1][(a1, a2)] * valpnot[v2][(b1, b2)]
  
  
    for (v1, v2) in pair8:
        for (w1, w2) in val[v1]:
            for (wt1, wt2) in valnot[v2]:
                if k1 **p2 * w1 + wt1 !=0 and k2**p2 * w2 + wt2 !=0:
                    count += val[v1][(w1, w2)]*valnot[v2][(wt1, wt2)]


############################################################
def data_structure68(k): #k = 6 or 8. They have 4 divisors
    global count
    pos_dv8_sml = [v for v in range(-10,10) if abs(v)<bound_sml[k]]

    if k == 6:
        [k1, k2, k3] = [1, 2, 3]  #other two divisors of 4
    elif k  == 8:
        [k1, k2, k3] = [1, 2, 4]

    pos_dv8_big = [-k**p2 * v for v in pos_dv8_sml]
    pairp = {}
    dvpsml = [v for v in dvp[k] if abs(v)< bound_sml[k]]
    
    for v1 in dvpsml:
        for v2 in dvp[k]:
            if (-k)**p * v1 + v2 in pos_dv8_sml:
                pairp[(v1, v2)] = True
                temp = (-k)**p * v1 + v2
                if temp not in dv8[k]:
                    dv8[k][temp] = dvp[k][v1] * dvp[k][v2]
                else:
                    dv8[k][temp] += dvp[k][v1] * dvp[k][v2]
    dv8not  = {}
    pairpnot = {}
    dvpbig = [v for v in dvpnot[k] if v% k**p==0]

    for v1 in dvp[k]:
        for v2 in dvpbig:
            if (-k)**p * v1 + v2 in pos_dv8_big:
                pairpnot[(v1, v2)] = True
                temp = (-k)**p * v1 + v2
                if temp not in dv8not:
                    dv8not[temp] = dvp[k][v1] * dvpnot[k][v2]
                else:
                    dv8not[temp] += dvp[k][v1] * dvpnot[k][v2]
    ######################################
    pair8 = {}
    pos_dv8_sml = [] 
    pos_dv8_big = []
    for v1 in dv8[k]: 
        if -k**p2 * v1 in dv8not:
            temp = -k**p2 * v1
            pos_dv8_sml.append(v1)
            pos_dv8_big.append(temp)
            pair8[(v1, temp)] = dv8[k][v1] * dv8not[temp]

    
    # update back pairp
    pairp_update = {}
    for (v1, v2) in pairp:
        if (-k)**p *v1 + v2 in pos_dv8_sml:
            pairp_update[(v1, v2)] = True
    # update back pairpnot_update
    pairpnot_update = {}
    for (v1, v2) in pairpnot:
        if (-k)**p *v1 + v2 in pos_dv8_big:
            pairpnot_update[(v1, v2)] = True

    valp = {}
    for v in dvp[k]:
        valp[v] = {}
    valpnot = {}
    for v in dvpnot[k]:
        valpnot[v] = {}
    ####
    #
    # one of the differences of k
    # depending on how many divisors of k
    # difference among {6, 8}, {4, 9}, and {2, 3, 5, 7}
    for n in range(0, bound1):
        if (P[n,k1], P[n, k2], P[n, k3]) not in valp[P[n,k]]:
            valp[P[n, k]][(P[n, k1], P[n, k2], P[n, k3])] = 1
        else:
            valp[P[n, k]][(P[n, k1], P[n, k2], P[n, k3])] += 1
        if P[n, 0]!=0:
            if (P[n,k1], P[n,k2], P[n, k3]) not in valpnot[P[n, k]]:
                valpnot[P[n, k]][(P[n, k1], P[n, k2], P[n, k3])] = 1
            else:
                valpnot[P[n, k]][(P[n, k1], P[n, k2], P[n, k3])] += 1            
    val = {}
    valnot = {}
    for v in pos_dv8_sml:
        val[v] = {}
        valnot [-k**p2 *v] = {}
    #
    #difference among {6, 8}, {4, 9}, and {2, 3, 5, 7}
    for (v1, v2) in pairp_update: 
        temp = (-k)**p * v1 + v2
        for (a1, a2, a3) in valp[v1]:
            for (b1, b2, b3) in valp[v2]:
                w = (a1 * k1**p + b1, a2 * k2**p + b1, a3 * k3**p + b3)
                if w not in val[temp]:
                    val[temp][w] = valp[v1][(a1, a2, a3)] \
                                              * valp[v2][(b1, b2, b3)]
                else:
                    val[temp][w] += valp[v1][(a1, a2, a3)] \
                                               * valp[v2][(b1, b2, b3)]
           
    for (v1, v2) in pairpnot_update:
        temp = (-k)**p * v1 + v2
        for (a1, a2, a3) in valp[v1]:
            for (b1, b2, b3) in valpnot[v2]:
                w = (a1* k1**p + b1, a2* k2**p + b2, a3 * k3**p + b3)
                if w not in valnot[temp]:
                    valnot[temp][w] = valp[v1][(a1, a2, a3)] \
                                      * valpnot[v2][(b1, b2, b3)]
                else:
                    valnot[temp][w] += valp[v1][(a1, a2, a3)] \
                                       * valpnot[v2][(b1, b2, b3)]
  
  
    for (v1, v2) in pair8:
      for (w1, w2, w3) in val[v1]:
            for (wt1, wt2, wt3) in valnot[v2]:
                if k1 **p2 * w1 + wt1 !=0 and k2**p2 * w2 + wt2 !=0\
                   and k3**p2 * w3 + wt3 !=0:
                    count += val[v1][(w1,w2, w3)]*valnot[v2][(wt1, wt2, wt3)]
       

######################################
#        
### Main
initialize_all_vp()
print "Time to prepare data: {}s".format(time.time() - start_time)

data_structure1()
print "Up to 1:", count
print "Time running so far: {}s".format(time.time() - start_time)


data_structure2357(2)

print "Up to 2:", count
print "Time running so far: {}s".format(time.time() - start_time)

data_structure49(3)
#
#print "Up to 3:", count
#print "Time running so far: {}s".format(time.time() - start_time)
#
data_structure49(4)
#print "Up to 4:", count
#print "Time running so far: {}s".format(time.time() - start_time)
#
data_structure2357(5)
#print "Up to 5:", count
#print "Time running so far: {}s".format(time.time() - start_time)
#
data_structure68(6)
#print "Up to 6:", count
#print "Time running so far: {}s".format(time.time() - start_time)
#
data_structure2357(7)
#print "Up to 7:", count
#print "Time running so far: {}s".format(time.time() - start_time)
#
data_structure68(8)
#print "Up to 8:", count
#print "Time running so far: {}s".format(time.time() - start_time)
#
data_structure49(9)
print "Z=", count
print "Time running so far: {}s".format(time.time() - start_time)

 
#Other people give beautiful solutions. 
#Lesson learnt: analyze mathematics carefully