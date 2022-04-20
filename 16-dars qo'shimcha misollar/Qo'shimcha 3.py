#!/usr/bin/env python
# coding: utf-8

# # 20/04/2022
# 
# # Python asoslari
# 
# # 16-dars: While,Funksiya,List misollarini yechish
# 
# # Muallif: Farrux Sotivoldiyev

# ### 1.While,for operatori

# ![1-misol.png](attachment:1-misol.png)

# In[17]:


#7 for
s = 103
for i in range(s-2,0,-2):
    s = (s*i+1)/s
print(1/s)


# In[20]:


#7 while
s = 103
k = s-2
while k>0:
    s = (s*k+1)/s
    k -= 2
print(1/s)


# In[49]:


#8 while
x = float(input("x = "))

s = x**2
i = 256
while i > 1:
    s = (s * x**2 + i)/s
    i//=2
print(x/s)


# In[50]:


#8 for
x = float(input("x = "))
s = x**2
i = 256
for j in range(8):
    s = (s * x**2 + i)/s
    i //=2
print(x/s)


# In[2]:


#1 yevklid algoritmi ikkita sonning ekubini topish
a = int(input("a = "))
b = int(input("b = "))
while a!=b:
    if a > b:
        a %= b
    else:
        b %= a
        
    if a == 0:
        a = b
    if b == 0:
        b = a
print(a)


# In[1]:


#2 yevklid algoritmi ikkita sonning ekubini topish
a = int(input("a = "))
b = int(input("b = "))
while a!=0 and b!=0:
    if a>b:
        a %= b
    else:
        b%=a
print("Ekub",a+b)


# In[16]:


#3 3 ta sonning ekub va ekukini topish
a = 45
b = 180
c = 30
ekub = a
ekuk = a
while a%ekub != 0 or b%ekub != 0 or c%ekub != 0:
    ekub -= 1
while ekuk%a != 0 or ekuk%b != 0 or ekuk%c != 0:
    ekuk += 1
print(ekuk)
print(ekub)


# In[39]:


#4 n ta sonning ekuki
n = int(input("n = "))
for i in range(1,n+1):
    k = int(input(f"k{i} = "))
    if i==1:
        ekuk = k
        m = k
    else:
        while ekuk%k != 0 or ekuk%m !=0:
            ekuk += 1
        m = k
print(ekuk)


# ### 2.Funksiya
# 

# In[ ]:


#1 swap funksiyasi
def swap(a,b):
    return b,a
a = 5; b = 3
a,b = swap(a,b)
print(f"a = {a} \nb = {b}")
print("a + b = ",a+b)


# In[5]:


#2 ikkita sonning ekuki 
def ekuk(a,b):
    if a<b:
        a,b = b,a
    kattasi = a
    qiymat = kattasi
    while True:
        if kattasi%a==0 and kattasi%b==0:
            return kattasi
        else:
            kattasi += qiymat
a = int(input("a = "))
b = int(input("b = "))
print(ekuk(a,b))


# In[1]:


#3 n kun keyingi kunni topish
def LeapYear(y):
    kabisa = False
    if y%4==0:
        kabisa = True
    if y%100==0 and y%400!=0:
        kabisa = False
    return kabisa

def MonthDays(y,m):
    if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
        days = 31
    elif m==4 or m==6 or m==9 or m==11:
        days = 30
    else:
        days = 28 + LeapYear(y)
    return days

def Ndayslater(y,m,d,n):
    nday = d + n
    while nday > MonthDays(y,m):
        nday -= MonthDays(y,m)
        m += 1
        if m > 12:
            m = 1
            y += 1

    return y,m,nday

year = int(input("Year = "))
month = int(input("Month = "))
day = int(input("Day = "))
n = int(input("Day++ = "))
print(Ndayslater(year,month,day,n))


# In[4]:


#4 n ta sonning ekukini topish
def Ekuk(a,b):
    p = a * b
    while a != b:
        if a > b:
            a %= b
        else:
            b %= a
            
        if a == 0:
            a = b
        if b == 0:
            b = a
    return p // a

def NEkuk(a,b,n):
    ekuk = Ekuk(a,b)
    for i in range(3,n+1):
        k = int(input(f"k{i} = "))
        ekuk = Ekuk(ekuk,k)
    return ekuk
n = int(input("n = "))
a = int(input("k1 = "))
b = int(input("k2 = "))
print(NEkuk(a,b,n))        


# ### 3.List

# In[18]:


#5 massivda kelgan tub sonning oldiga va orqasiga 0 ni qo'shish
from random import randint
n = int(input("n = "))
a = [randint(1,9) for i in range(n)]
print(a)
def tub(x):
    flag = True
    if x==1:
        flag = False
    for i in range(2,x):
        if x%i==0:
            flag = False
            break
    return flag
i = 0
while i<len(a):
    y = tub(a[i])
    if y:
        a.insert(i,0)
        a.insert(i+2,0)
        i+=3
        continue
    i+=1
print(a)


# In[1]:


#6 Massivning k-seriyasini o'chirish
from random import randint
n = int(input("n = "))
k = int(input("k = "))
a = [randint(3,5) for i in range(n)]
print(a)

x = a[0]
b = [x] #seriya qiymati
c = [1] #seriyalar soni
h = 0
for i in range(1,n):
    if a[i]==x:
        c[h] += 1
    else:
        x = a[i]
        b.append(x)
        c.append(1)
        h += 1
del b[k-1]
del c[k-1]
a.clear()
for i in range(len(c)):
    for j in range(c[i]):
        a.append(b[i])
print(b)
print(c)
print(a)


# In[4]:


# a massivni o'zgartirmasdan b listdagi indexlarni shunday tartiblash kerak natijada
# b massivdagi indexlar bo'yicha a massivni chiqarsak tartiblangan holda chiqsin
from random import randint
n = int(input("n = "))
a = [randint(1,9) for i in range(n)]
print(a)
b = [i for i in range(n)]
print(b)
for i in range(1,n):
    for j in range(0,n-i):
        if a[b[j]]>a[b[j+1]]:
            b[j],b[j+1] = b[j+1],b[j]   
print("\n")
print(a)
print(b)

