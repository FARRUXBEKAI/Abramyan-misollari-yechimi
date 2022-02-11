#!/usr/bin/env python
# coding: utf-8

# # 11/02/2022
# 
# # Python asoslari
# 
# # 1-dars: Kiritish va chiqarish
# 
# # Muallif: Farrux Sotivoldiyev
# 

# In[1]:


#1
a = 9
p = 4 * a
print(p)


# In[2]:


#2
a = 7
s = a ** 2
print(s)


# In[5]:


#3
a = 5
b = 6
s =  a * b
p = 2 *(a+b)
print(f"yuzi = {s} perimetri = {p}")


# In[6]:


#4
from math import pi
d = 7
l = pi * d
print(l)


# In[1]:


#5
a = 8
v = a**3
s = 6 * a**2
print(f"Hajmi: {v} Tola sirti: {s}")


# In[2]:


#6
a,b,c = 3,5,9
v = a * b * c
s = 2 * (a*b + b*c + a*c)
print(f"Hajmi: {v} Tola sirti: {s}")


# In[3]:


#7
from math import pi
r = 6
l = 2 * pi * r
s = pi * r**2
print(f"uzunligi: {l} yuzi: {s}")


# In[4]:


#8
a = 4
b = 8
A = (a + b)/2
print("A = ",A)


# In[6]:


#9
from math import sqrt
a = 2
b = 6
G = sqrt(a * b)
print("G = ",G)


# In[9]:


#10
a = 2
b = 9
Y = a + b
K = a * b
a = a**2
b = b**2
print(f"yegindi: {Y} \nkopaytma: {K} \na^2 = {a} \nb^2 = {b}")


# In[4]:


#12
from math import sqrt
a = 3
b = 4
c = sqrt(a**2 + b**2)
p = a + b +c
print(f"gipotenuza: {c} \nperimetr: {p}")


# In[5]:


#13
from math import pi
R1 = 9
R2 = 5
s1 = pi * R1
s2 = pi * R2
s3 = pi * (R1 - R2)
print(f"s1= {s1} s2= {s2} s3= {s3}")


# In[7]:


#17
ax , ay = 5 , 3
bx , by = 2 , 4
cx , cy = 1 , 5
ac = sqrt((cx-ax)**2 + (cy-ay)**2)
bc = sqrt((cx-bx)**2 + (cy-by)**2)
uzunlik = ac + bc
print(f"AC = {ac:.2f} \nBC = {bc:.2f} \nkesmalar uzunligi: {uzunlik:.2f}")


# In[3]:


#21
from math import sqrt
x1,y1 = 2,3
x2,y2 = 1,4 
x3,y3 = 6,5
a = sqrt((x2-x1)**2 + (y2-y1)**2)
b = sqrt((x3-x2)**2 + (y3-y2)**2)
c = sqrt((x1-x3)**2 + (y1-y3)**2)
p = (a+b+c)/2
s = sqrt(p*(p-a)*(p-b)*(p-c))
print(f"yuzasi: {s} \n perimetri: {p}")



# In[13]:


#22
#1-usul
a = 2
b = 5
a = int(a*b)
b = int(a/b)
a = int(a/b)
print(f"a = {a} b = {b}")
#2-usul
a = 2
b = 5
a = a+b
b = a-b
a = a-b
print(f"a = {a} b = {b}")


# In[8]:


#23
a = 7
b = 3
c = 2
a = a+b+c
c = a-(b+c)
b = a-(b+c)
a = a-(b+c)

print(c,b,a)


# In[10]:


#24
a = 7
b = 2
c = 3
a = a+b+c
c = a-(b+c)
b = a-(b+c)
a = a-(b+c)
print(c,b,a)


# In[1]:


#25
x = 5
y = 4*((x-3)**6) - 7*((x-3)**3) + 2
print(f"y = {y}")


# In[4]:


#27
a = 3
print(f"a^2={a**2}\na^3={a**4}\na^8={a**8}")


# In[6]:


#30
from math import pi
radian = (3*pi)/2
gradus = radian * (180/pi)
print(f"{radian} -> {gradus} gradusga teng")


# In[9]:


#32
T = int(input("Teperaturani gradus selsiyda kiriting: "))
K = (T-32)*5/9
print("K =",K)


# In[12]:


#34
x = 4  
xnarx = 6000
xbir = xnarx/x
y = 3
ynarx = 3600 
ybir = ynarx/y
print(f"1 kg shokolad 1 kg konfetdan {int(xbir-ybir)} so'm qimmat")


# In[30]:


#35
vq = 100 #km/soat
vo = 80 #km/soat
t = 2 #soat
toq = 4 #soat
sob = (vq + vo)/t
soq = (vq - vo)/t
print(f"Qayiqni yurgan yollari:\noqim boylab: {sob}\noqimga qarshi: {soq}")


# In[27]:


#36
v1 = 120 #km/soat
v2 = 180 #km/soat
t = 2 #soat
s = 800 #km
S = s - (v1*t + v2*t)
print(f"Ular orasidagi masofa: {S}km")


# In[31]:


#38
a = 5
b = 8
# AX + B = 0
print("x =",(-b/a))


# In[32]:


#39
from math import sqrt
a  = 4
b = 3
c = 2
D = sqrt(b**2)-(4*a*c)
x1 = (-b + D)/2*a
x2 = (-b - D)/2*a
print(f"x1 = {x1}\nx2 = {x2}")


# In[33]:


#40
a1,b1,c1 = 2,8,4
a2,b2,c2 = 3,9,1
# A1*x + B1*y = C1
# A2*x + B2*y = C2
D = (a1*b2 - a2*b1)
x = (c1*b2 - c2*b1)/D
y = (a1*c2 - a2*c1)/D
print(f"x = {x}\ny = {y}")


# # Qo'shimcha misollar

# In[22]:


#float sonni int ga o'tkazish
a = int(float(input("a = ")))
print(a)


# In[5]:


# darsdagi savol: a,b,c,d sonlarni bir biriga almshtirish
a,b,c,d = 1,2,3,4
a = a+b+c+d
d = a-(b+c+d)
c = a-(b+c+d)
b = a-(b+c+d)
a = a-(b+c+d)
print(f"a = {a}\nb = {b}\nc = {c} \nd = {d}")


# In[7]:


#Kun kiritilsa uni hafta va kunga ajratish
a = int(input("kunni kiriting: "))
print(f"{a // 7} haftayu {a % 7} kun")


# In[12]:


#Kb kiritilsa Mb va Kb ga bolish
kb = int(input("kb = "))
mb = kb//1024
k = kb-1024
print(f"mb = {mb}\nkb = {k}")


# In[2]:


# uch xonali sonni teskari tartibda chiqarish
a = int(input("a = "))
yuz = a // 100
on = a%100//10
bir = a % 10
print(bir*100+on*10+yuz*1)


# In[19]:


#sekund kiritilsa soat,minut,sekundlarga bolish
a = 7205
soat = a //3600
minut = a%3600//60 
sek = a %60
print(soat,"soat",minut,"minut",sek,"sek")


# In[ ]:




