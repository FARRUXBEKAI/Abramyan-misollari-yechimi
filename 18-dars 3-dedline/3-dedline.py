#!/usr/bin/env python
# coding: utf-8

# # 12/05/2022
# # Sotivoldiyev Farruxbek
# 
# # 3 - nazorat ishi

# # Imtihon 2 soat davom etadi:
# 20:00-22:00
# 
# Kodlar adminga shu vaqt oralig'ida jo'natiladi. Natijalarni Yakshanba kuni e'lon qilamiz!
# 
# 1. Nta elementdan iborat massiv berilgan, shu massivning elementlarini fagat bittadan qoldiruvchi dastur tuzing. Shart:
#    2 tadan ko'p element bo'lsa faqat oxirgi o'rinda turgan massiv oldirilsin
#    Masalan: N = 10
#    Kiruvchi massiv: [1,1,3,4,2,4,5,4,2,1]
#    Chiquvchi massiv: [3,5,4,2,1]
# 
# 
# 2. Nta elementdan iborat massiv berilgan, massivning eng katta 2 ta elementi orasidagi sonlarni almashtiruvchi dastur tuzing.
#    Qo'shimcha: Agar Faqat 1 ta katta son kelsa massiv o'zgarishsiz qoldirilsin, agar 2 tadan ko'p maximum son kelsa 1-uchragan      va oxirigi uchragan elementlari orasidagi elementlarni teskari yozish kerak.
# 
# 3. NxN o'lchamli matritsa berilgan, matritsaning ustunlarini ustunlarning minimum elementiari bo'yicha o'sish tartibida
#    saralovchi dastur tuzing. E'tibor bering ustunlarining minimum elementilari bo'yicha saralash kerak.
# 
# 4. NxM o'lchamli matritsa berilgan, matritsaning satrlarining eng katta elementlari yig'indisini toping.
# 
# 5. NxN matritsa berilgan.
# 
#    N = 5 bo'lsa:  
#                      0 -1 -2 -3 -4
#                      1  0 -1 -2 -3
#                      2  1  0 -1 -2
#                      3  2  1  0 -1
#                      4  3  2  1  0
#    N = 6 bo'lsa:
#                      0 -1 -2 -3 -4 -5
#                      1  0 -1 -2 -3 -4
#                      2  1  0 -1 -2 -3
#                      3  2  1  0 -1 -2
#                      4  3  2  1  0 -1
#                      5  4  3  2  1  0
#                          

# In[92]:


# 1-misol
from random import randint
n = int(input("n = "))
massiv = [randint(1,5) for i in range(n)]
print(massiv)

i = 0
while i<len(massiv):
    if massiv.count(massiv[i]) > 1:
        for _ in range(massiv.count(massiv[i])-1):
            massiv.remove(massiv[i])
        continue
    i += 1
    
print(massiv)


# In[71]:


# 2-misol
from random import randint
n = int(input("n = "))
massiv = [randint(1,9) for i in range(n)]
print(massiv)

maxi = max(massiv)
soni = massiv.count(maxi)
temp = []
flag = True
if soni>=2:
    for i in range(n):
        if flag and maxi==massiv[i]:
            temp.append(i)
            flag = False
        elif maxi==massiv[i]:
            index = i
    temp.append(index)
    
    massiv2 = list(reversed(massiv[temp[0]+1:temp[1]]))
    for _ in range(len(massiv2)):
        del massiv[temp[0]+1]
    for i in range(len(massiv2)-1,-1,-1):
        massiv.insert(temp[0]+1,massiv2[i])
        
print(massiv)


# In[90]:


# 3-misol
from random import randint
n = int(input("n = "))
matrix = [[randint(-5,9) for i in range(n)] for _ in range(n)]
for i in matrix:
    print(*i)
print()

for _ in range(n):
    for i in range(n-1):
        mini1 = matrix[0][i]
        mini2 = matrix[0][i+1]
        
        for k in range(1,n):
            if mini1>matrix[k][i]:
                mini1 = matrix[k][i]
                
        for k in range(1,n):
            if mini2>matrix[k][i+1]:
                mini2 = matrix[k][i+1]
                
        if mini1>mini2:
            for k in range(n):
                matrix[k][i],matrix[k][i+1] = matrix[k][i+1],matrix[k][i]
        
for i in matrix:
    print(*i)


# In[88]:


# 4-misol
from random import randint
n = int(input("n = "))
m = int(input("m = "))
matrix = [[randint(1,9) for i in range(n)] for _ in range(m)]
for i in matrix:
    print(*i)
print()

s = 0
for i in range(m):
    s += max(matrix[i])
    
print(s)


# In[87]:


# 5-misol
n = int(input("n = "))
matrix = [[0 for i in range(n)] for _ in range(n)]

for i in range(n):
    k = i
    for j in range(n):
        matrix[i][j] = k
        k -= 1
        
for i in matrix:
    print(*i)

