#!/usr/bin/env python
# coding: utf-8

# # 20/02/2022
# 
# # Python asoslari
# 
# # Qo'shimcha: Mukammal sonlar 
# 
# # Muallif: Farrux Sotivoldiyev

# In[1]:


# kiritilgan sonning  Mukammal son ekanligini topish 
#Mukammal sonlar:
#6
# 28
# 496
# 8128
# 33550336
# 8589869056
# 137438691328
# 2305843008138952128
# 2658455991569831744654692615953842176
# 191561942608236107294793378084303638130997321548169

n = int(input("n = "))

s = 0
for i in range(1,n):
    if n%i==0:
        s += i
if s==n:
    print("Mukammal son")
else:
    print("Mukammal emas")


# In[3]:


# kiritilgan n sonigacha bo'lgan Mukammal sonlarni topish

n = int(input("n = "))

for j in range(1,n+1):
    s = 0
    for i in range(1,j):
        if j%i==0:
            s += i
    if s==j:
        print(j)

