#!/usr/bin/env python
# coding: utf-8

# # 20/04/2022
# 
# # Python asoslari
# 
# # 15-dars : List bilan ishlash
# 
# # Muallif: Farrux Sotivoldiyev

# ### 1.Massivni hosil qilish va elementlarini kiritish

# In[1]:


a = [1,2,3,9,567,778,9,-6,9,-1,0]
print("len->",len(a))
print("type->",type(a))
del a[1]
print("del->",a)
a.append(1)
print("append->",a)
a.insert(1,5)
print("insert->",a)
a.extend(a)
print("extend->",a)
a.remove(9)
print("remove->",a)
print("pop->",a.pop(5))
print("min->",min(a))
print("sum->",sum(a))
print("list->",list(range(1,11,2)))
a.clear()
print("clear->",a)


# In[16]:


#Array1
n = int(input("n = "))
toq = []
i = 0
while len(toq) != n:
    if i%2==1:
        toq.append(i)
    i += 1
    
print(toq)


# In[15]:


#Array2
n = int(input("n = "))
daraja_2 = []
i = 0
while len(daraja_2) != n:
    daraja_2.append(2**i)
    i += 1
    
print(daraja_2)


# In[19]:


#Array3
n = int(input("n = "))
A = int(input("A = "))
D = int(input("D = "))
Arif_prog = []
while len(Arif_prog) != n:
    Arif_prog.append(A)
    A+=D
print(Arif_prog)


# In[21]:


#Array4
n = int(input("n = "))
A = int(input("A = "))
D = int(input("D = "))
Geo_prog = []
while len(Geo_prog) != n:
    Geo_prog.append(A)
    A*=D
print(Geo_prog)


# In[2]:


#Array5 1-usul
n = int(input("n = "))
fibonachi = []
f1 = 1
f2 = 1
while len(fibonachi) != n:
    fibonachi.append(f2)
    f1 = f1 + f2
    f2 = f1 - f2
print(fibonachi)

#Array5 2-usul
n = int(input("n = "))
fibonachi = [1,1]
for i in range(2,n):
    fibonachi.append(fibonachi[i-1]+fibonachi[i-2])
print(fibonachi)


# In[1]:


#Array6 1-usul
n = int(input("n = "))
a = int(input("A = "))
b = int(input("B = "))
massiv = [a,b]
c = a+b
while len(massiv)!=n:
    massiv.append(c)
    c+=c
print(massiv)

#Array6 2-usul
n = int(input("n = "))
a = int(input("A = "))
b = int(input("B = "))
massiv = [a,b]
for i in range(2,n):
    massiv.append(sum(massiv))
print(massiv)


# In[23]:


#Array7 1-usul
massiv = list(range(1,20,5))
for i in range(len(massiv)-1,-1,-1):
    print(massiv[i],end=" ")

#Array7 2-usul
massiv = list(range(1,20,5))
print(list(reversed(massiv)))

#Array7 3-usul
massiv = list(range(1,20,5))
print(massiv[::-1])

#Array7 4-usul
massiv = list(range(1,20,5))
massiv.reverse()
print(massiv)


# In[24]:


#Array8
massiv = list(range(2,20))
k = 0
for i in range(len(massiv)):
    if massiv[i]%2==1:
        k += 1
        print(massiv[i],end=" ")
print("soni:",k)


# In[27]:


#Array9 1-usul
massiv = list(range(2,20))
k = 0
for i in range(len(massiv)-1,-1,-1):
    if massiv[i]%2==0:
        k += 1
        print(massiv[i],end=" ")
print("soni:",k)

#Array9 2-usul
massiv = list(range(2,20))
massiv.reverse()
k = 0
for i in range(len(massiv)):
    if massiv[i]%2==0:
        k += 1
        print(massiv[i],end=" ")
print("soni:",k)


# In[28]:


#Array10
massiv = list(range(2,20))

for i in range(len(massiv)):
    if massiv[i]%2==0:
        print(massiv[i],end=" ")
        
for i in range(len(massiv)-1,-1,-1):
    if massiv[i]%2==1:
        print(massiv[i],end=" ")


# In[40]:


#Array11 1-usul
k = int(input("k = "))
massiv = list(range(2,20))
for i in range(k,len(massiv),k):
    print(massiv[i],end = " ")
    
#Array11 2-usul
k = int(input("k = "))
massiv = list(range(2,20))
print(massiv[k:len(massiv):k])


# In[39]:


#Array12 1-usul
massiv = list(range(20))
for i in range(0,len(massiv),2):
    print(massiv[i],end = " ")

#Array12 2-usul
massiv = list(range(20))
print(massiv[0:len(massiv):2])


# In[45]:


#Array13 1-usul
massiv = list(range(19)) 
for i in range(len(massiv)-1,-1,-2):
    print(massiv[i],end = " ")

#Array13 2-usul
massiv = list(range(19)) 
print(massiv[::-2])


# In[55]:


#Array14 1-usul
massiv = list(range(19)) 
for i in range(0,len(massiv),2):
    print(massiv[i],end = " ")
for i in range(1,len(massiv),2):
    print(massiv[i],end = " ")

#Array14 2-usul
massiv = list(range(19)) 
a = massiv[:len(massiv):2]
b = massiv[1:len(massiv):2]
a.extend(b)
print(a)


# In[105]:


#Array15 1-usul
massiv = list(range(10,int(input("n = "))))
for i in range(1,len(massiv),2):
    print(massiv[i],end = " ")
for i in range(len(massiv)-2,-1,-2):
    print(massiv[i],end = " ")

#Array15 2-usul
massiv = list(range(10,int(input("n = ")))) 
a = massiv[1:len(massiv):2]
b = massiv[len(massiv)-2::-2]
a.extend(b)
print(a)


# In[8]:


#Array16 1-usul
massiv = list(range(int(input("n = ")))) 
i = 0
uzunlik = len(massiv)
while i < uzunlik:
    uzunlik -= 1 
    print(massiv[i],end=" ")
    if i==uzunlik:
        break
    print(massiv[uzunlik],end=" ")
    i += 1 

#Array16 2-usul
massiv = list(range(int(input("n = ")))) 
m = massiv[:len(massiv)//2]
n = massiv[:len(massiv)//2-1:-1]
k = 0
while k < len(m) or k < len(n):
    if k!=len(m):
        print(m[k],end=" ")
    print(n[k],end=" ")
    k += 1
    
#Array16 3-usul
massiv = list(range(int(input("n = ")))) 
for i in range(len(massiv)//2):
    print(massiv[i],massiv[len(massiv)-i-1],end=" ")


# In[8]:


#Array17 1-usul
n = int(input("n = "))
massiv = [i for i in range(n+1)]
m = massiv[:len(massiv)//2+1]
n = massiv[:len(massiv)//2:-1]
k = 0
while k < len(m) or k < len(n):
    if k<len(m)-1:
        print(m[k],end=" ")
        print(m[k+1],end=" ")
    if k==len(m)-1:
        print(m[k],end=" ")
        
    if k<len(n)-1:
        print(n[k],end=" ")
        print(n[k+1],end=" ")
    if k==len(n)-1:
        print(n[k],end=" ")
    k += 2

#Array17 2-usul
n = int(input("n = "))
a = [i for i in range(n+1)]
i = 0
while i<=n:
    print(a[i],end=" ")
    i+=1
    if i>n:
        break
    print(a[i],end=" ")
    i+=1
    if i>n:
        break
    print(a[n],end=" ")
    n-=1
    if i>n:
        break
    print(a[n],end=" ")
    n-=1


# ### 2.Massiv elementlarini taxlil qilish 

# In[10]:


#Array18 1-usul
massiv = [9,6,1,3,8,6,2,8,6,5] 
for i in range(len(massiv)):
    if massiv[-1] > massiv[i]:
        print(massiv[i])
        break
else:
    print(0)
    
#Array18 2-usul
massiv = [9,6,1,3,8,6,2,8,6,5] 
oxirgi = massiv[len(massiv)-1]
for i in massiv:
    if oxirgi>i:
        print(i)
        break
else:
    print(0)


# In[92]:


#Array19 1-usul
massiv = [20,64,9,0,2,4,567,89,24,40]
for i in range(len(massiv)-1,-1,-1):
    if massiv[0] < massiv[i] < massiv[-1]:
        print(i)
        break
else:
    print(0)
    
#Array19 2-usul
massiv = [20,64,9,0,2,4,567,89,24,40]
o = massiv[-1]
b = massiv[0]
massiv.reverse()
for i in range(len(massiv)):
    if b<massiv[i]<o:
        print(len(massiv)-1-i)
        break
else:
    print(0)


# In[105]:


#Array20 1-usul
k = int(input("K = "))
l = int(input("L = "))
s = 0
massiv = [20,64,9,0,2,4,567,89,24,40]
for i in range(k+1,l):
    s += massiv[i]
print(s)

#Array20 2-usul
k = int(input("K = "))
l = int(input("L = "))
massiv = [20,64,9,0,2,4,567,89,24,40]
print(sum(massiv[k+1:l]))


# In[127]:


#Array21 1-usul
k = int(input("K = "))
l = int(input("L = "))
s = 0
p = 0
massiv = [20,64,9,0,2,4,567,89,24,40]
for i in range(len(massiv)):
    if k < i < l:
        p += 1
        s += massiv[i]
print(s/p)

#Array21 2-usul
massiv = [20,64,9,0,2,4,567,89,24,40]
k = int(input("K = "))
l = int(input("L = "))
print(sum(massiv[k+1:l])/(1 if l-k==1 else abs(l-k-1)))


# In[133]:


#Array22 1-usul
k = int(input("K = "))
l = int(input("L = "))
s = 0
massiv = [20,64,9,0,2,4,567,89,24,40]
for i in range(len(massiv)):
    if k >= i or l <= i:
        s += massiv[i]
print(s)

#Array22 2-usul
k = int(input("K = "))
l = int(input("L = "))
massiv = [20,64,9,0,2,4,567,89,24,40]
k1 = massiv[:k+1]
l1 = massiv[l::]
print(sum(k1)+sum(l1))


# In[138]:


#Array23 1-usul
k = int(input("K = "))
l = int(input("L = "))
massiv = [20,64,9,0,2,4,567,89,24,40]
s = 0
p = 0
for i in range(len(massiv)):
    if k >= i or l <= i:
        p += 1
        s += massiv[i]
print(s/p)
    
#Array23 2-usul
k = int(input("K = "))
l = int(input("L = "))
massiv = [20,64,9,0,2,4,567,89,24,40]
k1 = massiv[:k+1]
l1 = massiv[l::]
print((sum(k1)+sum(l1))/len(k1+l1))


# In[12]:


#Array24 1-usul
n = int(input("n = "))
k = 0
massiv = [2*i for i in range(n)]
d = massiv[1] - massiv[0]
for i in range(len(massiv)-1):
    if massiv[i+1]-massiv[i]==d:
        k += 1
if len(massiv)-1==k:
    print(d)
else:
    print(0)
    
#Array24 2-usul
n = int(input("n = "))
a = [2*i for i in range(n)]
d = a[1] - a[0]
for i in range(2,n):
    if a[i]-a[i-1]!=d:
        print(0)
        break
else:
    print(d)


# In[144]:


#Array25
k = 0
massiv = [2,6,18,54,162]
d = massiv[1] // massiv[0]
for i in range(len(massiv)-1):
    if massiv[i+1]//massiv[i]==d:
        k += 1
if len(massiv)-1==k:
    print(d)
else:
    print(0)


# In[61]:


#Array26 1-usul
from random import randint 
a = [randint(1,9) for i in range(n)]
print(a)
for i in range(len(a)-1):
    if (a[i]%2==0 and a[i+1]%2==1) or (a[i]%2==1 and a[i+1]%2==0):
        continue
    else:
        print(i+1)
        break
else:
    print(0)
    
#Array26 2-usul
from random import randint 
n = int(input("n = "))
a = [randint(1,9) for i in range(n)] 
print(a)
for i in range(1,n):
    if (a[i]+a[i-1])%2!=1:
        print(i)
        break
else:
    print(0)


# In[35]:


#Array27
m = [-9,8,-7,6,5,4,-8,3,-2,1]
for i in range(len(m)-1):
    if (m[i]>0 and m[i+1]<0) or (m[i]<0 and m[i+1]>0):
        continue
    else:
        print(i+1)
        break
else:
    print(0)


# In[49]:


#Array28 1-usul
m = [9,8,-7,6,5,4,-8,3,-2,1]
for i in range(0,len(m),2):
    if i==0:
        mini = m[0]
    elif mini > m[i]:
        mini = m[i]
print(mini)

#Array28 2-usul
m = [9,8,-7,6,5,4,-8,3,-2,1,0]
print(min(m[::2]))


# In[50]:


#Array29 1-usul
m = [9,2,-7,6,5,4,-8,3,-2,1]
for i in range(1,len(m),2):
    if i==1:
        maxi = m[1]
    elif maxi < m[i]:
        maxi = m[i]
print(maxi)

#Array29 2-usul
m = [9,2,-7,6,5,4,-8,3,-2,1]
print(max(m[1::2]))


# In[52]:


#Array30 
k = 0
m = [9,2,-7,6,5,4,-8,3,-2,1]
for i in range(len(m)-1):
    if m[i+1] < m[i]:
        k+=1
        print(i,end=" ")
print("soni:",k)


# In[56]:


#Array31
k = 0
m = [9,2,-7,6,5,4,-8,3,-2,1]
for i in range(len(m)-1,0,-1):
    if m[i-1] < m[i]:
        k+=1
        print(i,end=" ")
print("soni:",k)


# In[57]:


#Array32
m = [9,2,-7,6,5,4,-8,3,-2,1]
for i in range(1,len(m)-1):
    if m[i-1] > m[i] and m[i+1] > m[i]:
        print(i)
        break


# In[63]:


#Array33
m = [9,2,-7,6,5,4,-8,3,-2,1]
for i in range(1,len(m)-1):
    if m[i-1] < m[i] and m[i+1] < m[i]:
        k = i
print(k)


# In[64]:


#Array34
m = [9,2,-7,6,5,4,-8,3,-2,1]
flag = True
for i in range(1,len(m)-1):
    if m[i-1] > m[i] and m[i+1] > m[i]:
        if flag:
            maxi = m[i]
            flag = False
        elif maxi < m[i]:
            maxi = m[i]
print(maxi)


# In[65]:


#Array35
m = [9,2,-7,6,5,4,-8,3,-2,1]
flag = True
for i in range(1,len(m)-1):
    if m[i-1] < m[i] and m[i+1] < m[i]:
        if flag:
            mini = m[i]
            flag = False
        elif mini > m[i]:
            mini = m[i]
print(mini)


# In[100]:


#Array36
m = [9,2,-7,6,5,4,-8,3,-2,1]
def lok_max(m):
    l_max = []
    for i in range(1,len(m)-1):
        if m[i-1]<m[i] and m[i+1]<m[i]:
            l_max.append(m[i])
    return l_max

def lok_min(m):
    l_min = []
    for i in range(1,len(m)-1):
        if m[i-1]>m[i] and m[i+1]>m[i]:
            l_min.append(m[i])
    return l_min

def main(m):
    maxi = lok_max(m)
    mini = lok_min(m)
    for i in maxi:
        m.remove(i)
    for i in mini:
        m.remove(i)
    return max(m)

print(main(m))


# In[3]:


#Array37 
m = [9,2,-7,6,5,4,8,-3,2,1]
i = 1
s = 0
while i<len(m)-1:
    if m[i]>m[i-1] and m[i]>m[i+1]:
        s+=1
    i+=1
if m[-2]<m[-1]:
    s+=1
print(s)


# In[2]:


#Array38
m = [9,2,-7,6,5,4,8,-3,2,1]
i = 1
s = 0
while i<len(m)-1:
    if m[i] < m[i-1] and m[i] < m[i+1]:
        s += 1
    i += 1
if m[-1]<m[-2]:
    s += 1
print(s)


# In[11]:


#Array39
m = [9,2,-7,6,5,4,8,-3,2,1]
i = 1
m_o = 0
m_k = 0
while i < len(m)-1:
    if m[i-1]>m[i]<m[i+1]:
        m_k += 1
    if m[i-1]<m[i]>m[i+1]:
        m_o += 1
    i += 1
if m[-1]>m[-2]:
    m_o += 1   # 3 ta
if m[-1]<m[-2]:
    m_k += 1   # 4 ta
print(m_k + m_o)


# In[115]:


#Array40
r = int(input("R = "))
m = [1,12,-2,20,0,-15,9,56]
mini = abs(r - m[0])
son = m[0]
for i in range(len(m)):      
    if mini > abs(r - m[i]):
        mini = abs(r - m[i])
        son = m[i]
print("Eng yaqini:",son)


# In[127]:


#Array41
m = [1,12,-2,20,1,-15,9,5]
maxi = m[0]+m[1]
for i in range(1,len(m)-1):
    if maxi<m[i]+m[i+1]:
        maxi = m[i]+m[i+1]
        k = m[i]
        n = m[i+1]
print(k,n)


# In[12]:


#Array42
m = [1,12,-2,2,1,-15,9,5]
r = int(input("R = "))

def qoshni_max(m,r):
    k =  []
    for i in range(len(m)-1):
        k.append(m[i] + m[i+1])
    for i in range(len(k)):
        if i==0:
            mini = abs(r - k[0])  
            son = k[i]
        elif mini > abs(r - k[i]):
            mini = abs(r - k[i])
            index1 = i
            index2 = i+1
    return index1,index2

print(qoshni_max(m,r))


# In[7]:


#Array43 1-usul
from random import randint
n = int(input("n = "))
m = [randint(1,9) for i in range(n)]
m.sort()
print(m)
bir = m[0]
k = 1
for i in range(len(m)):
    if bir<m[i] or bir>m[i]:
        bir = m[i]
        k += 1
print(k)

#Array43 2-usul
from random import randint
n = int(input("n = "))
a = [randint(1,9) for i in range(n)]
a.sort()
print(a)
s = 1
for i in range(1,n):
    if a[i]!=a[i-1]:
        s += 1
print(s)


# In[12]:


#Array44
a = [1,6,3,5,4,7,6,2]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]==a[j]:
            print(i,j)
            break


# In[37]:


#Array45
m = [1,12,-2,2,4,-15,9,5]
yaqin = abs(m[0]-m[1])
for i in range(1,len(m)-1):
    if yaqin > abs(m[i]-m[i+1]):
        yaqin = abs(m[i]-m[i+1])
        bir = i
        ikki = i+1
print(bir,ikki)


# In[43]:


#Array46
m = [1,12,-2,2,1,-15,9,5]
r = int(input("R = "))

def katta_max(m,r):
    k =  []
    for i in range(len(m)-1):
        k.append(m[i] + m[i+1])
    for i in range(len(k)):
        if i==0:
            mini = abs(r - k[0])  
            son = k[i]
        elif mini > abs(r - k[i]):
            mini = abs(r - k[i])
            index1 = i
            index2 = i+1
    return m[index1],m[index2]

print(katta_max(m,r))


# In[9]:


#Array47 1-usul
m = [4,4,2,3,1,4,5,7,4,2]
m.sort(reverse=True)
maxi = m[0]
print(maxi,end=" ")
for i in range(len(m)):
    if maxi > m[i]:
        maxi = m[i]
        print(maxi,end=" ")

#Array47 2-usul
from random import randint
n = int(input("n = "))
a = [randint(1,9) for i in range(n)]
print(a)
matrix = []
for i in a:
    if i not in matrix:
        matrix.append(i)
print(matrix)


# In[25]:


#Array48
m = [1,2,4,5,8,7,2,3,4,5,8,7,8,8,1,1,2,2,2,6,1]
m.sort()
maxi = m[0]
soni = m.count(m[0])
for i in range(len(m)):
    if maxi < m[i] and soni < m.count(m[i]):
        maxi = m[i]
        soni = m.count(m[i])
print("son =",maxi,"\nsoni:",soni,"ta")


# In[26]:


#Array49
n = int(input("n = "))
a = [randint(-5,50) for i in range(n)]
print(a)
for i in range(n):
    if a[i]>n or a[i]<1:
        print(i)
        break
else:
    print("Done!")  


# In[33]:


#Array50
m = [1,2,4,5,8,7,2,3,4,5,8,7,8,6,9,8,0]
k = 0
for i in range(len(m)-1):
    if m[i] > m[i+1]:
        k += 1 
print(k)


# ### 3.Bir nechta massiv bilan ishlash

# In[29]:


#Array51
a = [1,2,4,58,8]
b = [4,5,2,4,7]
for i in range(len(a)):
    a[i],b[i] = b[i],a[i]
print(a,b)


# In[16]:


#Array52
from random import randint as r
n = int(input("n = "))
a = [r(1,11) for i in range(n)]
b = []
for i in range(n):
    if a[i]<5:
        b.append(2*a[i])
    else:
        b.append(a[i]/2)
print(b)


# In[20]:


#Array53
from random import randint as r
n = int(input("n = "))
a = [r(1,10) for i in range(n)]
b = [r(1,10) for i in range(n)]
c = []
for i in range(n):
    if a[i]>b[i]:
        c.append(a[i])
    else:
        c.append(b[i])
print(c)


# In[24]:


#Array54
from random import randint as r
n = int(input("n = "))
a = [r(1,10) for i in range(n)]
b = []
print(a)
for i in range(n):
    if a[i]%2==0:
        b.append(a[i])
print("soni =",len(b),"ta")
print(b)


# In[27]:


#Array55
from random import randint as r
n = int(input("n = "))
a = [r(1,10) for i in range(n)]
b = []
print(a)
for i in range(1,n,2):
    b.append(a[i])
print("Soni :",len(b))
print(b)


# In[26]:


#Array56
from random import randint as r
n = int(input("n = "))
a = [r(1,10) for i in range(n)]
b = []
print(a)
for i in range(3,n,3):
    b.append(a[i])
print("Soni :",len(b))
print(b)


# In[32]:


#Array57 1-usul
from random import randint as r
n = int(input("n = "))
a = [r(1,10) for i in range(n)]
b = []
for i in range(0,n,2):
    b.append(a[i])
for i in range(1,n,2):
    b.append(a[i])
print(b)

#Array57 2-usul
n = int(input("n = "))
a = [r(1,10) for i in range(n)]
b = a[::2] + a[1::2]
print(b)


# In[33]:


#Array58
from random import randint as r
n = int(input("n = "))
a = [r(1,10) for i in range(n)]
print(a)
b = []
for i in range(n):
    s = 0
    for j in range(i+1):
        s += a[j]
    b.append(s)
print(b)


# In[35]:


#Array59
from random import randint as r
n = int(input("n = "))
a = [r(1,10) for i in range(n)]
print(a)
b = []
for i in range(n):
    s = 0
    for j in range(i+1):
        s += a[j]
    b.append(s/a[i])
print(b)


# In[33]:


#Array60 1-usul
from random import randint as r
n = int(input("n = "))
a = [r(1,10) for i in range(n)]
print(a)
b = []
for i in range(n):
    s = 0
    for j in range(i,n):
        s += a[j]
    b.append(s)
print(b)

#Array60 2-usul
from random import randint as r
n = int(input("n = "))
a = [r(1,10) for i in range(n)]
print(a)
b = []
for i in range(n):
    b.append(sum(a[i:]))
print(b)


# In[38]:


#Array61
from random import randint as r
n = int(input("n = "))
a = [r(1,10) for i in range(n)]
print(a)
b = []
for i in range(n):
    s = 0
    k = 0
    for j in range(i,n):
        k += 1
        s += a[j]
    b.append(s/k)
print(b)


# In[45]:


#Array62
from random import randint as r
n = int(input("n = "))
a = [r(-10,12) for i in range(n)]
print(a)
b = []
c = []
for i in range(n):
    if a[i]>=0:
        b.append(a[i])
    else:
        c.append(a[i])
print(b)
print(c)


# In[54]:


#Array63
from random import randint as r
n = int(input("n = "))
a = [i for i in range(1,n+1)]
b = [i for i in range(n+1,2*n+1)]
c = []
print(a)
print(b)
if a[0]<b[0]:
    c.extend(a)
    c.extend(b)
else:
    c.extend(b)
    c.extend(a)
print(c)


# In[54]:


#Array64 
a = [1,5,10]
b = [4,11,20]
c = [6,21,40] 
d = a+b+c
d.sort()
print(d)


# ### 4.Massiv elementlarini o'zgartirish

# In[72]:


#Array65
from random import randint as r
n = int(input("n = "))
k = int(input("k = "))
a = [r(1,12) for i in range(n)]
print(a)
ak = a[k]
for i in range(n):
    a[i] = a[i] + ak
print(a)


# In[75]:


#Array66
from random import randint as r
n = int(input("n = "))
a = [r(1,12) for i in range(n)]
print(a)
for i in range(n):
    if a[i]%2==0:
        ak = a[i]
        break
for i in range(n):
    if a[i]%2==0:
        a[i] = a[i] + ak
print(a)


# In[80]:


#Array67
from random import randint as r
n = int(input("n = "))
a = [r(1,12) for i in range(n)]
print(a)
for i in range(n):
    if a[i]%2==1:
        ak = a[i]
for i in range(n):
    if a[i]%2==1:
        a[i] = a[i] + ak
print(a)


# In[81]:


#Array68 1-usul
from random import randint
n = int(input("n = "))
a = [randint(1,9) for i in range(n)]
print(a)
for i in range(n):
    if i==0:
        maxi = a[i]
        mini = a[i]
        continue
    if maxi<a[i]:
        maxi = a[i]
    if mini>a[i]:
        mini = a[i]
a[a.index(mini)] = maxi
a[a.index(maxi)] = mini
print(a)

#Array68 2-usul
from random import randint
n = int(input("n = "))
a = [randint(1,9) for i in range(n)]
print(a)

mini_index = a.index(min(a))
maxi_index = a.index(max(a))
a[mini_index],a[maxi_index] = a[maxi_index],a[mini_index]


# In[5]:


#Array69
from random import randint
n = int(input("n = "))
a = [randint(1,9) for i in range(n)]
print(a)
for i in range(0,n-1,2):
    a[i],a[i+1] = a[i+1],a[i]
print(a)


# In[8]:


#Array70
from random import randint
n = int(input("n = "))
a = [randint(1,9) for i in range(n)]
print(a)
a[:n//2],a[n//2:] = a[n//2:],a[:n//2]
print(a)


# In[17]:


#Array71 1-usul
from random import randint
n = int(input("n = "))
a = [randint(1,9) for i in range(n)]
print(a)
a.reverse()
print(a)

#Array71 2-usul
from random import randint
n = int(input("n = "))
a = [randint(1,9) for i in range(n)]
print(a)
for i in range(n//2):
    a[i],a[n-i-1] = a[n-i-1],a[i]
print(a)


# In[40]:


#Array72
from random import randint
n = int(input("n = "))
k = int(input("k = "))
h = int(input("h = "))
a = [randint(1,9) for i in range(n)]   
print(a)

d = h - k
for _ in range((d+1)//2):
    a[k],a[k+d] = a[k+d],a[k]
    d -= 2
    k += 1
print(a)


# In[14]:


#Array73 
from random import randint
n = int(input("n = "))
k = int(input("k = "))
h = int(input("h = "))
a = [randint(1,9) for i in range(n)]   
print(a)

while k<h:
    k += 1; h -= 1 
    a[k],a[h] = a[h],a[k]
    
print(a)


# In[34]:


#Array74
from random import randint
n = int(input("n = "))
a = [int(input("a = ")) for i in range(n)]
print(a)
kottasi = max(a)
kichigi = min(a)
for i in range(n):
    if a.index(kichigi)<i<a.index(kottasi):
        a[i] = 0
print(a)


# In[15]:


#Array75 1-usul
a = [5,-1,7,1,2,0,6,4,9,3,12,8,10] 
index1 = a.index(max(a))
index2 = a.index(min(a))

if index1>index2:
    index1,index2=index2,index1
d = index2-index1

for _ in range((d+1)//2):
    a[index1],a[index1+d] = a[index1+d],a[index1]
    d -= 2
    index1 += 1
print(a)

# Array 75 2-usul
from random import randint
a = list(set([randint(-20,20) for i in range(1,10)]))
print(a)
mi = a.index(min(a))
print(mi)
ma = a.index(max(a))
print(ma)
t = (1 if mi<ma else -1)
a[mi:ma+t:t] = list(reversed(a[mi:ma+t:t]))
print(a)


# In[40]:


#Array76
from random import randint
n = int(input("n = "))
a = [randint(1,9) for i in range(n)]    
print(a)
for i in range(1,n-1):
    if a[i-1]<a[i]>a[i+1]:
        a[i] = 0
print(a)


# In[18]:


#Array77
from random import randint
n = int(input("n = "))
a = [randint(1,9) for i in range(n)]    
print(a)
x = a[0]
for i in range(1,n-1):
    if x>a[i]<a[i+1]:
        x = a[i]
        a[i] = a[i] ** 2
        continue
    x = a[i]
print(a)


# In[56]:


#Array78
from random import randint
n = int(input("n = "))
a = [randint(1,9) for i in range(n)]    
print(a)
for i in range(n):
    if i==n-1:
        a[i] = (a[i]+a[0])/2
    else:
        a[i] = (a[i]+a[i+1])/2
print(a)


# In[19]:


#Array79 1-usul
from random import randint
n = int(input("n = "))
a = [randint(1,9) for i in range(n)]    
print(a)
for i in range(n-1,-1,-1):
    a[i] = a[i-1]
a[0] = 0
print(a)

#Array79 2-usul
from random import randint
n = int(input("n = "))
a = [randint(1,9) for i in range(n)]    
print(a)
a = [0] + a[:-1]
print(a)


# In[69]:


#Array80
from random import randint
n = int(input("n = "))
a = [randint(1,9) for i in range(n)]    
print(a)
for i in range(n-1):
    a[i] = a[i+1]
a[-1] = 0
print(a)


# In[13]:


#Array81
from random import randint
n = int(input("n = "))
k = int(input("k = "))
a = [randint(1,9) for i in range(n)]    
print(a)
for i in range(n-1,-1,-1):
    a[i] = a[i-k]
for i in range(k):
    a[i] = 0
print(a)


# In[11]:


#Array82
from random import randint
n = int(input("n = "))
k = int(input("k = "))
a = [randint(1,9) for i in range(n)]    
print(a)
x = 0
for i in range(k,n):
    a[x] = a[i]
    x += 1
for j in range(n-k,n):
    a[j] = 0
print(a)


# In[21]:


#Array83 1-usul
from random import randint
n = int(input("n = "))
a = [randint(1,9) for i in range(n)]    
print(a)
k = a[-1]
for i in range(n-1,-1,-1):
    a[i] = a[i-1]
a[0] = k
print(a)

#Array83 2-usul
from random import randint
n = int(input("n = "))
a = [randint(1,9) for i in range(n)]    
print(a)
a = [a[-1]] + a[:-1]
print(a)

#Array83 3-usul
from random import randint
n = int(input("n = "))
a = [randint(1,9) for i in range(n)]    
print(a)
a = a[-1:-2:-1] + a[:-1]
print(a)


# In[75]:


#Array84
from random import randint
n = int(input("n = "))
a = [randint(1,9) for i in range(n)]    
print(a)
k = a[0]
for i in range(n-1):
    a[i] = a[i+1]
a[-1] = k
print(a)


# In[64]:


#Array85
from random import randint
n = int(input("n = "))
k = int(input("k = "))
a = [randint(1,9) for i in range(n)]    
print(a)
m = 0
b = a[:-5:-1]
for i in range(n-1,-1,-1):
    a[i] = a[i-k]
for i in range(k-1,-1,-1):
    a[m] = b[i]
    m+=1
print(a)


# In[5]:


#Array86 1-usul
from random import randint
n = int(input("n = "))
k = int(input("k = "))
a = [randint(1,9) for i in range(n)]    
print(a)
b = a[:4]
x = 0
y = 0
for i in range(k,n):
    a[x] = a[i]
    x += 1
for j in range(n-k,n):
    a[j] = b[y]
    y += 1
print(a)

#Array86 2-usul
from random import randint
n = int(input("n = "))
k = int(input("k = "))
a = [randint(1,9) for i in range(n)]    
print(a)
a = a[k:] + a[:k]
print(a)


# In[87]:


#Array87
a = [21,3,5,8,9,12,20,22,34,90]
for i in range(1,len(a)-1):
    if a[i]<a[0]<a[i+1]:
        a.insert(i,a.pop(0))
print(a)


# In[105]:


#Array88
a = [3,5,8,9,12,13,20,22,34,90,15]
for i in range(len(a)-1):
    if a[i]<a[-1]<a[i+1]:
        a.insert(i+1,a.pop(-1))
print(a)


# In[36]:


#Array89 
a = [5,8,9,12,13,20,100,22,34,90]
for i in range(1,len(a)-1):
    if (a[i-1]>a[i]<a[i+1] or a[i-1]<a[i]>a[i+1]) and (a[i-1]<a[i+1]):
        k = a.pop(i)
        break
for i in range(len(a)-1):
    if a[i]<k<a[i+1]:
        print(k)
        a.insert(i+1,k)
        break
else:
    if a[-1]<k:
        a.append(k)
    else:
        a.insert(0,k)
print(a)


# ### 5.Massivga element qo'shish va o'chirish

# In[174]:


#Array90
from random import randint
n = int(input("n = "))
k = int(input('k = '))
a = [randint(1,9) for i in range(n)]    
print(a)
del a[k]
print(a)


# In[11]:


#Array91
from random import randint
n = int(input("n = "))
k = int(input('k = '))
m = int(input('m = '))
a = [randint(1,9) for i in range(n)]    
print(a)
for _ in range(k,m):
    a.remove(a[k])
print(a)


# In[18]:


#Array92
from random import randint
n = int(input("n = "))
a = [randint(1,9) for i in range(n)]    
print(a)
i = 0
while i < len(a): 
    if a[i]%2==1:
        del a[i]
    else:
        i += 1
print(len(a),"ta")
print(a)


# In[2]:


#Array93 1-usul
from random import randint
n = int(input("n = "))
a = [randint(1,9) for i in range(n)]    
print(a)
i = 0
while i < len(a):
    del a[i]
    i += 1
print(len(a),"ta")
print(a)

#Array93 2-usul
from random import randint
n = int(input("n = "))
a = [randint(1,9) for i in range(n)]    
print(a)
del a[::2]
print(len(a),"ta")
print(a)


# In[3]:


#Array94 1-usul
from random import randint
n = int(input("n = "))
a = [randint(1,9) for i in range(n)]    
print(a)
i = 1
while i < len(a):
    del a[i]
    i += 1
print(len(a),"ta")
print(a)

#Array94 2-usul
from random import randint
n = int(input("n = "))
a = [randint(1,9) for i in range(n)]    
print(a)
del a[1::2]
print(len(a),"ta")
print(a)


# In[8]:


#Array95
from random import randint
n = int(input("n = "))
a = [randint(1,9) for i in range(n)]    
print(a)
i = 0
while i < len(a)-1:
    if a[i]==a[i+1]:
        del a[i]
    else:
        i += 1
print(len(a),"ta")
print(a)


# In[9]:


#Array96
from random import randint
n = int(input("n = "))
a = [randint(1,9) for i in range(n)]
print(a)
i = 0
while i<len(a):
    if a.count(a[i])>1:
        x = a[i]
        for _ in range(a.count(a[i])):
            a.remove(x)
        a.insert(i,x)
    i += 1
print(a)


# In[21]:


#Array97
from random import randint
n = int(input("n = "))
a = [randint(1,9) for i in range(n)]
print(a)
i = 0
while i<len(a):
    if a.count(a[i])>1:
        x = a[i]
        for _ in range(a.count(a[i])-1):
            a.remove(x)
    i += 1
print(a)


# In[26]:


#Array98
from random import randint
n = int(input("n = "))
a = [randint(1,9) for i in range(n)]
print(a)
i = 0
while i<len(a):
    if a.count(a[i])<3:
        x = a[i]
        for _ in range(a.count(a[i])):
            a.remove(x)
    else:
        i += 1
print("soni",len(a),'ta')
print(a)


# In[28]:


#Array99
from random import randint
n = int(input("n = "))
a = [randint(1,9) for i in range(n)]
print(a)
i = 0
while i<len(a):
    if a.count(a[i])>2:
        x = a[i]
        for _ in range(a.count(a[i])):
            a.remove(x)
    else:
        i += 1
print("soni",len(a),'ta')
print(a)


# In[31]:


#Array100
from random import randint
n = int(input("n = "))
a = [randint(1,9) for i in range(n)]
print(a)
i = 0
while i<len(a):
    if a.count(a[i])==2:
        x = a[i]
        for _ in range(a.count(a[i])):
            a.remove(x)
    else:
        i += 1
print("soni",len(a),'ta')
print(a)


# In[33]:


#Array101
from random import randint
n = int(input("n = "))
k = int(input("k = "))
a = [randint(1,9) for i in range(n)]
print(a)
a.insert(k-1,0)
print(a)   


# In[34]:


#Array102
from random import randint
n = int(input("n = "))
k = int(input("k = "))
a = [randint(1,9) for i in range(n)]
print(a)
a.insert(k+1,0)
print(a)  


# In[40]:


#Array103
from random import randint
n = int(input("n = "))
a = [randint(1,9) for i in range(n)]
print(a)
a.insert(a.index(min(a)),0)
a.insert(a.index(max(a))+1,0)
print(a)  


# In[19]:


#Array104
from random import randint
n = int(input("n = "))
k = int(input("k = "))
m = int(input("m = "))
a = [randint(1,9) for i in range(n)]
print(a)
i = 0
while i<len(a):
    if a[i]==k:
        for j in range(m):
            a.insert(i,0)
        i+=m
    i += 1
print(a)


# In[45]:


#Array105
from random import randint
n = int(input("n = "))
k = int(input("k = "))
m = int(input("m = "))
a = [randint(1,9) for i in range(n)]
print(a)
for i in range(m):
    a.insert(k+1,0)
print(a)


# In[49]:


#Array106
from random import randint
n = int(input("n = "))
a = [randint(1,9) for i in range(n)]
print(a)
for i in range(0,len(a),2):
    a.append(a[i])
print(a)


# In[50]:


#Array107
from random import randint
n = int(input("n = "))
a = [randint(1,9) for i in range(n)]
print(a)
for i in range(1,len(a),2):
    a.append(a[i])
    a.append(a[i])
print(a)


# In[68]:


#Array108
from random import randint
n = int(input("n = "))
a = [randint(-6,9) for i in range(n)]  
print(a)
i = 0
while i<len(a):
    if a[i]>0:
        a.insert(i,0)
        i += 2
    else:
        i += 1
print(a)


# In[65]:


#Array109
from random import randint
n = int(input("n = "))
a = [randint(-6,9) for i in range(n)] 
print(a)
i = 0
while i<len(a):
    if a[i]<0:
        a.insert(i+1,0)
    i += 1
print(a)


# In[69]:


#Array110
from random import randint
n = int(input("n = "))
a = [randint(1,9) for i in range(n)]
print(a)
for i in range(len(a)):
    if a[i]%2==0:
        a.append(a[i])
print(a)


# In[70]:


#Array111
from random import randint
n = int(input("n = "))
a = [randint(1,9) for i in range(n)]
print(a)
for i in range(len(a)):
    if a[i]%2==1:
        a.append(a[i])
        a.append(a[i])
print(a)


# ### 6.Massivni saralash

# In[21]:


#Array112 (Pufaksimon saralash) 1-usul
from random import randint
n = int(input("n = "))
a = [randint(1,9) for i in range(n)]
print(a)
for _ in range(n):
    for i in range(n-1):
        if a[i]>a[i+1]:
            a[i],a[i+1] = a[i+1],a[i]
print(a)

#Array112 (Pufaksimon saralash) 2-usul
from random import randint
n = int(input("n = "))
a = [randint(1,9) for i in range(n)]
print(a)
for i in range(n-1):
    for j in range(n-1-i):
        if a[j]>a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
print(a)


# In[26]:


#Array113 Oddiy tanlash(selection sort)
from random import randint
n = int(input("n = "))
a = [randint(-5,5) for i in range(n)]  
print(a)
for i in range(n):
    mini = a[i]
    index = i
    for j in range(i+1,n):
        if mini>a[j]:
            mini = a[j]
            index = j
    a[i],a[index] = a[index],a[i]
print(a)


# In[54]:


#Array114 Oddiy qo'shish(insertion sort)
from random import randint
n = int(input("n = "))
a = [randint(-5,5) for i in range(n)]  
print(a)
for i in range(n):
    for j in range(n):
        if a[i]<a[j]:
            a.insert(j,a.pop(i))
print(a)


# In[1]:


#Array115 1-usul
from random import randint
n = int(input("n = "))
a = [randint(-5,10) for i in range(n)]
b = a.copy()
print(a)
index = list(range(n))
for _ in range(n):
    for i in range(n-1):
        if b[i]>b[i+1]:
            b[i],b[i+1] = b[i+1],b[i]
            index[i],index[i+1] = index[i+1],index[i]
print(a)
print(index)

#Array115 2-usul
from random import randint
n = int(input("n = "))
a = [randint(1,9) for i in range(n)]
print(a)
b = [i for i in range(n)]
print(b)
for i in range(1,n):
    for j in range(0,n-i):
        if a[b[j]]>a[b[j+1]]:
            b[j],b[j+1] = b[j+1],b[j]     
print(b)
print(a)


# ### 7.Butun sonlar seriyasi

# In[32]:


#Array116
from random import randint
n = int(input("n = "))
a = [randint(0,2) for i in range(n)]
print(a)

b = [] #Seriyalar soni
c = [] #Seriyani tashkil qilgan elementlar
x = a[0]

b.append(1)
c.append(x)

k = 0
for i in range(1,n):
    if a[i]==x:
        b[k] += 1
    else:
        x = a[i]
        b.append(1)
        c.append(x)
        k += 1

print("B =",b)
print("C =",c)


# In[10]:


#Array117
from random import randint
n = int(input("n = "))
a = [randint(1,5) for i in range(n)]
print(a)
a.insert(0,0)
i = 1
while i<len(a)-1:
    if a[i]!=a[i+1]:
        a.insert(i+1,0)
        i += 1
    i += 1
print(a)


# In[15]:


#Array118
from random import randint
n = int(input("n = "))
a = [randint(1,5) for i in range(n)]
print(a)
i = 0
while i<len(a)-1:
    if a[i]!=a[i+1]:
        a.insert(i+1,0)
        i += 1
    i += 1
a.append(0)
print(a)


# In[18]:


#Array119
from random import randint
n = int(input("n = "))
a = [randint(1,5) for i in range(n)]
print(a)
i = 0
while i<len(a)-1:
    if a[i]!=a[i+1]:
        a.insert(i+1,a[i])
        i += 1
    i += 1
a.append(a[i])
print(a)


# In[39]:


#Array120 
from random import randint
n = int(input("n = "))
a = [randint(1,5) for i in range(n)]
print(a)
i = 0
while i<len(a)-1:
    if a[i]!=a[i+1]:
        a.pop(i)
        continue
    i += 1
a.pop()
print(a)


# In[23]:


#Array121 1-usul
from random import randint
n = int(input("n = "))
k = int(input("k = "))
a = [randint(1,5) for i in range(n)]
print(a)
i = 0
seriya = 1
sanoq = 1
while i<len(a)-1:
    if a[i]!=a[i+1]:
        seriya += 1
        if seriya==k+1:
            for _ in range(sanoq):
                a.insert(i,a[i])
            break
        sanoq = 1
    elif a[i]==a[i+1]:
        sanoq += 1 
    i += 1
print(a)

#Array121 2-usul
from random import randint
n = int(input("n = "))
k = int(input("k = "))
a = [randint(3,5) for i in range(n)]
print(a)

x = a[0]
b = [x] #seriya qiymati
c = [1] #seriyalar soni
h = 0
for i in range(1,n):
    if a[i]==x:
        c[h] += 1
    else:
        x = a[i]
        b.append(x)
        c.append(1)
        h += 1
c[k-1] *= 2
a.clear()
for i in range(len(c)):
    for j in range(c[i]):
        a.append(b[i])
print(a)


# In[18]:


#Array122 1-usul
from random import randint
n = int(input("n = "))
k = int(input("k = "))
a = [randint(1,5) for i in range(n)]
print(a)
i = 0
seriya = 1
sanoq = 1
index = 0
while i<len(a)-1:
    if a[i]!=a[i+1]:
        seriya += 1
        if seriya==k+1:
            for _ in range(sanoq):
                del a[index]
            break
        index = i+1
        sanoq = 1
    elif a[i]==a[i+1]:
        sanoq += 1 
    i += 1
    
if a[-1]==a[-2] and seriya == k:
    for _ in range(sanoq):
        del a[index]
print(a)

#Array122 2-usul
from random import randint
n = int(input("n = "))
k = int(input("k = "))
a = [randint(3,5) for i in range(n)]
print(a)

x = a[0]
b = [x] #seriya qiymati
c = [1] #seriyalar soni
h = 0
for i in range(1,n):
    if a[i]==x:
        c[h] += 1
    else:
        x = a[i]
        b.append(x)
        c.append(1)
        h += 1
del b[k-1]
del c[k-1]
a.clear()
for i in range(len(c)):
    for j in range(c[i]):
        a.append(b[i])
print(a)


# In[17]:


#Array123 1-usul
n = int(input('n='))
k = int(input('k='))
a = [randint(1,3) for i in range(n)]
print(a)
k-=1
flag = True
son = a[0]
i = 0
while i<len(a):
    if a[i]!=son:
        son = a[i]
        if flag:
            bir_massiv = a[:i]
            bir_oxiri = i
            flag = False
        k -= 1
    if k==0:
        k_boshi = i
        while a[i] == son:
            k_oxiri = i
            i += 1
            if i>len(a)-1:
                break
        k_massiv = a[k_boshi:k_oxiri+1]
        
        del a[k_boshi:k_oxiri+1]
        for i in range(len(bir_massiv)):
            a.insert(k_boshi,bir_massiv[i])
        
        del a[:bir_oxiri]
        for i in range(len(k_massiv)):
            a.insert(0,k_massiv[i])
        break
    i += 1
print(a)

#Array123 2-usul
from random import randint
n = int(input("n = "))
k = int(input("k = "))
a = [randint(3,5) for i in range(n)]
print(a)

x = a[0]
b = [x] #seriya qiymati
c = [1] #seriyalar soni
h = 0
for i in range(1,n):
    if a[i]==x:
        c[h] += 1
    else:
        x = a[i]
        b.append(x)
        c.append(1)
        h += 1
b[k-1],b[0] = b[0],b[k-1]
c[k-1],c[0] = c[0],c[k-1]
a.clear()
for i in range(len(c)):
    for j in range(c[i]):
        a.append(b[i])
print(a)


# In[16]:


#Array124 1-usul
from random import randint
n = int(input("n = "))
k = int(input("k = "))
a = [randint(3,5) for i in range(n)]
print(a)

x = a[0]
b = [x] #seriya qiymati
c = [1] #seriyalar soni
h = 0
for i in range(1,n):
    if a[i]==x:
        c[h] += 1
    else:
        x = a[i]
        b.append(x)
        c.append(1)
        h += 1
a.clear()
if k<len(c):
    for j in range(len(c)-1):
        if j!=k-1:
            for _ in range(c[j]):
                a.append(b[j])
else:
    for j in range(len(c)):
        if j!=k-1:
            for _ in range(c[j]):
                a.append(b[j])
if k<len(c):
    for _ in range(c[k-1]):
        a.append(b[k-1])
    for _ in range(c[-1]):
        a.insert(sum(c[:k-1]),b[-1])
print(a)

#Array124 2-usul
from random import randint
n = int(input("n = "))
k = int(input("k = "))
a = [randint(3,5) for i in range(n)]
print(a)

x = a[0]
b = [x] #seriya qiymati
c = [1] #seriyalar soni
h = 0
for i in range(1,n):
    if a[i]==x:
        c[h] += 1
    else:
        x = a[i]
        b.append(x)
        c.append(1)
        h += 1
b[k-1],b[-1] = b[-1],b[k-1]
c[k-1],c[-1] = c[-1],c[k-1]
a.clear()
for i in range(len(c)):
    for j in range(c[i]):
        a.append(b[i])
print(a)


# In[21]:


#Array125
from random import randint
n = int(input('n='))
k = int(input('k='))
a = [randint(1,3) for i in range(n)]
print(a)
x = a[0]
b = [x] #seriya qiymati
c = [1] #seriya uzunligi
m = 0
for i in range(1,len(a)):
    if x==a[i]:
        c[m] += 1
    else:
        x = a[i]
        b.append(x)
        c.append(1)
        m += 1
a.clear()
for i in range(len(b)):
    if c[i] < k:
        a.append(0)
    else:
        for _ in range(c[i]):
            a.append(b[i])  
print(a)


# In[23]:


#Array126
from random import randint
n = int(input('n='))
k = int(input('k='))
a = [randint(1,3) for i in range(n)]
print(a)
x = a[0]
b = [x] #seriya qiymati
c = [1] #seriya uzunligi
m = 0
for i in range(1,len(a)):
    if x==a[i]:
        c[m] += 1
    else:
        x = a[i]
        b.append(x)
        c.append(1)
        m += 1
a.clear()
for i in range(len(b)):
    if c[i] == k:
        a.append(0)
    else:
        for _ in range(c[i]):
            a.append(b[i])  
print(a)


# In[28]:


#Array127
from random import randint
n = int(input('n='))
k = int(input('k='))
a = [randint(1,3) for i in range(n)]
print(a)
x = a[0]
b = [x] #seriya qiymati
c = [1] #seriya uzunligi
m = 0
for i in range(1,len(a)):
    if x==a[i]:
        c[m] += 1
    else:
        x = a[i]
        b.append(x)
        c.append(1)
        m += 1
a.clear()
for i in range(len(b)):
    if c[i] > k:
        a.append(0)
    else:
        for _ in range(c[i]):
            a.append(b[i])  
print(a)


# In[15]:


#Array128 1-usul
from random import randint
n = int(input('n='))
a = [randint(1,3) for i in range(n)]
print(a)
x = a[0]
b = [x] #seriya qiymati
c = [1] #seriya uzunligi
m = 0
for i in range(1,len(a)):
    if x==a[i]:
        c[m] += 1
    else:
        x = a[i]
        b.append(x)
        c.append(1)
        m += 1
maxi = max(c)
index = 1
for i in range(len(c)):
    if c[i] == maxi:
        a.insert(index-1,b[i])
        break
    else:
        index += c[i]
print(a)

#Array128 2-usul
from random import randint
n = int(input("n = "))
a = [randint(3,5) for i in range(n)]
print(a)

x = a[0]
b = [x] #seriya qiymati
c = [1] #seriyalar soni
h = 0
for i in range(1,n):
    if a[i]==x:
        c[h] += 1
    else:
        x = a[i]
        b.append(x)
        c.append(1)
        h += 1
maxi = b.index(max(b))
c[maxi] += 1

a.clear()
for i in range(len(c)):
    for j in range(c[i]):
        a.append(b[i])
print(a)


# In[14]:


#Array129 1-usul
from random import randint
n = int(input('n='))
a = [randint(1,3) for i in range(n)]
print(a)
x = a[0]
b = [x] #seriya qiymati
c = [1] #seriya uzunligi
m = 0
for i in range(1,len(a)):
    if x==a[i]:
        c[m] += 1
    else:
        x = a[i]
        b.append(x)
        c.append(1)
        m += 1
maxi = max(c)
s = 0
for i in range(len(c)):
    if maxi==c[i]:
        index = i
for i in range(len(c)):
    if index==i:
        break
    else:
        s+=c[i]
a.insert(s,b[index])
print(a)

#Array129 2-usul
from random import randint
n = int(input("n = "))
a = [randint(3,5) for i in range(n)]
print(a)

x = a[0]
b = [x] #seriya qiymati
c = [1] #seriyalar soni
h = 0
for i in range(1,n):
    if a[i]==x:
        c[h] += 1
    else:
        x = a[i]
        b.append(x)
        c.append(1)
        h += 1
maxi = max(b)
for i in range(len(b)):
    if maxi==b[i]:
        index = i
c[index] += 1
a.clear()
for i in range(len(c)):
    for j in range(c[i]):
        a.append(b[i])
print(a)


# In[43]:


#Array130
from random import randint
n = int(input('n='))
a = [randint(1,3) for i in range(n)]
print(a)
x = a[0]
b = [x] #seriya qiymati
c = [1] #seriya uzunligi
m = 0
for i in range(1,len(a)):
    if x==a[i]:
        c[m] += 1
    else:
        x = a[i]
        b.append(x)
        c.append(1)
        m += 1
a.clear()
for i in range(len(b)):
    for _ in range(c[i]+1):
            a.append(b[i])  
print(a)


# ### 8.Tekislikda nuqtalar to'plami

# In[96]:


#Array131
from random import randint
n = int(input("n = "))
a = [randint(1,5) for i in range(n*2)]
# Massiv x va y lardan iborat
# Ya'ni a[0]-> x ,a[1]-> y ,a[2]->x ...  h-k
b = [2,5]
print(a)
for i in range(0,2*n,2):
    x = ((a[i]-b[0])**2 + (a[i+1]-b[1])**2)**0.5
    if i==0:
        d = x
        index1 = i
        index2 = i+1
    elif d > x:
        d = x
        index1 = i
        index2 = i+1
print(d,index1,index2)


# In[102]:


#Array132
from random import randint
n = int(input("n = "))
a = [randint(-6,6) for i in range(n*2)]
# Massiv x va y lardan iborat
# Ya'ni a[0]-> x ,a[1]-> y ,a[2]->x ...  h-k
print(a)
flag = True
index1 = 0
index2 = 0
for i in range(0,2*n,2):
    x = ((a[i]-0)**2 + (a[i+1]-0)**2)**0.5
    if a[i]<0 and a[i+1]>0 and flag:
        d = x
        index1 = i
        index2 = i+1
        flag = False
    elif a[i]<0 and a[i+1]>0 and d<x:
        d = x
        index1 = i
        index2 = i+1
if index1 or index2:
    print(d,index1,index2)
else:
    print(index1,index2)


# In[103]:


#Array133
from random import randint
n = int(input("n = "))
a = [randint(-6,6) for i in range(n*2)]
# Massiv x va y lardan iborat
# Ya'ni a[0]-> x ,a[1]-> y ,a[2]->x ...  h-k
print(a)
flag = True
index1 = 0
index2 = 0
for i in range(0,2*n,2):
    x = ((a[i]-0)**2 + (a[i+1]-0)**2)**0.5
    if ((a[i]<0 and a[i+1]<0) or (a[i]>0 and a[i+1]>0)) and flag:
        d = x
        index1 = i
        index2 = i+1
        flag = False
    elif ((a[i]<0 and a[i+1]<0) or (a[i]>0 and a[i+1]>0)) and d<x:
        d = x
        index1 = i
        index2 = i+1
if index1 or index2:
    print(d,index1,index2)
else:
    print(index1,index2)


# In[114]:


#Array134
from random import randint
n = int(input("n = "))
a = [randint(-2,6) for i in range(n*2)]
# Massiv x va y lardan iborat
# Ya'ni a[0]-> x ,a[1]-> y ,a[2]->x ...  h-k
print(a)
for i in range(0,2*(n-1),2):
    x = ((a[i]-a[i+2])**2 + (a[i+1]-a[i+3])**2)**0.5
    if i==0:
        d = x
        index1 = i
    elif d<x:
        d = x
        index = i
print("Masofa:",d)
print("\nx1 =",a[index],"\nx2 =",a[index+1],"\nx3 =",a[index+2],"\nx4 =",a[index+3])


# In[137]:


#Array135
from random import randint
n1 = int(input("N1 = "))
n2 = int(input("N2 = "))
a = [randint(-2,6) for i in range(n1*2)]
b = [randint(-2,6) for i in range(n2*2)]
# Massiv x va y lardan iborat
# Ya'ni a[0]-> x ,a[1]-> y ,a[2]->x ...  h-k b massiv ham shu tartibda
print(a)
print(b)
for i in range(0,2*n1,2):
    d = 0
    for j in range(0,2*n2,2):
        x = ((a[i]-b[j])**2 + (a[i+1]-b[j+1])**2)**0.5
        if j == 0:
            d = x
            index1 = i
            index2 = j
        elif d > x:
            d = x
            index1 = i
            index2 = j
    print("orasidagi masofa",d)
    print("qiymatlari:",a[index1],a[index1+1],b[index2],b[index2+1])


# In[54]:


#Array136
from random import randint
n = int(input("n = "))
a = [randint(-2,6) for i in range(n*2)]
# Massiv x va y lardan iborat
# Ya'ni a[0]-> x ,a[1]-> y ,a[2]->x ...  h-k
print(a)
flag = True
for i in range(0,2*n,2):
    s = 0
    for j in range(0,2*n,2):
        if i != j:
            s += ((a[i]-a[j])**2 + (a[i+1]-a[j+1])**2)**0.5
    if flag:
        k = s
        index = i
        flag = False
    elif k > s:
        k = s
        index = i
print(k,index,index+1)   


# In[11]:


#Array137
from random import randint
n = int(input("n = "))
a = [randint(-2,6) for i in range(n*2)]
# Massiv x va y lardan iborat
# Ya'ni a[0]-> x ,a[1]-> y ,a[2]-> x ...  h-k
print(a)
flag = True
for i in range(0,2*n,2):
    for j in range(0,2*n,2):
        for k in range(0,2*n,2):
            if i != j and j != k and i!=k:
                x = ((a[i]-a[j])**2 + (a[i+1]-a[j+1])**2)**0.5
                y = ((a[i]-a[k])**2 + (a[i+1]-a[k+1])**2)**0.5 
                z = ((a[j]-a[k])**2 + (a[j+1]-a[k+1])**2)**0.5 
                m = x + y + z
                if flag:
                    p = m
                    index1 = i
                    index2 = j
                    index3 = k
                    flag = False
                elif p < m:
                    p = m
                    index1 = i
                    index2 = j
                    index3 = k
print("Perimetr =",p)
print(index1,index1+1,index2,index2+1,index3,index3+1) 


# In[8]:


#Array138
from random import randint
n = int(input("n = "))
x = [randint(-2,6) for i in range(n)]
y = [randint(-2,6) for i in range(n)]
print(x)
print(y)
flag = True
for i in range(n):
    for j in range(n):
        for k in range(n):
            if i!=j and j!=k and i!=k:
                a = ((x[i]-x[j])**2 + (y[i]-y[j])**2)**0.5
                b = ((x[i]-x[k])**2 + (y[i]-y[k])**2)**0.5 
                c = ((x[j]-x[k])**2 + (y[j]-y[k])**2)**0.5 
                m = a + b + c
                if flag:
                    p = m
                    index1 = i
                    index2 = j
                    index3 = k
                    flag = False
                elif p > m:
                    p = m
                    index1 = i
                    index2 = j
                    index3 = k
print("Perimetr =",p)
print("Indexlari:",index1,index2,index3) 


# In[8]:


#Array139
from random import randint
n = int(input("n = "))
a = [randint(-10,10) for i in range(2*n)]
# Massiv x va y lardan iborat
# Ya'ni a[0]-> x ,a[1]-> y ,a[2]->x ...  h-k
print(a)
for j in range(2*n):
    for i in range(0,n+2,2):
        if (a[i]>a[i+2]) or (a[i]==a[i+2] and a[i+1]>a[i+3]):
            a[i],a[i+1],a[i+2],a[i+3] = a[i+2],a[i+3],a[i],a[i+1]
print(a)


# In[20]:


#Array140
from random import randint
n = int(input("n = "))
a = [randint(-10,10) for i in range(2*n)]
# Massiv x va y lardan iborat
# Ya'ni a[0]-> x ,a[1]-> y ,a[2]->x ...  h-k
print(a)
for _ in range(2*n):
    for i in range(0,n+2,2):
        x1,y1 = a[i],a[i+1]
        x2,y2 = a[i+2],a[i+3]
        if (x1+y1 < x2+y2 or x1+y1 == x2+y2) and x1 < x2:
             a[i],a[i+1],a[i+2],a[i+3] = a[i+2],a[i+3],a[i],a[i+1]
print(a)

