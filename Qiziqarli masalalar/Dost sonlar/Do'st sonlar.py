#!/usr/bin/env python
# coding: utf-8

# # 25/02/2022
# 
# # Python asoslari
# 
# # Qo'shimcha: Do'st sonlar 
# 
# # Muallif: Farrux Sotivoldiyev

# In[ ]:


# Kiritilgan sonni do'stini topib beruvchi dastur

# 220 va 284
# 1184 va 1210
# 2620 va 2924
# 5020 va 5564
# 6232 va 6368                                            
# 10744 va 10856
# 12285 va 14595
# 17296 va 18416

n = int(input("son = "))

s = 0
for i in range(1,n):
    if n%i==0:
        s += i 
y = 0
for j in range(1,s):
        if s%j==0:
            y += j
if n==y:
    print("Do'st sonlar",y,s)
else:
    print("Do'st jufti yo'q")


# In[31]:


# Kiritilgan n sonigacha bo'lgan do'st sonlarni topib beruvchi dastur

# 220 va 284
# 1184 va 1210
# 2620 va 2924
# 5020 va 5564
# 6232 va 6368                                            
# 10744 va 10856
# 12285 va 14595
# 17296 va 18416

n = int(input("n = "))

i = 220
while True:
#     print(i,end=" ")
    if i > n:
        break
    s = 0 
    for j in range(1,int(i/2)+1):
        if i%j == 0:
            s += j
            
    h = 0
    for k in range(1,int(s/2)+1):
        if s%k == 0:
            h += k
            
    if i == h and i != s and i < s:
        print(i,s)
        i = s + 500 
    else:
        i += 1
if n < 220:
    print("Do'st sonlar yo'q")
print("Dastur tugadi")


# In[ ]:





# In[ ]:




