import numpy as np
s=np.array([[1,0.67,0.33],[0.45,1,0.55],[0.67,0.33,1]])
t=np.array([2,2,2])
print(np.linalg.solve(s,t))
