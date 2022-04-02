#!/usr/bin/env python
# coding: utf-8

# # 30/03/2022
# # Sotivoldiyev Farruxbek
# 
# # 2 - nazorat ishi

# # Imtihon 2 soat davom etadi:
# 20:30-22:30
# 
# Kodlar adminga shu vaqt oralig'ida jo'natiladi. Natijalarni Payshanba kuni e'lon qilamiz!
# 
# 1. S = 1/-n + 1/-(n-1) + 1/-(n-2) +...+ 1/(n-2) + 1/(n-1) + 1/n n kiritilgan tepadagi ketma-ketlikni hisoblovchi dastur tuzing.
# 
# 2. /,% va // amallarisiz a ni b ga bo'lgandagi butun qismi va qoldiq qismini topuvchi dastur tuzing.
# 
# 3. N berilgan , Nta sonning EKUK ini topuvchi dastur tuzing.Funksiya bilan ishlanishi kerak. 
# 
# 4. Nta son berilgan,Nta son ichidan 1-uchragan va oxirigi uchragan maximum elementlarning indexini toping,agar maximum element faqat bitta bo'lsa shu bitta elementning indeksi chiqishi kerak. 
# 
# 5. Nta son berilgan shu Nta sonning eng katta 3 tasini topuvchi dastur tuzing.
# 

# In[8]:


# 1-savol
n = int(input("n = "))
s = 0
for i in range(-n,n+1):
    if i == 0:
        continue
    s += 1 / i
print(s)


# In[17]:


# 2-savol
a = int(input("a = "))
b = int(input("b = "))
k = 0
while b <= a:
    a -= b
    k += 1
print("Butun:",k,"\nQoldiq:",a)


# In[35]:


# 3-savol
def Ekuk(a,b):
    p = a * b
    while a!=b:
        if a > b:
            a %= b
        else:
            b %= a
            
        if a==0:
            a = b
        if b==0:
            b = a
    return p // a

def NEkuk(n):
    for i in range(1,n+1):
        k = int(input(f"k{i} = "))
        if i==1:
            ekuk = k
        else:
            ekuk = Ekuk(ekuk,k)
    return ekuk

n = int(input("N = "))
print(NEkuk(n))


# In[43]:


# 4-savol
n = int(input("n = "))
for i in range(1,n+1):
    k = int(input(f"k{i} = "))
    if i == 1:
        maxi = k
        index = 1
        continue
    if maxi < k:
        maxi = k
        index1 = i
    if maxi <= k:
        maxi = k
        index2 = i
        
if index1 == index2:
    print(index1)
else:
    print(index1,index2)


# In[47]:


# 5-savol
n = int(input("n = "))

max1 = int(input("a1 = "))
max2 = int(input("a2 = "))
max3 = int(input("a3 = "))

if max1 <= max2:
    max1,max2 = max2,max1
if max1 <= max3:
    max1,max3 = max3,max1
if max2 <= max3:
    max2,max3 = max3,max2
    
for i in range(4,n+1):
    a = int(input(f"a{i} = "))
    if a > max1:
        max3 = max2
        max2 = max1
        max1 = a
    elif max1 >= a and a>max2:
        max3 = max2
        max2 = a
    elif a <= max2 and a > max3:
        max3 = a
print(max3,max2,max1)

