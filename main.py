#!/usr/bin/env python
# coding: utf-8

# ### Importing Dependencies

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
from random import uniform as rnd


# ### Setting the Problem and Algorithm Parameters

# In[ ]:


P      = 20
WIDTH  = 5
HEIGHT = 5
W      = 0.6
C1     = 0.1 
C2     = 0.1

EPOCH  = 30


# ### Init Population function

# In[ ]:


def init_folk(p, w, h):
    X = [[round(rnd(0,w),3),round(rnd(0,h),3)] for i in range(p)]
    V = [[round(rnd(0,0.1),3),round(rnd(0,0.1),3)] for i in range(p)]
    return X, V


# ### Update Positions Function

# In[ ]:


def update_positions(X,Vnew):
    X = [[round(i[0][0]+i[1][0],3),round(i[0][1]+i[1][1],3)]for i in zip(X,Vnew)]
    return X


# ### Update Velocities Function

# In[ ]:


def update_velocities(X , V, p_best, g_best):
    r1 = round(rnd(0,1),3)
    r2 = round(rnd(0,1),3)
    for i in range(P):
        new_vx = (W*V[i][0]) + (C1*r1*(p_best[i][0]-X[i][0])) + (C2*r2*(g_best[0]-X[i][0]))
        new_vy = (W*V[i][1]) + (C1*r1*(p_best[i][1]-X[i][1])) + (C2*r2*(g_best[1]-X[i][1]))
        V[i][0]=new_vx
        V[i][1]=new_vy
    return V


# ### Fitness Function

# In[ ]:


def fitness(x, y):
    val = (x-3.14)**2 + (y-2.72)**2 + np.sin(3*x+1.41) + np.sin(4*y-1.73)
    return round(val,3)


# In[ ]:


def bool_min(lst1,lst2,p1,p2):
    lst = []
    for i in range(len(lst1)):
        condition = True if lst1[i]<lst2[i] else False
        if condition:
            lst.append(p1[i])
        else:
            lst.append(p2[i])
    return lst


# ### Main

# In[ ]:


if __name__ == "__main__":
    X, V = init_folk(P, WIDTH, HEIGHT)
    p_best = X.copy()
    pbest_obj = [fitness(i[0], i[1]) for i in X]
    g_best = p_best[pbest_obj.index(min(pbest_obj))]
    gbest_obj = min(pbest_obj)
    while EPOCH:
        V = update_velocities(X , V, p_best, g_best)
        X = update_positions(X,V)
        obj = [fitness(i[0], i[1]) for i in X]
        p_best = bool_min(pbest_obj, obj, p_best, X)
        f = [fitness(i[0], i[1]) for i in p_best]
        g_best = p_best[f.index(min(f))]
        gbest_obj = min(f)
        EPOCH-=1
        
        img = np.full((WIDTH,HEIGHT,3), 255, np.uint8)
        plt.title(str(EPOCH+1))
        plt.imshow(img)
        plt.scatter([i[0] for i in X],[i[1] for i in X])
        plt.axis([0,WIDTH,0,HEIGHT])
        plt.pause(0.5)
        plt.clf()
    plt.imshow(img)
    plt.scatter([i[0] for i in X],[i[1] for i in X])
    plt.axis([0,WIDTH,0,HEIGHT])
    plt.show()


# In[ ]:

print(g_best)


