#!/usr/bin/env python
# coding: utf-8

# # 22/05/2022
# 
# # Python asoslari
# 
# # 20-dars : Satrlarga oid masalalar
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

# ### 1.Standart funksiyalar orqali satrlarni qayta ishlash.Qidiruv va almashtirish.

# In[67]:


# String26
n  = int(input("n = "))
satr = input("Satr kiriting: ")

x = len(satr)
if x > n:
    satr = satr[x-n:]
elif x < n:
    satr = "." * (n-x) + satr[:]
print(satr)


# In[73]:


# String27
n1  = int(input("n1 = "))
n2  = int(input("n2 = "))
s1 = input("Satr1 ni kiriting: ")
s2 = input("Satr2 ni kiriting: ")

s = s1[:n1] + s2[len(s2)-n2:]
print(s)


# In[25]:


# String28
c = input("Belgi kiriting: ")
s = input("Satr ni kiriting: ")

s = s.replace(c,2*c)
print(s)


# In[27]:


# String29
c = input("Belgi kiriting: ")
s1 = input("Satr1 ni kiriting: ")
s2 = input("Satr2 ni kiriting: ")

s = ''
for i in s1:
    if c==i:
        s += s2
    s += i
print(s)


# In[28]:


# String30
c = input("Belgi kiriting: ")
s1 = input("Satr1 ni kiriting: ")
s2 = input("Satr2 ni kiriting: ")

s = ''
for i in s1:
    s += i
    if c==i:
        s += s2
print(s)


# In[2]:


# String30
c = input("Belgi kiriting: ")
s1 = input("Satr1 ni kiriting: ")
s2 = input("Satr2 ni kiriting: ")

s = s1.replace(c,c+s2)
print(s)


# In[46]:


# String31
s1 = input("Satr1 ni kiriting: ")
s2 = input("Satr2 ni kiriting: ")

print(True if s1.find(s2)>=0 else False)


# In[47]:


# String32
s1 = input("Satr1 ni kiriting: ")
s2 = input("Satr2 ni kiriting: ")

print(s1.count(s2))


# In[56]:


# String33
s1 = input("Satr1 ni kiriting: ")
s2 = input("Satr2 ni kiriting: ")

if 0 <= s1.find(s2):
    print(s1[:s1.find(s2)]+s1[s1.find(s2)+1:])
else:
    print(s1)


# In[61]:


# String34
s1 = input("Satr1 ni kiriting: ")
s2 = input("Satr2 ni kiriting: ")

for i in range(len(s1)-1,-1,-1):
    if s2==s1[i]:
        print(s1[:i]+s1[i+1:])
        break
else:print(s1)


# In[64]:


# String35
s1 = input("Satr1 ni kiriting: ")
s2 = input("Satr2 ni kiriting: ")

s = ''
for i in s1:
    if s2==i:
        continue
    s += i
print(s)


# In[5]:


# String36
s1 = input("Satr1 ni kiriting: ")
s2 = input("Satr2 ni kiriting: ")
s3 = input("Satr3 ni kiriting: ")

print(s1.replace(s2,s3,1))


# In[2]:


# String37
s1 = input("Satr1 ni kiriting: ")
s2 = input("Satr2 ni kiriting: ")  
s3 = input("Satr3 ni kiriting: ")
print(s1[::-1].replace(s2[::-1],s3[::-1],1)[::-1])


# In[93]:


# String39
s = input("Satr kiriting: ")

probel = s.count(" ")
if probel>1:
    index1 = s.index(" ")
    for i in range(len(s)):
        if index1!=i and s[i]==" ":
            index2 = i
            break
    for i in range(index1+1,index2):
        print(s[i],end=" ")
        
else: print("") 


# In[94]:


# String40
s = input("Satr kiriting: ")

probel = s.count(" ")
if probel>1:
    index1 = s.index(" ")
    for i in range(len(s)):
        if index1!=i and s[i]==" ":
            index2 = i
    for i in range(index1+1,index2):
        print(s[i],end=" ")
        
else: print("") 


# ### 2.Satrdagi so'zlarni o'zgartirish  va taxlil qilish.

# In[5]:


# String41
s = input("Satr kiriting: ")
print(len(s.split()))


# In[11]:


# String42
s = input("Satr kiriting: ").upper()

a = s.split()
k = 0
for i in a:
    if i[0]==i[-1]:
        k += 1
print(k)


# In[13]:


# String43
s = input("Satr kiriting: ").upper()

a = s.split()
k = 0
for i in a:
    for j in range(len(i)):
        if i[j]=="A":
            k += 1
            break
print(k)


# In[17]:


# String44
s = input("Satr kiriting: ").upper()

a = s.split()
s = 0
for i in a:
    k = 0
    for j in range(len(i)):
        if i[j]=="A":
            k += 1
    if k==3:
        s += 1
print(s)


# In[21]:


# String45
s = input("Satr kiriting: ").lower()

a = s.split()
maxi = len(a[0])
for i in a:
    if len(i)<maxi:
        maxi = len(i)
print(maxi)


# In[22]:


# String46
s = input("Satr kiriting: ").lower()

a = s.split()
maxi = len(a[0])
for i in a:
    if len(i)>maxi:
        maxi = len(i)
print(maxi)


# In[23]:


# String47
s = input("Satr kiriting: ").lower()
print(s.replace(" ","."))


# In[47]:


# String48
s = input("Satr kiriting: ").lower()

a = s.split()
k = ''
for i in a:
    s = i[0]
    for j in range(1,len(i)):
        if i[0]==i[j]:
            s += "."
        else:
            s += i[j]
    k += s + " "
print(k)


# In[7]:


# String49
s = input("Satr kiriting: ").lower()

a = s.split()
k = ''
for i in a:
    s = ""
    for j in range(len(i)):
        if i[-1]==i[j] and j!=len(i)-1:
            s += "."
        else:
            s += i[j]
    k += s + " "
print(k)


# In[8]:


# String50
s = input("Satr kiriting: ").lower()

a = s.split()[::-1]
s = ' '.join(a)
print(s)


# In[11]:


# String51
s = input("Satr kiriting: ").upper()

print(" ".join(sorted(s.split())))


# In[5]:


# String52
s = input("Satr kiriting: ").lower()

a = s.split()
s = ''
for i in a:
    s += i.capitalize() + " "
print(s)


# In[1]:


# String53
s = input("Satr kiriting: ")

#  34:"  33:!  39:'  40:(  41:)  46:.  63:?  45:-  44:,  59:;
tinish_belgilari = [33,34,39,40,41,44,45,46,59,63,]
k = 0
for i in range(len(s)):
    x = ord(s[i])
    if x in tinish_belgilari:
        k += 1
print(k)


# In[56]:


# String54
s = input("Satr kiriting: ")

k = 0
for i in range(len(s)):
    if "A" <= s[i] <= "Z":
        k += 1
print(k)


# In[62]:


# String55
s = input("Satr kiriting: ")

a = s.split()
x = len(a[0])
soz = a[0]
for i in a:
    if x < len(i):
        x = len(i)
        soz = i
print(soz)


# In[64]:


# String56
s = input("Satr kiriting: ")

a = s.split()
x = len(a[-1])
soz = a[-1]
for i in a:
    if x > len(i):
        x = len(i)
        soz = i
print(soz)


# In[65]:


# String57
s = input("Satr kiriting: ")

a = s.split()
s = ''
for i in a:
    s += i + " "
print(s)


# ### 3.Satrlarni qayta ishlashga oid qo'shimcha masalalar.

# In[80]:


# String58
s = input("Satr kiriting: ")

a = s.split('\\')
print(a[-1][:a[-1].index(".")])


# In[83]:


# String59
s = input("Satr kiriting: ")

a = s.split('\\')
print(a[-1][a[-1].index(".")+1:])


# In[14]:


# String60
s = input("Satr kiriting: ")

a = s.split('\\')
if a[1].count(".")!=1 and 1 in list(range(len(a))):     
    print(a[1])
else:
    print("\\")


# In[17]:


# String61
s = input("Satr kiriting: ")

a = s.split('\\')
if a[1].count(".")!=1 and 2 in list(range(len(a))):     
    print(a[2])
else:
    print("\\")


# In[15]:


# String62
satr = input("Satr kiriting: ")
s = ''
for i in satr:
    if "A" <= i < "Z":
        s += chr(ord(i)+1)
    elif i == "Z":
        s += "A"
        
    elif "a" <= i < "z":
        s += chr(ord(i)+1)
    elif i == "z":
        s += "a"
        
    else:
        s += i
print(s)


# In[19]:


# String63 1-usul
satr = input("Satr kiriting: ")

k = int(input("k = "))
s = ''

for i in satr:
    if "A" <= i <= "Z":
        x = ord(i) + k
        if x > 90:
            x -= 26
        s += chr(x)
        
    elif "a" <= i <= "z":
        x = ord(i) + k
        if x > 122:
            x -= 26 
        s += chr(x)
        
    else:
        s += i
print(s)  

# String63 2-usul
satr = input("Satr kiriting: ")

k = int(input("k = "))
s = ''
for i in satr:
    if i.islower():
        s += chr((ord(i)+k-97)%26+97)
    elif i.isupper():
        s += chr((ord(i)+k-65)%26+65)
    else:
        s += i
print(s)


# In[36]:


# String64
satr = input("Satr kiriting: ")

k = int(input("k = "))
s = ''

for i in satr:
    if "A" <= i <= "Z":
        x = ord(i) - k
        if x < 65:
            x += 26          
        s += chr(x)
        
    elif "a" <= i <= "z":
        x = ord(i) - k
        if x < 97:
            x += 26    
        s += chr(x)
        
    else:
        s += i
print(s)  


# In[42]:


# String65
satr = input("Satr kiriting: ")

belgi = input("Birinchi belgini kiriting: ")
s = ''
flag = True

for i in satr:
    if "A" <= i <= "Z":
        if flag:
            k = ord(i)-ord(belgi)
            flag = False
        x = ord(i) - k
        if x < 65:
            x += 26          
        s += chr(x)
        
    elif "a" <= i <= "z":
        if flag:
            k = ord(i)-ord(belgi)
            flag = False
        x = ord(i) - k
        if x < 97:
            x += 26    
        s += chr(x)
        
    else:
        s += i
print(s)  


# In[54]:


# String66
satr = input("Satr kiriting: ")
k = []
for i in satr:
    k.append(i)
if len(satr)%2==0:
    s = k[::2]+k[::-2]
else:
    s = k[::2] + k[len(k)-2::-2]
s = "".join(s)
print(s)


# In[55]:


# String67
satr = input("Satr kiriting: ")
boshi = 0
oxiri = len(satr)-1
s = ''
while boshi <= oxiri:
    
    if boshi == oxiri:
        s += satr[boshi]
    else:
        s += satr[boshi] + satr[oxiri]
        
    boshi += 1
    oxiri -= 1
    
print(s)


# In[12]:


# String68
satr = input("Satr kiriting: ")
harflar = []
for i in satr:
    if "a"<=i<="z":
        harflar.append(i)

for i in range(len(harflar)-1):
    if harflar[i]<harflar[i+1]:
        continue
    print(harflar[i+1])
    break
else:
    print(0)


# In[2]:


# String69
satr = input("Satr kiriting: ")
qavslar = []
for i in satr:
    if i == "(" or i == ")":
        qavslar.append(i)
if len(qavslar)%2!=0:
    print(-1)
else:
    for i in range(0,len(qavslar),2):
        if qavslar[i]<qavslar[i+1]:
            continue
            
        elif qavslar[i]==qavslar[i+1]:
            if qavslar[i]==")": print(f"{i+1}-qavs xato qo'yilgan")
            else: print(f"{i+2}-qavs xato qo'yilgan")
            break
            
        print(f"{i+1}-qavs xato qo'yilgan")
        break
        
    else:
        print(0)

