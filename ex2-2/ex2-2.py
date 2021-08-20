#!/bin/bash

###(We have to pay attention that built-in function for converting integer to binary is not allowed, there for we should use 2's complement algorithm to make the calculation.) 
### The function can definitely be optimized, due to the fact that while loop uses more assembly than for loop, there for it could be improve by using for loop.
def binRep3():
    BOX=[]
    BIT=3
    print "The following print stdout shows the count up of binary number"
    for N in range(2 ** BIT) :
        ITEM=[]
        NN=N
        I=BIT
        while I>0 :
            I-=1
            BL=2 ** I
            if NN==BL:
                VAL=1
                NN=0
            elif NN<BL:
                VAL=0
            else:
                VAL=1
                NN-=BL
            #print VAL
            ITEM.append(VAL)
        print 'The following shows binary representation of %(index)s'  % {"index": N}
        print ITEM
        BOX.append(ITEM)
    print "The list of the binary number representations are stored in the list."
    print BOX
    return BOX 
#binRep3()
#The following function is just a modification which takes stdi input as the bit number        
def binRepI():
    BOX=[]
    BIT=int(raw_input("Please enter an integer: "))
    print "The following print stdout shows the count up of binary number"
    for N in range(2 ** BIT) :
        ITEM=[]
        NN=N
        I=BIT
        while I>0 :
            I-=1
            BL=2 ** I
            if NN==BL:
                VAL=1
                NN=0
            elif NN<BL:
                VAL=0
            else:
                VAL=1
                NN-=BL
            #print VAL
            ITEM.append(VAL)
        print 'The following shows binary representation of %(index)s'  % {"index": N}
        print ITEM
        BOX.append(ITEM)
    print "The list of the binary number representations are stored in the list."
    print BOX
    return BOX 
binRepI()
# The expression in the while loop meaning:
# i.e. BIT=3
# for unsinged two's complement of 3 bit
# all number with in the range of 2^3 can be represented with B2*2^2 + B1*2^1 + B0*2^0 
# for Ni - 2^i-1 may have three condition 
#   1. Ni - 2^i-1 = 0           if Ni=2^i-1 then Bi=1 and Ni'=0
#                 = negative    if Ni<2^i-1 then Bi=0 and Ni' stay the same
#                 = postive     if Ni>2^i-1 then Bi=1 and Ni'=Ni -2^i-1 
