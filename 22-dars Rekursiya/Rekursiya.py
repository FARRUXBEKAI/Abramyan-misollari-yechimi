#!/usr/bin/env python
# coding: utf-8

# # 8/07/2022
# 
# # Python asoslari
# 
# # 22-dars : Rekursiya bilan ishlash
# 
# # Muallif: Farrux Sotivoldiyev

# ![image.png](attachment:image.png)

# In[1]:


# Recur1
def fact(n):
    if n==1:
        return 1
    else:
        return n * fact(n-1)
    
print(fact(5))


# ![image.png](attachment:image.png)

# In[6]:


# Recur2
def fact2(n):
    if n==1 or n==0:
        return 1
    else:
        return n * fact2(n-2)
    
print(fact2(5))


# ![image.png](attachment:image.png)

# In[8]:


# Recur3
def Power(x,n):
    if n==0:
        return 1
    
    elif n<0:
        return 1 / Power(x,-n)
    
    elif n%2==0:
        return Power(x,n/2) ** 2 
    
    elif n%2==1:
        return Power(x,n-1) * x
        
print(Power(5,2))


# ![image.png](attachment:image.png)

# In[3]:


# Recur4
def Fib1(N):
    if N==1 or N==2:
        return 1
    else:
        return Fib1(N-2) + Fib1(N-1)
    
print(Fib1(10))


# ![image.png](attachment:image.png)

# In[22]:


# Recur5
def Fib1(N):
    fibonachi = [1,1]
    if N-1 <= len(fibonachi)-1:
        return fibonachi[N-1]
    else:
        return Fib1(N-2) + Fib1(N-1)
    
print(Fib1(10))


# ![image.png](attachment:image.png)

# In[24]:


# Recur6
def Combin1(N,K):
    if K==0 or N==K:
        return 1
    else:
        return Combin1(N-1,K) + Combin1(N-1,K-1)
print(Combin1(5,3))

