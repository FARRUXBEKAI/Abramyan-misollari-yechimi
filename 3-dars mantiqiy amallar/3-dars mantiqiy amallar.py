#!/usr/bin/env python
# coding: utf-8

# # 11/02/2022
# 
# # Python asoslari
# 
# # 3-dars: Mantiqiy amallar
# 
# # Muallif: Farrux Sotivoldiyev
# 

# In[1]:


#1
a = 9
print(f"{a > 0}")


# In[2]:


#2
a = 5 
print(a%2 != 0)


# In[3]:


#3
a = 5
print(a%2==0)


# In[4]:


#4
a = 5
b = 4
print(a>2 and b<=3)


# In[5]:


#5
a = 8
b = 3
print(a>=0 or b <= -2)


# In[6]:


#6
a,b,c = 2,4,8
print(a<=b<=c)


# In[7]:


#7
a,b,c = 3,6,9
print(a<b<c)


# In[8]:


#8
a = 5
b = 8 
print(a%2!=0 and b%2!=0)


# In[10]:


#9
a,b = 3,9
print(a%2!=0 or b%2!=0 )


# In[17]:


#10
a,b = 9,8
print((a%2!=0 and b%2==0) or (a%2==0 and b%2!=0))


# In[18]:


#11
a = 8
b = 4
print((a%2==0 and b%2==0) or (a%2!=0 and b%2!=0))


# In[19]:


#12
a,b,c = 2,5,8
print(a>0 and b>0 and c>0)


# In[43]:


#13
a,b,c = 5,2,-9
print(a>0 or b>o or c>0)


# In[42]:


#14
a,b,c = 2,-7,-1
print(a>0 and b<0 and c<0) or (a<0 and b>0 and c<0) or (a<0 and b<0 and c>0)


# In[4]:


#15
a,b,c = 2,-5,8
print((a<0 and b>0 and c>0) or (a>0 and b<0 and c>0) or (a<0 and b>0 and c<0))


# In[5]:


#16
a = 46
print(9<a<100 and a%2==0)


# In[23]:


#17
a = 345
print(99<a<1000 and a%2!=0)


# In[24]:


#18
a = 3
b = 9
c = 3
print(a==b or a==c or b==c)


# In[26]:


#19
a,b,c = 3,6,-3
print(a==-b or a==-c or b==-c)


# In[27]:


#20
a = 457
yuz = a//100
on =  a%100//10
bir = a%10
print(yuz!=on and yuz!=bir and on!=bir)


# In[7]:


#21
a = 367
yuz = a//100
on =  a%100//10
bir = a%10
print(yuz<on<bir)


# In[8]:


#22
a = 321
yuz = a//100
on =  a%100//10
bir = a%10
print(yuz<on<bir or bir<on<yuz)


# In[30]:


#23
a = 525
yuz = a//100
on =  a%100//10
bir = a%10
print(yuz==bir)


# In[34]:


#24
from math import sqrt
a = 1
b = 5
c = 2
d = b**2 - 4*a*c
x1 = (-b + sqrt(d))/2*a
x2 = (-b - sqrt(d))/2*a
print((a*(x1**2) + b*x1 + c == 0) or (a*(x2**2) + b*x2 + c == 0))


# In[9]:


#25
x,y = -4,7
print(x<0 and y>0)


# In[10]:


#26
x,y = 4,-7
print(x>0 and y<0)


# In[11]:


#27
x,y = -4,7
print((x<0 and y>0) or (x<0 and y<0))


# In[12]:


#28
x,y = 4,7
print((x>0 and y>0) or (x<0 and y<0))


# In[14]:


#29
x,y = 5,4
x1,y1 = 1,5
x2,y2 = 7,2

print(y<=y1 and x<=x2)


# In[43]:


#30
a,b,c = 2,2,2
print(a==b==c)


# In[46]:


#31
a,b,c = 3,5,3
print(a==b or a==c or b==c)


# In[48]:


#32
a,b,c = 3,5,4
print(c == sqrt(a**2 + b**2) or a == sqrt(b**2 + c**2) or b == sqrt(a**2 + c**2))


# In[49]:


#33
a,b,c = 3,5,4
print(a+b>c or c+b>a or a+c>b)


# In[50]:


#34
a,b = 3,4
print((a+b)%2!=0)


# In[53]:


#35
a,b = 1,5
c,d = 2,8
print(((a+b)%2==0 and (c+d)%2==0) or ((a+b)%2!=0 and (c+d)%2!=0))


# In[15]:


#36
x1,y1 = 6,2
x2,y2 = 6,8
print(x1==x2 or y1==y2)


# In[40]:


#37
x1,y1 = 4,4
x2,y2 = 5,3

print(x2-1<=x1<=x2+1 and y2-1<=y1<=y2+1)


# In[34]:


#38
x1,y1 = 6,4
x2,y2 = 7,5
print(abs(x1-x2)==abs(y1-y2))


# In[41]:


#39
x1,y1 = 6,2
x2,y2 =1,7

print(x1==x2 or y1==y2 or (abs(x1-x2)==abs(y1-y2)))
    


# In[28]:


#40
x1,y1 = 5,4
x2,y2 = 7,3
print((x1-x2)**2 + (y1-y2)**2 == 5)

    

