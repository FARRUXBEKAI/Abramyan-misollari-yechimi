#!/usr/bin/env python
# coding: utf-8

# # 18/03/2022
# 
# # Python asoslari
# 
# # 12-dars: Min va Max lar bilan ishlash
# 
# # Muallif: Farrux Sotivoldiyev

# In[1]:


#1
n = int(input("N = "))

flag = True
for i in range(1,n+1):
    n = int(input(f"n{i} = "))
    if flag:
        maxi = n
        mini = n
        flag = False
    if n > maxi:
        maxi = n
    if n < mini:
        mini = n
print(f"maxi = {maxi} \nmini = {mini}")


# In[3]:


#2
n = int(input("N = "))

flag = True
for _ in range(n):
    a = int(input("a = "))
    b = int(input("b = "))
    if flag:
        mini = a*b
        flag = False
    if mini > a*b:
        min = a*b
print("Yuza:",mini)
    


# In[5]:


#3
N = int(input("N = "))

for _ in range(N):
    a = int(input("a = "))
    b = int(input("b = "))
    if flag:
        maxi = 2*(a+b)
        flag = False
    if maxi < 2*(a+b):
        maxi = 2*(a+b)
print("Perimetr:",maxi)


# In[9]:


#4
N = int(input("N = "))

k = 0
flag = True
for i in range(1,N+1):
    n = int(input(f"n{i} = "))
    if flag:
        mini = n
        flag = False
    if mini > n:
        mini = n
        k = i 
print("Min =",mini,"\nNomeri:",k)


# In[10]:


#5
N = int(input("N = "))

flag = True
for i in range(1,N+1):
    m = int(input(f"m{i} = "))
    v = int(input(f"v{i} = "))
    if flag:
        maxi = m/v
        flag = False
    if maxi < m/v:
        maxi = m/v
        massa = m
        hajm = v
print("massa:",massa,"\nhajm:",hajm,"\nMax =",maxi)


# In[2]:


#6
# masalan: 2 -6 1 -9 45 -1 45 -9
# birinchi uchragan eng kichigi: -9 indeksi: 4
# oxirigi uchragan eng kattasi: 45 indeksi: 7

n = int(input("n = "))

flag = True

for i in range(1,n+1):
    k = int(input(f"k{i} = "))
    if flag:
        maxi = k
        mini = k
        flag = False
    if k >= maxi:
        maxi = k
        sanoq1 = i
    elif k < mini:
        mini = k
        sanoq2 = i
        
print(sanoq2,sanoq1)


# In[8]:


#7
# 8 ta masalan: 2 -6 1 -9 45 -1 45 -9
# oxirigi uchragan eng kichigi: -9 indeksi: 8
# birinchi uchragan eng kattasi: 45 indeksi: 5

n = int(input("n = "))

flag = True

for i in range(1,n+1):
    k = int(input(f"k{i} = "))
    if flag:
        maxi = k
        mini = k
        flag = False
    if k > maxi:
        maxi = k
        sanoq_maxi = i
    if k <= mini:
        mini = k
        sanoq_mini = i
        
print(sanoq_maxi,sanoq_mini)


# In[9]:


#8
# 8 ta masalan: 2 -6 1 -9 45 -1 45 -9
# oxirigi uchragan eng kichigi: -9 indeksi: 8
# birinchi uchragan eng kichigi: -9 indeksi: 4

n = int(input("n = "))

flag = True

for i in range(1,n+1):
    k = int(input(f"k{i} = "))
    if flag:
        mini = k
        flag = False
        
    if k <= mini:
        sanoq_oxir = i
        
    if k < mini:
        mini = k
        sanoq_bir = i
print(sanoq_bir,sanoq_oxir)


# In[10]:


#9     
# 8 ta masalan: 2 -6 1 -9 45 -1 45 -9
# oxirigi uchragan eng kattasi: 45    indeksi: 7
# birinchi uchragan eng kattasi: 45   indeksi: 5

n = int(input("n = "))

flag = True

for i in range(1,n+1):
    k = int(input(f"k{i} = "))
    if flag:
        maxi = k
        flag = False
        
    if k >= maxi:
        sanoq_oxir = i
        
    if k > maxi:
        maxi = k
        sanoq_bir = i
        
print(sanoq_bir,sanoq_oxir)


# In[12]:


#10   
# 8 ta masalan: 2 -6 1 -9 45 -1 45 -9
# birinchi uchragan ekstremal: -9    indeksi: 4

n = int(input("n = "))

flag = True

for i in range(1,n+1):
    k = int(input(f"k{i} = "))
    if flag:
        maxi = k
        mini = k
        flag = False 
        
    if k > maxi:
        maxi = k
        sanoq1 = i
        
    if k < mini:
        mini = k
        sanoq2 = i
print("Ekstremallar:",maxi,mini)
if sanoq1 > sanoq2:
    print("Birinchi Ekstremal tartibi:",sanoq2)
else:
    print("Birinchi Ekstremal tartibi:",sanoq1)


# In[15]:


#11
# 8 ta masalan: 2 -6 1 -9 45 -1 45 -9
# oxirigi uchragan ekstremal: -9    indeksi: 8

n = int(input("n = "))

flag = True

for i in range(1,n+1):
    k = int(input(f"k{i} = "))
    if flag:
        maxi = k
        mini = k
        flag = False
        
    if k >= maxi:
        maxi = k
        sanoq1 = i
        
    if k <= mini:
        mini = k
        sanoq2 = i
print("Ekstremallar:",maxi,mini)
if sanoq1 < sanoq2:
    print("Oxirgi Ekstremal tartibi:",sanoq2)
else:
    print("Oxirgi Ekstremal tartibi:",sanoq1)


# In[17]:


#12
n = int(input("n = "))

musbat = 0
flag = True
for i in range(1,n+1):
    k = int(input(f"k{i} = ")) 
    if flag and k > 0:
        musbat = k
        flag = False
    if k > 0 and k < musbat:
        musbat = k
print(musbat)


# In[19]:


#13
n = int(input("n = "))

flag = True

for i in range(1,n+1):
    k = int(input(f"k{i} = "))
    if flag and k%2==1:
        toq = k
        sanoq = i                    
        flag = False
    if k%2==1 and toq < k:
        toq = k
        sanoq = i
print(sanoq)


# In[22]:


#14
b = int(input("B = "))

flag = True
sanoq = 0
for i in range(1,11):
    k = int(input(f"k{i} = "))
    if k > b and flag:
        katta = k
        sanoq = i
        flag = False
    if k > b and katta > k:
        katta = k
        sanoq = i
if sanoq:
    print(sanoq)
else:
    print("00")


# In[23]:


#15
b = int(input("B = "))
c = int(input("C = "))

flag = True
sanoq = 0
for i in range(1,11):
    k = int(input(f"k{i} = "))
    if b < k < c and flag:
        son = k
        sanoq = i
        flag = False
    if b < k < c and son < k:
        son = k
        sanoq = i
if sanoq:
    print(sanoq)
else:
    print("00")


# In[31]:


#16
n = int(input("n = "))

flag = True
sanoq = 0
for i in range(1,n+1):
    k = int(input(f"k{i} = "))
    if flag:
        mini = k
        flag = False
    if mini>k:
        mini = k
        sanoq = i
if sanoq:
    print(sanoq-1)
else:
    print(sanoq)


# In[35]:


#17
n = int(input("n = "))

sanoq = 1
flag = True

for i in range(1,n+1):
    k = int(input(f"k{i} = "))
    if flag:
        maxi = k
        flag = False
    if maxi<=k:
        maxi = k
        sanoq = i
print(n-sanoq)


# In[40]:


#18
n = int(input("n = "))

flag = True
oxir = 0
bir = 0

for i in range(1,n+1):
    k = int(input(f"k{i} = "))
    if flag:
        max_oxir = k
        max_bir = k
        bir = i
        oxir = i
        flag = False
        
    if max_oxir <= k:
        max_oxir = k
        oxir = i
        
    if max_bir < k:
        max_bir = k
        bir = i
if oxir==bir:
    print("0")
else:
    print(oxir-bir-1)


# In[10]:


#19
# 8 ta masalan:-2 4 8 0 -6 2 -6 3 -6 -4
# eng kichik elementlar soni : 3 ta

n = int(input("n = "))

sanoq = 1
flag = True

for i in range(1,n+1):
    k = int(input("k = "))
    if flag:
        mini = k
        flag = False
    elif mini==k:
        sanoq += 1
        
    if mini>k:
        mini = k
        sanoq=1
print(sanoq)


# In[214]:


#20
# 10 ta masalan:-2 4 8 0 -6 2 -6 8 -6 -4
# ekstremallari soni : 3ta(-6) + 2ta(8) = 5

n = int(input("n = "))

flag = True
for i in range(1,n+1):
    k = int(input(f"k{i} = "))
    if flag:
        maxi = k
        mini = k
        sana_min = 0
        sana_max = 0
        flag = False
    
    if maxi < k:
        maxi = k
        sana_max = 1
    elif k==maxi:
        sana_max += 1
        
    if mini > k:
        mini = k
        sana_min = 1
    elif k==mini:
        sana_min += 1
if mini==maxi:
    print(sana_min)
else:
    print(sana_max + sana_min)    


# In[8]:


#21

n = int(input("n = "))

flag = True
s = 0
x = 1
y = 1
for i in range(1,n+1):
    k = int(input(f"k{i} = "))
    s += k
    if flag:
        maxi = k
        mini = k
        flag = False
        
    if maxi < k:
        maxi = k
        x = 1
    elif maxi==k:
        x += 1
    
    if mini > k:
        mini = k
        y = 1
    elif mini==k:
        y += 1
print((s - mini*y - maxi*x)/(n-x-y))


# In[71]:


#22
n = int(input("n = "))
                                
x = int(input("k1 = "))
y = int(input("k2 = "))

if x<y:
    mini1 = x
    mini2 = y
else:
    mini1 = y
    mini2 = x
    
for i in range(3,n+1):
    k = int(input(f"k{i} = "))
    if mini1<k<mini2:
        mini2 = k
    if k<mini1:
        mini2 = mini1
        mini1 = k
print(mini1,mini2)


# In[219]:


#23 1-usul
n = int(input("n = "))
                                
x = int(input("k1 = "))
y = int(input("k2 = "))
z = int(input("k3 = "))

if x<y<z:
    maxi1 = x
    maxi2 = y
    maxi3 = z
elif x<z<y:
    maxi1 = x
    maxi2 = z
    maxi3 = y
elif z<x<y:
    maxi1 = z
    maxi2 = x
    maxi3 = y
elif y<z<x:
    maxi1 = y
    maxi2 = z
    maxi3 = x
elif y<x<z:
    maxi1 = y
    maxi2 = x
    maxi3 = z
elif z<y<x:
    maxi1 = z
    maxi2 = y
    maxi3 = x
for i in range(4,n+1):
    k = int(input(f"k{i} = "))
    if maxi1 < k < maxi2:
        maxi1 = k
    if maxi2 < k < maxi3:
        maxi1 = maxi2
        maxi2 = k
    if maxi3 < k:
        maxi1 = maxi2
        maxi2 = maxi3
        maxi3 = k
print(maxi1,maxi2,maxi3)


# In[224]:


#23 2-usul
n = int(input("n = "))

maxi1 = int(input("a1 = "))
maxi2 = int(input("a2 = "))
maxi3 = int(input("a3 = "))

if maxi1<=maxi2:
    maxi1,maxi2 = maxi2,maxi1
if maxi1<=maxi3:
    maxi1,maxi3 = maxi3,maxi1
if maxi2<=maxi3:
    maxi2,maxi3 = maxi3,maxi2
    
for i in range(4,n+1):
    a = int(input(f"a{i} = "))
    if a>maxi1:
        maxi3 = maxi2
        maxi2 = maxi1
        maxi1 = a
    elif maxi1>=a and a>maxi2:
        maxi3 = maxi2
        maxi2 = a
    elif a<= maxi2 and a>maxi3:
        maxi3 = a
print(maxi1,maxi2,maxi3)


# In[226]:


#24
n = int(input("n = "))

flag = True
m =  int(input("k1 = "))
for i in range(2,n+1):
    k = int(input(f"k{i} = "))
    if flag:
        s = m + k
        flag = False
    if m + k > s:
        s = m + k
    m = k
        
print(s)


# In[225]:


#25
n = int(input("n = "))

flag = True
m = int(input("k1 = "))
for i in range(2,n+1):
    k = int(input(f"k{i} = "))
    if flag:
        s = m * k
        birinchi = 1
        ikkinchi = 2
        flag = False
    if m * k < s:
        s = m * k
        birinchi = i-1
        ikkinchi = i
    m = k
        
print("Javob:",s,"\n",birinchi,ikkinchi)


# In[238]:


#26 1-usul
n = int(input("n = "))
indeks = 0
sanoq = 0
s = 0
for i in range(1,n+1):
    k = int(input(f"k{i} = "))
    if k%2==0:   
        indeks = i
        sanoq += 1
        if sanoq > s:
            s = sanoq
    else:
        sanoq = 0
        indeks = i
print(s)


# In[239]:


#26 2-usul

n = int(input("n = "))
s = 0
maxi_s = 0
x = True
for i in range(1,n+1):
    k = int(input(f"k{i} = "))  
    if k%2==0:
        s += 1
    else:
        s = 0
    if maxi_s<s:
        maxi_s = s
if maxi_s==0:
    print("juft son yo'q")
else:
    print(maxi_s)


# In[96]:


#27
n = int(input("n = "))

sanoq = 1
s = 0
indeks = 1
m = int(input("k1 = "))
for i in range(2,n+1):
    k = int(input(f"k{i} = "))
    if m == k and indeks ==i-1 :
        indeks = i
        m = k
        sanoq += 1
        if sanoq > s:
            s = sanoq
            index = i
    if m!=k:
        m = k
        sanoq = 1
        indeks = i
print(s,"ta element","\nbirinchisining indeksi",index-s+1)


# In[233]:


#28
n = int(input("n = "))

index = 0
sanoq = 0
s = 0
for i in range(1,n+1):
    k = int(input(f"k{i} = "))
    if k==1:
        index = i
        sanoq += 1
        if sanoq>s:
            s = sanoq
            nomer = index
    else:
        sanoq = 0
        index = i
if s:
    print(s,nomer-s+1)
else:
    print(0)


# In[1]:


#29
n = int(input("n = "))

flag = True
for i in range(1,n+1):
    k = int(input(f"k{i} = "))
    if flag:
        m = k
        sanoq = 1
        s = 1
        flag = False
    elif m >= k:
        if m > k:
            sanoq = 1
            s = 1
            m = k
        elif m == k:
            sanoq += 1
            m = k
            if sanoq>s:
                s = sanoq
    else:
        sanoq = 0
print(s)


# In[2]:


#30
n = int(input("n = "))

flag = True
sanoq  = 1
for i in range(1,n+1):
    k = int(input(f"k{i} = "))
    if i == 1:
        maxi = k
        continue

    if maxi == k:
        sanoq += 1
    elif maxi < k:
        sanoq = 1
        s = 1
        maxi = k
        flag = True
    else:
        if flag == True:
            s = sanoq
            flag = False
        elif sanoq != 0 and sanoq < s:
            s = sanoq
        sanoq = 0
    if n == i:
            if flag == True:
                s = sanoq
            elif sanoq != 0 and sanoq < s:
                s = sanoq
print(f"Maximumi = {maxi}\nMinimum soni = {s} ta")

