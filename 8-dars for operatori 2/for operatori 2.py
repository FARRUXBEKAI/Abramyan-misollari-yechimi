#!/usr/bin/env python
# coding: utf-8

# # 04/03/2022
# 
# # Python asoslari
# 
# # 8-dars: for sikl operatori_2 ning misollarini yechish 
# 
# # Muallif: Farrux Sotivoldiyev

# In[1]:


# 1.  n natural soni berilgan. 1 dan n gacha bo’lgan sonlarning yig'indisini 
# hisoblovchi dastur tuzing. 
# Kiritish: 7
# 1 2 3 4 5 6 7
# Natural sonlarning yig'indisi: 28

n = int(input("n = "))

s = 0
for i in range(1,n+1):
    s += i
print(s)


# In[1]:


# 2.  1 - a + a^2 - a^3 +.....(-1)^n * a^n

n = int(input("n = "))
a = int(input("a = "))

s = 0
for i in range(n): #0,1,2,3,4   n = 5
    s += (-1)**i * a**i
print("Summa:",s)
    


# In[6]:


# 3. Kiritilgan sonning tub yoki tub emasligini aniqlovchi dastur tuzing. 
# Kiritish: 47
# Chiqarish: Tub

n = int(input("n = "))

for i in range(1,n+1):
    k = 0
    for j in range(2,i):
        if i%j==0:
            k += 1
if k > 0:
    print("Murakkab")
else:
    print("Tub")


# In[18]:


# 4. 1 dan n gacha bo’lgan sonlar oralig’idagi tub sonlarni va ularning sonini 
# ekranga chiqaruvchi dastur tuzing 
# Kiritish: 100
# Chiqarish:
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
# 1 dan 100 gacha bo'lgan tub sonlarning umumiy soni: 25

n = int(input("n = "))

sana = 0
for i in range(1,n+1):
    k = 0
    for j in range(2,i):
        if i%j==0:
            k += 1
            
            break
    if k==0:
        sana += 1
        print(i,end=' ')
print("\nTub sonlar:",sana)


# In[19]:


# 5. n soni berilgan. n faktorialni hisoblovchi dastur tuzing ( n!=1*2*3*…*n ).
# Kiritish: 5
# Chiqarish: 120 

n = int(input("n = "))

p = 1
for i in range(1,n+1):
    p *= i
print(p)


# In[7]:


# 6. n soni berilgan. n gacha bo’lgan tub sonlarning oxirgisini aniqlovchi dastur 
# tuzing. 
# Kiritish: 50
# Chiqarish: 47

n = int(input("n = "))

for i in range(n,1,-1):
    k = 0
    for j in range(1,i+1):
        if i%j==0:
            k += 1
    if k == 2:
        print(i)
        break


# In[13]:


# 7. Ikki sonning eng katta umumiy bo'linuvchisini (EKUB) aniqlovchi dastur tuzing.
# Kiritish: 45
#          135
# Chiqarish: 45

a = int(input("a = "))
b = int(input("b = "))

if a > b:
    oxir = a
else:
    oxir = b
    
for i in range(oxir):
    if a==b:
        print(a)
        break
    elif a>b:
        a -= b
    else:
        b -= a


# In[101]:


# 8.  Berilgan sonning raqamlari yig'indisini aniqlovchi dastur tuzing.
# Kiritish: 147852 
# Chiqarish: 27

n = int(input("n = "))

s = 0 
for i in str(n):
    s += int(i)
print(s)


# In[1]:


# 9.   n soni berilgan. 
# (1) + (1 + 2) + (1 + 2 + 3) + (1 + 2 + 3 + 4) + ... + (1 + 2 + 3 +…n) ni 
# hisoblovchi dastur tuzing.
# Kiritish: 3 
# Chiqarish: 10

# 1-usul

n = int(input("n = "))

s = 0
for i in range(1,n+1):
    for j in range(1,i+1):
        s += j
print(s)

# 2-usul

n = int(input("n = "))
s = 0
p = 0
for i in range(1,n+1):
    p += i
    s += p
print(s)


# In[100]:


# 10. Oxiri -1 bilan tugovchi sonlar ketma-ketligi berilgan, shu ketma-ketlikda
# nechta musbat son borligini va Maksimum, minimum qiymatlarini topuvchi dastur
# tuzing?

k = 0
maxi = -float('inf')
mini = float('inf')

while True:
    n = int(input("n = "))
    
    if n == -1:
        break
    elif n>0:
        k += 1
        
    if mini > n:
        mini = n
    elif maxi < n:
        maxi = n
print(f"{k} ta musbat son\nmax = {maxi}\nmin = {mini}")


# In[99]:


# 11. n soni berilgan. Berilgan songacha bo’lgan murakkab sonlarni ekranga 
# chiqaruvchi dastur tuzing. 
# Kiritish: 25
# Chiqarish: 4 6 8 9 10 12 14 15 16 18 20 21 22 24 25

n = int(input("n = "))

for i in range(1,n+1):
    k = 0
    for j in range(2,i):
        if i%j==0:
            k += 1
    if k>0:
        print(i,end=' ')


# In[98]:


# 12. n soni berilgan. Tomoni n ga teng bo’lgan kvadrat yasang. Kvadratni 
#  << # >> belgisi bilan bosib chiqaruvchi dastur tuzing.  
#Kiritish: 4
#Chiqarish:
# # # #
# # # #
# # # #
# # # # 

n = int(input("n = "))

for i in range(n):
    for j in range(n):
        print("#",end = ' ')
    print()


# In[23]:


# 13. 1 dan n gacha vertikal ravishda ko'paytirish jadvalini ko'rsatuvchi dastur 
# yozing. 
# Kiritish: 5
# Chiqarish:  
# 1x1 = 1    2x1 = 2      3x1 = 3     4x1 = 4     5x1 = 5
# 1x2 = 2    2x2 = 4      3x2 = 6     4x2 = 8     5x2 = 10
# 1x3 = 3    2x3 = 6      3x3 = 9     4x3 = 12    5x3 = 15
# 1x4 = 4    2x4 = 8      3x4 = 12    4x4 = 16    5x4 = 20
# 1x5 = 5    2x5 = 10     3x5 = 15    4x5 = 20    5x5 = 25
# 1x6 = 6    2x6 = 12.    3x6 = 18    4x6 = 24    5x6 = 30
# 1x7 = 7    2x7 = 14     3x7 = 21    4x7 = 28    5x7 = 35
# 1x8 = 8    2x8 = 16     3x8 = 24    4x8 = 32    5x8 = 40
# 1x9 = 9    2x9 = 18     3x9 = 27    4x9 = 36    5x9 = 45
# 1x10 = 10  2x10 = 20    3x10 = 30   4x10 = 40   5x10 = 50

n = int(input("n = "))

for i in range(1,n+1):
    for j in range(1,n+1):
        a = len("{j}x{i}={i*j}")
        print((f"{j}x{i}={i*j}"),end="\t")
    print()


# In[77]:


# 14. N musbat soni berilgan. Dastlabki N ta toq sonlarni ekranga chiqaruvchi va 
# ularning yig’indisini aniqlovchi dastur tuzing.
# Kiritish: 5 
# Chiqarish: 1 3 5 7 9  .........  25

n = int(input("n = "))

s = 0 
for i in range(1,2*n,2):
    s += i
    print(i,end=" ")
print("\nsumma:",s)


# In[76]:


# 15. N musbat soni berilgan. Dastlabki Nta juft sonlarni ekranga chiqaruvchi 
# va ularning yig’indisini aniqlovchi dastur tuzing.
# Kiritish: 5 
# Chiqarish: 2 4 6 8 10       Yeg'indisi = 30 

n = int(input("n = "))

s = 0
for i in range(2,2*n+1,2):
    s += i
    print(i,end=" ")
print("\nsumma:",s)


# In[24]:


# 16. 1 + 11 + 111 + 1111 + 11111 + …+ n qatorlarining yig'indisini aniqlovchi dastur tuzing. 
# Kiritish: 5
# Chiqarish: 12345

n = int(input("n = "))

k = 1
s = 0
for i in range(1,n+1):
    s += k
    k = (k*10)+1
print(s)


# In[73]:


# 17. Fibonachchi sonlarining dastlabki n tasini ekranga chiqaruvchi dastur tuzing.
# Kiritish: 10
# Chiqarish: 1 1 2 3 5 8 13 21 34 55

n = int(input("n = "))

f1 = 1
f2 = 1
for i in range(n):
    print(f1,end=" ")
    f2 = f1 + f2
    f1 = f2 - f1


# In[5]:


# 18. S musbat soni berilgan. Ushbu sonni ikki tub son yig’indisi ko’rinishida 
# ifodalash mumkinligini aniqlovchi dastur tuzing. Shu sonlarni ekranga chiqaring.
# Kiritish: 20
# Chiqarish: Mumkin  3 va 17

n = int(input("n = "))

for i in range(2,n):
    k = 0
    for j in range(1,i+1):
        if i % j == 0:
            k += 1
    if k == 2:
        a = n - i
        l = 0
        for h in range(1,a+1):
            if a % h == 0:
                l += 1
        if l == 2:
            print("Mumkin",i,a,end=" ")
            break
            
else:
    print("Mumkin emas")


# In[2]:


# 19. n musbat soni berilgan. Yulduzcha yordamida to'g'ri burchakli uchburchak 
# shaklini  ekranga chiqaruvchi dastur tuzing. 
# Kiritish: 5 
# Chiqarish:
# *
# **
# ***
# ****
# *****

n = int(input("n = "))

for i in range(1,n+1):
    print(i * '*')


# In[70]:


# 20. n musbat soni berilgan. Ekranga quyidagi “sonli uchburchak”ni chiqaruvchi 
# dastur tuzing. 
# Kiritish: 5
# Chiqarish: 
# 1
# 12
# 123
# 1234
# 12345

n = int(input("n = "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end='')
    print()


# In[69]:


# 21. n musbat soni berilgan. Ekranga quyidagi “sonli uchburchak”ni chiqaruvchi 
# dastur tuzing. 
# Kiritish: 5
# Chiqarish:
# 1                                                                                                             
# 22                                                                                                      
# 333                                                                                                         
# 4444                                                                                                         
# 55555 

n = int(input("n = "))

for i in range(1,n+1):
    print(f"{i}"*i)


# In[26]:


# 22. n musbat soni berilgan. Ekranga quyidagi “sonli uchburchak”ni chiqaruvchi 
# dastur tuzing. 
# Kiritish: 5
# Chiqarish:                                                                                   
# 1                                                                                  
# 2 3                                                                                                         
# 4 5 6                                                                                             
# 7 8 9 10 
# 11 12 13 14 15

n = int(input('n='))

k = 1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(k,end=" ")
        k += 1
    print()


# In[28]:


# 23. n musbat soni berilgan. Ekranga quyidagi “sonli piramida”ni chiqaruvchi 
# dastur tuzing. 
# Kiritish: 4
# Chiqarish:
#    1                                                          
#   2 3                                                        
#  4 5 6                                                             
# 7 8 9 10 

n = int(input('n='))

k = 1
for i in range(1,n+1):
    print(end=' '*(n+1-i))
    for j in range(1,i+1):
        print(k, end=' ')
        k+=1
    print()


# In[27]:


# 24. n musbat soni berilgan. Ekranga n qatordan iborat “yulduzchali piramida” 
# ni chiqaruvchi dastur tuzing:
# Kiritish: 5
# Chiqarish:                                                
#        *                                                              
#       * *                                                             
#      * * *                                                            
#     * * * *                                                           
#    * * * * *

n = int(input("n = "))

k = 1
for i in range(1,n+1):
    print(end=" "*(n+1-i))
    for j in range(1,i+1):
        print("*",end=" ")
        k += 1
    print()


# In[35]:


# 25. n musbat soni berilgan. Ekranga quyidagi “sonli piramida”ni chiqaruvchi 
# dastur tuzing.
# Kiritish: 5
# Chiqarish:                                              
#        1                                                              
#       2 2                                                             
#      3 3 3                                                            
#     4 4 4 4                                                           
#    5 5 5 5 5 

n = int(input("n = "))

k = 1
for i in range(1,n+1):
    print(end=" "*(n+1-i) )
    for j in range(1,i+1):
        print(k,end=" ")
    print()
    k += 1


# In[78]:


# 26. n musbat soni berilgan. Ekranga quyidagi toq qatorli “sonli piramida”ni 
# chiqaruvchi dastur tuzing.
# Kiritish: 5
# Chiqarish:                                                             
#    *                                                                  
#   ***                                                                 
#  *****                                                                
# ******* 

n = int(input("n = "))

k = 1
for i in range(1,2*n-2,2):
    print(end=" "*(n-k))
    for j in range(1):
        print("*"*i,end="")
        k += 1
    print()


# In[4]:


# 27. n musbat soni berilgan. Ekranga n qatorli Floyd uchburchagini chiqaruvchi 
# dastur tuzing.
# Kiritish: 5
# Chiqarish:                                             
# 1                                                                      
# 01                                                                     
# 101                                                                    
# 0101                                                              
# 10101

# 1-usul

n = int(input('n='))

for i in range(n):
    for j in range(i+1):
        print((i+j+1)%2,end="")
    print()

# 2-usul

for i in range(1,n+1):
    for j in range(i,0,-1):
        if j%2==1:
            print("1",end="")
        if j%2==0:
            print("0",end="")
    print()


# In[5]:


# 28. n musbat soni berilgan. Tomoni n ta yulduzchadan iborat bo’lgan romb shaklini 
# yasovchi dastur tuzing.
# Kiritish: 5
# Chiqarish:
                                                                       
#     *                                                                  
#    ***                                                                 
#   *****                                                                
#  *******                                                               
# *********                                                              
#  *******                                                               
#   *****                                                                
#    ***                                                                 
#     *

# 1-usul

n = int(input('n='))

for i in range(1,n+1):
    print(' '*(n-i),'*'*(2*i-1),end='\n')
for i in range(n-1,0,-1):
    print(' '*(n-i), '*'*(2*i-1),end='\n')

# 2-usul

n = int(input("n = "))

k = 1
for i in range(1,n+1):
    print(end=" "*(n-i))
    for j in range(1):
        print(k*"*",end=" ")
    k += 2
    print()
k-= 4  
for i in range(1,n+1):
    print(end=" "*i)
    for j in range(1):
        print(k*"*",end=" ")
    k -= 2
    print()


# In[7]:


# 29. n musbat soni berilgan. n-darajali Paskal uchburchagini piramida ko’rinishida 
# ekranga chiqaruvchi dastur tuzing.
# Kiritish: 5
# Chiqarish:                                  
#          1                                                            
#        1   1                                                          
#      1   2   1                                                        
#    1   3   3   1                                                    
#  1   4   6   4   1                          

# 1-usul

n = int(input("n = "))
for i in range(n):
    for j in range(n-i):
        print(' ',end="")
    for j in range(i+1):
        if j==0:
            c = 1
        else:
            c = c*(i+1-j)//j
        print(c,end=" ")
    print()
n = int(input("n = "))

# 2-usul funksiya bilan

def fak(x):
    if x>0:
        p = 1
        for i in range(1,x+1):
            p *= i
        return p
    elif x==0:
        return 1

for i in range(0,n):
    print(" "*(n-i),end="")
    for j in range(0,i+1):
        print(int(fak(i) / (fak(j) * fak(i-j))),end=" ")
    print()
        


# In[3]:


# 30. n musbat soni berilgan. Ekranga quyidagi “sonli piramida”ni chiqaruvchi dastur 
# tuzing.
# Kiritish: 5
# Chiqarish:
#         1                                                                  
#        121                                                                 
#       12321                                                                
#      1234321                                                               
#     123454321

n = int(input("n = "))

for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end="")
    for j in range(i-1,0,-1):
        print(j,end="")
    print()


# In[29]:


# 31.  n musbat soni berilgan. Ekranga quyidagi “sonli piramida”ni chiqaruvchi 
# dastur tuzing.
# Kiritish: 5
# Chiqarish:   
#       1                                                                  
#      232                                                                 
#     34543                                                                
#    4567654                                                               
#   567898765

n = int(input("n = "))

for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(i,2*i):
        print(j,end="")
    for j in range(2*i-2,i-1,-1):
        print(j,end="")
    print()


# In[68]:


# 32. n musbat soni berilgan. Quyidagi ko’rinishdagi kvadratni ekranga chiqaruvchi 
# dastur tuzing.
# Kiritish: 5
# Chiqarish:
# 0 1 2 3 4
# 1 0 1 2 3
# 2 1 0 1 2
# 3 2 1 0 1
# 4 3 2 1 0

# Kiritish: 8
# Chiqarish:                                                                                      
# 0 1 2 3 4 5 6 7                                                                                        
# 1 0 1 2 3 4 5 6                                                                                        
# 2 1 0 1 2 3 4 5                                                                                        
# 3 2 1 0 1 2 3 4                                                                                        
# 4 3 2 1 0 1 2 3                                                                                        
# 5 4 3 2 1 0 1 2                                                                                        
# 6 5 4 3 2 1 0 1                                                                                        
# 7 6 5 4 3 2 1 0 
#32
n = int(input("n = "))

for i in range(n):
    for j in range(i,0,-1):
        print(j,end=" ")
    for j in range(0,n-i):
        print(j,end=" ")
    print()


# In[1]:


# 33. O'nli sanoq sistemasidagi sonlarni ikkilik sanoq sistemasiga o’tkazib beruvchi 
# dastur tuzing. 
# Kiritish: 35
# Chiqarish: 10001122

n = int(input("n = "))

sonlar = ''
for i in range(n):
    if n%2 != n//2:
        sonlar += str(n % 2)
        n //= 2
a = int(sonlar[::-1]) 
print(a)


# In[3]:


# 34. O'nli sanoq sistemasidagi sonlarni sakkizlik sanoq sistemasiga o’tkazib 
# beruvchi dastur tuzing. 
# Kiritish: 15
# Chiqarish: 17

son = int(input("10 lik sanoq sistemasida son kiriting: "))

sonlar = ''
for i in range(son):                      
    if son % 8 != son // 8:
        k = son % 8
        sonlar += str(k)
        son //= 8
    else:
        break
print(int(sonlar[::-1]))


# In[67]:


# 35. Ikkilik sanoq sistemasidagi sonlarni o’nlik sanoq sistemasiga o’tkazib beruvchi dastur tuzing. 
# Kiritish: 1011
# Chiqarish: 11

son = int(input("n = "))

s = 0
k = len(str(son))-1
for i in str(son):
    s += int(i) * 2**k
    k -= 1
print("O'nlik sanoq sistemasida:",s,"ga teng")


# In[4]:


# Universal (10 - > x). O'nli sanoq sistemasidagi sonlarni boshqa bir sanoq sistemasiga o’tkazib 
# beruvchi dastur tuzing. 

son = int(input("10 lik sanoq sistemasida son kiriting: "))
sanoq = int(input("qaysi sanoq sistemasiga o'tkazasiz: "))

sonlar = ''
for i in range(son):                      
    if son % sanoq != son // sanoq:
        k = son % sanoq
        sonlar += str(k)
        son //= sanoq
    else:
        break
        
print(int(sonlar[::-1]))


# In[107]:


# Universal (x - > 10). O'nli sanoq sistemasidagi sonlarni boshqa bir sanoq sistemasiga o’tkazib 
# beruvchi dastur tuzing. 

sanoq = int(input("Qaysi sanoq sistemasida son kiritasiz: "))
son = int(input(f"{sanoq} lik sanoq sistemasida son kiriting: "))
s = 0
k = len(str(son)) - 1
for i in str(son):
    s += int(i) * sanoq**k
    k -= 1
print(s)


# In[1]:


# Universal (x - > x). O'nli sanoq sistemasidagi sonlarni boshqa bir sanoq sistemasiga o’tkazib 
# beruvchi dastur tuzing. 

sanoq = int(input("Qaysi sanoq sistemasida son kiritasiz: "))
sanoq2 = int(input("Qaysi sanoq sistemasiga o'tkazasiz: "))
son = int(input(f"{sanoq} lik sanoq sistemasida son kiriting: "))

if sanoq < 11 and sanoq2 < 11:
    s = 0
    k = len(str(son)) - 1
    for i in str(son):
        s += int(i) * sanoq**k
        k -= 1

    sonlar = ''
    for i in range(s):                      
        if s % sanoq2 != s // sanoq2:
            k = s % sanoq2
            sonlar += str(k)
            s //= sanoq2
        else:
            break
    print(int(sonlar[::-1]))
else:
    print("10 likdan kichik yoki 10 lik sanoq kiriting")

