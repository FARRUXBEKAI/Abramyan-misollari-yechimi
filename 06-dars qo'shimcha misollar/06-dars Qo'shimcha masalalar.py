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

# In[1]:


# 1-misol Sekund kiritilsa uni yil,oy,kun,soat,minut,sekund larda ifodalsh
n = int(input("Kun bo'yi o'tgan sekund: "))
yil = n//(86400*360)
oy = n%(86400*360)//(86400*30)
kun = n%(86400*30)//86400
soat = n%86400//3600
minut = n%3600//60
sekund = n%60
print(yil,"Yil\n",oy,"Oy\n",kun,"Kun\n",soat,"Soat\n",minut,"Minut\n",sekund,"Sekund")


# In[2]:


# 2-misol Bayt kiritilsa uni GB,MB,KB,B larda ifodalash
#1kb = 1024b
#1mb = 1024kb
#1gb = 1024mb

B = int(input("Baytlarda kiriting:"))
GB = B//(2**30)
MB = B%(2**30)//(2**20)
KB = B%(2**20)//(2**10)
B = B%(2**10)
print(GB,MB,KB,B)


# In[3]:


# 3-misol for->Qo'shish va ayirish amali yordamida * amalini bajarish
a = int(input("1-ko'paytuvchini kiriting:  a = "))  
b = int(input("2-ko'paytuvchini kiriting:  b = "))  
s=0
for i in range(1,a+1):
    s+=b
print(s)


# In[4]:


# 4-misol while->Qo'shish va ayirish amali yordamida * amalini bajarish
a = int(input("Bo'linuvchini kiriting:  a = "))  
b = int(input("Bo'luvchini kiriting:  b = "))
s = 0
k = 0
while k<a:
    s+=b
    k+=1
print(s)


# In[6]:


# 5-misol Qo'shish va ayirish amali yordamida // amalini bajarish
a = int(input("Bo'linuvchini kiriting:  a = "))  
b = int(input("Bo'luvchini kiriting:  b = "))
k = 0
while a>=b:
    k+=1
    a-=b
print(k)


# In[7]:


# 6-misol Qo'shish va ayirish amali yordamida % amalini bajarish
a = int(input("Bo'linuvchini kiriting:  a = "))  
b = int(input("Bo'luvchini kiriting:  b = "))
k = 0
while a>=b:
    a-=b
print(a)


# In[8]:


# 7-misol shart operatorini bir qatorda yozish
a = int(input("a = "))
b = 1 if a>0 else -1 if a==0 else 0
print(b)


# In[9]:


# 8-misol kun,oy va yil kiritiladi kabisa yili va oddiy yil ekanini ham nazarga olib oldingi kunni chiqarsin
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


# In[10]:


# 9-misol
# kun,oy va yil kiritiladi kabisa yili va oddiy yil ekanini ham nazarga
# olib kiritilgan kundan 2 kun keyingi kunni chiqarilsin

d = int(input("day = "))
m = int(input("month = "))
y = int(input("year = "))

if y%4==0:
    kabisa=True
if y%100==0 and y%400!=0:
    kabisa=False
if 1<=d<=31 and 1<=m<=12 and y>0:   
    if d==30 and (m==1 or m==3 or m==5 or m==7 or m==8 or m==10):
        print(f"{1}/{m+1}/y")
    elif d==29 and (m==4 or m==6 or m==9 or m==11):
        print(f"{1}/{m+1}/{y}")
    elif d==28 and kabisa:
        print(f"{1}/{m+1}/{y}")
    elif d==29 and kabisa:
        print(f"{2}/{m+1}/{y}")
    elif d==27 and not kabisa:
        print(f"{1}/{m+1}/{y}")
    elif d==28 and not kabisa:
        print(f"{2}/{m+1}/{y}")
    elif d==30 and m==12:
        print(f"{1}/{1}/{y+1}")  
    else:
        print(f"{d+2}/{m}/{y}")
else:
    print("Xato")


# # 10-misol
# ![image.png](attachment:image.png)

# In[11]:


y = int(input("Year = "))
h = (y-4)%12
r = (y-4)%5

hayvon = ["sichqon","sigir","yo'lbars","quyon","ajdar","ilon","ot","qo'y","maymun","tovuq","it","to'ng'iz"]
rang = ["yashil","qizil","sariq","oq","qora"]

print(rang[r],hayvon[h],"yili")


# In[12]:


# 3-misol
# kun,oy va yil kiritiladi kabisa yili va oddiy yil ekanini ham nazarga olib keyingi kunni chiqarsin
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


# In[13]:


# 4-misol
# 999 000 000 gacha sonni so'zda ifodalash

a = int(input("son kiriting: "))

yuzmln = a//10**8
onmln = a%10**8//10**7
mln = a%10**7//10**6
yuzming = a%10**6//10**5
onming = a%10**5//10**4
ming = a%10**4//10**3
yuz = a%10**3//10**2
on = a%10**2//10
bir = a%10

yuzlik = ["","biryuz","ikkiyuz","uchyuz","to'rtyuz","beshyuz","oltiyuz","yettiyuz","sakkizyuz","to'qqizyuz"]
onlik = ["","o'n","yigirma","o'ttiz","qirq","ellik","oltmish","yetmish","sakson","to'qson","yuz"]
birlik = ["","bir","ikki","uch","to'rt","besh","olti","yetti","sakkiz","to'qqiz","o'n"]

uzunlik = len(str(a))

if uzunlik==9:
    if yuzmln or onmln or mln:
        print(f"{yuzlik[yuzmln]} {onlik[onmln]} {birlik[mln]} million ",end=' ')
    if yuzming or onming or ming:
        print(f"{yuzlik[yuzming]} {onlik[onming]} {birlik[ming]} ming ",end=' ')      
elif uzunlik==8:
    if onmln or mln:
        print(f"{onlik[onmln]} {birlik[mln]} million ",end=' ')
    if yuzming or onming or ming:
        print(f"{yuzlik[yuzming]} {onlik[onming]} {birlik[ming]} ming ",end=' ')      
elif uzunlik==7:
    if mln:
        print(f"{birlik[mln]} million ",end=' ')
    if yuzming or onming or ming:
        print(f"{yuzlik[yuzming]} {onlik[onming]} {birlik[ming]} ming ",end=' ') 
elif uzunlik==6:
    if yuzming or onming or ming:
        print(f"{yuzlik[yuzming]} {onlik[onming]} {birlik[ming]} ming ",end=' ')      
elif uzunlik==5:
    if onming or ming:
        print(f"{onlik[onming]} {birlik[ming]} ming ",end=' ')  
elif uzunlik==4:
    if ming:
        print(f"{birlik[ming]} ming ",end=' ') 

print(f"{yuzlik[yuz]} {onlik[on]} {birlik[bir]}")

