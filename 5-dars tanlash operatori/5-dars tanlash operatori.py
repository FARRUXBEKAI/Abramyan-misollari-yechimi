#!/usr/bin/env python
# coding: utf-8

# # 14/02/2022
# 
# # Python asoslari
# 
# # 5-dars: Tanlash operatori misollarini ishlash
# 
# # Muallif: Farrux Sotivoldiyev

# In[1]:


#case1
n = int(input("<<<1-7>>> gacha son kiriting: "))
if n==1:
    print("Dushanba")
if n==2:
    print("Seshanba")
if n==3:
    print("Chorshanba")
if n==4:
    print("Payshanba")
if n==5:
    print("Juma")
if n==6:
    print("Shanba")
if n==7:
    print("Yakshanba")


# In[ ]:


#case2
k = int(input("K = "))
if k==1:
    print("Yomon")
elif k==2:
    print("Qoniqarsiz")
elif k==3:
    print("Qoniqarli")
elif k==4:
    print("Yaxshi")
elif k==5:
    print("A'lo")
else:
    print("Xato")


# In[ ]:


#case3
oy = int(input("Oy = "))
if oy==1 or oy==2 or oy==12:
    print("Qish")
if oy==3 or oy==4 or oy==5:
    print("Baxor")
if oy==6 or oy==7 or oy==8:
    print("Yoz")
else:
    print("Kuz")


# In[ ]:


#case4
oy = int(input("Oy = "))
if oy==1 or oy==3 or oy==5 or oy==7 or oy==8 or oy==10 or oy==12:
    print(31)
elif oy==4 or oy==6 or oy==9 or oy==11:
    print(30)
else:
    print(28)


# In[ ]:


#case5
a = int(input("A = "))
b = int(input("B = "))
ishora = int(input("Ishora <+-*/>")) 
if ishora==1:
    print(a+b)
elif ishora==2:
    print(a-b)
elif ishora==3:
    print(a/b)
elif ishora==4:
    print(a*b)
else:
    print("Xato")


# In[ ]:


#case6
birlik = int(input("birlik < 1-5 >: "))
qiymat = float(input("qiymat = "))
if birlik==1:
    print(qiymat/10,"m")
elif birlik==2:
    print(qiymat*1000,"m")
elif birlik==3:
    print(qiymat,"m")
elif birlik==4:
    print(qiymat/1000,"m")
elif birlik==5:
    print(qiymat/100,"m")
else:
    print("Xato")


# In[ ]:


#case7
birlik = int(input("birlik < 1-5 >: "))
qiymat = float(input("qiymat = "))
if birlik==1:
    print(qiymat,"kg")
elif birlik==2:
    print(qiymat/1000000,"kg")
elif birlik==3:
    print(qiymat/1000,"kg")
elif birlik==4:
    print(qiymat*1000,"kg")
elif birlik==5:
    print(qiymat*100,"kg")
else:
    print("Xato")


# In[14]:


#case8
# kun,oy va yil kiritiladi kabisa yili va oddiy yil ekanini ham nazarga olib oldingi kunni chiqarish
d = int(input('day = '))
m = int(input('month = '))
y = int(input('year = '))

kabisa = False
if y%4==0:
    kabisa=True
if y%100==0 and y%400!=0:
    kabisa=False
    
d = d - 1
if d == 0 and (m==5 or m==7 or m==10 or m==12):
        d = 30
        m = m - 1
elif d == 0 and m == 3:
        d = 28 + kabisa
        m = 2
else:
    if d == 0:
        d = 31
        m = m - 1
    if m == 0:
        m = 12
        y = y - 1

print(d,m,y,sep='/')


# In[ ]:


#case9
# kun,oy va yil kiritiladi kabisa yili va oddiy yil ekanini ham nazarga olib keyingi kunni chiqarish
d = int(input("day = "))
m = int(input("month = "))
y = int(input("year = "))

#kabisa yilini tekshirish
if y%4==0:
    kabisa=True
if y%100==0 and y%400!=0:
    kabisa=False
    
#kun/oy/yilni joylashtirish  
if (d==31 and (m==1 or m==3 or m==5 or m==7 or m==8 or m==10)) or (d==30 and (m==4 or m==6 or m==9 or m==11)):
    print(f"{1}/{m+1}/{y}")
elif d==31 and m==12:
    print(f"{1}/{1}/{y+1}")
elif m==2 and kabisa and d==29:
    print(f"{1}/{m+1}/{y}")
elif m==2 and d==28 and not kabisa:
    print(f"{1}/{m+1}/{y}")
else:
    print(f"{d+1}/{m}/{y}")


# In[7]:


#case10
y = input("Yo'nalishni tanlang < s,j,q,g > ")
k = int(input("Komandani tanlang < 0,1,2 > "))

if y=="s":
    y="shimol"
elif y=="j":
    y="janub"
elif y=="q":
    y="sharq"
elif y=="g":
    y="g'arb"

if k==0:
    k=y
elif k==1:
    if y=="shimol":
        k="g'arb"
    elif y=="janub":
        k="sharq"
    elif y=="sharq":
        k="shimol"
    else:
        k="janub"
elif k==2:
    if y=="shimol":
        k="sharq"
    elif y=="janub":
        k="g'arb"
    elif y=="sharq":
        k="janub"
    else:
        k="shimol"
print(f"{k}")


# In[35]:


#case11 
c = input("Lokatrning holati < s,j,q,g > ")
k1 = int(input("1-komandani tanlang < 0,1,2 > "))
k2 = int(input("2-komandani tanlang < 0,1,2 > "))

if 0<=k1<=2 and 0<=k2<=2: 
    if k1==0 and k2==0 and c=="s":
        c="janub"
    elif k1==0 and k2==1 and c=="s": 
        c="shimol"
    elif k1==0 and k2==2 and c=="s":
        c="g'arb"
    elif k1==1 and k2==0 and c=="s":
        c="shimol"
    elif k1==1 and k2==1 and c=="s":
        c="janub"
    elif k1==1 and k2==2 and c=="s":
        c="sharq"
    elif k1==2 and k2==0 and c=="s":
        c="g'arb"
    elif k1==2 and k2==1 and c=="s":
        c="sharq"
    elif k1==2 and k2==2 and c=="s":
        c="shimol"   

    elif k1==0 and k2==0 and c=="j":
        c="shimol"
    elif k1==0 and k2==1 and c=="j":
        c="janub"
    elif k1==0 and k2==2 and c=="j":
        c="sharq"
    elif k1==1 and k2==0 and c=="j":
        c="janub"
    elif k1==1 and k2==1 and c=="j":
        c="shimol"
    elif k1==1 and k2==2 and c=="j":
        c="g'arb"
    elif k1==2 and k2==0 and c=="j":
        c="sharq"
    elif k1==2 and k2==1 and c=="j":
        c="g'arb"
    elif k1==2 and k2==2 and c=="j":
        c="janub"  

    elif k1==0 and k2==0 and c=="g": 
        c="sharq"
    elif k1==0 and k2==1 and c=="g":
        c="g'arb"
    elif k1==0 and k2==2 and c=="g": 
        c="janub"
    elif k1==1 and k2==0 and c=="g":
        c="g'arb"
    elif k1==1 and k2==1 and c=="g": 
        c="sharq"
    elif k1==1 and k2==2 and c=="g":
        c="shimol"
    elif k1==2 and k2==0 and c=="g":
        c="janub"
    elif k1==2 and k2==1 and c=="g": 
        c="shimol"
    elif k1==2 and k2==2 and c=="g":
        c="g'arb"

    elif k1==0 and k2==0 and c=="q":
        c="g'arb"
    elif k1==0 and k2==1 and c=="q":
        c="sharq"
    elif k1==0 and k2==2 and c=="q":
        c="shimol"
    elif k1==1 and k2==0 and c=="q":
        c="sharq"
    elif k1==1 and k2==1 and c=="q":
        c="g'arb"
    elif k1==1 and k2==2 and c=="q":
        c="janub"
    elif k1==2 and k2==0 and c=="q":
        c="shimol"
    elif k1==2 and k2==1 and c=="q":
        c="janub"
    elif k1==2 and k2==2 and c=="q":
        c="sharq"
    print(c)
else:
    print("Xato")


# In[ ]:


#case12
from math import sqrt,pi
m = int(input("<1-R><2-D><3-L>4-S> sonni tanlang:"))
k = int(input("qiymat = "))
if m==1:
    print(f"R={k}\nD={2*k}\nL={2*pi*k}\nS={pi*(k**2)}")
elif m==2:
    print(f"R={k/2}\nD={k}\nL={pi*k}\nS={pi*((k/2)**2)}")
if m==3:
    print(f"R={k/(2*pi)}\nD={k/pi}\nL={k}\nS={pi*((k/(2*pi))**2)}")
if m==4:
    print(f"R={sqrt(k/pi)}\nD={2*sqrt(k/pi)}\nL={2*pi*sqrt(k/pi)}\nS={pi*(sqrt(k/pi)**2)}")


# In[ ]:


#case13
from math import sqrt,pi
m = int(input("<1-a><2-c><3-h>4-S> sonni tanlang:"))
k = int(input("qiymat = "))
if m==1:
    print(f"a={k}\nc={k*sqrt(2)}\nh={k*sqrt(2)/2}\ns={(k**2)/2}")
elif m==2:
    print(f"a={k/sqrt(2)}\nc={k}\nh={k/2}\ns={(k**2)/4}")
elif m==3:
    print(f"a={(2*k)/sqrt(2)}\nc={2*k}\nh={k}\ns={k**2}")
elif m==4:
    print(f"a={sqrt(2*k)}\nc={2*sqrt(k)}\nh={sqrt(k)}\ns={k}")


# In[ ]:


#case14
from math import sqrt,pi
m = int(input("<1-a><2-R1><3-R2><4-S> sonni tanlang:"))
k = int(input("qiymat = "))
if m==1:
    print(f"a={k}\nR1={k*sqrt(3)/6}\nR2={k*sqrt(3)/3}\ns={(k**2)*sqrt(3)/4}")
elif m==2:
    print(f"a={6*k/sqrt(3)}\nR1={k}\nR2={2*k}\ns={3*sqrt(3)*(k**2)}")
elif m==3:
    print(f"a={sqrt(3)*k}\nR1={k/2}\nR2={k}\ns={3*sqrt(3)*(k**2)/4}")
elif m==4:
    print(f"a={2*sqrt(k)/(3**(1/4))}\nR1={sqrt(k)/(3*sqrt(3))}\nR2={2*sqrt(k)/(3*sqrt(3))}\nS={k}")


# In[ ]:


#case15
m = int(input("Karta turini kiriting <1-4>: "))
n = int(input("Karta qiymatini kiriting <6-14>: "))

if m==1:
    m="g'isht"
elif m==2:
    m="olma"
elif m==3:
    m="chillik"
elif m==4:
    m="qarg'a"
    
if n==6:
    n="Olti"
elif n==7:
    n="Yetti"
elif n==8:
    n="Sakkiz"
elif n==9:
    n="To'qqiz"
elif n==10:
    n="O'n"
elif n==11:
    n="Valet"
elif n==12:
    n="Dama"
elif n==13:
    n="Qirol"
elif n==14:
    n="Tuz"
print(f"{n} {m}") 


# In[13]:


#case16
a = int(input("Yoshingiz nechada: "))
on = a//10
bir = a%10
if a>0 and a<70:
    if bir==1:
        bir="bir"
    elif bir==2:
        bir="ikki"
    elif bir==3:
        bir="uch"
    elif bir==4:
        bir="to'rt"
    elif bir==5:
        bir="besh"
    elif bir==6:
        bir="olti"
    elif bir==7:
        bir="yetti"
    elif bir==8:
        bir="sakkiz"
    elif bir==9:
        bir="to'qqiz"

    if on==1:
        on="O'n"
    if on==2:
        on="Yigirma"
    if on==3:
        on="O'ttiz"
    if on==4:
        on="Qirq"
    if on==5:
        on="Ellik"
    if on==6:
        on="Oltmish"

    if bir==False:
        print(f"{on} yosh")
    elif on==False:
        print(f"{bir} yosh")
    else:
        print(f"{on} {bir} yosh")
else:
    print("Xato")


# In[23]:


#case17
a = int(input("Nechta masala: "))
on = a//10
bir = a%10
if a>0 and a<40:
    if bir==1:
        bir="bir"
    elif bir==2:
        bir="ikki"
    elif bir==3:
        bir="uch"
    elif bir==4:
        bir="to'rt"
    elif bir==5:
        bir="besh"
    elif bir==6:
        bir="olti"
    elif bir==7:
        bir="yetti"
    elif bir==8:
        bir="sakkiz"
    elif bir==9:
        bir="to'qqiz"

    if on==1:
        on="O'n"
    if on==2:
        on="Yigirma"
    if on==3:
        on="O'ttiz"

    if bir==False:
        print(f"{on}ta masala")
    elif on==False:
        print(f"{bir}ta masala")
    else:
        print(f"{on} {bir}ta masala")
else:
    print("Xato")


# In[13]:


#case18
a = int(input("Nechta masala: "))
yuz = a//100
on = a%100//10
bir = a%10

if a>99 and a<1000:
    if yuz==1:
        yuz="bir"
    elif yuz==2:
        yuz="ikki"
    elif yuz==3:
        yuz="uch"
    elif yuz==4:
        yuz="to'rt"
    elif yuz==5:
        yuz="besh"
    elif yuz==6:
        yuz="olti"
    elif yuz==7:
        yuz="yetti"
    elif yuz==8:
        yuz="sakkiz"
    elif yuz==9:
        yuz="to'qqiz"

    if on==1:
        on="o'n"
    elif on==2:
        on="yigirma"
    elif on==3:
        on="o'ttiz"
    elif on==4:
        on="qirq"
    elif on==5:
        on="ellik"
    elif on==6:
        on="oltmish"
    elif on==7:
        on="yetmish"
    elif on==8:
        on="sakson"
    elif on==9:
        on="to'qson"

    if bir==1:
        bir="bir"
    elif bir==2:
        bir="ikki"
    elif bir==3:
        bir="uch"
    elif bir==4:
        bir="to'rt"
    elif bir==5:
        bir="besh"
    elif bir==6:
        bir="olti"
    elif bir==7:
        bir="yetti"
    elif bir==8:
        bir="sakkiz"
    elif bir==9:
        bir="to'qqiz"

    if bir==False and on==False:
        print(f"{yuz} yuz ta")
    elif on==False:
        print(f"{yuz} yuz {bir} ta")
    elif bir==False:
        print(f"{yuz} yuz {on} ta")
    else:
        print(f"{yuz} yuz {on} {bir} ta")
else:
    print("Xato")


# In[12]:


#case19
y = int(input("Year = "))
h = (y-4)%12
r = (y-4)%5

if r==0:
    r="yashil"
elif r==1:
    r="qizil"
elif r==2:
    r="sariq"
elif r==3:
    r="oq"
elif r==4:
    r="qora"

if h==0:
    h="sichqon"
elif h==1:
    h="sigir"
elif h==2:
    h="yo'lbars"
elif h==3:
    h="quyon"
elif h==4:
    h="ajdar"
elif h==5:
    h="ilon"
elif h==6:
    h="ot"
elif h==7:
    h="qo'y"
elif h==8:
    h="maymun"
elif h==9:
    h="tovuq"
elif h==10:
    h="it"
elif h==11:
    h="to'ng'iz"

print(f"{r} {h} yili")


# In[5]:


#case20
d = int(input("day = "))
m = int(input("month = "))

if d<31 and m<13 :
    if m==1 and 19<d<=31:
        print("Qovg'a")
    elif m==2 and 1<=d<19:
        print("Qovg'a")
    elif m==2 and 18<d<=28:
        print("Baliq")
    elif m==3 and 1<=d<21:
        print("Baliq")
    elif m==3 and 20<d<=31:
        print("Qo'y")
    elif m==4 and 1<=d<20:
        print("Qo'y")  
    elif m==4 and 19<d<=30:
        print("Buzoq")
    elif m==5 and 1<=d<21:
        print("Buzoq")
    elif m==5 and 20<d<=31:
        print("Egizaklar")
    elif m==6 and 1<=d<22:
        print("Egizaklar")
    elif m==6 and 21<d<=30:
        print("Qisqichbaqa")
    elif m==7 and 1<=d<23:
        print("Qisqichbaqa")
    elif m==7 and 22<d<=31:
        print("Arslon")
    elif m==8 and 1<=d<23:
        print("Arslon")
    elif m==8 and 22<d<=31:
        print("Parizod")
    elif m==9 and 1<=d<23:
        print("Parizod")    
    elif m==9 and 22<d<=30:
        print("Tarozi")
    elif m==10 and 1<=d<23:
        print("Tarozi") 
    elif m==10 and 22<d<=31:
        print("Chayon")
    elif m==11 and 1<=d<23:
        print("Chayon")
    elif m==11 and 22<d<=30:
        print("O'qotar")
    elif m==12 and 1<=d<22:
        print("O'qotar")
    elif m==12 and 21<d<=31:
        print("Echki")
    elif m==1 and 1<=d<20:
        print("Echki")
    else:
        print("Kun yoki oyda xatolik bor")
else:
    print("Kun yoki oyda xatolik bor")


# In[ ]:


22

