### packages
import re
import json
import array
import string
import time
from collections import Counter

### Example of reading json file. stdi->FILEOBJ->JSONBJ
#FN=raw_input("Enter a json file name plz ")
#print "The file will return to a file object first."
#FO=open(FN)
#print "Then the file object is return to json object."
#JFO=json.load(FO)
#FO.close()

### i.e. of iterating json object with for loop.
#for ITEM in JFO:
    #for RTXT in ITEM["request_text"]
#    print ITEM["request_text"]    

### Example of regular expression
### regex pattern compile, question, how to not stop when meet EOL while scanning string?
### i.e. 
#W1=re.compile("(\w+(?:\'\w{0,2})?)")
#W2=re.compile("(\w+)")

### i.e. \b means boundary if raw string is in use i.e. r"" otherwise it means back space, \w mean alphanumerical character class. (?:...) group try to matches whatever inside paranthesis'(' and ')' with defined pattern with out creating a new gourp since it is none capturing mote, with (...), it does, since it is captruing mode.

### A string for testing the follow functions.
TXT="  I live in California and I'm happy. (1)    (You're) Some words."
UTXT=u"  I live in California and I'm happy. (1)    (You're) Some words."

###  i.e. iterating object by using for loop.
#for WORD in TXT:
#    print WORD  

### i.e. re.match(), compare with regex pattern try to find a match from beginning of a string
#print W1.match(TXT)
### i.e. re.search(), similar with the match but try to find a match from any position of astring
#SEARCH=W1.search(TXT) 
#print SEARCH

### EXAMPLE. re.findall(), The regex match pattern such like I'll
#W1=re.compile("([a-zA-Z]+(?:\'\w{0,2})?)") 
### Test the Regex
### Relust: fine, quite slow compare to string operation
#M1=time.time()
#W1=re.compile("([a-zA-Z]+)")
#FINDALL=W1.findall(TXT)
#TEST=time.time()-M1
#print "Test Regex %s sec" % TEST
#print FINDALL


### i.e. interating output of re.findall()
#for WORD in FINDALL:
#    print WORD
### i.e. convert string to array, with encoding style
#print array.array('B',TXT)

### Example of list()
#e.g.   list(STRING)
#length of iterable object 
#e.g.   len(STRING)
#range over 0 ~ INTEGER - 1 
#e.g.   range(len(STRING))

### Example string package constants
#print string.punctuation
#print string.ascii_letters
#print string.ascii_letters + string.punctuation 


### Test: STR.split()
### Result: it is the most fastest with nano seconds level, but it does not do the job, since it only saperates the words by space, which means the words would have punctuation included.
#M3=time.time()
#TXT.split()
#ENDM3=time.time()
#print "STR.split() test %s sec" % (ENDM3 - M3)


### Test: STR.translate().replace().split()
### Result: The most fastest one and does the job in nano seconds level.
#M4=time.time()
#T1=TXT.translate(None,"!\"#$%&()*+,-./:;<=>?@[\]^_`{|}~"+string.digits)
#T2=T1.replace('\'',' ')
#T3=T2.split()
#ENDM4=time.time()
#print "STR.translate() test %s sec" % (ENDM4 - M4)### Function. Measure function  execution timer.
#print T3


### joint function for iterable object
#T4 = ''.join([ch for ch in TXT if ch in string.ascii_letters])
#print T4



### Function: timer
def timeFn(fn,*ARGS) :
    START=time.time()
    fn(*ARGS)
    END=time.time()-START
    return END



### Test string operation by using for loop.
### Result: This one is the second fastest, beats Regex but not the STRING.translate().replace().split(). For many reasons and test, for large data we should use the DIY for loop in python for string operations, because the fact if we use built-in function for unicode, it is generally slower than loop.
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

### Function: String operation with built-in function, those are link to C language functions, which are the best in performance wise. 
### Test: compare to unicode version or for loop.
### Result: 10 times faster than for loop but does not work for unicode string.
#def stringOp(STR) :
#    T1=STR.translate(None,"!\"#$%&()*+,-./:;<=>?@[\]^_`{|}~"+string.digits)
#    T2=T1.replace('\'',' ')
#    LIST=T2.split()
#    return LIST



### Function for unicode string need to be taken care of when using string.translate(), for unicode string u'STR' cannot apply u'STR'.translate(None,"STRING"). Instead can only use tranlate(MAP)
### Testi: unicode string translate().replace().split() compare to for loop or string stranslate()
### Result: It is twice slower than for loop. This can work for translating the unicode string but twislower for the final bag of words function.
#def stringOp(STR) :
#    MAP=dict((CHAR,None) for CHAR in "!\"#$%&()*+,-./:;<=>?@[\]^_`{|}~"+string.digits) 
#    LIST=STR.translate(MAP).replace('\'',' ').split()
#    return LIST


### Function for unicode string operation using translate, it requires to make the conversion with str()
### Test: compare the function with pure loop
### Result: slight faster than loop, 1/3 less time compare to loop. But get UnicodeEncoderError for operating the data.
#def stringOp(STR) : 
#    LIST=str(STR).translate(None,"!\"#$%&()*+,-./:;<=>?@[\]^_`{|}~"+string.digits).replace('\'',' ').split()
#    return LIST
#print stringOp(u"1243ljawelkfrmu werjl walekrj  walerj ")





### Encode unicode u'STRING' to string
### Test : apply translate() to unicode string 
### Result : encode() function drastically slows down entire string translation compare to ascii string translate(). 5 times slower than for loop.
#def stringOp(STR) :
#    T1=STR.encode().translate(None,"!\"#$%&()*+,-./:;<=>?@[\]^_`{|}~"+string.digits)
#    T2=T1.replace('\'',' ')
#    LIST=T2.split()
#    return LIST
#print u'u' == 'u'


#print "Test loop %s sec" % timeFn(stringOp,TXT)
#print "Test translate().replace().split() %s sec" % timeFn(stringOp,UTXT)





### Example Sorting with bulit-in function
#sorted(stringOp(TXT))
#print sorted(stringOp(TXT))

### Test: package function Counter convert list to dictionary with element occurence frequency
### Result: the function is slower than looping tech
#TCounter=time.time()
#Counter(stringOp(TXT))
#ECounter=time.time()-TCounter
#print  "Test package function Counter %s sec" % ECounter
#print Counter(stringOp(TXT))



### Test: Count word occurency, the function takes LIST and DICT as input.
### Result: is pretty fast compare to library one
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
### The result compare to for loop with iterable object is simmilar has higher high and also has lower low. I think gennerally, when data is not that large, using iterator or indexing have no significant difference, but for large amount of data. Indexing could be faster. Buts, as too many operation invole indexing array in multiple dimention could cause slow. Such as following, with index as a key for getting a value in dictionary casues slow.
#def listToDict(LIST,DICT) :
#    for I in range(len(LIST)) :
#        if LIST[I] in DICT.keys() :
#            DICT[LIST[I]]+=1
#        else :
#            DICT[LIST[I]]=1
#    return DICT
#print "Test loop for converting list to dictionary %s sec" % timeFn(listToDict,stringOp(TXT),{})
#print listToDict(stringOp(TXT),{})



### Function: the function go through BAG(a dictionary type data) for each key if it exits in the DICT(dictionary) then appends the value(DICT[key]) to a list 
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


### Function: it takes file object as input and convert to json object.
def fileToJobj(FILE) :
    FO=open(FILE)
    JO=json.load(FO)
    FO.close()
    return JO


### Function takes json object as input and convert to dictionary with all words occur in the "request_text" field of json object as key and occurence count as value.
### Test: the for loop indexing version compare to for loop iterable version
### Result: tiny bit faster than the iterable version.
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

### Test: iterator
### Result: tiny bit slower than the idexing for loop
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







### Function counting json object fields's word occurence regarding to entire json objects' word occurence
### Test, counting exactly one json object field's takesabout 52 seconds, it includes timing for entire json objects twice, first one is for converting entire json objects to a bag, which the bag is the entire word as a dictionary' key and occurencies as value. Then the second one is the time for scanning the entire bag to get one json object's  word occurency and convert it to a list. The list is ordered as how the bas is ordered. The elements of the list is the word occurency of the json object regarding to the bag.
### Completeness result: for entire json object, the function can run through entire json object by printing out the last index of the json objects.
### Time result of the function, the function takes 
def bagInRow(JOBJ,f_j):
    LIST_LIST=[]
    BAG=f_j(JOBJ)
    for I in range(len(JOBJ)) : 
        ROW=listToDict(stringOp(JOBJ[I]["request_text"]),{})
        #print listOfCount(BAG,ROW)
        LIST_LIST.append(listOfCount(BAG,ROW))
        #if I==len(JOBJ)-1 :
        #4039
        #    print I
    return LIST_LIST
ARG1=bagInRow(fileToJobj("pizza.json"),bagInTotal)
### Timer for the function.                                                 
#print "List of list for each row words occurencies regarding to the entire bag of words. %s sec" % timeFn(bagInRow,fileToJobj("pizza.json"),bagInTotal)
### Printer for the function.
#print bagInRow(fileToJobj("pizza.json"),bagInTotal)




def listToFile(LIST,F) :
    with open(F,'w') as FO :
        for Ei in LIST :
            for Ej in Ei :
                FO.write('%d ' % Ej)
            FO.write('\n')
    FO.close()
print "Time consumed at the task %s sec." % timeFn(listToFile,ARG1,'pizza.output')
































#########################Some  tests for function generally not perfoming better than above ones.


### Test: Iterable json object
### Result: the result is simmilar, tiny bit slower.
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
### Result: a bit slower than version 1 due to repeated control flow.
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


