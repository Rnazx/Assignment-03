#We have Ax=b and have to find x
#The Augmented matrix is stored in the txt file
#function for storing the augmented matrix matrix(A) from a file
def storeA(st,col):
    X=[]
    T=[]
    col=int(col)
    with open(st,'r+') as file:
        i=0
        while i<3:
            s=file.readline()
            p=s.split()
            j=0
            while (j<col):
                T.append(float(p[j]))
                j=j+1
            X.append(T)
            T=[]
            i=i+1 
        return X
#function for partial pivoting
def parpiv(A):
    n=len(A)
    for k in range(n-1):
        if A[k][k]==0:
            for l in range(k+1,n):
                if abs(A[l][k])>abs(A[k][k]):
                    A[k],A[l]=A[l],A[k]
                else : continue
        else : continue
#function for Gauss jordan method
def GauJo(Aug):
    n=len(Aug)
    m=len(Aug[1])
    k=0
    flag=True
    while (k<n) and flag:
        parpiv(Aug)
        piv = Aug[k][k]
        for l in range(k,m):
            Aug[k][l]/=piv
        for i in range(n):
            if i==k or Aug[i][k]==0: continue
            else: 
                factor=Aug[i][k]
                for j in range(k,m):
                    Aug[i][j]-=factor*Aug[k][j]
        k+=1
        #to check if unique solution exists
        l=0
        for i in range(n):
            if A[n-1][i]==0:
                l+=1
        if (l==3):
            flag=False
            if (A[n-1][n]!=0): print("The system has no solution")
            else: 
                print("The system has no unique solution")
                print("One of the infinite solutions is")
#function for matrix multiplication
def matmul(A,B):
    n=len(A)
    prod=[[] for x in range(n)]
    t=0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                t+=A[i][k]*B[k][j]
            prod[i].append(t)
            t=0
        j=0
    return prod
#function for identity matrix of order n 
def iden(n):
    I=[[int(x==y) for x in range(n)] for y in range(n)]
    return I
#function for transpose of a matrix
def Tr(A):
    T = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))] 
    return T
#function for augmenting a matrix upon the other
def augment(A,b):
    X=Tr(A)+Tr(b)
    return Tr(X)
#function to print matrix
def printmat(A):
    for i in range(3):
        if(i>0):
            print('\n')
        for j in range(3):
            print(A[i][j],end="   ")
    print('\n')
#Question 1
print("Question 1 :")
A=storeA("Q1.txt",4)
s=len(A)
GauJo(A)
print("x=",A[0][s])
print("y=",A[1][s])
print("z=",A[2][s])
print()
#Question 2
print("Question 2 :")
A=storeA("Q2.txt",4)
s=len(A)
GauJo(A)
print("x=",A[0][s])
print("y=",A[1][s])
print("z=",A[2][s])
print()
#Question 3
print("Question 3 :")
A=storeA("Q3.txt",3)
Au=augment(A,iden(3))
GauJo(Au)
print("The matrix is : ")
printmat(A)
Ainv=[[Au[i][j] for j in range(3,6)] for i in range(3)]
print("The inverse of the matrix is : ")
printmat(Ainv)
if (matmul(A,Ainv)==iden(3)):
    print("The property A*Ainv=I is verified")
else : print("There is some error in calculating the inverse" )
#Output
'''
Question 1 :
x= 3.0
y= 1.0
z= -2.0

Question 2 :       
x= -2.0
y= -2.0
z= 1.0

Question 3 :
The matrix is : 
1.0   -3.0   7.0   

-1.0   4.0   -7.0

-1.0   3.0   -6.0

The inverse of the matrix is :
-3.0   3.0   -7.0

1.0   1.0   0.0

1.0   0.0   1.0

The property A*Ainv=I is verified'''