#!/usr/bin/env python
# coding: utf-8

# # 15/09/2022
# 
# # Python asoslari
# 
# # 26-dars : Dekorator
# 
# # Muallif: Farrux Sotivoldiyev

# In[2]:


def dek(func):
    def salom(a,b):
        return func(a,b)
    return salom

@dek

def div(a,b):
    return a/b

print(div(5,2))


# In[25]:


# 2-ustun bilan 4-ustunni almashtirib beruvchi decorator

from random import randint

def swap_col(func):
    def dek(m,n):
        matrix = func(m,n)
        print("ichki: ")
        for i in matrix:
            print(*i)
        for i in range(m):
            matrix[i][2],matrix[i][4] = matrix[i][4],matrix[i][2]
        return matrix
    return dek

@swap_col
def input_matrix(m,n):
    return [[randint(1,9) for _ in range(n)] for _ in range(m)]

@swap_col
def salom(m,n):
    return [[i for i in range(n)] for j in range(m)]

print("Tashqi1: ",input_matrix(5,6))
print("Tashqi2: ",salom(5,6))


# In[39]:


# mXn matritsani decorator yordamida 4X4 qilish
def tortgatort(func):
    def tort(m,n):
        matrix = func(m,n)
        print("Asl matrix: ",matrix)
        matrix = matrix[:4]
        for i in range(4):
            matrix[i] = matrix[i][:4]
        print("\n4X4 Matrix: ")
        return matrix
    return tort

@tortgatort
def input_matrix(m,n):
    return [[randint(1,9) for _ in range(n)] for _ in range(m)]


for i in input_matrix(6,8):
    print(*i)

