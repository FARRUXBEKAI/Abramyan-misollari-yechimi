#!/usr/bin/env python
# coding: utf-8

# # 12/05/2022
# 
# # Python asoslari
# 
# # 17-dars : Matritsa bilan ishlash
# 
# # Muallif: Farrux Sotivoldiyev

# ## 67 - 100 gacha 👇🤏 

# In[3]:


# Matrix67
from random import randint
m = int(input("m = "))
n = int(input("n = "))
matrix = [[randint(-1,9) for i in range(n)] for _ in range(m)]
for i in matrix:
    print(*i)
print()

i = 0
while i<n:
    k = 0
    for j in range(m):
        if matrix[j][i]>0:
            k += 1
    if k==m:
        for l in matrix:
            del l[i]
        n -= 1
    else:
        i += 1
        
for i in matrix:
    print(*i)


# In[4]:


# Matrix68
from random import randint
m = int(input("m = "))
n = int(input("n = "))
matrix = [[randint(1,9) for i in range(n)] for _ in range(m)]
for i in matrix:
    print(*i)
print()

k = int(input("k = "))
temp = [0 for _ in range(n)]
for i in range(m):
    if i==k:
        matrix.insert(i,temp)
        break
        
for i in matrix:
    print(*i)


# In[6]:


# Matrix69
from random import randint
m = int(input("m = "))
n = int(input("n = "))
matrix = [[randint(1,9) for i in range(n)] for _ in range(m)]
for i in matrix:
    print(*i)
print()

k = int(input("k = "))
for i in range(n):
    if i==k:
        for j in range(m):
            matrix[j].insert(i+1,1)
        break
        
for i in matrix:
    print(*i)


# In[7]:


# Matrix70
from random import randint
m = int(input("m = "))
n = int(input("n = "))
matrix = [[randint(1,9) for i in range(n)] for _ in range(m)]
for i in matrix:
    print(*i)
print()

for i in range(m):
    if i==0:
        maxi = max(matrix[i])
        index = i
    elif maxi<max(matrix[i]):
        maxi = max(matrix[i])
        index = i
temp = matrix[index].copy()
matrix.insert(index,temp)
       
for i in matrix:
    print(*i)


# In[10]:


# Matrix71
from random import randint
m = int(input("m = "))
n = int(input("n = "))
matrix = [[randint(1,9) for i in range(n)] for _ in range(m)]
for i in matrix:
    print(*i)
print()

mini = matrix[0][0]
index = 0
for i in range(n):
    for j in range(m):
        if mini>matrix[j][i]:
            mini = matrix[j][i]
            index = i
for i in range(m):
    matrix[i].insert(index+1,matrix[i][index])
       
for i in matrix:
    print(*i)


# In[11]:


# Matrix72
from random import randint
m = int(input("m = "))
n = int(input("n = "))
matrix = [[randint(-2,9) for i in range(n)] for _ in range(m)]
for i in matrix:
    print(*i)
print()

for i in range(n):
    k = 0
    for j in range(m):
        if matrix[j][i]>0:
            k += 1
    if k==m:
        for k in range(m):
            matrix[k].insert(i,1)
        break
        
for i in matrix:
    print(*i)


# In[19]:


# Matrix73
from random import randint
m = int(input("m = "))
n = int(input("n = "))
matrix = [[randint(-9,2) for i in range(n)] for _ in range(m)]
for i in matrix:
    print(*i)
print()

index = -1
for i in range(n):
    k = 0
    for j in range(m):
        if matrix[j][i]<0:
            k += 1
    if k==m:
        index = i
if index!=-1:
    for k in range(m):
        matrix[k].insert(index+1,0)
    
for i in matrix:
    print(*i)


# In[1]:


# Matrix74
from random import randint
m = int(input("m = "))
n = int(input("n = "))
matrix = [[randint(1,9) for _ in range(n)]  for _ in range(m)]
for i in matrix:
    print(*i)
print()

def circle_max(m,n,matrix):
    maxi = max(matrix[0])
    for i in range(1,m):
        if max(matrix[i]) > maxi:
            maxi = max(matrix[i])

    for i in range(m):
        matrix[i].insert(0,maxi)
        matrix[i].append(maxi)

    temp = [maxi for _ in range(n+2)]
    matrix.insert(0,temp)
    matrix.append(temp)
    return matrix

def lok_min(m,n,matrix):
    matrix = circle_max(m,n,matrix)
    index = []
    for i in range(1,m+1):
        for j in range(1,n+1):
            if matrix[i][j-1]>matrix[i][j]<matrix[i][j+1] and matrix[i-1][j]>matrix[i][j]<matrix[i+1][j]:
                index.append(i)
                index.append(j)
    for i in range(0,len(index),2):
        matrix[index[i]][index[i+1]] = 0
    return matrix
    
def asliga_qaytar(m,n,matrix):
    matrix = lok_min(m,n,matrix)
    del matrix[0]
    del matrix[-1]
    for i in range(m):
        del matrix[i][0]
        del matrix[i][-1]
    return matrix

for i in asliga_qaytar(m,n,matrix):
    print(*i)


# In[6]:


# Matrix75
from random import randint
m = int(input("m = "))
n = int(input("n = "))
matrix = [[randint(1,9) for _ in range(n)]  for _ in range(m)]
for i in matrix:
    print(*i)
print()

def circle_min(m,n,matrix):
    mini = min(matrix[0])
    for i in range(1,m):
        if min(matrix[i]) < mini:
            mini = min(matrix[i])

    for i in range(m):
        matrix[i].insert(0,mini)
        matrix[i].append(mini)

    temp = [mini for _ in range(n+2)]
    matrix.insert(0,temp)
    matrix.append(temp)
    return matrix

def lok_max(m,n,matrix):
    matrix = circle_min(m,n,matrix)
    index = []
    for i in range(1,m+1):
        for j in range(1,n+1):
            if matrix[i][j-1]<matrix[i][j]>matrix[i][j+1] and matrix[i-1][j]<matrix[i][j]>matrix[i+1][j]:
                index.append(i)
                index.append(j)
    for i in range(0,len(index),2):
        matrix[index[i]][index[i+1]] = 0
    return matrix

def asliga_qaytar(m,n,matrix):
    matrix = lok_max(m,n,matrix)
    del matrix[0]
    del matrix[-1]
    for i in range(m):
        del matrix[i][0]
        del matrix[i][-1]
    return matrix

for i in asliga_qaytar(m,n,matrix):
    print(*i)


# In[21]:


# Matrix76
from random import randint
m = int(input("m = "))
n = int(input("n = "))
matrix = [[randint(-2,9) for i in range(n)] for _ in range(m)]
for i in matrix:
    print(*i)
print()

for _ in range(m):
    for j in range(m-1):
        if matrix[j][0]>matrix[j+1][0]:
            matrix[j],matrix[j+1] = matrix[j+1],matrix[j]
        
for i in matrix:
    print(*i)


# In[28]:


# Matrix77
from random import randint
m = int(input("m = "))
n = int(input("n = "))
matrix = [[randint(-2,9) for i in range(n)] for _ in range(m)]
for i in matrix:
    print(*i)
print()

for _ in range(n):
    for j in range(n-1):
        if matrix[-1][j]<matrix[-1][j+1]:
            for k in range(m):
                matrix[k][j],matrix[k][j+1] = matrix[k][j+1],matrix[k][j]
        
for i in matrix:
    print(*i)


# In[37]:


# Matrix78
from random import randint
m = int(input("m = "))
n = int(input("n = "))
matrix = [[randint(-5,9) for i in range(n)] for _ in range(m)]
for i in matrix:
    print(*i)
print()

for _ in range(m):
    for i in range(m-1):
        if min(matrix[i])<min(matrix[i+1]):
            matrix[i],matrix[i+1] = matrix[i+1],matrix[i]
        
for i in matrix:
    print(*i)


# In[30]:


# Matrix79
from random import randint
m = int(input("m = "))
n = int(input("n = "))
matrix = [[randint(-2,9) for i in range(n)] for _ in range(m)]
for i in matrix:
    print(*i)
print()

for _ in range(n):
    for i in range(n-1):
        maxi1 = matrix[0][i]
        maxi2 = matrix[0][i+1]
        for k in range(1,m):
            if maxi1<matrix[k][i]:
                maxi1 = matrix[k][i]
        for k in range(1,m):
            if maxi2<matrix[k][i+1]:
                maxi2 = matrix[k][i+1]
        if maxi1>maxi2:
            for k in range(m):
                matrix[k][i],matrix[k][i+1] = matrix[k][i+1],matrix[k][i]
        
for i in matrix:
    print(*i)


# ### 4.Kvadrat matritsaning diagonallari

# In[35]:


# Matrix80
from random import randint
m = int(input("m = "))
matrix = [[randint(1,9) for i in range(m)] for _ in range(m)]
for i in matrix:
    print(*i)

s = 0
for i in range(m):
    for j in range(m):
        if i-j==0:
            s += matrix[i][j]
print(s)


# In[8]:


# Matrix81
from random import randint
m = int(input("m = "))
matrix = [[randint(1,9) for i in range(m)] for _ in range(m)]
for i in matrix:
    print(*i)

s = 0
for i in range(m):
    for j in range(m):
        if i+j==m-1:
            s += matrix[i][j]
print(s)


# In[54]:


# Matrix82 # Asosiy dioganalga nisbatan
from random import randint
m = int(input("m = "))
matrix = [[randint(1,9) for i in range(m)] for _ in range(m)]
for i in matrix:
    print(*i)

x = m-1  
for k in range((m-1)*2):
    s = 0
    y = 0
    if m-1==k:
        x = 1
    if m-1>k:
        for i in range(x,m):
            s += matrix[y][i]
            y+=1
            
        x -= 1
    else:
        for i in range(x,m):
            s += matrix[i][y]
            y+=1
        x += 1
    print(s) 


# In[64]:


# Matrix83 # Yordamchi dioganalga nisbatan
from random import randint
m = int(input("m = "))
matrix = [[randint(1,9) for i in range(m)] for _ in range(m)]
for i in matrix:
    print(*i)

x = 0
for _ in range((m-1)*2):
    s = 0
    if m-1==_:
        x = 1
    if m-1>_:
        y = 0
        for i in range(x,-1,-1):
            s += matrix[y][i]
            y+=1
        x += 1
    else:
        y = m-1
        for i in range(x,m):
            s += matrix[i][y]
            y-=1
        x += 1
    print(s) 


# In[68]:


# Matrix84 
from random import randint
m = int(input("m = "))
matrix = [[randint(1,9) for i in range(m)] for _ in range(m)]
for i in matrix:
    print(*i)

x = m-1  
for k in range((m-1)*2):
    s = 0
    y = 0
    if m-1==k:
        x = 1
    if m-1>k:
        for i in range(x,m):
            s += matrix[y][i]
            y+=1
            
        x -= 1
    else:
        for i in range(x,m):
            s += matrix[i][y]
            y+=1
        x += 1
    print(s/(y)) 


# In[91]:


# Matrix85
from random import randint
m = int(input("m = "))
matrix = [[randint(1,9) for i in range(m)] for _ in range(m)]
for i in matrix:
    print(*i)

x = 0
for _ in range((m-1)*2):
    s = 0
    if m-1==_:
        x = 1
    if m-1>_:
        y = 0
        for i in range(x,-1,-1):
            s += matrix[y][i]
            y+=1
        print(s/y)
        x += 1
    else:
        y = m
        for i in range(x,m):
            y-=1
            s += matrix[i][y]
        print(s/(abs(i-y)+1))
        x += 1


# In[133]:


# Matrix86
from random import randint
m = int(input("m = "))
matrix = [[randint(1,9) for i in range(m)] for _ in range(m)]
for i in matrix:
    print(*i)

x = m-1  
for k in range((m-1)*2):
    s = 0
    y = 0
    if m-1==k:
        x = 1
    if m-1>k:
        for i in range(x,m):
            if y==0:
                mini = matrix[y][i]
            elif mini>matrix[y][i]:
                mini = matrix[y][i]
            y+=1
        x -= 1
    else:
        for i in range(x,m):
            if y==0:
                mini = matrix[i][y]
            elif mini>matrix[i][y]:
                mini = matrix[i][y]
            y+=1
        x += 1
    print(mini) 


# In[135]:


# Matrix87
from random import randint
m = int(input("m = "))
matrix = [[randint(1,9) for i in range(m)] for _ in range(m)]
for i in matrix:
    print(*i)

x = 0
for _ in range((m-1)*2):
    s = 0
    if m-1==_:
        x = 1
    if m-1>_:
        y = 0
        for i in range(x,-1,-1):
            if y==0:
                maxi = matrix[y][i]
            elif maxi<matrix[y][i]:
                maxi = matrix[y][i]
            y+=1
        x += 1
    else:
        y = m-1
        for i in range(x,m):
            if y==m-1:
                maxi = matrix[i][y]
            elif maxi<matrix[i][y]:
                maxi = matrix[i][y]
            y-=1
        x += 1
    print(maxi) 


# In[16]:


# Matrix88
from random import randint
m = int(input("m = "))
matrix = [[randint(1,9) for i in range(m)] for _ in range(m)]
for i in matrix:
    print(*i)
print()  

for i in range(m):
    for j in range(i+1):
        matrix[i][j] = 0
    
for i in matrix:
    print(*i)


# In[19]:


# Matrix89
from random import randint
m = int(input("m = "))
matrix = [[randint(1,9) for i in range(m)] for _ in range(m)]
for i in matrix:
    print(*i)
print()  

for i in range(m):
    for j in range(m-i):
        matrix[i][j] = 0
    
for i in matrix:
    print(*i)


# In[22]:


# Matrix90
from random import randint
m = int(input("m = "))
matrix = [[randint(1,9) for i in range(m)] for _ in range(m)]
for i in matrix:
    print(*i)
print()  

for i in range(m):
    for j in range(m-1,m-i-2,-1):
        matrix[i][j] = 0
    
for i in matrix:
    print(*i)


# In[29]:


# Matrix91
from random import randint
m = int(input("m = "))
matrix = [[randint(1,9) for i in range(m)] for _ in range(m)]
for i in matrix:
    print(*i)
print()  

for i in range(m):
    for j in range(m-1,(i-1),-1):
        matrix[i][j] = 0
    
for i in matrix:
    print(*i)


# In[59]:


# Matrix92
from random import randint
m = int(input("m = "))
matrix = [[randint(1,9) for i in range(m)] for _ in range(m)]
for i in matrix:
    print(*i)
print()

for i in range((m%2!=0)+m//2):
    for j in range(i,m-i):
            matrix[i][j]=0
            
for i in matrix:
    print(*i)


# In[60]:


# Matrix93
from random import randint
m = int(input("m = "))
matrix = [[randint(1,9) for i in range(m)] for _ in range(m)]
for i in matrix:
    print(*i)
print()

for i in range(m-1,(m%2!=0)+m//2-2,-1):
    for j in range(m-i-1,i+1):
            matrix[j][i]=0
            
for i in matrix:
    print(*i)


# In[61]:


# Matrix94
from random import randint
m = int(input("m = "))
matrix = [[randint(1,9) for i in range(m)] for _ in range(m)]
for i in matrix:
    print(*i)
print()

for i in range((m%2!=0)+m//2):
    for j in range(i,m-i):
            matrix[j][i]=0
            
for i in matrix:
    print(*i)


# In[62]:


# Matrix95
from random import randint
m = int(input("m = "))
matrix = [[randint(1,9) for i in range(m)] for _ in range(m)]
for i in matrix:
    print(*i)
print()

for i in range(m-1,(m%2!=0)+m//2-2,-1):
    for j in range(m-i-1,i+1):
            matrix[i][j]=0
            
for i in matrix:
    print(*i)


# In[66]:


# Matrix96
from random import randint
m = int(input("m = "))
matrix = [[randint(1,9) for i in range(m)] for _ in range(m)]
for i in matrix:
    print(*i)
print()

for i in range(m-1):
    for j in range(i+1,m):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
            
for i in matrix:
    print(*i)


# In[71]:


# Matrix97
from random import randint
m = int(input("m = "))
matrix = [[randint(1,9) for i in range(m)] for _ in range(m)]
for i in matrix:
    print(*i)
print()

for i in range(m-1):
    for j in range(m-i-1):
            matrix[i][j],matrix[m-j-1][m-i-1]=matrix[m-j-1][m-i-1],matrix[i][j]
            
for i in matrix:
    print(*i)


# In[41]:


# Matrix98 1-usul
from random import randint
m = int(input("m = "))
matrix = [[randint(1,9) for i in range(m)] for _ in range(m)]
for i in matrix:
    print(*i)
print()

for i in range((m%2!=0)+m//2):
    x = (m%2!=0)+m//2                  #bundan maqsad oxirgi sikldagi birhilliklardan qochish
    for j in range((i==m-x)*(-x)+m):
        matrix[i][j],matrix[m-i-1][m-j-1]=matrix[m-i-1][m-j-1],matrix[i][j]     
print()
for k in matrix:
    print(*k)
    
# Matrix98 2-usul
from random import randint
m = int(input("m = "))
matrix = [[randint(1,9) for i in range(m)] for _ in range(m)]
for i in matrix:
    print(*i)
print()

matrix.reverse()
for i in range(m):
    matrix[i].reverse()
    
print()
for k in matrix:
    print(*k)
    
# Matrix98 3-usul
from random import randint
m = int(input("m = "))
matrix = [[randint(1,9) for i in range(m)] for _ in range(m)]
for i in matrix:
    print(*i)
print()
    
matrix = [[matrix[i][j] for j in range(m-1,-1,-1)] for i in range(m-1,-1,-1)]

for k in matrix:
    print(*k)


# In[72]:


# Matrix99 
from random import randint
m = int(input("m = "))
matrix = [[randint(1,9) for i in range(m)] for _ in range(m)]
for i in matrix:
    print(*i)
print()
    
matrix = [[matrix[i][j] for i in range(m)] for j in range(m-1,-1,-1)]

for k in matrix:
    print(*k)


# In[1]:


# Matrix100 
from random import randint
m = int(input("m = "))
matrix = [[randint(1,9) for i in range(m)] for _ in range(m)]
for i in matrix:
    print(*i)
print()
    
matrix = [[matrix[i][j] for i in range(m-1,-1,-1)] for j in range(m)]

for k in matrix:
    print(*k)


# In[3]:


# 74-75 ishlash kerak

