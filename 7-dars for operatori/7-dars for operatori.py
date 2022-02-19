#!/usr/bin/env python
# coding: utf-8

# # 19/02/2022
# 
# # Python asoslari
# 
# # 7-dars: For sikl operatori
# 
# # Muallif: Farrux Sotivoldiyev

# In[35]:


#for1
k = int(input("k = "))
n = int(input("n = "))
for i in range(n):
    print(k)


# In[47]:


#for2
a = int(input("a = "))
b = int(input("b = "))
k = 0
for i in range(a,b+1):
    k += 1
    print(i)
print(k,"ta son")


# In[46]:


#for3
a = int(input("a = "))
b = int(input("b = "))
k = 0
for i in range(b-1,a,-1):
    k += 1
    print(i)
print(k,"ta son")


# In[45]:


#for4
narx = float(input("Narx = "))
for i in range(1,11):
    print(f"{i} kg konfet {narx*i} so'm")


# In[1]:


#for5
narx = float(input("Narx = "))
for i in range(1,11):
    print(f"{i/10:.1f} kg konfet {i/10*narx:.1f} so'm")


# In[5]:


#for6
narx = float(input("Narx = "))
for i in range(12,21):
    print(f"{i/10:.1f} kg konfet {narx*i/10:.1f} so'm")


# In[42]:


#for7
a = int(input("a = "))
b = int(input("b = "))
s = 0
for i in range(a,b+1):
    s += i
print("summa:",s)


# In[41]:


#for8
a = int(input("a = "))
b = int(input("b = "))
k = 1
for i in range(a,b+1):
     k *= i
print("jami kopaytma:",k)


# In[38]:


#for9
a = int(input("a = "))
b = int(input("b = "))
s = 0
for i in range(a,b+1):
    s += i**2
print("kvadratlari yeg'indisi:",s)


# In[2]:


#for10
n = int(input("n = "))
s = 0 
for i in range(1,n+1):
    s += 1/i
print("summa:",s)


# In[6]:


#for11
n = int(input("n = "))
s = 0 
for i in range(n,2*n+1):
    s += i**2
print("summa:",s)


# In[26]:


#for12
n = int(input("n = "))
k = 1
for i in range(11,n+11):
    print(i/10)
    k *= i/10
print("jami:",k)


# In[28]:


#for13                          
n = int(input("n = "))
s = 0
for i in range(11,n+11):
    s += (i/10)*((-1)**(i+1))
print(s)


# In[30]:


#for14
n = int(input("n = "))
s = 0
for i in range(1,2*n,2):
    s += i
print("kvadrati:",s)


# In[18]:


#for15                                   
n = int(input("n = "))
a = float(input("a = "))
p = 1
for i in range(1,n+1):
    p *= a
print(p)


# In[1]:


#for16
n = int(input("n = "))
a = float(input("a = "))
k = 1
for i in range(1,n+1):
    k *= a
    print(k)


# In[61]:


#for17
n = int(input("n = "))
a = float(input("a = "))
s = 0
for i in range(0,n+1):
    print(f"{i}-darajasi {a**(i):.2f}")
    s += a**(i)
print("Summa:",s)


# In[66]:


#for18
n = int(input("n = "))
a = float(input("a = "))
s = 0
for i in range(0,n+1):
    s += ((-1)**i)*(a**(i))
    print(f"{i}- darajasi {a**(i)*((-1)**i)}")
print("jami:",s)


# In[17]:


#for19
n = int(input("n = "))
p = 1
for i in range(1,n+1):
    p *= i
print(p)


# In[36]:


#for20
n = int(input("n = "))
s = 0
p = 1
for i in range(1,n+1):
    p *= i
    s += p
print("summa:",s)


# In[41]:


#for21
n = int(input("n = "))
s = 0
p = 1
for i in range(1,n+1):
    p *= i
    s += 1/p
print(1+s)


# In[16]:


#for22
n = int(input("n = "))
x = float(input("x = "))
s = 0
p = 1
for i in range(1,n+1):
    p *= i
    s += (x**i)/p
print("yeg'indi:",s)


# In[15]:


#for23                     
n = int(input("n = "))
x = float(input("x = "))
s = 0
p = 1
for i in range(1,n+1):
    p *= (2*i+1)*2*i
    s += (((-1)**i) * (x**(2*i+1)))/p
print('Summa:',x+s)


# In[12]:


#for24                  
n = int(input("n = "))
x = float(input("x = "))
p = 1
s = 0
for i in range(1,n+1):
    p *= (2*i-1)*2*i
    s += ((-1)**i * (x**(2*i)))/p
print('Summa:',1+s)


# In[13]:


#for25
n = int(input("n = "))
x = float(input("x = "))
s = 0
for i in range(1,n+1):
    s += (((-1)**(i-1))*(x**i))/i
print("Summa:",s)


# In[117]:


#for26
n = int(input("n = "))
x = float(input("x = "))
s = 0
for i in range(0,n+1):
    s += (((-1)**i)*(x**(2*i+1)))/(2*i+1) 
print("Summa:",s)


# In[1]:


#for27
n = int(input("n = "))
x = float(input("x = "))
s = 1
m = 1
yegindi = 0
for i in range(1,n+1):
    s *= 2*i-1
    m *= 2*i
    yegindi += (s*x**(2*i+1))/(m*(2*i+1))
print("summa:",yegindi+x)


# In[32]:


#for28
n = int(input("n = "))
x = float(input("x = "))
s = 1
m = 1
yegindi = 0
for i in range(1,n+1):
    s *= 2*i-3
    m *= 2*i
    yegindi += ((s*((-1)**(i-1))*x**i)/m)*(-1)
print("summa:",1+yegindi)


# In[10]:


#for29
n = int(input("N = "))
a = float(input("A = "))
b = float(input("B = "))

if a < b:
    a,b = b,a
c = (a-b) / n
for i in range(n+1):
    print(round(a,3))
    a -= c


# In[11]:


#for30 
from math import sin
n = int(input("N = "))
a = float(input("A = "))
b = float(input("B = "))

if a < b:
    a,b = b,a
c = (a-b) / n
for i in range(n+1):
    print(f"F(X) = {1 - sin(a)}")
    a -= c


# In[33]:


#for31
n = int(input("n = "))
A0 = 2
A1 = 0

for i in range(1,n+1):
    A1 = 2 + 1/A0
    print(f"A{i} = {A1}")
    A0 = A1


# In[82]:


#for32
n = int(input("n = "))
A0 = 1
A1 = 0

for i in range(1,n+1):
    A1 = (A0 + 1)/i
    print(f"A{i} = {A1}")
    A0 = A1


# In[11]:


#for33 Fibonachi sonlari 1-usul
n = int(input("n = "))
F1 = 1
F2 = 1

for i in range(1,n+1):
    print(F1)
    F1,F2 = F2,F1+F2


# In[34]:


#for33 Fibonachi sonlari 2-usul
n = int(input("n = "))
F1 = 1
F2 = 1

for i in range(1,n+1):
    print(F1)
    F = F1 + F2
    F1 = F2
    F2 = F


# In[85]:


#for34
n = int(input("n = "))
A1 = 1
A2 = 2

for i in range(n):
    print(A1)
    A = (A1 + 2*A2)/3
    A1 = A2
    A2 = A


# In[86]:


#for35
n = int(input("n = "))
A1 = 1
A2 = 2
A3 = 3

for i in range(n):
    print(A1)
    A = A3 + A2 - 2*A1
    A1 = A2
    A2 = A3
    A3 = A


# In[63]:


#for36
n = int(input("n = "))
k = int(input("k = "))
s = 0 
for i in range(1,n+1):
    s += i**k
print("Summa:",s)


# In[64]:


#for37
n = int(input("n = "))
s = 0
for i in range(1,n+1):
    s += i**i
print("Summa:",s)


# In[66]:


#for38
n = int(input("n = "))
s = 0
for i in range(1,n+1):
    s += i**((n+1)-i)
print("Summa:",s)


# In[62]:


#for39                      
a = int(input("A = "))
b = int(input("B = "))

for i in range(a,b+1):
    print(f"{i}\n"*i)


# In[61]:


#for40                       
a = int(input("A = "))
b = int(input("B = "))
t = 1

for i in range(a,b+1):
        print(f"{i}\n"*t)
        t += 1


# In[36]:


#for39    ichma-ich for
a = int(input("A = "))
b = int(input("B = "))

for i in range(a,b+1):
    for j in range(i):
        print(i,end = " ")


# In[ ]:


#for40     ichma-ich for              
a = int(input("A = "))
b = int(input("B = "))
c = 1

for i in range(a,b+1):
    for j in range(c):
        print(i,end = " ")
    c += 1


# In[34]:


#for40 Unversal usul   
a = int(input("A = "))
b = int(input("B = "))
c = 1
if a > b:
    a,b = b,a
for i in range(a,b+1):
    for j in range(c):
        print(i)
    c += 1

