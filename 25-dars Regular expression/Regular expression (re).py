#!/usr/bin/env python
# coding: utf-8

# # 12/09/2022
# 
# # Python asoslari
# 
# # 25-dars : Regular expression
# 
# # Muallif: Farrux Sotivoldiyev

# ## Misollar

# ### re.match() - boshidan boshlab tekshiradi.

# In[45]:


#1
import re 
print("Shablon: Farrux Sotivoldiyev")
satr = input("Ism va Familyani kiriting: ")

if re.match(r"[A-Z]{1}[a-z']+ [A-Z]{1}[a-z']+",satr):
    print("To'g'ri kiritildi ",re.match(r"[A-Z]{1}[a-z']+ [A-Z]{1}[a-z']+",satr))
else:
    print("Xato kiritildi ")


# In[44]:


#2
import re 
print("Shablon: +998(01)-001-01-01")
satr = input("Tel nomeringizni kiriting: ")

if re.match(r"\+998\([0-9]{2}\)-[0-9]{3}-[0-9]{2}-[0-9]{2}",satr):
    print("To'g'ri kiritildi ",re.match(r"\+998\([0-9]{2}\)-[0-9]{3}-[0-9]{2}-[0-9]{2}",satr))
else:
    print("Xato kiritildi ")


# In[43]:


#3
import re 
print("Shablon: H...o")
satr = input("Satr: ")

if re.match(r"H...o$",satr):
    print("To'g'ri kiritildi ",re.match(r"H...o$",satr))
else:
    print("Xato kiritildi ")


# ### re.search() - hohlagan joydan qidiradi satrda o'sha so'z bo'lsa kifoya. ^ va $ ni qo'shmasligimiz kerak.

# In[41]:


#4
import re 
print("Shablon: H...o")
satr = input("Satr: ")

if re.search(r"S...m",satr):
    print("To'g'ri kiritildi ",re.search(r"S...m",satr))
else:
    print("Xato kiritildi ")


# **` * `** - vazifasi: o'sha belgi 0 ta yoki cheksiz

# In[74]:


satr = input("Satr: ")
if re.search(r"Sal*om*",satr):
    print("To'g'ri kiritildi ",re.search(r"Sal*om*",satr))
else:
    print("Xato kiritildi ")


# **` + `** - vazifasi: o'sha belgi 1 ta yoki cheksiz

# In[73]:


satr = input("Satr: ")
if re.search(r"Sal+om+",satr):
    print("To'g'ri kiritildi ",re.search(r"Sal*om*",satr))
else:
    print("Xato kiritildi ")


# **` ? `** - vazifasi: boshidagi + bor bo'lsa ham yo'q bo'lsa ham ishlayveradi +2134-214

# In[86]:


satr = input("Satr: ")
if re.search(r"\+?[0-9]+[\+-][0-9]+",satr):
    print("To'g'ri kiritildi ",re.search(r"\+?[0-9]+[\+-][0-9]+",satr))
else:
    print("Xato kiritildi ")


# **` {} `** - vazifasi: Aniq belgilar soni

# In[87]:


satr = input("Satr: ")
if re.search(r"Sal{1,2}om{1,2}",satr):
    print("To'g'ri kiritildi ",re.search(r"Sal{1,2}om{1,2}",satr))
else:
    print("Xato kiritildi ")


# **` () `** - vazifasi: Gruppalash |-bu belgi or ligini () qavs ichida bildiradi 

# In[92]:


satr = input("Satr: ")
if re.search(r"Sa{1,2}(lo|la)m{1,2}",satr):
    print("To'g'ri kiritildi ",re.search(r"Sa{1,2}(lo|la|laa)m{1,2}",satr))
else:
    print("Xato kiritildi ")


# ### re.findall() , ?: bu buyruq tashqi regex ga bu gruppa emas degan buyruq beradi

# In[94]:


satr = input("Satr: ")
print(re.findall(r"Sa{1,2}(?:lo|la|laa)m{1,2}",satr))


# In[42]:


# filedan 999 55fef1e5f1 dfdfdf birikmalarni alohida alohida qilish kerak
from re import findall
with open(input("Filename: ")) as f:
    data = f.read()
    regex1 = findall(r"[0-9a-zA-z]+",data)
    regex2 = findall(r"\d+",data)
    regex3 = findall(r"[a-zA-z]+",data)
print("sonlar va harflar: ",regex1)
print("sonlar: ",regex2)
print("harflar: ",regex3)


# ###  re.split() - satr yoki faylni biz yozgan so'z yoki belgi bo'yicha split qilib beradi.

# In[43]:


satr = input("Satr: ")
print(re.split(r"salom",satr))


# ### re.compile 

# In[44]:


satr = input("Satr: ")
tekshir = re.compile(r"salom")
print(tekshir.split(satr))


# ### span() - tekshirilayotgan narsa qaysi index oralig'ida ekanligi

# In[46]:


satr = input("Satr: ")
print(re.search(r"salom",satr).span())


# ### RegEx belgilari

# **` \A `**

# In[3]:


import re
satr = input("satr kiriting: ")
print(re.search(r"\AAssalom",satr))


# **` \Z `**

# In[9]:


import re
satr = input("satr kiriting: ")
print(re.search(r"salom\Z",satr))


# **` \b `**

# In[19]:


import re
satr = input("satr kiriting: ")
print(re.search(r"\bsalom\b",satr))


# **` \B `**

# In[25]:


import re
satr = input("satr kiriting: ")
print(re.search(r"\Bsalom\B",satr))


# **` \d `**

# In[26]:


import re
satr = input("satr kiriting: ")
print(re.search(r"\d+",satr))


# **` \D `**

# In[27]:


import re
satr = input("satr kiriting: ")
print(re.search(r"\D+",satr))


# **` \s `**

# In[34]:


import re
satr = input("satr kiriting: ")
print(re.search(r"\s+",satr))


# **` \S `**

# In[36]:


import re
satr = input("satr kiriting: ")
print(re.search(r"\S+",satr))


# **` \w `**

# In[38]:


import re
satr = input("satr kiriting: ")
print(re.search(r"\w+",satr))


# **` \W `**

# In[40]:


import re
satr = input("satr kiriting: ")
print(re.search(r"\W+",satr))


# In[ ]:





# ## Qo'shimcha.

# In[163]:


#satrdagi sonlarni topish
import re  

txt = "That 85 will 130 be 59 sollars"

#Find all digit characters:

x = re.findall("\d+", txt)
print(x)


# In[11]:


# (UNIVERSAL) Sananing to'g'ri yoki xatoligini RegEx orqali tekshirish
from re import match
sana = input("shablon(dd.mm.yyyy): ")
# 1900 <= year <= 2100
#                                    31 kun                                    \                 30 kun                                    \                29 kun                                          \                   28 kun   
if match(r"((([012][1-9]|10|20|30|31)\.(0[13578]|10|12)\.((?:19|20)[0-9]|2100))|(([012][1-9]|10|20|30)\.(0[469]|11)\.((?:19|20)[0-9]|2100))|(([012][1-9]|10|20)\.02\.(?:19|20)(?:[13579][26]|[02468][048])$)|(([0-2][1-8]|10|20|09|19)\.02\.((?:19|20)[0-9]|2100)))",sana):
    print("Sana to'g'ri kiritildi!")
else:
    print("Bunday sana yo'q!")


# In[109]:


# ID ni to'g'ri yoki xatoligini tekshirish
from re import match

satr = input("shablon(AA0000000): ")

if match(r"A[A-Z][0-9]{7}$",satr):
    print("to'g'ri!")
else:
    print("Xato!")


# In[13]:


# Filedan so'zlarni o'qib alohida kelgan yani bo'shliq bilan ajratilgan so'z yoki belgilarni bitta listga jamlash
from re import findall
with open("Filename/file_10.txt") as f:
    txt = f.read()
    file = findall(r"[a-zA-Z0-9]+",txt)
print(file)

