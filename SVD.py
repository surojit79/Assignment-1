import numpy as np
import time 
from numpy import linalg as LA
A=np.array([[0,1,1],[0,1,0],[1,1,0],[0,1,0],[1,0,1]])
st1=time.time()
C=np.matmul(A,np.transpose(A))
D=np.matmul(np.transpose(A),A)
x,X=np.linalg.eigh(C)
y,Y=np.linalg.eigh(D)
u=np.zeros(5)
v=np.zeros(3)
U=np.zeros((5,5))
V=np.zeros((3,3))
for i in range(5):
    u[i]=x[-i-1]
    for k in range(5):
        U[k][-i-1]=X[k][i]

for j in range(3):
    v[j]=y[-j-1]
    for l in range(3):
        V[l][-j-1]=Y[l][j]
#print("time before svd: ", time.time()-st1)
S=np.matmul(np.transpose(U),np.matmul(A,V))
print(U)
print(V)
print(S)
print("time before svd: ", time.time()-st1)

st2=time.time()
U1, S1, V1=np.linalg.svd(A)
print(U1)
print(V1)
print(S1)
print("time after svd: ", time.time()-st2)


