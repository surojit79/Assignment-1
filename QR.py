import numpy as np 
import math
A=np.array([[5,-2],[-2,8]])
x,X=np.linalg.eigh(A)
ev1=x[1]
ev2=x[0]
while abs((A[0][1])>=0.00001 or abs(A[1][0])>=0.00001):
    Q,R=np.linalg.qr(A)
    A=np.matmul(R,Q)
QRv1=A[0,0]
QRv2=A[1,1]
	
print(ev1,ev2)
print(QRv1,QRv2)
