#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Vazifa 1
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


# # Vazifa 2
# ![image.png](attachment:image.png)

# In[91]:



y = int(input("Year = "))
h = (y-4)%12
r = (y-4)%5

hayvon = ["sichqon","sigir","yo'lbars","quyon","ajdar","ilon","ot","qo'y","maymun","tovuq","it","to'ng'iz"]
rang = ["yashil","qizil","sariq","oq","qora"]

print(rang[r],hayvon[h],"yili")


# In[ ]:




