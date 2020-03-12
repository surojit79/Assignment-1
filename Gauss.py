import numpy as np 
s=np.array([[0.2,0.1,1,1,0],[0.1,4,-1,1,-1],[1,-1,60,0,-2],[1,1,0,8,4],[0,-1,-2,4,700]])
t=np.array([1,2,3,4,5])
y=np.array([7.859713071,0.422926408,-0.073592239,-0.540643016,0.010626163])
x=np.zeros(5)  
count=0
while(abs(y[0]-x[0])>=0.01 or abs(y[1]-x[1])>=0.01 or abs(y[2]-x[2])>=0.01 or abs(y[3]-x[3])>=0.01 or abs(y[4]-x[4])>=0.01):
    for i in range(5):
        p=t[i]
        for j in range(5):
            if (j!=i):
                p=p-s[i][j]*x[j]
                
        x[i]=p/s[i][i]
        print(x)
    count=count+1
    print(count)
print(x,count)
           
