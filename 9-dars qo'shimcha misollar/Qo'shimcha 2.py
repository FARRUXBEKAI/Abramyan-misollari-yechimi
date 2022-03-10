#!/usr/bin/env python
# coding: utf-8

# # 5/03/2022
# 
# # Python asoslari
# 
# # 9-dars: For operatori misollarni yechish
# 
# # Muallif: Farrux Sotivoldiyev
# 

# # For qo'shimcha masalalar 1

# In[9]:


#1 n soni kiritganimizda n x n matritsani chiqarish 

n = int(input("n = "))

for i in range(n):
    for j in range(i,0,-1):
        print(j,end=" ")
    for j in range(0,n-i):
        print(j,end=" ")
    print()


# In[10]:


#2 Formulaga asosan hisoblash

k = int(input("k = "))
n = int(input("n = "))

s = 0
for i in range(1,n+1):
    s += i/(k**5)
print(s)


# In[19]:


#3  Formulaga asosan hisoblash

n = int(input("n = "))
x = int(input("x = "))

for i in range(1,n+1):
    k = 1
    for j in range(1,i+1):
        k *= j
    s += (1/k) + x**0.5 
print(s)


# In[5]:


#4 kiritilgan sonning bo'luvchilarini topuvchi dastur

n = int(input("n = "))

for i in range(1,n+1):
    if n%i==0:
        print(i)


# In[27]:


#5  kiritilgan sonning bo'luvchilarini yeg'indisini topuvchi dastur

n = int(input("n = "))

s = 0
for i in range(1,n+1):
    if n%i==0:
        s += i
print(s)


# # For qo'shimcha masalalar 2

# In[1]:


#1 kiritilgan sonni bo'luvchilari nechtaligini topuvchi dastur

n = int(input("n = "))

k = 0
for i in range(1,n+1):
    if n%i==0:
        k += 1
print(k)


# In[9]:


#2 Kiritilgan sonni tub yoki murakkabligini aniqlash dasturi

n = int(input("n = "))

k = 0
for i in range(2,n):
    if n%i==0:
        k += 1
if k > 0:
    print("Murakkab")
else:
    print("Tub")


# In[16]:


#3 kiritilgan songacha bo'lgan tub sonlarni chiqarish dasturi

n = int(input("n = "))

for i in range(1,n+1):
    k = 0
    for j in range(2,i):
        if i%j==0:
            k += 1
            break
    if k==0:
        print(i,end=' ')


# In[18]:


#4  -n dan n gacha bolgan sonlarni formulaga asoslangan holda yeg'indisini hisoblash

n = int(input("n = "))

s = 0
for i in range(-n,n+1):
    if i == 0:
        continue
    s += 1/i
print(s)


# In[3]:


#5 n ta son kiritganimizda 0 dan katta eng kichik sonni topish dasturi

n = int(input("n = "))

min = 'Siz 0 dan katta son kiritmadingiz'
flag = True
for i in range(1,n+1):
    a = int(input(f"son{i}>>>"))
    if a>0 and flag:
        min = a
        flag = False
    if a > 0 and min > a:
            min = a
print(min)


# # For qo'shimcha masalalar 3 

# In[1]:


#1 kiritilgan n ta sonning max va min qiymatlarining o'rta arifmetigi
N = int(input("N = "))
m = True
for _ in range(1,N+1):
    n = int(input(f"n{_} = "))
    if m:
        max = n
        min = n
        m = False
    if n > max:
        max = n
    if n < min:
        min = n
print(f"O'rta arifmetik ={(max+min)/2}")


# In[8]:


#2 n kiritilsa n ta tub sonni chiqarib beruvchi dastur 
n = int(input("n = "))
i = 1
h = 0
while i < n**4:
    k = 0
    for j in range(1,i+1):
        if i%j==0:
            k += 1
    if k==2:
        h += 1
        print(i,end=" ")
        if h==n:
            break
    i += 1


# In[4]:


#3 dastlabki 5 ta tub sonni topish
n = 5
h = 1
print(2,end=' ')
for i in range(3,n**2,2):
    k = True
    for j in range(3,int(i**(1/2)),2):
        if i%j==0:
            k = False
    if k:
        h += 1
        print(i,end=" ")
    if h==5:
        break
print("jami",h)


# In[38]:


#4 sonning nechta raqamdan iboratligini topuvchi dastur
a = int(input("n = "))
s=0
while a!=0:
    a //= 10
    s += 1
print(s)


# In[41]:


#5 sonning ichida 2 raqami nechtaligini topuvchi dastur
a = int(input("n = "))
s=0
while a!=0:
    if a%10==2:
        s += 1
    a //= 10
print(s)


# # For qo'shimcha masalalar 4

# ![image.png](attachment:image.png)

# In[3]:


#1
n = int(input("n = "))
i = 1
while i<=n:
    if n%i==0:
        print(i,end=" ")
    i += 1


# ![image.png](attachment:image.png)

# In[7]:


#2
n = int(input("n = "))
s = 0
i = 1
while i <= n:
    if n%i == 0:
        s += i
    i += 1
print("Summa:",s)


# ![image.png](attachment:image.png)

# In[14]:


#3
n = int(input("n = "))
s = 0
i = 1
while i < n:
    if n%i ==0:
        s += i
    i += 1
if s == n:
    print("Mukammal son")
else:
    print("Mukammal emas")


# ![image.png](attachment:image.png)

# In[19]:


#5
n = int(input("n  = "))
i = 1
while i <= n:
    if i%3 == 0 and not i%5 == 0:
        print(i,end=" ")
    i += 1
    


# ![image.png](attachment:image.png)

# In[1]:


#8
from math import sqrt

n = int(input("n = "))

for c in range(1,n+1):
    for b in range(1,c):
        a = sqrt(c*c - b*b)
        if a%1==0 and b>a :
            print(int(a),b,c)


# ![image.png](attachment:image.png)

# In[22]:


#f
n = int(input("n = "))

p = 0
s = 0
i = 1
while i <= n:
    p += sin(i)
    s += 1/p
    i += 1
print("Summa:",s)


# In[28]:


#g
n = int(input("n = "))

cosinus = 0
sinus = 0
s = 0
i = 1
while i <= n:
    sinus += sin(i)
    cosinus += (1-(sin(i))**2)**(1/2)
    s += cosinus/sinus
    i += 1
print("Summa:",s)

