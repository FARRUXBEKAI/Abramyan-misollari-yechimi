#!/usr/bin/env python
# coding: utf-8

# # 02/08/2022
# 
# # Sotivoldiyev Farruxbek
# 
# # 4 - nazorat ishi

# Imtihon - 4
# 
# Imtihon 2 soat davom etadi:
# 10:10-12:10
# 
# 1️⃣ +,- belgilar va sonlardan iborat satr berilgan, shu satrning matematik yechimini topuvchi dastur tuzing.
# Masalan:  15+8+4-85 = -58 Natijasi chiqsin, e'tibor bering bu ifoda satrda berilgan
# 
# 2️⃣ Matn berilgan, matnda polindrom so'zlar sonini chiqaruvchi dastur tuzing. Iltimos hajmi katta matn kiritib tekshirib ko'ring.
# 
# 3️⃣ Fayllar bilan ishlash. 
# 1. Fayl nomini kiriting.
# 2. Pathda shunday fayl bormi tekshiring, agar bor bo'lsa fayl nomini boshqatdan kiritish talab qilinsin, yo'q bo'lsa keyingi boshqichga o'ting
# 3. Faylga O'zbekiston haqida ma'lumot yozing va faylni yoping.
# 4. Faylni ochib ichidan eng katta so'zni o'chirib qaytadan faylni yoping.
# 
# 4️⃣ Pathda tayyor fayldan ma'lumot o'qing va ma'lumot ichidan boshi va oxiri "A" yoki "a" bilan ifodalangan so'zlarni topib o'chiring, keyin faylni yoping.
# 
# 5️⃣ Studentlar ma'lumotlari keltirilgan fayl hosil qiling. 
# 1. FIO
# 2. Student ID
# 3. Fakulteti
# 4. Bahosi
# 5. Viloyati
# 
# Shu ma'lumotlardan iborat fayl hosil qilinsin va quyidagi funksiyalardan iborat dastur tuzing,
# 
# 1. FIO ga qarab studentni topuvchi funksiya
# 2. Student ID ga qarab studentni topuvchi funksiya
# 3. Fakultetga qarab studentlarni chiqarib beruvchi funksiya
# 4. Bahosiga qarab studentlarni chiqarib beruvchi funksiya
# 5. Vilayatga qarab studentlarni chiqarib beruvchi funksiya.
# 
# E'tibor bering, Fayl yaratish ham kod bilan amalga ochirilsin.
# 

# In[73]:


# 1-masala
import re
satr = input("Satr kiriting:")
s = 0
sonlar = list(map(int, re.findall(r"[+-]?\d+",satr)))
for i in sonlar:
    s += i
print("Javob:",s)


# In[74]:


# 2-masala
words = input("matn kiriting: ")

word = words.split()
polindrom = 0

for i in range(len(word)):
    if word[i]==word[i][::-1]:
        polindrom += 1

print("Polindrom so'zlar soni:",polindrom)


# In[26]:


# 3-masala
import re
satr = input()

try:
    x = open("salom.txt","r+")
    
except:
    x = open("salom.txt","x+")
    
finally:
    x.write(satr)
    x.close()
    
    x = open("salom.txt")
    words = x.read()
    sozlar = ((words.replace("."," ")).replace(","," ")).split()
    maxi = sozlar[0]
    for i in sozlar:
        if len(maxi)<len(i):
            maxi = i
    index = words.index(maxi)
    new_words = words[:index] + words[index+len(maxi):] 
    x.close()
    
    x = open("salom.txt","w")
    x.write(new_words)
    x.close()
print(new_words)


# In[93]:


# 4-masala
import re
flag = True
with open("salom.txt") as f:
    words = f.read()
    words2 = []
    sozlar = ((words.replace("."," ")).replace(","," ")).split()
    for i in sozlar:
        if re.match(r"((?:A|a)[A-Za-z]+|[A-Za-z]+(?:A|a)$)",i):
                words2.append(i)
    for j in words2:
        if flag:
            index1 = words.index(j)
            new_words = words[:index1] + words[index1+len(j):] 
            flag = False
            continue
        index2 = new_words.index(j)
        new_words = new_words[:index2] + new_words[index2+len(j):] 
        
with open("salom.txt","w") as f:
    f.write(new_words)
    
print(new_words)


# In[107]:


# 5-masala
ism = input()
baxo = input()

with open("talabalar.txt") as f:
    talabalar_info = f.readlines()
    talabalar_soni = 0
    for i in range(1,len(talabalar_info)):
        talaba = talabalar_info[i].split("|")
        if talaba[1].strip()==ism and talaba[3].strip()==baxo:
            talabalar_soni += 1
print(talabalar_soni)

