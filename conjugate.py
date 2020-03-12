import numpy as np 
A=np.array([[0.2,0.1,1,1,0],[0.1,4,-1,1,-1],[1,-1,60,0,-2],[1,1,0,8,4],[0,-1,-2,4,700]])
b=np.array([1,2,3,4,5])
y=np.array([7.859713071,0.422926408,-0.073592239,-0.540643016,0.010626163])
x=np.zeros(5)
r=b-np.matmul(A,x)
d=r
for i in range(100):
    
    s=np.matmul(np.transpose(r),r)/np.matmul(np.transpose(d),np.matmul(A,d))
    x=x+s*d
    t=r-s*np.matmul(A,d)
    flag=0
    for j in range(5):
        if(abs(x[j]-y[j])>=0.01):
            flag=1
    if(flag==0):
        break
    
    c=np.matmul(np.transpose(t),t)/np.matmul(np.transpose(r),r)
    r=t
    d=r+c*d
   
print(x,'iteration=',i+1)
           
         

