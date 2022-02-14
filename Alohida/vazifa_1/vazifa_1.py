#!/usr/bin/env python
# coding: utf-8

# # 12/02/2022
# 
# # Python asoslari
# 
# # 1-vazifa: shart va tanlash operatori misollari 
# 
# # Muallif: Farrux Sotivoldiyev
# 

# In[ ]:


# Vazifa 1
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


# In[ ]:


# Vazifa 2
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

