#!/bin/bash
#Exercise 2.3:
#    Write a script that takes this file (from this Kaggle competition), extracts the request_text field from each dictionary in the list, and construct a bag of words representation of the string (string to count-list).

#    There should be one row pr. text. The matrix should be N x M where N is the number of texts and M is the number of distinct words in all the texts.

 #   The result should be a list of lists ([[0,1,0],[1,0,0]] is a matrix with two rows and three columns).
### packages
import re
import json
import array
import string
import time
from collections import Counter

###Example of reading json file. stdi->FILEOBJ->JSONBJ
#FN=raw_input("Enter a json file name plz ")
#print "The file will return to a file object first."
#FO=open(FN)
#print "Then the file object is return to json object."
#JFO=json.load(FO)
#FO.close()

#for ITEM in JFO:
    #for RTXT in ITEM["request_text"]
#    print ITEM["request_text"]    

#regex pattern compile, question, how to not stop when meet EOL while scanning string.
#\b means boundary if raw string is in use i.e.r"" other wise it means back space, \w mean alphanumerical character class. (?:...) group try to matches whatever inside paranthesis'(' and ')' with defined pattern with out creating a new gourp since it is none capturing mote, with (...), it does, since it is captruing mode.
#W1=re.compile("(\w+(?:\'\w{0,2})?)")
#W2=re.compile("(\w+)")
TXT="  I live in California and I'm happy. (1)    (You're) Some words."


###Example of string interation.
#for WORD in TXT:
#    print WORD  

### re.match(), re.search
#compare with regex pattern try to find a match from beginning of a string
#print W1.match(TXT)
#similar with the match but try to find a match from any position of astring
#SEARCH=W1.search(TXT) 
#print SEARCH

### re.findall()
### The regex match pattern such like I'll
#W1=re.compile("([a-zA-Z]+(?:\'\w{0,2})?)") 
### Test the Regex
### Reust: fine
#M1=time.time()
#W1=re.compile("([a-zA-Z]+)")
#FINDALL=W1.findall(TXT)
#TEST=time.time()-M1
#print "Test Regex %s sec" % TEST
#print FINDALL




###Example of interating output of re.findall()
#for WORD in FINDALL:
#    print WORD
#convert string to array, with encoding style
#print array.array('B',TXT)

###list()
#e.g.   list(STRING)
#length of iterable object 
#e.g.   len(STRING)
#range over 0 ~ INTEGER - 1 
#e.g.   range(len(STRING))

###string package constants
#print string.punctuation
#print string.ascii_letters
#print string.ascii_letters + string.punctuation 



def timeFn(fn,*ARGS) :
    START=time.time()
    fn(*ARGS)
    END=time.time()-START
    return END



### Test string operation by using for loop.
### Result: This one is fastest, beats Regex
### tried slicing with assigment LIST[len(LIST):]=["STR1"] is not better than append()
###

def stringOp(STR) :
    WORD=""
    LIST=[]
    for I in range(len(STR)) :
        if STR[I] in string.ascii_letters :
            WORD+=STR[I]            
            if I==len(STR)-1 or STR[I+1] not in string.ascii_letters :
                LIST.append(WORD)
                WORD=""
    return LIST
#print "Test loop %s sec" % timeFn(stringOp,TXT)
#print stringOp(TXT)

### Test string operation by using for I,V in enumerate(LIST):, this one is quite close but a tiny bit slower than for I in range(len(LIST)):
#def stringOp(STR) :
#    WORD=""
#    LIST=[]
#    for I,V in enumerate(STR) :
#        if V in string.ascii_letters :
#            WORD+=V            
#            if I==len(STR)-1 or STR[I+1] not in string.ascii_letters :
#                LIST.append(WORD)
#                WORD=""
#    return LIST
#print "Test loop %s sec" % timeFn(stringOp,TXT)
#print stringOp(TXT)






###Sorting with bulit-in function
#sorted(stringOp(TXT))
#print sorted(stringOp(TXT))
### Test package function Counter convert list to dictionary with element occurence frequency
#TCounter=time.time()
#Counter(stringOp(TXT))
#ECounter=time.time()-TCounter
#print  "Test package function Counter %s sec" % ECounter
#print Counter(stringOp(TXT))



### Count word occurency, the function takes LIST and DICT as input.
### The result is pretty fast compare to library one
def listToDict(LIST,DICT) :
    for WORD in LIST :
        if WORD in DICT.keys() :
            DICT[WORD]+=1
        else :
            DICT[WORD]=1
    return DICT
#print "Test loop for converting list to dictionary %s sec" % timeFn(listToDict,stringOp(TXT),{})
#print listToDict(stringOp(TXT),{})



### Test for loop with index
### The result compare to for loop with iterable object is simmilar has higher high and also has lower low. I think gennerally, should use iterable object instead of indexing an array if you have a lot array accessing operation, such as below.
#def listToDict(LIST,DICT) :
#    for I in range(len(LIST)) :
#        if LIST[I] in DICT.keys() :
#            DICT[LIST[I]]+=1
#        else :
#            DICT[LIST[I]]=1
#    return DICT
#print "Test loop for converting list to dictionary %s sec" % timeFn(listToDict,stringOp(TXT),{})
#print listToDict(stringOp(TXT),{})




### The function go through BAG(a dictionary type data) for each key if it exits in the DICT(dictionary) then appends the value(DICT[key]) to a list 
def listOfCount(BAG,DICT) :
    LIST=[]
    for KEY in BAG :
        if KEY in DICT :
            LIST.append(DICT[KEY])
        else :
            LIST.append(0)
    return LIST
#print "Test loop function for counting word occurencies from a dictionary regarding to a bag %s sec" % timeFn(listOfCount,listToDict(stringOp(TXT,[]),{}),listToDict(stringOp(TXT,[]),{}))
#print listOfCount(listToDict(stringOp(TXT,[]),{}),listToDict(stringOp(TXT,[]),{}))


### Function takes file object as input and convert to json object
def fileToJobj(FILE) :
    FO=open(FILE)
    JO=json.load(FO)
    FO.close()
    return JO
### Test the for loop indexing version compare to for loop iterable version
### Result, tiny bit faster than the iterable version.
def bagInTotal(JOBJ) :
    DICT={}
    for I in range(len(JOBJ)) :
        #print ELEM["request_text"]    
        listToDict(stringOp(JOBJ[I]["request_text"]),DICT)
    #print "%s * %s" % (len(DICT),len(JOBJ))    
    #14402 * 4040
    return DICT
#bagInTotal(fileToJobj("pizza.json"))
#print "Time for deriving sum of bag of words %s sec" % timeFn(bagInTotal,fileToJobj("pizza.json"))
#print bagInTotal(fileToJobj("pizza.json")) 

### Function takes json object as input and convert to dictionary with all words occur in the "request_text" field of json object as key and occurence count as value.
#def bagInTotal(JOBJ) :
#    DICT={}
#    for ELEM in JOBJ:
#        #print ELEM["request_text"]    
#        listToDict(stringOp(ELEM["request_text"]),DICT)
#    #print "%s * %s" % (len(DICT),len(JOBJ))    
#    #14402 * 4040
#    return DICT
#bagInTotal(fileToJobj("pizza.json"))
#print "Time for deriving sum of bag of words %s sec" % timeFn(bagInTotal,fileToJobj("pizza.json"))
#print bagInTotal(fileToJobj("pizza.json")) 


###  Dict.update() updates the DICT1 with DICT2 if the key in DICT2 does not exist in the DICT1. The if the key exists in DICT1 the result is not know.
#def bagInTotal(JOBJ) :
#    DICT={}
#    for ELEM in JOBJ:
#        #print ELEM["request_text"]    
#        DICT.update(listToDict(stringOp(ELEM["request_text"]),DICT))
#    #print "%s * %s" % (len(DICT),len(JOBJ))    
#    #14402 * 4040
#    return DICT
#bagInTotal(fileToJobj("pizza.json"))
#print bagInTotal(fileToJobj("pizza.json"))
#print "Time for deriving sum of bag of words %s sec" % timeFn(bagInTotal,fileToJobj("pizza.json"))




#def bagInRow(JOBJ,f_j):
#    LIST_LIST=[]
#    BAG=f_j(JOBJ)
#    with open("RESULT.data",'w') as F:
#        for I in range(len(JOBJ)) : 
#            ROW=listToDict(stringOp(JOBJ[I]["request_text"]),{})
#            LIST=listOfCount(BAG,ROW)
#            LIST_LIST.append(LIST)
#            F.writelines(LIST)
#    F.close()
#    return LIST_LIST
#bagInRow(fileToJobj("pizza.json"),bagInTotal)



### Test counting exactly one json object fields's word occurence regarding to entire json objects' word occurence
### Time result about 52 seconds, it includes timing for entire json objects twice, first one is for converting entire json objects to a bag, which the bag is the entire word as a dictionary' key and occurencies as value. Then the second one is the time for scanning the entire bag to get one json object's  word occurency and convert it to a list. The list is ordered as how the bas is ordered. The elements of the list is the word occurency of the json object regarding to the bag.
### Completeness result of the function for entire json object, the function can run through entire json object by printing out the last index of the json objects.
### Time result of the function, the function takes 
def bagInRow(JOBJ,f_j):
    LIST_LIST=[]
    BAG=f_j(JOBJ)
    for I in range(len(JOBJ)) : 
        ROW=listToDict(stringOp(JOBJ[I]["request_text"]),{})
        #print listOfCount(BAG,ROW)
        LIST_LIST.append(listOfCount(BAG,ROW))
        #if I==len(JOBJ)-1 :
        #    print I
    return LIST_LIST
#bagInRow(fileToJobj("pizza.json"),bagInTotal)
### Timer for the function.                                                 
#print "List of list for each row words occurencies regarding to the entire bag of words. %s sec" % timeFn(bagInRow,fileToJobj("pizza.json"),bagInTotal)
### Printer for the function.
#print bagInRow(fileToJobj("pizza.json"),bagInTotal)





### Iterator is slower than for loop with index
### Result the result is simmilar, tiny bit slower.
#def bagInRow(JOBJ,f_j):
#    LIST_LIST=[]
#    BAG=f_j(JOBJ)
#    for ELEM in JOBJ:
#        ROW=listToDict(stringOp(ELEM["request_text"]),{})     
#        LIST_LIST.append(listOfCount(BAG,ROW))
#    return LIST_LIST
#bagInRow(fileToJobj("pizza.json"),bagInTotal)
### Timer for the function.
#print "List of list for each row words occurencies regarding to the entire bag of words. %s sec" % timeFn(bagInRow,fileToJobj("pizza.json"),bagInTotal)
### Printer for the function.
#print bagInRow(fileToJobj("pizza.json"),bagInTotal)











### Test string operation by using for I,V in enumerate(LIST):, this one is quite close but a tiny bit slower than for I in range(len(LIST)):
#def stringOp(STR,LIST) :
#    WORD=""
#    for I,V in enumerate(STR) :
#        if V in string.ascii_letters :
#            WORD+=V            
#            if I==len(STR)-1 or STR[I+1] not in string.ascii_letters :
#                LIST.append(WORD)
#                WORD=""
#    return LIST
#print "Test loop %s sec" % timeFn(stringOp,TXT,[])
#print stringOp(TXT,[])






### recursive function is not that fast, if the CFG is not desinded well compare to well desinged loops.
### Result: similar to Regex
#def stringOpR(txt,I,BAG,WORD) :
#    if I<len(txt) :
##        print txt[I]
#        if txt[I] in string.ascii_letters :
#            WORD+=txt[I]
#            if txt[I+1] not in string.ascii_letters :
#                BAG.append(WORD)
#                WORD=""
#        return stringOpR(txt,I+1,BAG,WORD)
#    else : 
#        return BAG
#print "Test recursive function %s sec" % timeFn(stringOpR,TXT,0,[],"")
#print stringOpR(TXT,0,[],"")




### A better tail recursive.
### Result: simmilar to Regex as well
#def stringOpTR(txt,I,BAG,WORD) :
#    if I==len(txt) :
#        return BAG
#    if txt[I] in string.ascii_letters :
#        WORD+=txt[I]
#        if txt[I+1] not in string.ascii_letters :
#            BAG.append(WORD)
#            WORD=""
#    return stringOpTR(txt,I+1,BAG,WORD)
#print "Test tail recursive function %s sec" % timeFn(stringOpTR,TXT,0,[],"")
#print stringOpTR(TXT,0,[],"")





### Test string operation version 2.
### Result: a bit slower thant version 1 due to repeated control flow.
#def stringOpv2() :
#    BAG=[]
#    WORD=""
#    for I in range(len(TXT)) :
#        if TXT[I] in string.ascii_letters and TXT[I+1] in string.whitespace+string.punctuation :
#            WORD+=TXT[I]
#            BAG.append(WORD)
#            WORD=""
#            continue
#        if TXT[I] in string.ascii_letters :
#            WORD+=TXT[I]
#    return BAG
#print "Test loop v2 %s sec" % timeFn(stringOpv2)
#print stringOpv2()




#M3=time.time()
#BAG3=TXT.split()
#print BAG3
#print("--- %s seconds ---" % (time.time() - M3))


###string -> array object. output format is ascii value 
#print array.array('B',TXT)
###\NUM represent octal value
#print "\45"
### string to ascii function
#print ord('I')



### Test: use ascii value for string operation,
### Result pretty slow due to the built in function call. ord(), range(), but still OK compare to Regex
#def stringOpv3() :
#    BAG=[]
#    WORD=""
#    for I in range(len(TXT)) :
#        if ord(TXT[I]) in range(65,91) or ord(TXT[I]) in range(97,123) :
#            WORD+=TXT[I]                                                                 
#            if not (ord(TXT[I+1]) in range(65,91) or ord(TXT[I+1]) in range(97,123)) :
#                BAG.append(WORD)
#                WORD=""
#    return BAG
#
#print "Test loop v3 %s sec" % timeFn(stringOpv3)
#print stringOpv3()


