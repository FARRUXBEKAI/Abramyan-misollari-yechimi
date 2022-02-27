# #!/usr/bin/env python
# # coding: utf-8

# # # 23/02/2022
# # # Sotivoldiyev Farruxbek
# # 
# # # 1- nazorat ishi

# # # Imtihon 2 soat davom etadi:
# # 20:30-22:30
# # 
# # Kodlar adminga shu vaqt oralig'ida jo'natiladi. Natijalarni Seshanba kuni e'lon qilamiz!
# # 
# # 1. 4ta son berilgan shu 4ta sonni 5-son qo'shmasdan va boshqa toifa ishlatmasdan, 4tasini qiymatini almashtiruvchi dastur tuzing!
# # 
# # 2. 4 xonali son berilgan, shu sonlarni teskari tartibda yozuvchi dastur tuzing. While, for, satr ishlatish mumkin emas
# # 
# # 3. 3ta son berilgan shu 3ta sonning o'rtancha qiymatga ega sonni toping:
# # Masalan: 6, 11, 100 kiritilsa javob 6 chiqishi kerak
# # 
# # 4. for 23 misolni ishlash kerak
# # 
# # 5. Nta son berilgan shu N ta sonning ichidan eng kichik musbat sonni topish kerak.
# # 

# # In[1]:


# #1-savol

# a = 1
# b = 2
# c = 3
# d = 4

# a = a + b + c + d
# d = a - b - c - d
# c = a - b - c - d
# b = a - b - c - d
# a = a - b - c - d

# print(a,b,c,d,end = " ")


# # In[2]:


# #2-savol

# a = 2483

# ming = a // 1000
# yuz = a % 1000 // 100
# on = a % 100 // 10
# bir = a % 10
# print(bir*1000 + on*100 + yuz*10 + ming*1)


# # In[8]:


# #3-savol

# a = 6
# b = 11
# c = 100

# if a > b and a < c:
#     print(a)
# elif b > a and b < c:
#     print(b)
# else:
#     print(c)


# # In[5]:


# #4-savol

# n = int(input("n = "))
# x = float(input("x = "))

# p = 1
# s = x
# for i in range(1,n+1):
#     p *= (2*i+1)*2*i
#     s += ((-1)**i * x**(2*i+1))/p
# print("summa:",s)


# # In[33]:


# #5-savol

n = int(input("n = "))

min = 'Siz 0 dan katta son kiritmadingiz'
flag = True
for i in range(1,n+1):
    a = int(input(f"son{i}>>>"))
    if a>0 and flag:
        min = a
        flag = False
    if a > 0 and min > a:
            min = a
print(min)

