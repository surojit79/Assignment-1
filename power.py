import numpy as np
A=np.array([[2,-1,0],[-1,2,-1],[0,-1,2]])
X=np.array([[0],[1],[0]])
for i in range(3):
    Y=np.matmul(A,X)
    k=0
    for j in range(3):
        if(k<abs(Y[j])):
            k=Y[j]
X1=Y/k
iteration=1
while(abs(X1[0]-X[0])>=0.01 or abs(X1[1]-X[1])>=0.01 or abs(X1[2]-X[2])>=0.01):
    X=X1
    for i in range(3):
        Y=np.matmul(A,X)
        k=0
        for j in range(3):
            if(k<abs(Y[j])):
                k=Y[j]
	        
        X1=Y/k
    iteration=iteration+1
print(k,X1)         
                      

