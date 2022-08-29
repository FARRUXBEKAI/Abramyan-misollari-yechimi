#!/usr/bin/env python
# coding: utf-8

# # 18/09/2022
# 
# # Python asoslari
# 
# # 27-dars : assert,try,except,else,finally
# 
# # Muallif: Farrux Sotivoldiyev

# In[6]:


def yosh(ism,x):
    assert x>0,"Yosh manfiy ham 0 ham bo'lmaydi bo'lmaydi"
    return f"Salom {ism}.Sizning yoshingiz {x} da"
print(yosh("Farruxbek",20))


# In[1]:


x = int(input("x = "))
try:
    print(1/x)
except:
    print("Aniqlanmagan")
else:
    print("else ishladi")
finally:
    print("finally ishladi")
    


# In[50]:


try:
    f = open("tryexcept_test.txt","r+")
except:
    f = open("tryexcept_test.txt","x+")
finally:
    print(f.read())
    f.write("qalesan\n")
    f.close()

