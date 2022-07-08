#!/usr/bin/env python
# coding: utf-8

# # 20/06/2022
# 
# # Python asoslari
# 
# # 21-dars : Matnli fayllarga oid masalalar
# 
# # Muallif: Farrux Sotivoldiyev

# ### 1.Matn fayllari ustida amallar

# In[1]:


#Text1
n = int(input("n = "))
k = int(input("k = "))
x = open(input("File name: "),"x")

for i in range(n):
    x.write("*" * k + "\n")
x.close()


# In[2]:


#Text2
n = int(input("n = "))
x = open(input("File name: "),"x")

for i in range(1,n):
    for j in range(i):
        x.write(chr(97+j))
    x.write("\n")
x.close()


# In[3]:


#Text3
n = int(input("n = "))
x = open(input("File name: "),"x")

for i in range(n):
    for j in range(i+1):
        x.write(chr(65+j))
    if i != n-1:
        x.write('*'*(n-i-1) + "\n")
        continue
    x.write('*'*(n-i-1))
x.close()


# In[4]:


#Text4
x = (open(input("File name: "),"r"))
k = x.read()
print(f"Belgilar: {len(k)} ta")
print(f"Satrlar: {len(k.split())} ta")
x.close()


# In[5]:


#Text5
s = input("Satr kiriting: ")
x = (open(input("File name: "),"a"))
x.write(s)
x.close()


# In[7]:


#Text6
x = (open(input("File name 1: "),"a")) 
y = (open(input("File name 2: ")))
x.write(y.read())
x.close()
y.close()


# In[8]:


#Text7
s = input("Satr kiriting: ")
k = input("File name: ")
x = (open(k))
m = x.read() 
x.close()

x = (open(k,"w"))
x.write(s + "\n"); x.write(m)
x.close()


# In[9]:


#Text8
k = input("File name 1: ")
a = (open(k))
m = a.read() 
a.close()

b = (open(input("File name 2: ")))

x = (open(k,"w"))
x.write(b.read() + "\n"); x.write(m)
x.close()


# In[16]:


#Text9
f = input("File name: ")
k = int(input("k = "))

x = open(f)
y = x.readlines()
x.close()

if len(y)>k:
    y.insert(k,"\n")
    
x = open(f,"w")
x.writelines(y)
x.close()


# In[17]:


#Text11
f = input("File name: ")

x = open(f)
y = x.readlines()
x.close()

for i in range(len(y)):
    if y[i]=="\n":
        y[i] *= 2
        
    
x = open(f,"w")
x.writelines(y)
x.close()


# In[14]:


#Text15
f = input("File name: ")
k = int(input("k = "))

x = open(f)
y = x.readlines()
x.close()

del y[k-1]
    
x = open(f,"w")
x.writelines(y)
x.close()


# In[37]:


#Text16
k = input("Filename: ")
with open(k) as f:
    s = f.readlines()
    
with open(k,"w") as f:
    for _ in range(s.count("\n")):
        s.remove("\n")
    f.writelines(s)


# In[42]:


#Text17
m = input("Filename 1: ")
n = input("Filename 2: ")
with open(m) as f:
    s = f.readlines()
    
with open(n) as f:
    k = f.readlines()
    
with open(m,"w") as f:
    for i in range(len(s)):
        f.writelines(s[i])
        if (i+1) < len(k):
            f.writelines(k[i+1])


# In[7]:


#Text18
k = int(input("k = "))
p = input("Filename: ")

with open(p) as f:
    m = f.readlines()
with open(p,"w") as f:
    for i in range(len(m)):
        f.write(m[i][k:])


# In[56]:


#Text19
with open(input("Filename: "),"r+") as f:
    r = f.read()
    f.seek(0)
    f.write(r.swapcase())


# In[68]:


#Text20
k = input("Filename: ")
with open(k) as f:
    r = " ".join((f.read()).split())
with open(k,"w") as f:
    f.write(r)


# In[79]:


#Text21
k = input("Filename: ")
with open(k) as f:
    r = (f.read()).split()
    
with open(k,"w") as f:
    for _ in range(3):
        del r[-1]
    f.write(" ".join(r))


# In[91]:


#Text22
k = int(input("k = "))
m = input("Filename: ")
with open(m) as f:
    r = (f.read()).split()
    
with open(m,"w") as f:
    for _ in range(3):
        del r[-1]
    f.write(" ".join(r))


# In[89]:


#Text23
k = int(input("k = "))
m = input("Filename: ")
h = input("What file do you create: ")
with open(m) as f:
    r = (f.read()).split()
    new_string = []
    for _ in range(k):
        new_string.append(r.pop(-1))
    
with open(h,"x+") as f:
    f.write(" ".join(new_string))


# ### 2.Matnni formatlash va tahlil qilish.

# In[24]:


#Text24
with open(input("Filename: ")) as f:  
    file = (f.read()).split("\n\n")
    for i in range(file.count("")):
        file.remove("")
            
print(f"Matndagi abzaslar soni {len(file)} ta ")


# In[22]:


#Text25
k = int(input("k = "))
h = input("Filename: ")
with open(h) as f:
    file = (f.read()).split("\n\n")
    for i in range(file.count("")):
        file.remove("")
    for i in range(len(file)):
        if file[i].startswith("\n"):
            file[i] = file[i][1:]
    if len(file)>=k:
        file.pop(k-1)
with open(h,"w") as f:
    file_2 = "\n\n".join(file)
    f.write(file_2) 


# In[44]:


#Text26
with open(input("Filename: ")) as f:  
    file = (f.read()).split("\n\n")
    for i in range(file.count("")):
        file.remove("")
    for i in range(len(file)):
        if file[i].startswith("\n"):
            file[i] = file[i][1:]
    qizil_satr = 0
    for i in file:
        sanoq = 0
        for j in range(6):
            if i[j]==" ":
                sanoq += 1
        if sanoq==5:
            qizil_satr += 1
if qizil_satr == len(file):
    print("Qizil satr")
else:
    print(f"Abzaslar soni: {len(file)} ta")


# In[63]:


#Text27
k = int(input("k = "))
file = input("Filename: ")
with open(file) as f:
    mal = (f.read()).split("     ")
    for i in mal:
        if i=='':
            mal.remove(i)
    if len(mal)>=k:
        del mal[k-1]
    n = " ".join(mal)
with open(file,"w") as f:
    f.write(n)


# In[16]:


#Text28
file = input("Filename: ")
with open(file,"r+") as f:
    k = (f.read()).split("     ")
    for i in range(len(k)-1):
        if k[i]=='':
            k.pop(i)
    for i in range(1,len(k)+1,2):
        k.insert(i,'\n')
    gaplar = " ".join(k)

    f.seek(0)
    f.write(gaplar)


# In[48]:


#Text29
with open(input("Filename: ")) as f:
    k = (f.read()).split()
    maxi = 1
    for i in range(len(k)):
        if maxi < len(k[i]):
            maxi = len(k[i])
            soz = k[i]
print(soz)


# In[51]:


#Text30
with open(input("Filename: ")) as f:
    k = (f.read()).split()
    mini = len(k[0])
    soz = k[0]
    for i in range(1,len(k)):
        if mini > len(k[i]):
            mini = len(k[i])
            soz = k[i]
print(soz) if len(soz)>1 else print("Bunday so'z yo'q")


# In[69]:


#Text31
from string import punctuation as p
k = int(input("k = "))

with open(input("Filename: ")) as f:
    s = f.read()
    m = (s.translate(s.maketrans('','',p))).split()
    h = [i for i in m if len(i)>1]
    
with open(input("What file do you create: "),"x+") as f:
    if k<=len(h):
        f.writelines(" ".join(h[:k]))


# In[10]:


#Text32
from string import punctuation as p
k = "C"

with open(input("Filename: ")) as f:
    s = f.read()
    m = (s.translate(s.maketrans('','',p))).split()
    h = [i for i in m if len(i)>1]
    
with open(input("What file do you create: "),"x+") as f:
    s = ''
    for i in range(len(h)):
        if h[i][0]==k or h[i][0]==k.lower():
            s += h[i] + " "
    f.write(s)


# In[11]:


#Text33
from string import punctuation as p
k = "c"

with open(input("Filename: ")) as f:
    s = f.read()
    m = (s.translate(s.maketrans('','',p))).split()
    h = [i for i in m if len(i)>1]
    
with open(input("What file do you create: "),"x+") as f:
    s = ''
    for i in range(len(h)):
        if h[i][0]==k or h[i][0]==k.upper():
            s += h[i] + " "
    f.write(s)


# ### 3.Sonli ma'lumotlarga ega bo'lgan matnli fayllar.

# In[20]:


#Text40
with open("filename\son_16.txt") as f:
    file1 = (f.read()).split("\n")
    
with open("filename\son_17.txt") as f:
    file2 = (f.read()).split("\n")
    
with open("filename\son_18.txt","x+") as f:
    for i in range(len(file1)):
        f.write(111 * " ")
        f.write("|"+file1[i]+" "*(28-len(file1[i])-len(file2[i])) + file2[i]+"|\n")


# In[22]:


#Text41
with open("filename\son_16.txt") as f:
    file1 = (f.read()).split("\n")
    
with open("filename\son_17.txt") as f:
    file2 = (f.read()).split("\n")
    
with open("filename\son_19.txt","x+") as f:
    for i in range(len(file1)):
        f.write("|"+file1[i]+" "*(28-len(file1[i])-len(file2[i])) + file2[i]+"|\n")


# In[46]:


#Text42
from math import sqrt
n = int(input("N = "))
a = float(input("A = "))
b = float(input("B = "))

qadamlar = []
qadam = abs((b-a)/n)
for i in range(n+1):
    qadamlar.append(round(a,1))
    a += qadam

with open("filename\son_20.txt","x+") as f:
    f.write(63*' '+"No".center(5)+"|"+"x".center(10)+"|"+"Ildizda->x".center(10)+"|\n")
    f.write(63*' ' + 28*("-")+"\n")
    for i in range(len(qadamlar)):
        f.write(63*' ' +(str(i+1)).center(5)+"|"+(str(qadamlar[i])).center(10)+"|"+(str(round(sqrt(qadamlar[i]),1))).center(10)+"|\n")


# In[57]:


#Text43
from math import sqrt,cos,sin
n = int(input("N = "))
a = float(input("A = "))
b = float(input("B = "))

qadamlar = []
qadam = abs((b-a)/n)
for i in range(n+1):
    qadamlar.append(round(a,1))
    a += qadam
    
sinuslar = [round(sin(i),4) for i in qadamlar]
cosinuslar = [round(cos(i),4) for i in qadamlar]

with open("filename\son_21.txt","x+") as f:
    f.write(f"{55*' '}{'No'.center(5)}|{'x'.center(10)}|{'sin(x)'.center(10)}|{'cos(x)'.center(10)}|\n")
    f.write(57*' ' + 37*("-")+"\n")
    for i in range(len(qadamlar)):
        f.write(55*' ' +(str(i+1)).center(5)+"|"+(str(qadamlar[i])).center(10)+"|"+(str(sinuslar[i])).center(10)+"|"+(str(cosinuslar[i])).center(10)+"|\n")


# In[22]:


#Text44
with open(input("Filename: ")) as f:
    sonlar = (f.read()).split()
    butun_sonlar = [int(i) for i in sonlar]
    print("Soni:",len(sonlar),"ta")
    print("Yeg'indi:",sum(butun_sonlar))


# In[30]:


#Text45
with open(input("Filename: ")) as f:
    sonlar = (f.read()).split()
    haqiqiy_sonlar = [float(i) for i in sonlar if i.count(".")==1]
    print("Soni:",len(haqiqiy_sonlar),"ta")
    print("Yeg'indi:",sum(haqiqiy_sonlar))


# In[38]:


#Text46
with open(input("Filename: ")) as f:
    sonlar = (f.read()).split()
    haqiqiy_sonlar = [float(i) for i in sonlar if i.count(".")==1]
with open(input("New filename: "),"x") as f:
    f.writelines([str(i)+"\n" for i in haqiqiy_sonlar])


# In[40]:


#Text47
with open(input("Filename: ")) as f:
    sonlar = (f.read()).split()
    butun_sonlar = [int(i) for i in sonlar if i.count(".")==0]
    print("Soni:",len(butun_sonlar),"ta")
    print("Yeg'indi:",sum(butun_sonlar))


# In[10]:


#Text48
with open(input("Filename: ")) as f:
    sonlar = (f.read()).split()
    butun_sonlar = [int(i) for i in sonlar if i.count(".")==0]
    
with open(input("New filename: "),"x") as f:
    f.writelines([str(i)+"\n" for i in butun_sonlar])


# In[12]:


#Text49
with open(input("Integer Filename: ")) as f:
    sonlar = [int(i) for i in ((f.read()).split())]


with open(input("Filename: "),"r+") as f:
    satrlar = (f.read()).split("\n")
    f.seek(0)
    for i in range(len(satrlar)):
        f.write(f"{satrlar[i]}{sonlar[i]}\n")


# In[27]:


#Text50
with open(input("Filename: ")) as f:
    hammasi = (f.read()).split()
    sonlar = [i for i in hammasi if i.count(".")==1]
    sozlar = [i for i in hammasi if i.isalpha()]

with open(input("Text Filename: "),"x") as f:
    f.write(" ".join(sozlar))
    
with open(input("Integer Filename: "),"x") as f:
    f.write(" ".join(sonlar))


# In[3]:


#Text51
with open(input("Filename: ")) as f:
    hammasi = (f.read()).split()
    
with open(input("Float Filename 1: "),"x") as f:
    f.write("\n".join([hammasi[i] for i in range(0,len(hammasi),3)]))
    
with open(input("Float Filename 2: "),"x") as f:
    f.write("\n".join([hammasi[i] for i in range(1,len(hammasi),3)]))
    
with open(input("Float Filename 3: "),"x") as f:
    f.write("\n".join([hammasi[i] for i in range(2,len(hammasi),3)]))


# In[16]:


#Text52
with open(input("Filename: ")) as f:
    hammasi = [i for i in ((f.read()).split()) if i!="|"]
    butun_sonlar = []
    
    for i in hammasi:
        s = ''
        for j in i:
            if 48<=ord(j)<=57:
                s += j
        butun_sonlar.append(int(s))
        
        file_1 = [];file_2 = [];file_3 = []
        for i in range(0,len(butun_sonlar),9):
            file_1.append(str(sum(butun_sonlar[i:i+3])))
            file_2.append(str(sum(butun_sonlar[i+3:i+6])))
            file_3.append(str(sum(butun_sonlar[i+6:i+9])))    

with open(input("Integer Filename 1: "),"x") as f:
    f.write("\n".join(file_1))
    
with open(input("Integer Filename 2: "),"x") as f:
    f.write("\n".join(file_2))
    
with open(input("Integer Filename 3: "),"x") as f:
    f.write("\n".join(file_3))


# ### 4.Matn fayllarni qayta ishlashga oid qo'shimcha masalalar.

# In[19]:


#Text53
from string import punctuation as p
with open(input("Filename: ")) as f:
    k = f.read()
    tinish_bel = ''
        if k[i] in p:
            tinish_bel += k[i]
with open(input("What file do you create: "),"x") as f:
    f.write(tinish_bel)


# In[11]:


#Text54
from string import punctuation as p
with open(input("Filename 1: ")) as f:
    k = f.read()
    
with open(input("What file do you create: "),"x") as f:
    belgilar = ''
    for i in k:
        if (i in p or i==" ") and i not in belgilar:
            belgilar += i
    f.write(belgilar)


# In[22]:


#Text55
from string import punctuation as p
with open(input("Filename 1: ")) as f:
    k = f.read()
    
with open(input("What file do you create: "),"x") as f:
    belgilar = []
    for i in k:
        if (i in p or i==" ") and i not in belgilar:
            belgilar.append(i)
    f.write("".join(sorted(belgilar)))


# In[24]:


#Text56
from string import punctuation as p
with open(input("Filename 1: ")) as f:
    k = f.read()
    
with open(input("What file do you create: "),"x") as f:
    belgilar = []
    for i in k:
        if (i in p or i==" ") and i not in belgilar:
            belgilar.append(i)
    f.write("".join(sorted(belgilar,reverse=True)))


# In[35]:


#Text57
from string import punctuation as p
with open(input("Filename 1: ")) as f:
    k = f.read()
    harflar = {}
    for i in k:
        if "a"<= i <="z" and i not in harflar.keys():
            harflar[i] = k.count(i)
    
with open(input("What file do you create: "),"x") as f:
    for i,j in harflar.items():
        print(f"{i}-{j}",file=f)


# In[19]:


#Text58
from string import punctuation as p
with open(input("Filename 1: ")) as f:
    k = f.read()
    harflar = {}
    for i in k:
        if "a"<= i <="z" and i not in harflar.keys():
            harflar[i] = k.count(i)

with open(input("What file do you create: "),"x") as f:
    a = dict(sorted(harflar.items(), key=lambda item: item[1],reverse=True))
    for i,j in a.items():
        print(f"{i}-{j}",file=f)


# In[97]:


#Text59
s = '0123456789'
with open(input("Filename: "),"r+") as f:
    k = int(input("k = "))
    m = f.read()
    belgilar = [i for i in m]
    n = k
    while k>len(s):
        k-=10
    belgilar[n] = chr(ord(belgilar[n])+int(s[k-1]))
    f.seek(0)
    f.write("".join(belgilar))


# In[99]:


#Text60
s = '0123456789'
with open(input("Filename: "),"r+") as f:
    k = int(input("k = "))
    m = f.read()
    belgilar = [i for i in m]
    n = k
    while k>len(s):
        k-=10
    belgilar[n] = chr(ord(belgilar[n])-int(s[k-1]))
    f.seek(0)
    f.write("".join(belgilar))

