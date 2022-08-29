#!/usr/bin/env python
# coding: utf-8

# # 24/09/2022
# 
# # Python asoslari
# 
# # 29-dars : OOP
# 
# # Muallif: Farrux Sotivoldiyev

# **` Talaba haqida Class yaratish. `**

# In[39]:


class Talaba:
    
    def __init__(self,ism,familya,talim_maskani,kurs,fakultet,yunalish,guruh,talim_turi,talim_shakli):
        self.talim_maskani = talim_maskani
        self.ismi = ism
        self.familyasi = familya
        self.kursi = kurs
        self.fakulteti = fakultet
        self.yunalishi = yunalish
        self.guruhi = guruh
        self.talim_turi = talim_turi
        self.talim_shakli = talim_shakli
        
    def talim_maskanini_ozgartir(self,maskan):
        self.talim_maskani = maskan
        
    def yuqori_kursga_otish(self):
        if self.kursi=='Siz bitirdingiz':
            self.kursi = 'Siz bitirdingiz'
        elif self.kursi < 4:
            self.kursi += 1
        else:
            self.kursi = 'Siz bitirdingiz'
        
    def kursdan_kursga_qolish(self):
        if self.kursi=='Siz bitirdingiz':
            self.kursi = "Siz bitirdingiz"
        else:
            self.kursi += 0
        
    def fakultetni_ozgartir(self,fakultetlar):
        self.fakulteti = fakultetlar
    
    def yunalishni_ozgartir(self,yunalishlar):
        self.yunalishi = yunalishlar
        
    def guruhni_uzgartir(self,guruhlar):
        self.guruhi = guruhlar
        
    def talim_turini_ozgartir(self,turi):
        self.talim_turi = turi
        
    def talim_shaklini_ozgartir(self,shakli):
        self.talim_shakli = shakli
        


# In[53]:


a = Talaba("TATUFF","Farruxbek","Sotivoldiyev",2,"TT va KT","Dasturiy injenering","653-20","Bakalavr","Kunduzgi")
b = Talaba("Moliya","Sherali","Vohobov",1,"Moliya","Bank ishi","220A-21","Magistr","Kechki")


# In[54]:


print(a.kursi)
a.kursdan_kursga_qolish()
print(a.kursi)


# In[55]:


print(a.kursi)
a.yuqori_kursga_otish()
print(a.kursi)


# In[56]:


print(a.fakulteti)
a.fakultetni_ozgartir("KIF")
print(a.fakulteti)


# In[57]:


print(a.yunalishi)
a.yunalishni_ozgartir("Axborot xavfsizligi")
print(a.yunalishi)


# In[58]:


print(a.guruhi)
a.guruhni_uzgartir("610-20")
print(a.guruhi)


# In[59]:


print(a.talim_turi)
a.talim_turini_ozgartir("Magistratura")
print(a.talim_turi)


# In[60]:


print(a.talim_shakli)
a.talim_shaklini_ozgartir("Sirtqi")
print(a.talim_shakli)


# ### Qo'shimcha.

# In[84]:


class Pul_birlik:
    umumiy_pul_birlik = 'Dollar'
    
    def __init__(self,pul):
        self.pul_birlik = pul
    
    def um_pul_bir_voz_kech1(self):
        ichki_pul_birlik = "So'm"
        self.umumiy_pul_birlik = ichki_pul_birlik
        
    def um_pul_bir_voz_kech2(self):
        self.umumiy_pul_birlik = self.pul_birlik


# In[85]:


a = Pul_birlik("Sum")
a.um_pul_bir_voz_kech1()
a.umumiy_pul_birlik


# In[86]:


a.um_pul_bir_voz_kech2()
a.umumiy_pul_birlik


# # Classga obyekt jo'natish

# In[15]:


class Futbolchi:
    def __init__(self,ism,familya,yosh,narx,ampula,team):
        self.__ismi = ism
        self.__familyasi = familya
        self.__yoshi = yosh
        self.__narxi = narx
        self.__ampulasi = ampula
        self.__jamoasi = team
    
    def get_info(self):
        return f"Ism: {self.__ismi}\nFamilyasi: {self.__familyasi}\nYoshi: {self.__yoshi}\nJamoasi: {self.__jamoasi}\nAmpulasi: {self.__ampulasi}"
    
    def get_tansfer_narx(self,new_team,transfer_narxi):
        self.__jamoasi = new_team
        self.__narxi = transfer_narxi
        
    def set_yoshi(self):
        self.__yoshi += 1 
        
    def get_ism(self):
        return self.__ismi
    
    def get_familya(self):
        return self.__familyasi
    
    def get_yosh(self):
        return self.__yoshi


# In[21]:


class UEFA:
    def __init__(self,ism,familya,yoshi,oltin_top_soni):
        self.__ism = ism
        self.__familya = familya
        self.__yoshi = yoshi
        self.__oltin_top_soni = oltin_top_soni
    
    def update_oltin_top_soni(self):
        self.__oltin_top_soni += 1
        
    def oltin_top_soni(self):
        return self.__oltin_top_soni
        
    def get_info(self):
        return f"Ism: {self.__ism.get_ism()}\nFamilyasi: {self.__familya.get_familya()}\nYoshi: {self.__yoshi.get_yosh()}\nOltin to'plar soni: {self.__oltin_top_soni}"


# In[22]:


ronaldu = Futbolchi("Cristiano","Ronaldu",18,3000000,"Hujumchi","MYU")
ronaldu2 = UEFA(ronaldu,ronaldu,ronaldu,5)


# In[23]:


print(ronaldu2.get_info())


# In[24]:


print(ronaldu.get_info())


# # Voris olish

# In[48]:


class Hayvon:
    def __init__(self,nomi,jinsi):
        self.nomi = nomi
        self.jinsi = jinsi
        
    def ovqatlanish(self):
        return f"Men {self.nomi} ovqat yeyapman"
    
    def uxlash(self):
        return f"Men {self.nomi} uxlayapman"


# In[49]:


class Kuchuk(Hayvon):
    def __init__(self,nomi,jinsi):
        super().__init__(nomi,jinsi)
        
    def suyak_yeyish(self):
        return "Suyak yeyman"


# In[51]:


kuchuk = Kuchuk("Olapar","Erkak")


# In[53]:


kuchuk.ovqatlanish()


# # Dounder methods

# * _ _lt_ _(self, other)	To get called on comparison using < operator. 
# * _ _le__(self, other)	To get called on comparison using <= operator.
# * _ _eq_ _(self, other)	To get called on comparison using == operator.
# * _ _ne_ _(self, other)	To get called on comparison using != operator.
# * _ _ge_ _(self, other)	To get called on comparison using >= operator.

# In[73]:


import math
class Dounder:
    def __init__(self,a):
        self.a = a
        
    # <   
    def __lt__(self,other): 
        if self.a < other.a:
            return True
        else:
            return False
    # <=   
    def __le__(self,other): 
        if self.a <= other.a:
            return True
        else:
            return False
    
    # ==     
    def __eq__(self,other): 
        if self.a == other.a:
            return True
        else:
            return False
     
    # != 
    def __ne__(self,other): 
        if self.a != other.a:
            return True
        else:
            return False
     
    # >=
    def __ge__(self,other): 
        if self.a >= other.a:
            return True
        else:
            return False
        
    def __int__(self):
        return  int(self.a)
    
    def __float__(self):
        return float(self.a)
    
    def __complex__(self):
        return complex(self.a)
    
    def __ceil__(self):
        return math.ceil(self.a)
    
    def __floor__(self):
        return math.floor(self.a)
        
    def __add__(self,other):
        return self.a + other.a
    
    def __sub__(self,other):
        return self.a - other.a
    
    def __mul__(self,other):
        return self.a * other.a
    
    def __truediv__(self,other):
        return self.a / other.a
    
    def __abs__(self):
        return abs(self.a)
    
    def __floordiv__(self,other):
        return self.a // other.a
    
    def __mod__(self,other):
        return self.a % other.a
    
    def __pow__(self,other):
        return self.a ** other.a
    
    def __divmod__(self,other):
        return divmod(self.a,other.a)
    
    # +=
    def __iadd__(self,other):
        self.a += other.a
        return self.a
    
    # -=
    def __isub__(self,other):
        self.a -= other.a
        return self.a
    
    # *=
    def __imul__(self,other):
        self.a /= other.a
        return self.a
    
    # /=
    def __itruediv__(self,other):
        self.a /= other.a
        return self.a
    
    # //=
    def __ifloordiv__(self,other):
        self.a //= other.a
        return self.a
    
    # %=
    def __imod__(self,other):
        self.a %= other.a
        return self.a
    
    # **=
    def __ipow__(self,other):
        self.a **= other.a
        return self.a
    
    # round
    def __round__(self,n=None):
        return round(self.a,n)
    
    # trunc
    def __trunc__(self):
        return math.trunc(self.a)
    
    #Qo'shimcha
    
    def __invert__(self):
        return ~self.a
    
    def __pos__(self):
        return +self.a
    
    def __neg__(self):
        return -self.a
    
    def __and__(self,other):
        return self.a & other.a

    def __or__(self,other):
        return self.a | other.a
    
    def __xor__(self,other):
        return self.a ^ other.a
    
    def __rshift__(self,other):
        return self.a >> other.a
    
    def __lshift__(self,other):
        return self.a << other.a


# In[74]:


import math
x = Dounder(5)
y = Dounder(10)
z = Dounder(2.6)

print(x>y)
print(x<y)
print(x>=y)
print(x<=y)
print(x!=y)
print(x==y)


# # Vazifa 

# ![image.png](attachment:image.png)

# In[38]:


class Talaba:
    def __init__(self,ism,familya):
        self.__ism = ism
        self.__familya = familya
    
    def get_full_name(self):
        return f"{self.__ism} {self.__familya}"

    
class Fan(Talaba):
    __matematika = []
    __fizika = []
    __ingliztili = []
    __tarix = []
    def __init__(self,ism,familya):
        super().__init__(ism,familya)
        
    def set_fan_info(self,fan_nomi):
        while True:
            if fan_nomi=="matematika":
                (Fan.__matematika).append(self.get_full_name())
                break
            elif fan_nomi=="fizika":
                (Fan.__fizika).append(self.get_full_name())
                break
            elif fan_nomi=="ingliztili":
                (Fan.__ingliztili).append(self.get_full_name())
                break
            elif fan_nomi=="tarix":
                (Fan.__tarix).append(self.get_full_name())
                break
            else:
                print("Fan nomi xato kiritilgan!")
                fan_nomi = input("Qaytatdan kiriting: ").lower()

        
    def get_fan_info(self,fan_nomi):
        while True:
            if fan_nomi=="matematika":
                if Fan.__matematika:
                    print(f"Fan nomi: {fan_nomi}\nTalabalar soni: {len(Fan.__matematika)}\n\n")
                    for i in range(len(Fan.__matematika)):
                        print(f"{i+1}.{Fan.__matematika[i]}")
                    break
                else:
                    print("Xech narsa topilmadi!")
                    break
            elif fan_nomi=="fizika":
                if Fan.__fizika:
                    print(f"Fan nomi: {fan_nomi}\nTalabalar soni: {len(Fan.__fizika)}\n\n")
                    for i in range(len(Fan.__fizika)):
                        print(f"{i+1}.{Fan.__fizika[i]}")
                    break
                else:
                    print("Xech narsa topilmadi!")
                    break
            elif fan_nomi=="ingliztili":
                if Fan.__ingliztili:
                    print(f"Fan nomi: {fan_nomi}\nTalabalar soni: {len(Fan.__ingliztili)}\n\n")
                    for i in range(len(Fan.__ingliztili)):
                        print(f"{i+1}.{Fan.__ingliztili[i]}")
                    break
                else:
                    print("Xech narsa topilmadi!")
                    break
            elif fan_nomi=="tarix":
                if Fan.__tarix:
                    print(f"Fan nomi: {fan_nomi}\nTalabalar soni: {len(Fan.__tarix)}\n\n")
                    for i in range(len(Fan.__tarix)):
                        print(f"{i+1}.{Fan.__tarix[i]}")
                    break
                else:
                    print("Xech narsa topilmadi!")
                    break
            else:
                    print("Fan nomi xato kiritilgan!")
                    fan_nomi = input("Qaytatdan kiriting: ").lower()


# In[39]:


sherali = Fan("Sherali","salomov")
asad = Fan("Asad","Halilov")
jasmina = Fan("Jasmina","Hamidova")


# In[30]:


farrux.get_full_name()


# In[31]:


jasmina.get_full_name()


# In[40]:


asad.set_fan_info("matematika")
asad.set_fan_info("fizika")
jasmina.set_fan_info("matematika")
sherali.set_fan_info("tarix")
asad.set_fan_info("ingliztili")
jasmina.set_fan_info("tarix")


# In[41]:


asad.get_fan_info("matematika")


# In[42]:


asad.get_fan_info("fizika")


# In[43]:


asad.get_fan_info("tarix")


# In[44]:


asad.get_fan_info("ingliztili")


# In[ ]:





# In[8]:


class Fan:
    def __init__(self,fan_nomi):
        self.__fan_nomi = fan_nomi
        self.__talabalar = []
        self.__talabalar_soni = 0
        
    def add_talaba(self,talaba):
        self.__talabalar.append(talaba)
        self.__talabalar_soni += 1
        
    def get_fan_info(self):
        return f"Fan nomi: {self.__fan_nomi}\nTalabalar soni: {self.__talabalar_soni}\n{self.__talabalar}"


# In[9]:


mat = Fan("Xisob")


# In[10]:


mat.add_talaba("Farrux")


# In[11]:


mat.add_talaba("Sherali")


# In[13]:


print(mat.get_fan_info())

