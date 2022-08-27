#!/usr/bin/env python
# coding: utf-8

# # 2/01/2021
# 
# # Python asoslari
# 
# # Mavzu: Tub va murakkab sonni topish
# 
# # Muallif: Farrux Sotivoldiyev
# 

# In[5]:


# Kiritilgan son tub yoki murakkabligini topuvchi dastur
a = int(input("Son = "))
murakkab = 0
for i in range(2, a):
    if a % i == 0:
        murakkab += 1
if murakkab:
    print("Murakkab son")
else:
    print("Tub son")


# In[6]:


#kiritilgan songacha bolgan tub va murakkab sonlarni topuvchi dastur
a = int(input("Son = "))
boshi = 2
tub = []
murakkab = []
while boshi <= a:
    datchik = 0
    for i in range(2,boshi):
        if boshi % i == 0:
            datchik += 1
    if datchik:
        murakkab.append(boshi)
    else:
        tub.append(boshi)
    boshi +=1
print(f"Murakkab sonlar: {murakkab}\nTub sonlar: {tub}")


# In[ ]:




