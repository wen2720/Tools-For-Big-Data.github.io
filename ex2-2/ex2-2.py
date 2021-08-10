#!/bin/bash
#Exercise 2.2:
#Write a script that takes an integer N, and outputs all bit-strings of length N as lists. For example: 3 -> [0,0,0], [0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]. As a sanity check, remember that there are 2^N such lists.
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
