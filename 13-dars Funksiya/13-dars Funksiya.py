#!/usr/bin/env python
# coding: utf-8

# # 24/03/2022
# 
# # Python asoslari
# 
# # 13-dars : Funksiya bilan ishlash
# 
# # Muallif: Farrux Sotivoldiyev

# In[6]:


#FunSimple1
def PowerA3(x):
    return x**3

a = float(input("a = "))
print(PowerA3(a))


# In[7]:


#FunSimple2
def PowerA234(x):
    a = x**2
    b = x**3
    c = x**4
    return a,b,c

a = float(input("a = "))
print(PowerA234(a))


# In[12]:


#FunSimple3
def MEAN(x,y):
    arif = (x+y)/2
    geo = (x*y)**(1/2)
    return arif,geo

a = float(input("a = "))
b = float(input("b = "))
print(MEAN(a,b))


# In[14]:


#FunSimple4
def Triangle(x):
    s = (x**2 * 3**(1/2)) / 4
    p = 3 * x
    return s,p

a = float(input("a = "))
print(Triangle(a))


# In[20]:


#FunSimple5
def RectPS(x1,y1,x2,y2):
    x = abs(x1 - x2)
    y = abs(y1 - y2)
    s = x * y
    p = 2 * (x + y)
    return s,p

a1 = int(input("a1 = "))
b1 = int(input("b1 = "))
a2 = int(input("a2 = "))
b2 = int(input("b2 = "))
print(RectPS(a1,b1,a2,b2))


# In[15]:


#FunSimple6
def DigitCountSum(x):
    s = 0
    k = 0
    while x > 0:
        k += 1
        s += x%10
        x //= 10
    return k,s

a = int(input("a = "))
print(DigitCountSum(a))


# In[17]:


#FunSimple7
def InvertDigit(x):
    s = 0
    while x != 0:
        s = x%10 + s*10
        x//=10
    return s

a = int(input("a = "))
print(InvertDigit(a))


# In[51]:


#FunSimpl8
def AddRightDigit(x,y):
    add = (x + y / 10) * 10
    return int(add)

K = int(input("k = "))
R = int(input("r = "))
print(AddRightDigit(K,R))


# In[63]:


#FunSimple9
def AddLeftDigit(x,y):
    k = 0
    s = x
    while s != 0:
        k += 1
        s //= 10
    add = x + 10**k * y
    return add

K = int(input("k = "))
R = int(input("r = "))
print(AddLeftDigit(K,R))


# In[3]:


#FunSimple10
def swap(x,y):
    return y,x

a = int(input("a = "))
b = int(input("b = "))
print(swap(a,b))


# In[24]:


#FunSimple11
def Minmax(x,y):
    if x < y:
        x,y = y,x
    return x,y

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
d = int(input("d = "))
a,b = Minmax(a,b)
c,d = Minmax(c,d)
a,c = Minmax(a,c)
b,d = Minmax(b,d)
print(a,d)


# In[21]:


#FunSimple12
def Sortlnc3(a,b,c):
    if a <= b <= c:
        return a,b,c
    elif a <= c <= b:
        return a,c,b
    elif c <= a <= b:
        return c,a,b
    elif c <= b <= a:
        return c,b,a
    elif b <= c <= a:
        return b,c,a
    elif b <= a <= c:
        return b,a,c
    
A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))
print(Sortlnc3(A,B,C))


# In[23]:


#FunSimple13
def sort3(a,b,c):
    if a<c:
        a,c = c,a
    if a<b:
        a,b = b,a
    if b<c:
        b,c = c,b
    return a,b,c

A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))
print(sort3(A,B,C))


# In[46]:


#FunSimple14
def ShiftRight(a,b,c):
    c = a + b + c
    a = c - a - b
    b = c - a - b 
    c = c - a - b
    return a,b,c

A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))
print(ShiftRight(A,B,C))


# In[47]:


#FunSimple15
def ShiftLeft(a,b,c):
    a = a + b + c
    c = a - b - c
    b = a - b - c
    a = a - b - c
    return a,b,c

A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))
print(ShiftLeft(A,B,C))


# In[51]:


#FunSimple16
def ishora(x):
    if x > 0:
        x = 1
    elif x < 0:
        x = -1
    else:
        x = 0
    return x

a = int(input("a = "))
b = int(input("b = "))
s = ishora(a) + ishora(b)
print(s)


# In[114]:


#FunSimple17
def tenglama(x,y,z):
    if (z == 0 and y != 0) or (y**2 - 4 * x * z) > 0:
        s = 2
    elif y==0 and x<0 and z>0:
        s = 1
    elif y==0 and x>0 and z<0:
        s = 1
    elif y**2 - 4 * x * z == 0:
        s = 1
    else:
        s = "Mavjud emas"
    return s

A = int(input("A = "))
B = int(input("B = "))       
C = int(input("C = "))
print(tenglama(A,B,C))


# In[64]:


#FunSimple18
def D_yuzi(x):
    s = pi * x**2
    return s

R = int(input("R = "))
print(D_yuzi(R))


# In[22]:


#FunSimple19
from math import pi
def RingS(x,y):
    s1 = pi * x**2
    s2 = pi * y**2
    return abs(s2 - s1)

R1 = int(input("R1 = "))
R2 = int(input("R2 = "))
print(RingS(R1,R2))


# In[66]:


#FunSimple20
def TriangleP(x,y):
    z = (x**2 +y**2)**(1/2)
    p = x + y + z
    return p

A = int(input("A = "))
B = int(input("B = "))
print(TriangleP(A,B))


# In[67]:


#FunSimple21
def SumRange(x,y):
    if x > y:
        return 0
    else:
        s = 0
        for i in range(x,y+1):
            s += i
        return s
    
print(SumRange(1,10))


# In[76]:


#FunSimple22
def Calc(x,y,amal):
    if amal == 1:
        s = x - y
    elif amal == 2:
        s = x * y
    elif amal == 3:
        s = x / y
    else:
        s = x + y
    return s

A = int(input("A = "))
B = int(input("B = "))
Amal = int(input("Amal = "))
print(Calc(A,B,Amal))


# In[90]:


#FunSimple23
def Quarter(x,y):
    if x > 0 and y > 0:
        s = "1-chorak"
    elif x < 0 and y > 0:
        s = "2-chorak"
    elif x < 0 and y < 0:
        s = "3-chorak"
    elif x > 0 and y < 0:
        s = "4-chorak"
    return s

x = int(input("x = "))
y = int(input("y = "))
print(Quarter(x,y))


# In[89]:


#FunSimple24
def Even(x):
    if x%2==0:
        s = True
    else:
        s = False
    return s

k = int(input("k = "))
print(Even(k))


# In[3]:


#FunSimple25
def Square(x):
    if x**0.5 % 1==0:
        s = True
    else:
        s = False
    return s

k = int(input('k = '))
print(Square(k))


# In[140]:


#FunSimple26
def Power5(x):
    i = 1
    while 5**i != x:
        if 5**i>x:
            s = False
            break
        i += 1
    else:
        s = True
    return s

k = int(input("k = "))
print(Power5(k))


# In[148]:


#FunSimple27
def PowerN(x,y):
    i = 1
    while y**i != x:
        if y**i>x:
            s = False
            break
        i += 1
    else:
        s = True
    return s

K = int(input("K = "))
N = int(input("N = "))
print(PowerN(K,N))


# In[166]:


#FunSimple28
def Prime(x):
    k = 0
    for i in range(1,x+1):
        if x%i==0:
            k += 1
    if k==2:
        return True
    else:
        return False
    
N = int(input("N = "))
print(Prime(N))


# In[169]:


#FunSimple29
def DigitCount(x):
    k = 0
    while x != 0:
        k += 1
        x //= 10
    return k

K = int(input("K = "))
print(DigitCount(K))


# In[20]:


#FunSimple30
def Digit(x,y):
    k = 1
    for i in str(x):
        if k==y:
            return int(i)
            break
        k+=1
    else:
        return -1
    
K = int(input("K = "))
N = int(input("N = "))
Digit(K,N)


# In[63]:


#FunSimple31
def Palindrom(x):
    k = x
    s = 0
    while k != 0:
        s = k%10 + s*10
        k //= 10
        
    if s == x:
        return True
    else:
        return False
N = int(input("N = "))
print(Palindrom(N))


# In[64]:


#FunSimple32
from math import pi
def DegToRad(x):
    rad = (pi / 180) * x
    return rad

D = int(input("D = "))
print(DegToRad(D))


# In[19]:


#FunSimple33
from math import pi
def RadToDeg(x):
    deg = (180 / pi ) * x
    return deg

R = float(input("R = "))
print(RadToDeg(R))


# In[97]:


#FunSimple34
def Fact(x):
    s = 1
    for i in range(1,x+1):
        s *= i
    return s

N = int(input("N = "))
print(Fact(N))


# In[100]:


#FunSimple35
def Fact2(x):
    s = 1
    for i in range(x,0,-2):
        s *= i
    return s

N = int(input("N = "))
print(Fact2(N))


# In[110]:


#FunSimple36
def Fib(x):
    f1 = 1
    f2 = 1
    for i in range(x-2):
        f1 = f1 + f2
        f2 = f1 - f2
    return f1

N = int(input("N = "))
print(Fib(N))


# In[113]:


#FunSimple37
def Power1(x,y):
    return x**y

A = float(input("A = "))
B = int(input("B = "))
print(Power1(A,B))
print(Power1(3,B))
print(Power1(3.5,B))


# In[119]:


#FunSimple38
def Power2(x,y):
    if x >= 0:
        s = x**y
    else:
        s = 1 / x**y
    return s

A = float(input("A = "))
B = int(input("B = "))
print(Power2(A,B))


# In[38]:


#FunSimple39
def Power1(x,y):
    return x**y

def Power2(x,y):
    if x >= 0:
        s = x**y
    else:
        s = 1 / x**y
    return s

def Power3(a,n):
    if n%1 != 0:
        return Power2(a,n)
    else:
        return Power1(a,n)
        
A = float(input("A = "))
N = float(input("B = "))
print(Power3(A,N))


# In[40]:


#FunSimple40
def Exp1(x,e):
    p = 1
    s = 1
    i = 1
    while True:
        p *= i
        if x**i/p < e:
            return s
        else:
            s+= x**i / p
            i += 1
            
x = int(input("x = "))
e = float(input("e = "))
print(Exp1(x,e))


# In[75]:


#FunSimple41
def Sin1(x,e):
    fact = 1
    s = x
    i = 1
    while True:
        fact *= 2*i * (2*i + 1)
        daraja = (-1)**i * x**(2*i+1)
        if abs(daraja/fact) < e:
            return s
        else:
            s += daraja / fact
            i += 1
            
x = int(input("x = "))
e = float(input("e = "))
print(Sin1(x,e))


# In[42]:


#FunSimple42
def Cos1(x,e):
    s = 1
    fact = 1
    i = 1
    while True:
        fact *= (2*i-1) * 2*i
        daraja = (-1)**i * x**(2*i)
        if abs(daraja/fact) < e:
            return s
        else:
            s += daraja / fact
            i += 1
            
x = int(input("x = "))
e = float(input("e = "))
print(Cos1(x,e))


# In[89]:


#FunSimple43
def Ln1(x,e):
    s = 0
    i = 1
    while True:
        daraja = ((-1)**(i-1) * x**i) / i   
        if abs(daraja)  < e:
            return s
        else:
            s +=  daraja
            i += 1
            
x = float(input("x = "))
e = float(input("e = "))
print(Ln1(x,e))      


# In[90]:


#FunSimple44
def Arctg1(x,e):
    s = 0
    i = 0
    while True:
        daraja = (-1)**(i) * x**(2*i+1) / (2*i+1)
        if abs(daraja) < e:
            return s
        else:
            s += daraja
            i += 1
            
x = float(input("x = "))
e = float(input("e = "))
print(Arctg1(x,e))   


# In[16]:


#FunSimple45
def Power4(x,a,e):
    s = 1
    i = 1
    p = 1
    a1 = a
    while True:
        p *= i
        daraja = x**i
        if abs(a*daraja/p) < e:
            return s
        else:
            s += a*daraja / p
            if (a1 - i) != 0 :
                a *= (a1 - i)     
            i += 1
            
x = int(input("x = "))
a = int(input("a = "))
e = float(input("e  = "))
print(Power4(x,a,e))


# In[4]:


#FunSimple46
def Ekub(x,y):
    while x != y:
        if x > y:
            x %= y
        else:
            y %= x
        if x == 0:
            x = y
        if y == 0:
            y = x
            
    return x

A = int(input("A = "))
B = int(input("B = "))
print(Ekub(A,B))


# In[34]:


#FunSimple47
def Frac1(x,y):
    ekub =  x
    while x%ekub != 0 or y%ekub != 0:
        ekub -= 1
    x //= ekub
    y //= ekub 
    
    return x,y

a =  int(input("a = "))
b =  int(input("b = "))
c,d = Frac1(a,b)
print(f"{c}/{d}")


# In[7]:


#FunSimple48
def Ekuk(x,y):
    s = x * y
    while x != y:
        if x > y:
            x %= y
        else:
            y %= x
        if x == 0:
            x = y
        if y == 0:
            y = x
            
    return s // x

A = int(input("A = "))
B = int(input("B = "))
ekuk = Ekuk(A,B)
print("Ekuk = ",ekuk)


# In[25]:


#FunSimple49
def Ekub_Ekuk(x,y,z):          
    ekub = x
    ekuk = x
    while x%ekub != 0 or y%ekub != 0 or z%ekub != 0:
        ekub -= 1
    while ekuk%x != 0 or ekuk%y != 0 or ekuk%z != 0:
        ekuk += 1
        
    return  ekub,ekuk

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

print(Ekub_Ekuk(a,b,c))


# In[11]:


#FunSimple50
def TimeToHMS(x):
    soat = x // 3600
    minut = x % 3600 // 60
    sekund = x % 60
    
    return soat,minut,sekund

T = int(input("T = "))
print(TimeToHMS(T))


# In[14]:


#FunSimple51
def IncTime(x,y,z):
    soat = x * 3600
    minut = y * 60
    sekund = z
    T = soat + minut + sekund
    
    return T

H = int(input("H = "))
M = int(input("M = "))
S = int(input("S = "))
print(IncTime(H,M,S))


# In[26]:


#FunSimple52
def IsLeapYear(x):
    kabisa = False
    if x % 4 ==0:
        kabisa = True
    if x%100 == 0 and x%400 != 0:
        kabisa = False
        
    return kabisa

Y = int(input("Year =  "))
print(IsLeapYear(Y))


# In[27]:


#FunSimple53
def MonthDays(x,y):
    kabisa = False
    if y%4==0:
        kabisa = True
    if y%100==0 and y%400!=0:
        kabisa = False
        
    if x==1 or x==3 or x==5 or x==7 or x==8 or x==10 or x==12:
        kun = 31
    elif x==4 or x==6 or x==9 or x==11:
        kun = 30
    elif x==2:
        kun = 28 + kabisa
        
    return kun

Y = int(input("Year =  "))
M = int(input("Month =  "))
print(MonthDays(M,Y))


# In[9]:


#FunSimple54
def PrevDate(d,m,y):
    kabisa = False
    if y%4==0:
        kabisa=True
    if y%100==0 and y%400!=0:
        kabisa=False

    if d == 1 and (m==5 or m==7 or m==10 or m==12):  
            d = 30
            m -= 1
    elif d == 1 and m == 3:
            d = 28 + kabisa
            m = 2
    else:
        if d == 1:
            d = 31
            m -= 1
        if m == 0:
            m = 12
            y -= 1
        else:
            d -= 1

    return d,m,y

D = int(input("Day =  "))
M = int(input("Month =  "))
Y = int(input("Year =  "))
print(PrevDate(D,M,Y))


# In[15]:


#FunSimple55
def NextDate(d,m,y):
    kabisa = False
    if y%4==0:
        kabisa=True
    if y%100==0 and y%400!=0:
        kabisa=False

    if d == 31 and (m==1 or m==3 or m==5 or m==7 or m==8 or m==10):  
            d = 1
            m += 1
    elif d == 30 and (m==4 or m==6 or m==9 or m==11):
            d = 1
            m += 1
    elif d == 31 and m == 12:
        d = 1
        m = 1
        y += 1
    elif d == 28 + kabisa:
        d = 1
        m = 3
    else:
        d+=1
        
    return d,m,y

D = int(input("Day =  "))
M = int(input("Month =  "))
Y = int(input("Year =  "))
print(NextDate(D,M,Y))


# In[17]:


#FunSimple56
def Leng(x1,y1,x2,y2):
    x = abs(x1-x2)
    y = abs(y1-y2)
    z = (x**2 + y**2)**0.5
    return z

x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))
print(Leng(x1,y1,x2,y2))


# In[6]:


#FunSimple57
def Leng(x1,y1,x2,y2):
    x = abs(x1-x2)
    y = abs(y1-y2)
    z = (x**2 + y**2)**0.5
    return z

def Perim(x1,y1,x2,y2,x3,y3):
    a = Leng(x1,y1,x2,y2) 
    b = Leng(x1,y1,x3,y3)    
    c = Leng(x3,y3,x2,y2)
    p = a + b + c
    return p

x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))
x3 = int(input("x3 = "))
y3 = int(input("y3 = "))
print(Perim(x1,y1,x2,y2,x3,y3))


# In[5]:


#FunSimple58
def HalfPerim(a,b,c):
    p = (a + b + c) / 2
    return p

def Leng(x1,y1,x2,y2):
    x = abs(x1-x2)
    y = abs(y1-y2)
    z = (x**2 + y**2)**0.5
    return z

def Area(x1,y1,x2,y2,x3,y3):
    a = Leng(x1,y1,x2,y2) 
    b = Leng(x1,y1,x3,y3)    
    c = Leng(x3,y3,x2,y2)
    p = HalfPerim(a,b,c)
    s = (p*(p-a)*(p-b)*(p-c))**0.5
    return s

x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))
x3 = int(input("x3 = "))
y3 = int(input("y3 = "))
print(Area(x1,y1,x2,y2,x3,y3))


# In[4]:


#FunSimple59
def Leng(x1,y1,x2,y2):
    x = abs(x1-x2)
    y = abs(y1-y2)
    z = (x**2 + y**2)**0.5
    return z

def Area(x1,y1,x2,y2,x3,y3):
    a = Leng(x1,y1,x2,y2) 
    b = Leng(x1,y1,x3,y3)    
    c = Leng(x3,y3,x2,y2)
    p = (a + b + c) / 2
    s = (p*(p-a)*(p-b)*(p-c))**0.5
    return s

def Dist(x1,y1,x2,y2,x3,y3):
    s = Area(x1,y1,x2,y2,x3,y3)
    a = Leng(x1,y1,x2,y2)
    h = 2 * s / a 
    return h

x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))
x3 = int(input("x3 = "))
y3 = int(input("y3 = "))
print(Dist(x1,y1,x2,y2,x3,y3))


# In[5]:


#FunSimple60
def HalfPerim(a,b,c):
    p = (a + b + c)/2
    return p

def Leng(x1,y1,x2,y2):
    x = abs(x1-x2)
    y = abs(y1-y2)
    z = (x**2 + y**2)**0.5
    return z

def Dist(x1,y1,x2,y2,x3,y3):
    a = Leng(x1,y1,x2,y2)
    b = Leng(x1,y1,x3,y3)    
    c = Leng(x3,y3,x2,y2)
    return a,b,c

def Area(a,b,c):
    p = HalfPerim(a,b,c)
    s = (p*(p-a)*(p-b)*(p-c))**0.5
    return s

def Heights(x1,y1,x2,y2,x3,y3):
    a,b,c = Dist(x1,y1,x2,y2,x3,y3)
    s = Area(a,b,c)
    h1 = 2 * s / a 
    h2 = 2 * s / b 
    h3 = 2 * s / c 
    return h1,h2,h3

x1 = int(input("x1 = "))
y1 = int(input("y1 = "))
x2 = int(input("x2 = "))
y2 = int(input("y2 = "))
x3 = int(input("x3 = "))
y3 = int(input("y3 = "))
print(Heights(x1,y1,x2,y2,x3,y3))

