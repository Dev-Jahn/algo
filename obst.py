import numpy as np

def obst(n,p,R):
    A = np.pad(np.diag(p),(1,0),mode='constant',constant_values=(0))
    A = np.array(list(A.ravel()) + [0]*(n+1)).reshape((n+2,n+1))
    R = np.pad(np.diag(np.arange(1,n+1)),(1,0),mode='constant',constant_values=(0))
    for diag in range(1,n):
        for i in range(1,n-diag+1):
            j = i+diag
            mlist = [A[i,k-1]+A[k+1,j] for k in range(i,j+1)]
            A[i,j] = min(mlist)+sum(p[i-1:j])
            R[i,j] = i+np.argmin(mlist)
    return A[1,n]

n = 4
p = [3/8,3/8,1/8,1/8]
R = np.zeros((n+1,n+1))
print('minimum cost:',obst(n,p,R))

n = 6
p = [2/16,1/16,3/16,2/16,5/16,3/16]
R = np.zeros((n+1,n+1))
print('minimum cost:',obst(n,p,R))
