#!/usr/bin/env python
# coding: utf-8

# # 13/05/2022
# 
# # Python asoslari
# 
# # 19-dars : Belgilar massivi bilan ishlash
# 
# # Muallif: Farrux Sotivoldiyev

# ### ASCII kodi
# 
# * Raqamlar (48 : 57)
# * Katta lotin harflari (65 : 90)
# * Kichik lotin harflari (97 : 122)
# * Katta krill harflari (1040 : 1071) -> "Ё" = 1025
# * Kichik krill harflari (1072 : 1103) -> "ё" = 1105
# 

# ### 1.Belgilar va ularning kodlari. Satrlarni hosil qilish.

# In[2]:


# String1
belgi = input("Belgi kiriting:")
print(ord(belgi))


# In[12]:


# String2
n = int(input("Raqam kiriting:"))
print(chr(n))


# In[39]:


# String3
belgi = input("Belgi kiriting:")
for i in range(126):
    if i==ord(belgi):
        continue
    print(chr(i),end=" ")


# In[43]:


# String4
n = int(input("Raqam kiriting:"))
for i in range(1,n+1):
    print(chr(i+64),end=" ")


# In[46]:


# String5
n = int(input("Raqam kiriting:"))
for i in range(122,122-n,-1):
    print(chr(i),end=" ")


# In[62]:


# String6
belgi = input("Belgi kiriting:")
if 48 <= ord(belgi) <= 57:
    print("digit")
    
elif 65 <= ord(belgi) <= 90 or 97 <= ord(belgi) <= 122:
    print("lotin")
    
else:
    print(0)


# In[63]:


# String7
satr = input("Satr kiriting:")
print(ord(satr[0]),ord(satr[-1]),sep=" ")


# In[67]:


# String8
n = int(input("Raqam kiriting:"))
belgi = input("Belgi kiriting:")
s = ""
for i in range(n):
    s += belgi
print(s)


# In[69]:


# String9
satr1 = input("satr1 ni kiriting:")
satr2 = input("satr2 ni kiriting:")
print(satr1+satr2)


# In[86]:


# String10
satr = input("satr kiriting:")
print(satr[::-1])


# In[95]:


# String11
satr = input("satr kiriting:")
s = ""
for i in range(len(satr)):
        s += satr[i] + " "
print(s)


# In[96]:


# String12
satr = input("Satr kiriting:")
n = int(input("Raqam kiriting:"))
s = ""
for i in range(len(satr)):
        s += satr[i] + n * "*"
print(s)


# ### 2.Belgili taxlil va satrlarni qayta ishlash.

# In[97]:


# String13
satr = input("Satr kiriting:")
k = 0
for i in range(len(satr)):
    if 48 <= ord(satr[i]) <= 57:
        k += 1
print(k)


# In[99]:


# String14
satr = input("Satr kiriting:")
k = 0
for i in range(len(satr)):
    if 65 <= ord(satr[i]) <= 90:
        k += 1
print(k)


# In[157]:


# String15
satr = input("Satr kiriting:")
k = 0
for i in range(len(satr)):
    if 97 <= ord(satr[i]) <= 122 or 1072 <= ord(satr[i]) <= 1103:
        k += 1
print(k)


# In[156]:


# String16
satr = input("Satr kiriting:")
s = ""
for i in range(len(satr)):
    if 65 <= ord(satr[i]) <= 90:
        s += chr(ord(satr[i])+32)
        continue
    s += satr[i]
print(s)


# In[155]:


# String17
satr = input("Satr kiriting:")
s = ""
for i in range(len(satr)):
    if 65 <= ord(satr[i]) <= 90 or 1040 <= ord(satr[i]) <= 1071:
        s += chr(ord(satr[i])+32)                               
    elif ord(satr[i])==1025:          # Ё -> ё
        s += chr(1105)
    else: s += satr[i]
print(s)


# In[158]:


# String18
satr = input("Satr kiriting:")
s = ""
for i in range(len(satr)):
    if 65 <= ord(satr[i]) <= 90 or 1040 <= ord(satr[i]) <= 1071:
        s += chr(ord(satr[i])+32)                                
    elif ord(satr[i])==1025:          # Ё -> ё
        s += chr(1105)
        
    elif 97 <= ord(satr[i]) <= 122 or 1072 <= ord(satr[i]) <= 1103:
        s += chr(ord(satr[i])-32)                                
    elif ord(satr[i])==1105:          # ё -> Ё
        s += chr(1025)
print(s)


# In[37]:


# String19
satr = input("Satr kiriting:")

flag = True
haqiqiy,butun = False,False
for i in satr:
    if flag and i == "-":
        continue
    flag = False
        
    if "0"<= i <="9" or i == ".":
        if satr.count(".")==0:
            butun = True
        elif satr.count(".")==1:
            haqiqiy = True
        
    else:
        haqiqiy,butun = False,False
        break
        
        
if butun:
    print("Butun son")
elif haqiqiy:
    print("Haqiqiy son")
else:
    print("Oddiy satr")


# In[38]:


# String20
satr = input("Satr kiriting:")
for i in satr:
    print(int(i),end=" ")


# In[39]:


# String21
satr = input("Satr kiriting:")
for i in range(len(satr)-1,-1,-1):
    print(int(satr[i]),end=" ")


# In[183]:


# String22
satr = input("Satr kiriting:")
s = 0
for i in range(len(satr)):
    s += int(satr[i])
print(s)


# In[30]:


# String23
satr = input("Satr kiriting:")
amal = []
for i in satr:
    if i=="+" or i=="-":
        amal.append(i)
        satr = satr.replace(i," ")
satr = satr.split()

s = int(satr[0])
for i in range(len(amal)):
    if amal[i]=="+":
        s += int(satr[i+1])
    elif amal[i]=="-":
        s -= int(satr[i+1])
print(s)


# In[46]:


# String24
satr = input("Satr kiriting:")
n = len(satr)
s = 0
for i in range(n-1,-1,-1):
    s += 2**(n-i-1) * int(satr[i])
    
satr = str(s)

print(satr)


# In[55]:


# String25
satr = input("Satr kiriting:")
x = int(satr)
s = ''
while x >= 2:
    s += str(x%2)
    x //= 2
    
s += str(x)
satr = s[::-1]

print(satr)

