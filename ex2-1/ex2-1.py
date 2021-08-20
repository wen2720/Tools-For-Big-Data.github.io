#!/bin/bash
#Exercise 2.1:
#Write a script with two methods. The first method should read in a matrix like the one here and return a list of lists. The second method should do the inverse, namely take, as input, a list of lists and save it in a file with same format as the initial file. The first method should take the file name as a parameter. The second method should take two arguments, the list of lists, and a filename of where to save the output.

### Example, convertions from stdi to file object 
#import os
###i.e path builder; use strings to form a path regarding to the local operating system
#path = os.path.join(os.path.expanduser('~'),"Tools-For-Big-Data.github.io","ex2-1","R9FVAdXW.txt")
###i.e function of path directed file to read stdi ,  then write stdout line by line.
#def printfileStd(P):
#   with open(P,'r') as F  
#        for LINE in F:
#            print LINE
#printFileStd(path)
#print "hello world~"

### Example from previous example, we add function of stdi and output LIST1 of LIST2 and each LIST1 ontains the stdi's each line and LIST2 contains the line's elment that saperated by space. 
##i.e. the file object is iterable object and each element is the stdi escape with '\n'. Then we use the built-in function STRING.split() to saperate each LINE element whenever hav empty string or space.
###Read stdin file use STR.split() split string by whitespace and each splitted string is popped into the list. Then the list will be appended to the BOX.
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

##Read stdin file use STR.split() split string by space and each splitted string is appended into the list. Then the list will be appended to the BOX.
import os
import time
import string
DATAFILE="R9FVAdXW.txt"
CWD=os.getcwd()
OUTPUTFILE="NEW"+DATAFILE

### Example, a timer function which takes any function fn as first argument and the rest arguments are the arguments of function fn. The timer function measures the execution time by first recoding current time just before calling fn as starting point and then record another current time as end point. Sustracting end point by the strating point would give the total time of fn's perfomance.  

def timeFn(fn,*ARGS) :
    START=time.time()
    fn(*ARGS)
    END=time.time()-START
    return END


### Example, DIV string operation which could be faster than STR.split()
def stringOp(LINE) :
    ELEM=''
    LIST=[]
    for I in range(len(LINE)) :
        if LINE[I] not in string.whitespace :
            ELEM+=LINE[I]
            if I==len(LINE)-1 or LINE[I+1] in string.whitespace :
                LIST.append(ELEM)
                ELEM=''
    return LIST





def fileToList(F) :
    LIST_LIST=[]
    with open(F,'r') as FO:
        for LINE in FO:
        #file object does not support indexing in for loop.
        #for I in range(len(FO)) :
            LIST_LIST.append(stringOp(LINE))
            #MY DIY stringOperation is tiny slower than STR.split(), linke 1*10^-5 sec slower. Maybe because of the if statements, the logic is not concise enough. But for small amount of data built-in may faster; and for large one's it could be slower. As in ex2-3, both Regex and STR.split() is slower than the DIY stirng operation.
            #LIST_LIST.append(LINE.split())
    FO.close()
    return LIST_LIST
print fileToList(DATAFILE)
#print "String operation test: %s sec" % timeFn(fileToList,DATAFILE)
#print "Built-in split() test: %s sec" % timeFn(fileToList,DATAFILE)


### Example for converting LIST of LIST to stdo file. Thie requries create a FILE object by built-in function open() and write(). Here the LIST of LIST would be the meta.

ARG1=fileToList(DATAFILE)
def listToFile(LIST,F):
    with open(F,'w') as FO:
        for Ei in LIST:
            for Ej in Ei:
                FO.write(Ej+' ')
            FO.write('\n')   
    FO.close()
listToFile(ARG1,OUTPUTFILE)
os.system("cat "+OUTPUTFILE)
### The following result shows it is slower than STR.split().
#print "String operation test: %s sec" % timeFn(listToFile,ARG1,OUTPUTFILE)
### The following result shows it faster than the string operation.
#print "Built-in split() test: %s sec" % timeFn(listToFile,ARG1,OUTPUTFILE)
