from __future__ import division
from array import array
import time
import operator
### Linear matrix equation Ax=b

### A should be a invertible matrix, square matrix that on left side of the equation.
### Example, 3x3 matrix interpretation of A:
### i.e. [[0,1,2],[3,4,5,],[6,7,8]] 
### A = A_(0,0) A_(0,1) A_(0,2)
###     A_(1,0) A_(1,1) A_(1,2)
###     A_(2,0) A_(2,1) A_(2,2)
### b is a column on right side of the equation.
### Example, interpretation of b:
### [[2],[5],[8]]

### Sloving the equation is equivalent to solve x=A^(-1)b.
### Inverse of a matrix A^-1=1/det(A)adj(A)
### Determinat of a matrix regading a row or column is weighted sum of minors.
### Example for row 1 
### det(A)=sum(A_(0,0)(-1)^(0+0)*M_(0,0)+A_(0,1)(-1)^(0+1)*M(0,1)+A_(0,2)(-1)^(0+2)*M(0,2))


### M_(i,j) Minor, is determinant of a sub matrix. The sub matrix is without row i and column j.
### Example, M_(0,0)(A)=[[4,5],[7,8]], M_(0,1)(A)=[[3,5],[6,8]], M_(0,2)(A)=[[3,4],[6,7]], 
###          M_(1,0)(A)=[[1,2],[7,8]], M_(1,1)(A)=[[0,2],[6,8]], M_(1,2)(A)=[[0,1],[6,7]],
###          M_(2,0)(A)=[[1,2],[4,5]], M_(2,1)(A)=[[0,2],[3,5]], M_(2,2)(A)=[[0.1],[3,4]]
### 

### Cofactor matrix is square matrix formed with cofactors where cofactor is derived by minor times sign factor.
### C_(i,j)=(-1)^(i+j)M_(i,j))
### Example, C_(0,0)=(-1)^(0+0)M_(0,0), C_(0,1)=(-1)^(0+1)M_(0,1), C_(0,2)=(-1)^(0+2)M_(0,2),
###          C_(1,0)=(-1)^(1+0)M_(1,0), C_(1,1)=(-1)^(1+1)M_(1,1), C_(1,2)=(-1)^(1+2)M_(1,2),
###          C_(2,0)=(-1)^(2+0)M_(2,0), C_(2,1)=(-1)^(2+1)M_(2,1), C_(2,2)=(-1)^(2+2)M_(2,2)

### Adjugate adj(A) is the transpose of cofactor matrix.
### Example, adj(A)=C^T =>
###          A'_(0,0)=C_(0,0), A'_(0,1)=C_(1,0), A'_(0,2)=C_(2,0),
###          A'_(1,0)=C_(0,1), A'_(1,1)=C_(1,1), A'_(1,2)=C_(2,1),
###          A'_(2,0)=C_(0,2), A'_(2,1)=C_(1,2), A'_(2,2)=C_(2,2)



### Gaussian elimination
### row enchelon form, upper triangle
###
### Function: function execution timer
def timeFn(fn,*ARGS) :
    START=time.time()
    fn(*ARGS)
    XTIME=time.time()-START
    return XTIME



### Create a class for fraction number 
class Frac :
    def __init__ (self,nom,denom) :
        self.a=nom
        self.b=denom
    ### try : ... except ... : exception is not needed for division.
    def toFloat (self) :
        #try :
            return self.a/self.b
        #except ValueError:
            #print("Denominator must be non-zero integer")

    def mulS (F,S) :
        return Frac(F.a*S,F.b)

    def mulF (F1,F2) :
        return Frac(F1.a*F2.a,F1.b*F2.b)


TV=[[0,0,2],[4,5,6],[7,8,9]]
### Function: 
### Row operations
### Swap two rows for an Array
def swapRow(LL,R1,R2) :
    TL=LL[R1]
    LL[R1]=LL[R2]
    LL[R2]=TL
    return LL
#print "Swapping row vector with normal way %s sec" % timeFn(swapRow,TV,0,2)
#print swapRow(TV,0,2)


### Count leading zeros for a row in matrix.
def countLeading0(L) :
    COUNT=0
    J=0
    while L[J]==0 and J<len(L)-1 :
        J+=1
        COUNT+=1
    return COUNT
#print countLeading0(TV[0])
#print "While loop for counting leading zeros, %s sec" % timeFn(countLeading0,TV[0])



### scala devision for a row vector
### lsit -> Frac list
def divideScala(L,S) :
    NL=[ N/S for N in L ]
    return NL
#print divideScala([1,2,3], 2)
def divideScalaF(L,S) :
    NL=[Frac(E,S) for E in L]
    return NL
#print divideScala(TV[0],3)

### string operation, replace comma to space, then split patterns into list when meet a space.
def stringOp(STR) :
    T1=STR.replace(',', ' ')
    L=T1.split()
    return L
### convert file object to list. We have to go through the full data conversion from file object to list. It is neccessary because of the nature of matrix has value and row and column(not just the entry) attributes. In order to do row operations, we need the row and column index to access each entry. Therefore, by completing the conversion we can have the list length or arity those kind of information for row operation.
def fileToList(F) :
    with open(F,'r') as FO :
        ### list of list using list comprehansion
        LL=[ [ int(N) for N in stringOp(LINE) ] for LINE in FO ]   
        ### slower than forming outter list by for loop and inner list by list comprehansion
    FO.close()
    return LL
#print fileToList("matrix.data")
#print "String operation with using list comprehansion, %s sec" % timeFn(fileToList,"matrix.data")


### Applying operator between vector and scala
def opScala(op,A,S) :
    CA=[ op(N,S) for N in A ]
    return CA
#print opScala(operator.add,[1.0, 2.0, 3.0],4)
### the integer to floating number conversion is automatically done by the operator.



### Row operation regarding a given matrix, a pivot and current rank.
def rowOp(L,P,Rn) :
    NL=[]
    for I in range(len(L)) :
        if I<Rn :
            NL.append(L[I])
        elif I==Rn :
            NL.append(P)
        else :
            #NR=[]
            #for J in range(len(L[I])) :
            #    NR.append(L[I][J]-L[I][Rn]*P[J])
            NR=[ L[I][J]-L[I][Rn]*P[J] for J in range(len(L[I]))]
            NL.append(NR)
    return NL
#print rowOp([[1,2,3],[-1,1,1],[0,1,-1]],[1,2,3],0)
#print "Row operation with for loop, %s sec" % timeFn(rowOp,[[1,2,3],[-1,1,1],[0,1,-1]],[1,2,3],0)  



### Row operation regarding a given matrix, a pivot and current rank.
def rowOpT(L,P,Rn) :
    NL=[]
    for I in range(Rn+1,len(L)) :
        #NR=[]
        #for J in range(len(L[I])) :
        #    NR.append(L[I][J]-L[I][Rn]*P[J])
        NR=[ L[I][J]-L[I][Rn]*P[J] for J in range(len(L[I]))]
        NL.append(NR)
    return NL
#print rowOp([[1,2,3],[-1,1,1],[0,1,-1]],[1,2,3],0)
#print "Row operation with for loop test version, %s sec" % timeFn(rowOpT,[[1,2,3],[-1,1,1],[0,1,-1]],[1,2,3],0)  




def rowOp1(L,Rn) :
    for I in range(Rn+1,len(L)) :
        #NR=[]
        #for J in range(len(L[I])) :
        #    NR.append(L[I][J]-L[I][Rn]*P[J])
        L[I]=[ L[I][J]-L[I][J]*L[Rn][J] for J in range(len(L[I]))]
    return L
#print rowOp([[1,2,3],[-1,1,1],[0,1,-1]],0)
#print "Row operation with for loop test version, %s sec" % timeFn(rowOp1,[[1,2,3],[-1,1,1],[0,1,-1]],,0)  




def isEchelonF(L) :
    for I in range(len(L)) :
        if countLeading0(L[I])<I :
            B=False
            break
        else :
            B=True
    return B
#print isEchelonF([[1,1,1],[0,1,1],[0,0,1]])
#print "Function for checking wether a list is an echelon form, %s sec" % timeFn(isEchelonF,[[1,1,1],[0,1,1],[0,0,1]])  


### find a valid coefficient from current column postion of each row
def findCoeff(LL,L,D,E) :
    for I in range(D+1,len(LL)) :  
        for J in range(D,E) :
            if LL[I][J]!=0 :
                LL[D]=LL[I]
                LL[I]=L
                break
        if LL[D]!=L :
            break 
    return LL

#print findCoeff([[0,1,1],[1,1,1],[0,0,0]],[0,1,1],0,1)
#print "Searching for first valid coefficients from next row from given column until second last column %s sec" % timeFn(findCoeff,[[0,1,1],[1,1,1],[0,0,0]],[0,1,1],0,1)



def findCoeff1(LL,L,D) :
    for I in range(D+1,len(LL)) :  
        for J in range(D,len(LL[I])-1) :
            if LL[I][J]!=0 :
                LL[D]=LL[I]
                LL.append(L)
                break
        if LL[D]!=L :
            break 
    return LL




#TL1=[1,2,3]
#TL1[1]=TL1[1]+1
#print TL1

# Convert matrix to row echelon form.
def listToEchelon(L) :
   NL=[ ITEM for ITEM in L]
   for I in range(len(NL)) :
        if countLeading0(NL[I])==I :
            NL[I]=divideScala(NL[I],NL[I][I])
            rowOp1(NL,I)
        elif countLeading0(NL[I])>I and countLeading0(NL[I])<len(NL[I])-1 :
            findCoeff(NL,NL[I],I,countLeading0(NL[I]))
            NL[I]=divideScala(NL[I],NL[I][I])
            rowOp1(NL,I)
        elif countLeading0(NL[I]==len(NL[I]-1)) :
            findCoeff1(NL,NL[I],I)
            rowOp1(NL,I)
   return NL

#print listToEchelon([[1,2,3],[-1,1,1],[0,1,-1]])
print "Test matrix to row echelon form %s sec" % timeFn(listToEchelon,[[1,2,3],[-1,1,1],[0,1,-1]])

#L1=[[1,1],[0,0],[3,3,],[4,4]]
#L1.append(L1[1])
#print L1
#L1.pop(1)
#print L1








##################################################################### Appendix


### Row operation,  substract pivot from each row in the list. Not a correct one, but shows nested list list comprehension.
### A, a list of list representing matrix
### P, a list representing pivot
### C, an integer representing column postion of leading coefficient
#def rowOp(L,P,C) :
#    ###The comment is for testing the function to append the row operation with pivot and append those to pivot
#    #LL=[]
#    #LL.append(P)
#    LL= [ [ L[I][J]-L[I][C]*P[J] for J in range(len(A[I])) ] for I in range(C+1,len(L)) ]
#    #for I in range(C+1,len(A)) :
#        #NL=[ A[I][J]-A[I][C]*P[J] for J in range(len(A[I])) ]
#        #LL.append(NL)
#    return LL
#print rowOp([[1,2,3],[-1,1,1],[0,1,-1]],[1,2,3],0)
#print "Nested list comprehension, %s sec"  % timeFn(rowOp,[[3,6,6],[2,3,3]],[1,3,3],0)
###  Generally, it faster than nested for loop



### LIST.append() is a modification of LIST, requires oneline operation of it, return LIST.append() does not work
#L=[1,2,3]
#L.append(4)
#print L

### LIST.insert()
#L=[1,2,3]
#L.insert(1,4)
#print L
### the function remove an element from its postion and insert to a new postion function inserts new element into given index position of iterable object

### the function remove an element from its postion and insert to a new postion function inserts new element into given index position of iterable object
#L1=[1,2,3,4]
#L2=[1,2,3,4]
#def testBuiltIn(L) :
#    ###side effect
#    #NL=L
#    ###for avoiding side effect
#    NL=[ ITEM for ITEM in L ]
#    T=NL[3]
#    ###Delete an element
#    NL.pop(3)
#    ###insert an element to a postion 
#    NL.insert(1,T)
#    return NL
#print testBuiltIn(L1)
#print "Test1 %s sec" % timeFn(testBuiltIn,L1)
#print L1


### Applying function on parameter or argument would have side effects.
### Generally make a safe copy by iterating through the argument and assign each item if we don't want to avoid side effects. Side effects comes from the equal assgiment.
### Desired side effects are neccessary such like updating hash table,dictionary,list or array .

### remove and insert item from a list, self-made function is slightly slower than built-ins
#def testLoop(L) :
#    T=L[3]
#    NL=[]
#    ###copy all element but the last to a new list
#    for I in range(len(L)) :
#        if I==3 :
#            continue
#        NL.append(L[I])
#    NNL=[]
#    ###copy every element in the LIST1 until a postion to LIST2, then copy the element wish to insert to LIST2, and then copy the rest of LIST1's element to LIST2.
#    for I in range(len(NL)) :
#        if I==1 :
#            NNL.append(T)
#        NNL.append(NL[I])
#    return NNL
#print testLoop(L2)
#print "Test2 %s sec" % timeFn(testLoop,L2)  
#print L2            








#### Substract row vector R2 times a scala S from R1.
#def substractRow(S,R1,R2) :
#    NR= [ R1[J]-S*R2[J] for J in range(len(R1)) ] 
#    return NR
##print substractRow(2,[1,2,3],[1,2,3])
#
#### substractRow for each row in the list
#### fn, a substraction function substract a pivot row R1 from row vector R2 
#### A, a list of list
#### P, a pivot
#### J, an index of column
#def substractFER(fn,A,P,J) :
#    LL= [ fn(A[I][J],A[I],P) for I in range(len(A)) ]
#    return LL
##print substractFER(substractRow,[[3,6,6],[2,3,3]],[1,3,3],0)
#print "list comprehension with calling a function, %s sec" % timeFn(substractFER,substractRow,[[3,6,6],[2,3,3]],[1,3,3],0)





### Nested for loop for row operation
#def rowOpF(A,P,C) :
#    LL=[]
#    for I in range(len(A)) :
#        L=[]
#        for J in range(len(A[I])) :
#            L.append(A[I][J]-A[I][C]*P[J])
#        LL.append(L)
#    return LL
#print "Nested for loop, %s sec"  % timeFn(rowOpF,[[3,6,6],[2,3,3]],[1,3,3],0)
### This solution is slower than nested list comprehension







### Read file then manipulate each line of the file object as desired form. And also for each string of the line convert them to integer.
#def fileToListF(F) :
#    with open(F,'r') as FO :
#        LL=[]
#        for LINE in FO :
#            L=[ int(N) for N in stringOp(LINE) ]
#            #L=[]
#            ### nested for loop
#            #for N in stringOp(LINE) :
#            #    L.append(int(N))
#            ### list comprehansion is faster, nested inner for loop always slow, either use list comprehansion or make inner one as a function so it can be called from stack and improve speed.
#            LL.append(L)
#    FO.close()
#    return LL
#print fileToListF("matrix.data")
#print "String operation with using for loop combined list comprehansion, %s sec" % timeFn(fileToListF,"matrix.data")
### The performance test result is pretty similar compare to the full list comprehansion.





### Compare for loop vs while loop for escaping an iteration for certain condition.
#def countLeading0(A) :
#    COUNT=0
#    for I in range(len(A)) :
#        if A[I]==0 :
#            COUNT+=1
#        else :
#            break
#    return COUNT
#print "For loop for counting leading zeros, %s sec" % timeFn(countLeading0,TV[0])
### Use while loop for escaping a loop for certain condition is faster than for loop







### Boolean function for checking row echelon form, by using while loop.
#def isEchelon(L) :
#    I=0
#    while I<len(L) :
#        if countLeading0(L[I])<I :
#            B=False
#            break
#        else :
#            B=True
#        I+=1
#    return B
#print isEchelon([[1,1,1],[0,1,1],[0,0,1]])
#print "Function for checking wether a list is an echelon form, %s sec" % timeFn(isEchelon,[[1,1,1],[0,1,1],[0,0,1]])  
### Does not do better than for loop. Generally, we want use while loop when have more than one condition and no inner condition.




### compare list comprehension vs for loop
#def listComp(L) :
#    newlist = [X for X in L if "a" in X]    
#    return newlist 
#print "Append list with list comprehension, %s sec" % timeFn(listComp,fruits)

#def listForloop(L) :
#    newlist = []
#    for X in L:
#        if "a" in X:
#            newlist.append(X)
#    return newlist
#print "Append list with for loop, %s sec" % timeFn(listForloop,fruits)
### list comprehansion is faster than using for loop to iterable object




### Swapping element of list of list
### The python interpretation of swapping array element. This takes more time than normal way which assgin an element E1 to a variable then overwrite the E1 with E2.
#def swapRowS(A,V1,V2) :
#    A[V1],A[V2]=A[V2],A[V1] 
#    return A
#print "Swapping row vector in special way %s sec" % timeFn(swapRowS,TV,0,2)
#print swapRowS(TV,0,2)




### Array operation
### Using array is somehow not that flexible such like it doesn't accept array of array. 
#def fileToArray(F) :
#    with open(F,'rb') as FO :
#        AA=array('c',[])
#        for LINE in FO :
#        #AA.fromfile(FO,3)
#            AA.fromstring(LINE)
#    FO.close()
#    return AA
#print fileToArray("matrix.data") 
#print "String operation with using array built-in, %s sec" % timeFn(fileToArray,"matrix.data")
