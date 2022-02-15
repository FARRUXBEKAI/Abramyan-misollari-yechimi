#!/usr/bin/env python
# coding: utf-8

# # 15/02/2022
# 
# # Python asoslari
# 
# # 6-dars: Tanlash operatorigacha bo'lgan vazifa misollarni yechish
# 
# # Muallif: Farrux Sotivoldiyev
# 

# In[17]:


#1 Sekund kiritilsa uni yil,oy,kun,soat,minut,sekund larda ifodalsh
n = int(input("Kun bo'yi o'tgan sekund: "))
yil = n//(86400*360)
oy = n%(86400*360)//(86400*30)
kun = n%(86400*30)//86400
soat = n%86400//3600
minut = n%3600//60
sekund = n%60
print(yil,"Yil\n",oy,"Oy\n",kun,"Kun\n",soat,"Soat\n",minut,"Minut\n",sekund,"Sekund")


# In[20]:


#2 Bayt kiritilsa uni GB,MB,KB,B larda ifodalash
#1kb = 1024b
#1mb = 1024kb
#1gb = 1024mb

B = int(input("Baytlarda kiriting:"))
GB = B//(2**30)
MB = B%(2**30)//(2**20)
KB = B%(2**20)//(2**10)
B = B%(2**10)
print(GB,MB,KB,B)


# In[20]:


# for->Qo'shish va ayirish amali yordamida * amalini bajarish
a = int(input("1-ko'paytuvchini kiriting:  a = "))  
b = int(input("2-ko'paytuvchini kiriting:  b = "))  
s=0
for i in range(1,a+1):
    s+=b
print(s)


# In[22]:


# while->Qo'shish va ayirish amali yordamida * amalini bajarish
a = int(input("Bo'linuvchini kiriting:  a = "))  
b = int(input("Bo'luvchini kiriting:  b = "))
s = 0
k = 0
while k<a:
    s+=b
    k+=1
print(s)


# In[27]:


#Qo'shish va ayirish amali yordamida // amalini bajarish
a = int(input("Bo'linuvchini kiriting:  a = "))  
b = int(input("Bo'luvchini kiriting:  b = "))
k = 0
while a>=b:
    k+=1
    a-=b
print(k)


# In[31]:


#Qo'shish va ayirish amali yordamida % amalini bajarish
a = int(input("Bo'linuvchini kiriting:  a = "))  
b = int(input("Bo'luvchini kiriting:  b = "))
k = 0
while a>=b:
    a-=b
print(a)


# In[11]:


# shart operatorini bir qatorda yozish
a = int(input("a = "))
b = 1 if a>0 else -1 if a==0 else 0
print(b)


# In[8]:


# kun,oy va yil kiritiladi kabisa yili va oddiy yil ekanini ham nazarga olib oldingi kunni chiqarsin
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

