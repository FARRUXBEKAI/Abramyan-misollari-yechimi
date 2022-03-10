#!/usr/bin/env python
# coding: utf-8

# # 10/03/2022
# 
# # Python asoslari
# 
# # 10-dars: While operatori
# 
# # Muallif: Farrux Sotivoldiyev

# In[6]:


#while1

a  = int(input("A = "))
b  = int(input("B = "))

k = 0
while b <= a:
    a -= b 
    k +=1
print("butun:",k,"qoldiq:",a)


# In[11]:


#while2

a  = int(input("A = "))
b  = int(input("B = "))

k = 0
while b < a:
    a -= b 
    k +=1
print("butun:",k)


# In[4]:


#while3

n  = int(input("N = "))
k  = int(input("K = "))

h = 0
while k <= n:
    n -= k 
    h +=1
print("butun:",h,"qoldiq:",n)


# In[6]:


#while4 

n  = int(input("N = "))

while n>0:
    n-=3
if n==0:
    print("3 ga karrali")
else:
    print("3 karrali emas")
    


# In[105]:


#while5   

n  = int(input("N = "))

i = 1
while 2**i != n:
    i += 1
print(i)


# In[15]:


#while6  

n  = int(input("N = "))

k = 1
while n > 1:
    k *= n    
    n -= 2
print(k)


# In[94]:


#while7  

n  = int(input("N = "))

k = 1
while k**2 < n+1:
    k += 1
print(k)


# In[87]:


#while8

n  = int(input("N = "))

k = 1
while k**2 <= n:
    k += 1
print(k-1)


# In[83]:


#while9

n  = int(input("N = "))

k = 1
while 3**k <= n:
    k += 1
print(k)


# In[81]:


#while10

n  = int(input("N = "))

k = 1
while 3**k <= n:
    k += 1
print(k-1)


# In[75]:


#while11

n  = int(input("N = "))

s = 0
k = 0
while s < n:
    k += 1
    s += k 
print(k,"\nyeg'indi =",s)


# In[72]:


#while12

n  = int(input("N = "))

s = 0
k = 0
while s <= n:
    k += 1
    s += k 
print(k-1)


# In[109]:


#while13

a = int(input("a = "))

i = 1
s = 0
while True:
    p = 1 / i
    s += p
    if s >= a:
        print("k =",i,"\nsumma:",s)
        break
    i += 1


# In[59]:


#while14

a = int(input("a = "))
s = 0                           
i = 1
while True:
    p = 1 / i
    s += p
    if s >= a:
        print("k =",i-1,"\nsumma:",s-p)
        break
    i += 1


# In[17]:


#while15

s = int(input("s = "))
p = int(input("har oyda necha  foizga oshsin (0<p<50):"))

oy = 0
summa = s
while True:
    summa += s*p/100
    oy += 1
    if summa > 2*s:
        print(oy,"oyda")
        break


# In[10]:


#while16

p = int(input("har oyda necha  foizga oshsin (0<p<25):"))

oy = 0
jami = 10
while True:
    jami += p/10
    oy += 1
    if jami > 200:
        print(jami,"km")
        print(oy,"oyda")
        break


# In[1]:


#while17

n = int(input("n = "))
m = int(input("m = "))

k = 0
while n > m:
    k += 1
    n -= m
print("Qoldiq:",n,"\nButun",k)


# In[13]:


#while18

n = int(input("n = "))

s = 0
while n>0:
    s = n%10 + s*10
    n //= 10                    
print(s)


# In[47]:


#while19

n = int(input("n = "))

s = 0
r = 0
while n!=0:
    k = n%10
    r += 1
    s += k
    n //= 10
print("raqamlari yeg'indisi:",s,"\nraqamlari soni:",r,"ta")


# In[39]:


#while20

a = int(input("n = "))

s=0
while a!=0:
    if a%10==2:
        s += 1
    a //= 10
if s > 0:
    print("2 raqami bor")
else:
    print("2 raqami yo'q")


# In[65]:


#while21

n = int(input("n = "))

while n!=0:
    k = n%10
    n //= 10
    if k%2 == 1:
        print("Bor")
        break
else:
    print("yo'q")


# In[80]:


#while22

n = int(input("n = "))

i = 2
while i < n:
    k = 0
    if n%i==0:
        k += 1
        break
    i += 1
if k>0:
    print("Tub emas")
else:
    print("Tub")


# In[92]:


#while23

a = int(input("a = "))
b = int(input("b = "))

c = a * b
if a < b:
    a,b = b,a
while a != b:
    if a > b:
        a -= b
    elif b > a:
        b -= a
print("Ekub = ", a ,"\nEkuk = ", c // a)


# In[116]:


#while24

n = int(input("n = "))

i = 1
f1 = 1
f2 = 1
while i <= n:
    if f2 == n:
        print("Bor")
        break
    elif f2<=n:
        f1 = f1 + f2
        f2 = f1 - f2
    else:
        print("yo'q")
        break
    i += 1
else:
    print("yo'q")


# In[130]:


#while25

n = int(input("n = "))

i = 0
f1 = 1
f2 = 1
while i <= n:
    if f2 > n:
        print(f2)
        break
    f1 = f1 + f2
    f2 = f1 - f2
    i += 1


# In[7]:


#while26

n = int(input("n = "))

i = 0
f1 = 1
f2 = 1
maxi = 0
while i <= n:
    if f2 > n:
        print("Kattasi:",f2)
        break
    if n > f2 and maxi < f2:
        maxi = f2
    f1 = f1 + f2
    f2 = f1 - f2
    i += 1
print("Kichigi:",maxi)


# In[20]:


#while27

n = int(input("n = "))

i = 1
f1 = 1
f2 = 1
while i <= n:
    if f2 == n:
        print(f2)
        print(i,"- xadi")
        break
    f1 = f1 + f2
    f2 = f1 - f2
    i += 1


# In[38]:


#while28

e = float(input("e = "))

k = 1
a1 = 2
while True:                         
    k += 1                          
    a2 = 2 + 1 / a1
    if abs(a2 - a1) < e:
        print(a2,a1,sep = " | ")
        print(k,"- xadi")
        break
    a1 = a2  


# In[37]:


#while29

e = float(input("e = "))

a1 = 1
a2 = 2
k = 1
while True:
    a3 = (a1 + 2 * a2)/3           
    if abs(a2 - a1) < e:           
        print(a1,a2,sep=" | ")
        print(k,"- xad")
        break
    a1 = a2
    a2 = a3
    k+=1


# In[15]:


#while30

a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))

k1 = 0
while a >= c:
    k1 += 1
    a -= c
k2 = 0
while b >= c:
    k2 += 1
    b -= c
s = 0
while k1>0:
    s+=k2
    k1-=1
print(s)

