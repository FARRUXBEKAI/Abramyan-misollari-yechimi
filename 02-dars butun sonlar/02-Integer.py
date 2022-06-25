#!/usr/bin/env python
# coding: utf-8

# # 11/02/2022
# 
# # Python asoslari
# 
# # 2-dars: Butun sonlar. Qoldiqli va butun bo'lish
# 
# # Muallif: Farrux Sotivoldiyev

# In[1]:


#integer1
L = int(input("L = "))

print(L,"sm =>",L//100,"m",L%100,"sm")


# In[4]:


#integer2
M = int(input("M = "))

print(M,"kg =>",M//1000,"t",M%1000,"kg")


# In[5]:


#integer3
B = int(input("Bayt = "))

print(B,"bayt =>",B//1024,"Kb",B%1024,"bayt")


# In[6]:


#integer4
A = int(input("A = "))
B = int(input("B = "))

print(A//B,"marta joylashtirish mumkin")


# In[9]:


#integer5
A = int(input("A = "))
B = int(input("B = "))

print(A//B,"marta joylashtirish mumkin","\nJoylashmagan qismi:",A%B)


# In[11]:


#integer6
A = int(input("A = "))

print(A//10,"\t",A%10)


# In[12]:


#integer7
A = int(input("A = "))

print(A//10 + A%10)


# In[14]:


#integer8
A = int(input("A = "))

print(A//10 + (A%10)*10)


# In[16]:


#integer9
A = int(input("A = "))

print(A//100)


# In[20]:


#integer10
A = int(input("A = "))

print(A%100%10,"\t",A%100//10)


# In[24]:


#integer11
A = int(input("A = "))

print(A%10 + A%100//10 + A//100)


# In[28]:


#integer12
A = int(input("A = "))

print((A%10)*100 + (A%100//10)*10 + A//100)


# In[30]:


#integer13
A = int(input("A = "))

print((A%10)*10 + (A%100//10)*100 + (A//100))


# In[31]:


#integer14
A = int(input("A = "))

print((A%10)*100 + (A%100//10) + (A//100)*10)


# In[32]:


#integer15
A = int(input("A = "))

print((A%10) + (A%100//10)*100 + (A//100)*10)


# In[33]:


#integer16
A = int(input("A = "))

print((A%10)*10 + (A%100//10) + (A//100)*100)


# In[35]:


#integer17
A = int(input("A = "))

print(A%1000//100)


# In[36]:


#integer18
A = int(input("A = "))

print(A%10000//1000)


# In[42]:


#integer19
N = int(input("N = "))

print(N//60,"min o'tdi")


# In[46]:


#integer20
N = int(input("N = "))

print(N//3600,"soat o'tdi")


# In[43]:


#integer21
N = int(input("N = "))

print(N,"sekund =>",N//60,"min",N%60,"sek")


# In[44]:


#integer22
N = int(input("N = "))

print(N//3600,"soat",N%60,"sek o'tdi")


# In[45]:


#integer23
N = int(input("N = "))

print(N,"sekund =>",N//3600,"soat",N%3600//60,"min",N%60,"sek")


# In[50]:


#integer24
print("""
0-yakshanba
1-dushanba
2-seshanba
3-chorshanba
4-payshanba
5-juma
6-shanba
""")

kun = int(input("kun = "))

print(kun%7,"- hafta kuni")


# In[51]:


#integer25
print("""
0-yakshanba
1-dushanba
2-seshanba
3-chorshanba
4-payshanba
5-juma
6-shanba
""")

kun = int(input("kun = "))

print((kun+3)%7,"- hafta kuni")


# In[3]:


#integer26
print("""
1-dushanba
2-seshanba
3-chorshanba
4-payshanba
5-juma
6-shanba
7-yakshanba
""")

kun = int(input("kun = "))

print((kun)%7+1,"- hafta kuni")


# In[13]:


#integer27
print("""
1-dushanba
2-seshanba
3-chorshanba
4-payshanba
5-juma
6-shanba
7-yakshanba
""")

kun = int(input("kun = "))

print((kun+5)%7+1,"- hafta kuni")


# In[15]:


#integer28                            
print("""
1-dushanba
2-seshanba                                    
3-chorshanba
4-payshanba
5-juma
6-shanba
7-yakshanba
""")

kun = int(input("kerakli kun = "))
N = int(input("N-hafta kuni = ")) #-> 1-kun shu hafta kunidan boshlanadi

print((kun%7+N-2)%7+1,"- kerakli hafta kuni")


# In[117]:


#integer29
A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))

joylashish = (A//C) * (B//C)
Qolgan_qismi = A*B - (C**2 * joylashish)

print(joylashish,"ta joylashadi Ya'ni",(C**2 * joylashish),"m^2","\nQolgan qismi:",Qolgan_qismi,"m^2")


# In[122]:


#integer30
yil = int(input("Yil = "))

asr = (yil//100)+1

print(yil,"yil =>",asr,"asr")


# # Qo'shimcha
# 

# In[18]:


# Hozirgi kungacha bolgan sekundlar kiritilsa yil,oy,kun,soat
# minut,sekund larga bo'lish

n = int(input("Sekundlarni kiriting: "))

yil = n//(360*24*3600)
oy = n%(360*24*3600)//(30*24*3600)
kun = n%(30*24*3600)//(24*3600)
soat = n%(24*3600)//3600
minut = n%(24*3600)%3600//60
sekund = n%(24*3600)%60

print( yil,'-yil\n',oy,'-oy\n',kun,'-kun\n',soat,'-soat\n',minut,'-minut\n',sekund,'-sekund')


# In[20]:


# kun kiritiladi(k) va u qaysi hafta kuniga to'g'ri kelishi ham 
# kiritiladi(h) keyin kerakli kun(m) kiritilsa u qaysi hafta kuniga(kun)
# to'g'ri kelishini topish kerak.

print("""
1-dushanba
2-seshanba                                    
3-chorshanba
4-payshanba
5-juma
6-shanba
7-yakshanba
""")
k = int(input("kun = "))
h = int(input("hafta kuni = "))
m = int(input("kerakli kun = "))
kun = (m+(h-1-k%7))%7+1
print("haftaning",kun,"- kuniga to'g'ri keladi")

