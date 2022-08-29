#!/usr/bin/env python
# coding: utf-8

# # 21/09/2022
# 
# # Python asoslari
# 
# # 28-dars : funksiya(global,local,nonlocal)
# 
# # Muallif: Farrux Sotivoldiyev

# # Lokal

# In[48]:


n = 0
def local():
    p = 0
    for i in range(11):
        p += i
    print(p)
local()
print(n)


# In[125]:


# local p ni tashqaridan chaaqirib bo'lmaydi
print(p)


# # Global

# In[43]:


n = 0
def glob():
    global n
    for i in range(11):
        n += i
    print(n)
glob()
print(n)


# In[44]:


print(n)


# # nonlocal

# In[4]:


def nonloc():
    k = 3
    def nonloc2():
        nonlocal k
        k = 9
    nonloc2()
    return k

nonloc()


# # Funksiya qo'shimcha
# 

# In[80]:


def katta(satr):
    return satr.upper()

kichik,qale = katta,katta

print(kichik("Salom"))
print(qale("Alik"))


# In[81]:


def bir(a,*b):
    print(a,b)
bir(1,2,3,4,5)


# In[88]:


def bir(a,**b):
    print(a,b)
bir(a=1,o=3,j=2,v=8,k=9)


# In[89]:


def bir(a,*b,**c):
    print(a,b,c)
bir(1,2,44,5,65,o=3,j=2,v=8,k=9)


# In[8]:


x = [1,2,3,4,5]
print(id(x))
def massiv(x):
    x[0] = 10101010101
    x += [6,7,8]
    print(x)
    print(id(x))
massiv(x)
print(x)
print(id(x))


# In[9]:


x = [1,2,3,4,5]
print(id(x))
def massiv(x):
    x[0] = 10101010101
    x = x + [6,7,8]
    print(x)
    print(id(x))
massiv(x)
print(x)
print(id(x))


# # Yield orqali

# In[25]:


def yield_orqali(n):
    for i in range(n):
        yield i
        
x = yield_orqali(5)


# In[26]:


for i in x:
    print(i)


# # Return orqali

# In[20]:


def return_orqali(n):
    for i in range(n):
        return i
x = return_orqali(5)


# In[21]:


print(x)


# In[63]:


import math
dir(math)

