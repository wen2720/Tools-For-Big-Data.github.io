#!/bin/bash
#Exercise 2.1:
#Write a script with two methods. The first method should read in a matrix like the one here and return a list of lists. The second method should do the inverse, namely take, as input, a list of lists and save it in a file with same format as the initial file. The first method should take the file name as a parameter. The second method should take two arguments, the list of lists, and a filename of where to save the output.

##open(), file object 
#import os
#
#path = os.path.join(os.path.expanduser('~'),"Tools-For-Big-Data.github.io","ex2-1","R9FVAdXW.txt")
#def printfileStd(P):
#   with open(P,'r') as F  #with VALUE as IDENTIFIER:
#        for LINE in F:
#            print LINE
#printFileStd(path)
#print "hello world~"

##Read stdin file use STR.split() split string by whitespace and each splitted string is popped into the list. Then the list will be appended to the BOX.
#import os
#path = os.path.join(os.path.expanduser('~'),"Tools-For-Big-Data.github.io","ex2-1","R9FVAdXW.txt")
#def printListStr(P):
#    with open(P,'r') as F:
#        BOX=[]
#        for LINE in F:
#           ITEM=LINE.split()
#           BOX.append()
#           print ITEM
#    F.close()
#    print "The list of list is shown as follows:"
#    print BOX
#printListStr(path)

##Read stdin file use STR.split() split string by whitespace and each splitted string is popped into the list. Then the list will be appended to the BOX.
import os
import time
DATAFILE="R9FVAdXW.txt"
CWD=os.getcwd()
OUTPUTFILE="NEW"+DATAFILE

def ioListOfList(P):
    BOX=[]
    with open(os.path.join(P,DATAFILE),'r') as F:
        print "Each STR.split are shown as follows:"
        for LINE in F:
            ITEM=LINE.split()
            BOX.append(ITEM)
            print ITEM
            #the following is not correct, because ITEM is list and writelines only work for iterable string. there for they are written in one line.
            with open(os.path.join(P,"listOflist.txt"),'a') as NF:
                NF.writelines(ITEM)
        NF.close()
        F.close()
        print "The list of list is shown as follows:"
        print BOX
        print "And the file is save to listOflist.txt."
    return BOX
ARG1=ioListOfList(CWD)
def ioMatrix(L,P):
    BOX=[]
    with open(os.path.join(P,OUTPUTFILE),'w') as F:
        for L1 in L:
            for L2 in L1:
                F.write(L2+' ')
            F.write('\n')   
    F.close()
    print "The matrix is in the new file."
    os.system("cat "+P+"/"+OUTPUTFILE)
ioMatrix(ARG1,CWD)
   
