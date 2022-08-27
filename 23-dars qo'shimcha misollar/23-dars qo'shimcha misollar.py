#!/usr/bin/env python
# coding: utf-8

# # 27/08/2022
# 
# # Python asoslari
# 
# # 23-dars: Matritsa,String,Lambda,Map,Filter,Reduce va Dekoratorlarga oid qo'shimcha misollarni yechish
# 
# # Muallif: Farrux Sotivoldiyev

# In[4]:


# savol-1
# random matritsa hosil qiling va uni shunday o'zgartiring yani o'sh elementga uzi turgan indexni darajaga ko'tarib 
# qo'shilsin .Masalan 2 5 7 9 -> 2+0^0  5+0^1 ....
#                     3 1 0 4 -> 3+1^0  1+1^1 ....
    
from random import randint
m = int(input("m = "))
n = int(input("n = "))
matrix = [[randint(1,9) for i in range(n)] for j in range(m)]
for i in matrix:
    print(*i)
    
for i in range(m):
    for j in range(n):
        matrix[i][j] = matrix[i][j] + i**j
print()     
for i in matrix:
    print(*i)


# In[ ]:





# In[7]:


# savol-2 Random massiv berilgan uning toq indexdagi elementlarini o'chiring va qolgan
# elementlarini teskari sort qilamiz

#1-usul
from random import randint
k = int(input("k = "))
massiv = [randint(1,9) for i in range(k)]
print(massiv)

i = 1
while i<len(massiv):
    massiv.pop(i)
    i+=1
    
massiv.sort(reverse=True)

print(massiv)

#2-usul
from random import randint

k = int(input("k = "))
massiv = [randint(1,9) for i in range(k)]
print(massiv)

massiv = massiv[::2]
print(sorted(massiv,reverse=True))


# In[2]:


# savol-3 by Farrux
# matn berilgan shu matndagi so'zlarning uzunligi bo'yicha saralash kerak uzundan kaltagacha.

# 1-usul
matn = input("matn kiriting: ")
x = matn.split()

for _ in range(len(x)):
    for i in range(len(x)-1):
        if len(x[i])<len(x[i+1]):
            x[i],x[i+1] = x[i+1],x[i]
            
print(" ".join(x))

# 2-usul
matn = input("matn kiriting: ")
x = matn.split()

y = sorted(x,key=len,reverse=True)

print(" ".join(y))


# # Lambda funksiyasi

# In[32]:


# savol-4
# 100 ga yaqinligi bo'yicha saralash
x = [3,56,8,9,23,43,78,92]
print(sorted(x,key=lambda i: 100-i))


# In[16]:


# savol-5 Matn berilgan
# 1- Hamma katta harflarni kichigiga aylantiramiz
# 2- Uzunligi 3 dan kichik so'zlarni o'chiramiz
# 3- So'zlarni 2-index bo'yicha sort qilamiz

matn = input("matn kiriting: ")
matn = matn.lower()
x = matn.split()

i = 0
while i<len(x):
    if len(x[i])<3:
        del x[i]
        continue
    i += 1
    
y = sorted(x,key=lambda i:i[2])   

print(" ".join(y))


# In[18]:


# savol-6 Matn berilgan.
# Oxirgi belgisi bo'yicha sortlaymiz o'zimiz yasagan funksiya orqali.

matn = input("matn kiriting: ")
x = matn.split()

def oxirgi_belgi(i):
    return i[-1]
y = sorted(x,key=oxirgi_belgi)
print(" ".join(y))


# ### sort() funksiyasi bilan ishlatilishi

# In[23]:


# sort funksiyasi bilan ishlatilishi

massiv = ["so'zlarning", 'kaltaga.', 'ber', 'matndagi', 'uzun', "bo'yicha"]

massiv.sort(key=lambda i:len(i))

print(massiv)


# ### map() funksiyasi bilan ishlatilishi.

# In[19]:


# map() funksiyasi bilan ishlatilishi

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2 , my_list))

print(new_list)


# In[63]:


# Python code to illustrate
# map() with lambda()
# to get double of a list.
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(map(lambda x: x*2, li))
print(final_list)


# In[64]:


# Python program to demonstrate
# use of lambda() function
# with map() function
animals = ['dog', 'cat', 'parrot', 'rabbit']

# here we intend to change all animal names
# to upper case and return the same
uppered_animals = list(map(lambda animal: str.upper(animal), animals))

print(uppered_animals)


# ### filter() funksiyasi bilan ishlatilishi.

# In[20]:


# filter() funksiyasi bilan ishlatilishi

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

print(new_list)


# In[61]:


# filter() with lambda()
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

final_list = list(filter(lambda x: (x%2 != 0) , li))
print(final_list)


# In[62]:


# Python 3 code to people above 18 yrs
ages = [13, 90, 17, 59, 21, 60, 5]

adults = list(filter(lambda age: age>18, ages))

print(adults)


# ### reduce() funksiyasi bilan ishlatilishi.

# In[ ]:


# Python code to illustrate
# reduce() with lambda()
# to get sum of a list

from functools import reduce
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print (sum)


# In[65]:


# python code to demonstrate working of reduce()
# with a lambda function

# importing functools for reduce()
import functools

# initializing list
lis = [ 1 , 3, 5, 6, 2, ]

# using reduce to compute maximum element from list
print ("The maximum element of the list is : ",end="")
print (functools.reduce(lambda a,b : a if a > b else b,lis))


# ### lambda ni ichida ham funksiyaga murojat.

# In[31]:


# lambda ni ichida ham funksiyaga murojat
k = lambda x,daraja:x*daraja(x)
print(k(2,lambda x:x+5))


# ### Lambdani boshqacha tarzda ham ishlatilishi.

# In[35]:


# Lambdani boshqacha tarzda ham ishlatilishi

print((lambda x, y, z: x + y + z)(1, 2, 3))

print((lambda x, y, z=3: x + y + z)(1, 2))

print((lambda x, y, z=3: x + y + z)(1, y=2))

print((lambda *args: sum(args))(1,2,3))

print((lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3))

print((lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3))


# In[43]:


tables = [lambda x=x: x*10 for x in range(1, 11)]   # ko'rsataman
for table in tables:
    print(table(),end=" ")


# In[58]:


List = [[2,3,4],[1, 4, 16, 64],[3, 6, 9, 12]]

# Sort each sublist
sortList = lambda x: (sorted(i) for i in x)

# Get the second largest element
secondLargest = lambda x, f : [y[len(y)-2] for y in f(x)]      # ko'rsataman
res = secondLargest(List, sortList)

print(res)


# **`DETERMINANT topish`**

# In[43]:


n = int(input("n = "))
print("Matritsani kiriting:")

matrix = [list(map(int,input().split())) for i in range(n)]

assert len(matrix)==len(matrix[0]),"Ustun va satr bir biriga teng emas!"
    
def det(matrix):
    if len(matrix)==1:
        return matrix[0][0]
    elif len(matrix)==2:
        return matrix[0][0]*matrix[1][1] - matrix[1][0]*matrix[0][1]
    elif len(matrix)==3:
        return matrix[0][0]*matrix[1][1]*matrix[2][2]+matrix[0][1]*matrix[1][2]*matrix[2][0]+\
               matrix[0][2]*matrix[1][0]*matrix[2][1]-matrix[0][2]*matrix[1][1]*matrix[2][0]-\
               matrix[0][0]*matrix[1][2]*matrix[2][1]-matrix[0][1]*matrix[1][0]*matrix[2][2]
    s = 0
    for i in range(len(matrix)):
        s += matrix[0][i] * (1 if i%2==0 else -1) * det([j[:i]+j[i+1:] for j in matrix[1:]])
    return s

print("Determinanti:",det(matrix))


# **`Dekorator`**

# In[10]:


from random import randint
n = int(input("n = "))
matrix = [[randint(1,9) for _ in range(n)] for _ in range(n)]

for i in matrix:
    print(*i)
    
def almashtir(func):
    def salom(matrix):
        for i in range(n):
            for j in range(n):
                if i==2:
                    matrix[j][2],matrix[j][4] = matrix[j][4],matrix[j][2]
            break
        return matrix
    return salom
    
@almashtir
def hello(matrix):
    return matrix

print(hello(matrix))


# # 4-savol
# * nxn o'lchamli matritsa berilgan, 
# * matritsani 90 gradusga o'ngga buruvchi dastur yarating.
# 
# * Kirishda n matritsa o'lchami kiritiladi va keyingi nxn 
# * qatorda matritsa elementlari. Chiqishda matritsa
# * elementlari  n ta qatorda probel bilan ajratilgan holatda chiqariladi.
# 
# * (Juda muhim eslatma, input kiritishlarda va print 
# * chiqarishlarda hech qanday so'z ishlatilmaydi, 
# * faqat kiruvchi qiymatlar yoki natijalar chiqishi kerak. 
# * Quyidagi misollarga qarang!)
# 
# * Kirishda
# * 3
# * 1
# * 2
# * 3
# * 4
# * 5
# * 6
# * 7
# * 8
# * 9  
# * Chiqishda:
# *                                     7 4 1
# *                                     8 5 2
# *                                     9 6 3

# In[3]:


#1-usul
from random import randint  # by Farrux

n = int(input())

matrix = [[int(input()) for i in range(n)] for _ in range(n)] 

matrix = [[matrix[i][j] for i in range(n-1,-1,-1)] for j in range(n)]

for k in matrix:
    print(*k)


# In[4]:


#2-usul
n = int(input())
matrix = [[int(input()) for i in range(n)] for i in range(n)]

for j in range(n-1,-1,-1):
    for i in range(j):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    matrix[j].reverse()
    
for i in matrix:
    print(*i)

