#!/usr/bin/env python
# coding: utf-8

# # 11/02/2022
# 
# # Python asoslari
# 
# # 1-dars: Butun sonlar. Qoldiqli va butun bo'lish
# 
# # Muallif: Farrux Sotivoldiyev

# In[2]:


#1
l = 1045 #sm
print(f"{l//100}m {l%100}sm")


# In[4]:


#2
m = 4505
print(f"{m//1000} tonna {m%1000}kg")


# In[7]:


#3
bayt = 2058
print(f"{bayt//1024}kb {bayt%1024} bayt")


# In[9]:


#4
a = 25
b = 4
print(f"{a//b} ta joylashtirish mumkin")


# In[10]:


#5
a = 45
b = 7
print(f"{a//b}-> ta joylashtirish mumkin {a%b}-> joylashmagani")


# In[11]:


#6
a = 45
on = a//10
bir = a%10
print("onlik->",on,"birlik->",bir)


# In[12]:


#7
son = 67
on = son // 10
bir = son % 10
print(f"raqamlari yegindisi: {on+bir}")


# In[14]:


#8
son = 98
on = son // 10
bir = son % 10
print(bir*10 + on*1)


# In[15]:


#9
son = 329
print(f"yuzlar->{son//100}")


# In[16]:


#10
son = 456
print(f"birlik->{son%10} onlik->{son%100//10}")


# In[18]:


#11
son = 967
yuz =  son//100
on = son%100//10
bir = son%10
print(f"raqamlari yegindisi: {yuz+on+bir}")


# In[40]:


#12
son = 967
yuz = son//100
on = son %100//10
bir = son %10
print(f"{bir*100 + on*10 + yuz*1}")


# In[21]:


#13
son = 735
yuz = son//100
on = son%100//10
bir = son%10
print(f"{yuz*1 + on*100 +bir*10}")


# In[22]:


#14
son = 967
yuz = son//100
on = son %100//10
bir = son %10
print(f"{yuz*10 + on*1 + bir*100}")


# In[23]:


#15
son = 349
yuz = son //100
on = son%100//10
bir = son%10
print(f"{yuz*10 + on*100 + bir*1}")


# In[24]:


#16
son = 452
yuz = son //100
on = son%100//10
bir = son%10
print(f"{yuz*100 + on*1 + bir*10}")


# In[25]:


#17
son =2345
yuz = son%1000//100
print(f"yuz->{yuz}")


# In[26]:


#18
son = 4782
minglik = son//1000
print(f"minglik->{minglik}")


# In[27]:


#19
sekund = 4336
minut = sekund//60
print(f"minut->{minut}")


# In[28]:


#20
sekund =9134
soat = sekund//3600
print(f"soat->{soat}")


# In[29]:


#21
sekund = 14245
minut =  sekund//60
sekund = sekund%60
print(f"minut->{minut} sekund->{sekund}")


# In[30]:


#22
n = 32435
soat = n//3600
sekund = n%60
print(f"soat->{soat} sekund->{sekund}")


# In[31]:


#23
n = 29364
soat = n//3600
minut = n%3600//60
sekund = n%60
print(f"{soat} soat {minut} minut {sekund} sekund")


# In[4]:


#24
k = int(input("kun = "))
kun = k%7
print(f"0-yakshanba\n1-dushanba\n2-seshanba\n3-chorshanba\n4-payshanba\n5-juma\n6-shanba\nsiz kiritgan kun: {kun}")


# In[2]:


#25
k = int(input("kun = "))
kun = (k+3)%7
print(f"0-yakshanba\n1-dushanba\n2-seshanba\n3-chorshanba\n4-payshanba\n5-juma\n6-shanba\nsiz kiritgan kun: {kun}")


# In[5]:


#26
k = int(input("kun = "))
kun = (k+1)%7
print(f"1-dushanba\n2-seshanba\n3-chorshanba\n4-payshanba\n5-juma\n6-shanba\n7-yakshanba\nsiz kiritgan kun: {kun}")


# In[35]:


#27
k = int(input("kun = "))
kun = (k+5)%7+1
print(f"1-dushanba\n2-seshanba\n3-chorshanba\n4-payshanba\n5-juma\n6-shanba\n7-yakshanba\nsiz kiritgan kun: {kun}")


# In[37]:


#28
k = int(input("kun = "))
h = int(input("hafta kuni = "))
m = int(input("kerakli kun = "))
kun = (m+(h-1-k%7))%7+1
print(f"1-dushanba\n2-seshanba\n3-chorshanba\n4-payshanba\n5-juma\n6-shanba\n7-yakshanba\nsiz kiritgan kun: {kun}")


# In[18]:


#29
a = 6
b = 8
c = 3
butun = (a//c) * (b//c)
qoldiq = a*b - butun*c*c
print(f"Joylashtirish mumkin: {butun}\nOrtiqchasi: {qoldiq}")


# In[13]:


#30
yil = int(input("Yilni kiriting: "))
asr = (yil//100) + 1

print(f"{asr} asr {yil}-yil")

#1800-1899 ->19 asr
#1900-1999 ->20 asr
#2000-2099 ->21 asr
#2100-2199 ->22 asr

# boshi_oxiri = yil%100//10
# if 0<=boshi_oxiri<5:
#     print(f"{asr} asrning boshi {yil}-yil")
# else:
#     print(f"{asr} asrning oxiri {yil}-yil")
    
    


# # Qo'shimcha
# 

# In[39]:


# Hozirgi kungacha bolgan sekundlar kiritilsa yil,oy,kun,soat,minut,sekund larga bo'lish
n = int(input("Sekundlarni kiriting: "))

yil = n//(360*24*3600)
oy = n%(360*24*3600)//(30*24*3600)
kun = n%(30*24*3600)//(24*3600)
soat = n%(24*3600)//3600
minut = n%(24*3600)%3600//60
sekund = n%(24*3600)%60

print( yil,'-yil\n',oy,'-oy\n',kun,'-kun\n',soat,'-soat\n',minut,'-minut\n',sekund,'-sekund')


# In[ ]:




