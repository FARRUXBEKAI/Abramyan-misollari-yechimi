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


#begin1
a = int(input("a = "))

p = 4 * a

print("Perimetr:",p)


# In[2]:


#begin2
a = int(input("a = "))

s = a**2

print("Yuzi:",s)


# In[4]:


#begin3
a = int(input("a = "))
b = int(input("b = "))

s = a * b
p = 2 * (a + b)

print("Yuzi:",s,"\nPerimetr:",p)


# In[5]:


#begin4
d = int(input("d = "))

pi = 3.14
l = pi * d

print("Uzunligi:",l)


# In[6]:


#begin5
a = int(input("a = "))

v = a**3
s = 6 * a**2

print("Yuzi:",s,"\nHajmi:",v)


# In[7]:


#begin6
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

v = a * b * c
s = 2 * (a*b + b*c + a*c)

print("Hajmi:",v,"\nTo'la sirti:",s)


# In[8]:


#begin7
r = int(input("R = "))

pi = 3.14
l = 2 * pi * r
s = pi * r**2

print("Uzunligi:",l,"\nYuzasi:",s)


# In[9]:


#begin8
a = int(input("a = "))
b = int(input("b = "))

orta_arif = (a+b)/2

print("orta_arif:",orta_arif)


# In[10]:


#begin9
a = int(input("a = "))
b = int(input("b = "))

orta_geo = (a*b)**(1/2)

print("orta_geo:",orta_geo)


# In[11]:


#begin10
a = int(input("a = "))
b = int(input("b = "))

print("Yeg'indi:",a+b,"\nKo'paytmaL:",a*b,"\na^2 =",a**2,"\nb^2 =",b**2)


# In[12]:


#begin11
a = int(input("a = "))
b = int(input("b = "))

print("Yeg'indi:",a+b,"\nKo'paytmaL:",a*b,"\n|a| =",abs(a),"\n|b| =",abs(b))


# In[13]:


#begin12
a = int(input("a = "))
b = int(input("b = "))

c = (a**2 + b**2)**(1/2)
p = a + b + c

print("gipotenuzasi:",c,"\nPerimetri:",p)


# In[16]:


#begin13
r1 = int(input("R1 = "))
r2 = int(input("R2 = "))

pi = 3.14
s1 = pi * r1
s2 = pi * r2
s3 = pi * (r1 - r2)

print("S1 =",s1,"\nS2 =",s2,"\nS3 =",s3)


# In[19]:


#begin14
l = int(input("L = "))

pi = 3.14
r = l / (2 * pi)
s = pi * r**2

print("Radiusi:",r,"\nYuzasi:",s)


# In[22]:


#begin15
s = int(input("S = "))

pi = 3.14
r = (s / pi)**(1/2)
d = 2 * r

print("Diametri:",d,"\nRadiusi:",r)


# In[24]:


#begin16
x1 = int(input("x1 = "))
x2 = int(input("x2 = "))

print("masofa:",abs(x2-x1))


# In[26]:


#begin17
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

ac = abs(c - a)
bc = abs(c - b)

print("AC =",ac,"\nBC =",bc,"\nyeg'indisi:",ac+bc)


# In[29]:


#begin18
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

ac = abs(c - a)
bc = abs(c - b)

print("AC * BC =",abs(c-a) * abs(b-c))


# In[26]:


#begin19 
x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x3 = int(input("x3 = "))
y3 = int(input("y3 = "))
x2 = x1
y2 = y3
x4 = x3
y4 = y1

a = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
b = ((x3-x2)**2 + (y3-y2)**2)**(1/2)
s = a * b
p = 2 * (a + b)

print("S =",s,"\nP =",p)


# In[30]:


#begin20
x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))

print("Masofa:",((x2-x1)**2 + (y2-y1)**2)**(1/2))


# In[2]:


#begin21
x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))
x3 = int(input("x3 = "))
y3 = int(input("y3 = "))

a = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
b = ((x3-x2)**2 + (y3-y2)**2)**(1/2)
c = ((x3-x1)**2 + (y3-y1)**2)**(1/2)

p = (a+b+c)/2
s = (p*(p-a)*(p-b)*(p-c))**(1/2)

print("Yuzasi:",s,"\nPerimetri:",p*2)


# In[7]:


#begin22
a = int(input("a = "))
b = int(input("b = "))

a = a + b
b = a - b
a = a - b

print("a =",a,"b =",b)


# In[14]:


#begin23
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

c = a + b + c
a = c - b - a
b = c - b - a
c = c - b - a


print("a =",a,"b =",b,"c =",c)


# In[12]:


#begin24
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

a = a + b + c

c = a - b - c
b = a - b - c
a = a - b - c


print("a =",a,"b =",b,"c =",c)


# In[15]:


#begin25
x = int(input("x = "))

y = 3 * x**6 - 6 * x**2 - 7

print("y =",y)


# In[16]:


#begin26
x = int(input("x = "))

y = 4 * (x-3)**6 - 7 * (x-3)**3 + 2

print("y =",y)


# In[17]:


#begin27
a = int(input("A = "))

print("a^2 =",a**2,"\na^4",a**4,"\na^8 =",a**8)


# In[18]:


#begin28
a = int(input("A = "))

print("a^2 =",a**2,"\na^3",a**3,"\na^5 =",a**5,"\na^10",a**10,"\na^15 =",a**15)


# In[21]:


#begin29
a = int(input("a = "))

pi = 3.14
radian = a * (pi/180)

print("radian =",radian)


# In[23]:


#begin30
a = int(input("a = "))

pi = 3.14
gradus = a * (180/pi)

print("gradus =",gradus)


# In[28]:


#begin31
Tf = int(input("Kelvinda kiriting: "))

Tc = (Tf - 32) * 5/9

print("gradus =",Tc)


# In[30]:


#begin32
Tc = int(input("gradusda kiriting: "))

Tf = (Tc - 32) * 5/9

print("Kelvinda =",Tf)


# In[31]:


#begin33
x = int(input("kg = "))
a = int(input("so'm = "))
y = int(input("kg = "))

kg_1 = a / x
y_kg = y * kg_1

print("1 kg =",kg_1,"\ny kg =",y_kg)


# In[32]:


#begin34
x = int(input("kg = "))
a = int(input("so'm = "))
y = int(input("kg = "))
b = int(input("so'm = "))

kg_1_shokolad = a / x
kg_1_konfet = b / y
martta = kg_1_shokolad // kg_1_konfet

print(martta,"katta")


# In[36]:


#begin35
vq = int(input("v_qayiq = "))
vs = int(input("v_oqim = "))
t1 = int(input("T1_oqim_bo'ylab = "))
t2 = int(input("T2_oqimga_qarshi = "))

S_oqim_boylab = (vq + vs) * t1
S_oqimga_qarshi = (vq - vs) * t2
S = S_oqim_boylab + S_oqimga_qarshi

print("Yurgan yo'li:",S)


# In[1]:


#begin36
v1 = int(input("v1 = "))
v2 = int(input("v2 = "))
s = int(input("s = "))
t = int(input("t = "))

S = t * (v1 + v2) + s

print("Ular orasidagi masofa:",S)


# In[2]:


#begin37
v1 = int(input("v1 = "))
v2 = int(input("v2 = "))
s = int(input("s = "))
t = int(input("t = "))

S = s - t * (v1 + v2)

print("Ular orasidagi masofa:",S)


# In[3]:


#begin38
A = int(input("A = "))
B = int(input("B = "))

x = -B/A

print("x =",x)


# In[11]:


#39
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

D = (b**2 - 4*a*c)**(0.5)
x1 = (-b + D) / (2*a)
x2 = (-b - D) / (2*a)

print(f"x1 = {x1}\nx2 = {x2}")


# In[22]:


# 40
a1 = int(input("a1 = "))
b1 = int(input("b1 = "))
c1 = int(input("c1 = "))
a2 = int(input("a2 = "))
b2 = int(input("b2 = "))
c2 = int(input("c2 = "))

D = (a1*b2 - a2*b1)
x = (c1*b2 - c2*b1)/D
y = (a1*c2 - a2*c1)/D

print(f"x = {x}\ny = {y}")


# # Qo'shimcha misollar.

# In[15]:


#float sonni int ga o'tkazish

a = int(float(input("a = ")))

print(a)


# In[16]:


# darsdagi savol: a,b,c,d sonlarni bir biriga almshtirish

a,b,c,d = 1,2,3,4

a = a+b+c+d
d = a-(b+c+d)
c = a-(b+c+d)
b = a-(b+c+d)
a = a-(b+c+d)

print(f"a = {a}\nb = {b}\nc = {c} \nd = {d}")


# In[17]:


#Kun kiritilsa uni hafta va kunga ajratish

a = int(input("kunni kiriting: "))

print(f"{a // 7} haftayu {a % 7} kun")


# In[18]:


#Kb kiritilsa Mb va Kb ga ajratish

kb = int(input("kb = "))

mb = kb//1024
k = kb-1024

print(f"mb = {mb}\nkb = {k}")


# In[19]:


# uch xonali sonni teskari tartibda chiqarish

a = int(input("a = "))

yuz = a // 100
on = a%100//10
bir = a % 10

print(bir*100+on*10+yuz*1)


# In[21]:


#sekund kiritilsa soat,minut,sekundlarga bolish

a = 7295

soat = a //3600
minut = a%3600//60 
sek = a %60

print(soat,"soat",minut,"minut",sek,"sek")

