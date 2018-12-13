
# coding: utf-8

# In[55]:


from numpy import *


# In[56]:


def hamiltonian(i) :
    def promising(i) :
        if i==n-1 and not W[vindex[n-1]][vindex[0]] :
            switch = False
        elif i>0 and not W[vindex[i-1]][vindex[i]] :
            switch = False
        else :
            switch = True
            for j in range(1,i) :
                if vindex[i] == vindex[j] :
                    switch = False
                    break
        return switch
    #print('promising(',i,')=',promising(i))
    if promising(i) :
        if i == n-1 :
            for j in range(n-1) :
                print(vindex[j], ', ',end='')
            print()
        else :
            for j in range(2,n+1) :
                #print('vindex[',i+1,']=',j)
                vindex[i+1] = j
                #print('hamilton',i+1)
                hamiltonian(i+1)
            #print('end>>>',vindex)


# In[57]:


I = True
O = False
n = 5
W = array([ [O,O,O,O,O,O],
            [O,I,I,O,O,I],
            [O,I,I,I,I,I],
            [O,O,I,I,I,O],
            [O,O,I,I,I,O],
            [O,I,I,O,O,I] ])
vindex = zeros((n,),dtype=int64)


# In[63]:


vindex


# In[59]:


vindex[0] = 1
hamiltonian(0)


# In[60]:


I = True
O = False
n = 8
W = array([ [O,O,O,O,O,O,O,O,O],
            [O,I,I,I,O,O,O,I,I],
            [O,I,I,I,O,O,O,I,I],
            [O,I,I,I,I,O,I,O,O],
            [O,O,O,I,I,I,O,O,O],
            [O,O,O,O,I,I,I,O,O],
            [O,O,O,I,O,I,I,I,O],
            [O,I,I,O,O,O,I,I,I],
            [O,I,I,O,O,O,O,I,I] ])
vindex = zeros((n,),dtype=int64)


# In[61]:


vindex


# In[62]:


vindex[0] = 1
hamiltonian(0)


# In[22]:


cnt

