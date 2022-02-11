#!/usr/bin/env python
# coding: utf-8

# # 11/02/2022
# 
# # Python asoslari
# 
# # 4-dars: Shart operatori
# 
# # Muallif: Farrux Sotivoldiyev

# In[2]:


#1
a = -3
if a>0:
    a += 1
print(a)


# In[3]:


#2
a = 2
if a>0:
    a += 1
else:
    a -=2
print(a)


# In[12]:


#3
a = -3
if a>0:
    a += 1
elif a<0:
    a -= 2
else:
    a = 10
print(a)


# In[18]:


#4
a,b,c = 5,3,-5
s = 0
if a>0:
    k1 += 1
if b>0:
    k2 += 1
if c>0:
    k3 += 1
print(f"{k1+k2+k3} ta musbat son bor")


# In[2]:


#5
a,b,c = 5,3,-5
s1 = 0
if a>0:
   s1+=1
if b>0:
   s1+=1
if c>0:
   s1+=1
print(f"{s1} ta musbat va {3-s1} ta  manfiy son bor")


# In[22]:


#6
a,b = 5,3
if a > b:
    print(a)
else:
    print(b)


# In[23]:


#7
a,b = 3,8
if a<b:
    print(a)
else:
    print(b)


# In[24]:


#8
a = 4
b = 7
if a<b:
    print(b,a)
else:
    print(a,b)


# In[25]:


#9
a = 9 
b = 6
if a<b:
    print(b,a)
else:
    a = a*b
    b = a/b
    a = a/b
    print(b,a)


# In[29]:


#10
a,b = 4,1
c = a+b
if a != b:
    a = c 
    b = c
else:
    a,b = 0,0
print(a,b)
    


# In[31]:


#11
a,b = 9,9
if a != b:
    if a<b:
        a = b
        b = b
    else:
        a = a
        b = a
elif a==b:
    a = 0
    b = 0
print(a,b)


# In[33]:


#12
a,b,c = 2,9,-2
if (a<b) and (a<c):
    print(a)
elif (b<a) and (b<c):
    print(b)
else:
    print(c)
    


# In[36]:


#13
a,b,c = 3,-2,1
if (a<b and a>c) or (a>b and a<c):
    print(a)
elif (b<a and b>c) or (b>a and b<c):
    print(b)
else:
    print(c)


# In[38]:


#14
a,b,c = 3,8,67
if a<b<c:
    print(a,c)
elif a<c<b:
    print(a,b)
elif b<a<c:
    print(b,c)
elif b<c<a:
    print(b,a)
elif c<b<a:
    print(c,a)
elif c<a<b:
    print(c,b)


# In[2]:


#15
a,b,c = 3,90,67
if a<b and a<c:
    print(b,c,"yegindi:",c+b)
elif b<c and b<a:
    print(a,c,"yegindi:",c+a)
elif c<a and c<b:
    print(a,b,"yegindi:",b+a)


# In[40]:


#16
a,b,c = 3,8,67
if a<b<c:
    a *= 2
    b *= 2    
    c *= 2
else:
    a *= -1
    b *= -1   
    c *= -1
print(a,b,c)
    


# In[46]:


#17
a,b,c = 12,8,6
if a<b<c or c<b<a :
    a *= 2
    b *= 2    
    c *= 2

else:
    a *= -1
    b *= -1   
    c *= -1
print(a,b,c)


# In[57]:


#18
a,b,c = 8,8,7
if a==b:
    print("ikkitasi teng qolganini tartib raqami:",3)
elif a==c:
    print("ikkitasi teng qolganini tartib raqami:",2)
elif b==c:
    print("ikkitasi teng qolganini tartib raqami:",1)
else:
    print("hamma raqam har hil")
    
    


# In[59]:


#19
a,b,c,d = 8,8,8,3
if a==b==c:
    print(f"uchtasi o'zaro teng,qolganini tartib raqami:{4}")
elif a==b==d:
    print(f"uchtasi o'zaro teng,qolganini tartib raqami:{3}")
elif a==d==c:
    print(f"uchtasi o'zaro teng,qolganini tartib raqami:{2}")
else:
    print(f"uchtasi o'zaro teng,qolganini tartib raqami:{1}")


# In[3]:


#20
a,b,c = 2,-6,9
if abs(b)-a < abs(c)-a:
    print(f"eng yaqin nuqta:{b} va ular orasidagi masofa: {b-a}")
elif b-a > c-a:
    print(f"eng yaqin nuqta:{c} va ular orasidagi masofa: {c-a}")


# In[7]:


#21
x = int(input("x = "))
y = int(input("y = "))
if x==0 and y==0:
    print(0)
elif y==0:
    print(1)
elif x==0:
    print(2)
else:
    print(3)


# In[5]:


#22
x,y =  2,0
if x<0 and y>0:
    print(x,y,"nuqta 1-chorakda joylashgan")
elif x>0 and y>0:
    print(x,y,"nuqta 2-chorakda joylashgan")
elif x<0 and y<0:
    print(x,y,"nuqta 3-chorakda joylashgan")
elif x>0 and y<0:
    print(x,y,"nuqta 4-chorakda joylashgan")
elif x==0:
     print(x,y,"nuqta OY o'qida joylashgan")
else:
     print(x,y,"nuqta OX o'qida joylashgan")


# In[6]:


#23     ishlanadi
x1,y1 = 2,5
x2,y2 = 8,5
x3,y3 = 2,2
if x1==x2 and y1==y3:


# In[63]:


#24
from math import sin
x = int(float(input("x = ")))
if x > 0:
    fx = 2* sin(x)
elif x <= 0:
    fx = x-6
print(f"fx = {fx}")


# In[4]:


#25
x = int(float(input("x = ")))
if x<-2 or x>2:
    print("Fx =",x*2)
else:
    print("Fx =",x*-3)


# In[5]:


#26
x = int(float(input("x = ")))
if x<=0:
    print("Fx =",-x)
elif 0<x<2:
    print("Fx =",x**2)
elif x>=2:
    print("Fx =",4)
    


# In[10]:


#27
x = int(float(input("x=")))
if x<0:
    print("Fx =",0)
elif x%2==0:
    print("Fx =",1)
elif x%2==1:
    print("Fx =",-1)


# In[24]:


#28
x = int(input("Yil = "))
if x%100 == 0:
    if x%400 == 0:
        print("Kabisa")
    else:
        print("Kabisa emas")
elif x%4 == 0:
    print("Kabisa")

else:
    print("Kabisa emas")


# In[26]:


#29
x = -26
if x>0:
    if x%2 ==0:
        print(f"{x} musbat juft son")
    else:
        print(f"{x} musbat toq son")
elif x<0:
    if x%2 ==0:
        print(f"{x} manfiy juft son")
    else:
        print(f"{x} manfiy toq son")
else:
    print(f"son 0 ga teng")
    
        


# In[29]:


#30
x =int(input("x = "))
if x<10:
    if x%2 ==0:
        print("Bir xonali juft son")
    else:
        print("Bir xonali toq son")
elif x>9 and x<100 :
    if x%2 ==0:
        print("Ikki xonali juft son")
    else:
        print("Ikki xonali toq son")
elif x>99 and x<1000:
    if x%2 ==0:
        print("Uch xonali juft son")
    else:
        print("Uch xonali toq son")
else:
    print("Kiritgan soningiz 3 xonalidan kichik bolishi kerak")

