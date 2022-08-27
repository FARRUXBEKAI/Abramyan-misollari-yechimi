#!/usr/bin/env python
# coding: utf-8

# # 01/03/2022
# 
# # Python asoslari
# 
# # Qo'shimcha: Paskal uchburchagi
# 
# # Muallif: Farrux Sotivoldiyev

# In[1]:


# paskal uchburchagi
n = int(input("n = "))
for i in range(n):
    for j in range(n-i):
        print(' ',end="")
    for j in range(i+1):
        if j==0:
            c = 1
        else:
            c = c*(i+1-j)//j
        print(c,end=" ")
    print()
    

