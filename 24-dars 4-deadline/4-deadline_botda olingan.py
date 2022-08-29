#!/usr/bin/env python
# coding: utf-8

# # 10/08/2022
# 
# # Sotivoldiyev Farruxbek
# 
# # 4 - nazorat ishi Botda olingan

# Imtihon - 4
# 
# Imtihon 2 soat davom etadi:
# 10:10-12:10
# 
# 1️⃣
# * Regex: Kiritilgan sanani tekshiruvchi regex tuzing, 
# * kabisa va kabisa emasligi inobotga olinsin.
# * Kiruvchi format kun-oy-yil ko'rinishida bo'ladi.
# 
# * Kirishda satr kiritiladi, chiqishda agar shunday sana
# * mavjud bo'lsa, 1 aks holda 0 chiqariladi.
# 
# * (Juda muhim eslatma, input kiritishlarda va print 
# * chiqarishlarda hech qanday so'z ishlatilmaydi, 
# * faqat kiruvchi qiymatlar yoki natijalar chiqishi kerak. 
# * Quyidagi misollarga qarang!)
# 
# * Masalan,
# * Kirishda                                      
# * 12-12-2012            
# * 32-12-2021             
# * Chiqishda
# * 1
# * 0
# 
# 2️⃣
# * Regex: O'zbekiston telefon raqamlarini tekshiruvchi regex tuzing.
# * Kiruvchi format +(998)97 007-07-07 ko'rinishida bo'ladi(chiziqchalar bilan).
# 
# * Kirishda satr kiritiladi, chiqishda agar shunday nomer
# * mavjud bo'lsa, 1 aks holda 0 chiqariladi.
# 
# * (Juda muhim eslatma, input kiritishlarda va print 
# * chiqarishlarda hech qanday so'z ishlatilmaydi, 
# * faqat kiruvchi qiymatlar yoki natijalar chiqishi kerak. 
# * Quyidagi misollarga qarang!)
# 
# * Masalan,
# * Kirishda                                      
# * +(998)91 460-95-50         
# * +(998)91460-95-50         
# * +(998)90 007 07 07         
# * Chiqishda
# * 1
# * 0
# * 0
# 
# 3️⃣ 
# 
# * Person nomli class yarating. U atribut sifatida name va age
# * satr sifatidagi so'zlarni olsin. class ga myfunc nomli funksiya
# * tuzing. U "Hello my name is {self.name}" gapini qaytarsin.
# 
# * Kirishda 2 ta qatorda satr kiritiladi, name va age uchun.
# * Chiqishda yuqoridagi gap mos name uchun myfunc funksiyasi natijasi
# * print orqali chiqariladi. Diqqat, print class ichida ishlatilmaydi!
# 
# * (Juda muhim eslatma, input kiritishlarda va print 
# * chiqarishlarda hech qanday so'z ishlatilmaydi, 
# * faqat kiruvchi qiymatlar yoki natijalar chiqishi kerak. 
# * Quyidagi misollarga qarang!)
# 
# * Masalan,
# * Kirishda                                      
# * Shaxboz         
# * 21                  
# * Chiqishda
# * Hello my name is Shaxboz
# 
# 4️⃣
# 
# * nxn o'lchamli matritsa berilgan, 
# * matritsani 90 gradusga o'ngga buruvchi dastur yarating.
# 
# * Kirishda n matritsa o'lchami kiritiladi va keyingi nxn 
# * qatorda matritsa elementlari. Chiqishda matritsa
# * elementlari  n ta qatorda probel bilan ajratilgan holatda chiqariladi.
# 
# 
# * (Juda muhim eslatma, input kiritishlarda va print 
# * chiqarishlarda hech qanday so'z ishlatilmaydi, 
# * faqat kiruvchi qiymatlar yoki natijalar chiqishi kerak. 
# * Quyidagi misollarga qarang!)
# 
# * Masalan,
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
# * Chiqishda
# * 7 4 1
# * 8 5 2
# * 9 6 3
# 
# 5️⃣
# * Triangle nomli class yarating. U o'ziga 3 ta atribut olsin.
# * Bu atributlar tekislikdagi nuqta ko'rinishida bo'lsin.
# * Ular yordamida uchlari class atributlari bo'lgan uchburchak yuzasi topilsin.
# * Agar uchlari bu nuqtalarda bo'lgan uchburchak mavjud bo'lmasa, 0 chiqariladi.
# 
# * Kirishda 6 ta haqiqiy son, mos ravishda 1-nuqta, 2-nuqta va 3-nuqta koordinatalari.
# * Chiqishda uchlari shu nuqtalarda bo'lgan uchburchak yuzasini 2 birlikkacha yaxlitlab
# * chiqariladi. Agar bunday uchburchak mavjud bo'lmasa 0 chiqariladi.
# 
# 
# * (Juda muhim eslatma, input kiritishlarda va print 
# * chiqarishlarda hech qanday so'z ishlatilmaydi, 
# * faqat kiruvchi qiymatlar yoki natijalar chiqishi kerak. 
# * Quyidagi misollarga qarang!)
# 
# * Masalan,
# * Kirishda                                      
# * 1
# * 2
# * 5
# * 6
# * 4
# * 4                  
# * Chiqishda
# * 2.0

# In[2]:


# 1
from re import match
sana = input()
if match(r"(((0?[1-9]|[12][0-9]|30|31)-(0?[13578]|10|12)-((?:19|20)[0-9]|2100))|((0?[1-9]|[12][0-9]|30)-(0?[469]|11)-((?:19|20)[0-9]|2100))|((0?[1-9]|[12][0-9])-0?2-(?:19|20)(?:[13579][26]|[02468][048])$)|((0?[1-9]|[12][0-8]|19)-0?2-((?:19|20)[0-9]|2100)))",sana):
    print(1)
else:
    print(0)


# In[3]:


# 2
import re
raqam = input().strip()
if re.match(r"\+\(998\)(33|88|90|91|93|94|95|97|98|99) \d{3}-\d{2}-\d{2}$",raqam):
    print(1)
else:
    print(0)


# In[4]:


# 3
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def myfunk(self):
        return f"Hello my name is {self.name}"

ism = input()
yosh = input()
farrux = Person(ism,yosh)
print(farrux.myfunk())


# In[5]:


# 4
n = int(input())

matrix = [[int(input()) for i in range(n)] for _ in range(n)] 
matrix = [[matrix[i][j] for i in range(n-1,-1,-1)] for j in range(n)]

for k in matrix:
    print(*k)


# In[6]:


# 5
class Triangle:
    def __init__(self,x,y,z):
        self.x1 = x[0]
        self.y1 = x[1]
        self.x2 = y[0]
        self.y2 = y[1]
        self.x3 = z[0]
        self.y3 = z[1]

    def xisobla(self):
        a = ((self.x1-self.x2)**2 + (self.y1-self.y2)**2)**(0.5)
        b = ((self.x1-self.x3)**2 + (self.y1-self.y3)**2)**(0.5)
        c = ((self.x3-self.x2)**2 + (self.y3-self.y2)**2)**(0.5) 
        if (a+b)>c>abs(a-b):
            p = (a+b+c)/2
            s = (p*(p-a)*(p-b)*(p-c))**(0.5)
            return round(s,2)
        else:
            return 0
            
x = [float(input()) for _ in range(2)]
y = [float(input()) for _ in range(2)]
z = [float(input()) for _ in range(2)]

x = Triangle(x,y,z)
print(x.xisobla())

