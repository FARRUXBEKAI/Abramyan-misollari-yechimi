#!/usr/bin/env python
# coding: utf-8

# # 03/03/2022
# 
# # Python asoslari
# 
# # Qo'shimcha: Tub sonlarni topish
# 
# # Muallif: Farrux Sotivoldiyev

# In[6]:


#5 Tub sonlarning optimal yechimi

n = int(input("n = "))
sanoq = 0
print(2,end=" ")
for i in range(3,n+1,2):
    k = False
    for j in range(3,int(i**(1/2))+1,2):
        sanoq += 1
        if i%j==0:
            k = True
            break
    if not k:
        print(i,end=" ")
print("Sanoq:",sanoq)

