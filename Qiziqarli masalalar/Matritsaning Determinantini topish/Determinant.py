#!/usr/bin/env python
# coding: utf-8

# # 13/07/2022
# 
# # Python asoslari
# 
# # Matritsaning Determinantini topish
#  
# # Muallif: Farrux Sotivoldiyev

# In[1]:


n = int(input("n = "))
print("Matritsani kiriting:")

matrix = [list(map(int,input().split())) for i in range(n)]

assert len(matrix)==len(matrix[0]),"Ustun va satr bir biriga teng emas!"
    
def det(matrix):
    if len(matrix)==1:
        return matrix[0][0]
    elif len(matrix)==2:
        return matrix[0][0]*matrix[1][1] - matrix[1][0]*matrix[0][1]
    elif len(matrix)==3:
        return matrix[0][0]*matrix[1][1]*matrix[2][2]+matrix[0][1]*matrix[1][2]*matrix[2][0]+\
               matrix[0][2]*matrix[1][0]*matrix[2][1]-matrix[0][2]*matrix[1][1]*matrix[2][0]-\
               matrix[0][0]*matrix[1][2]*matrix[2][1]-matrix[0][1]*matrix[1][0]*matrix[2][2]
    s = 0
    for i in range(len(matrix)):
        s += matrix[0][i] * (1 if i%2==0 else -1) * det([j[:i]+j[i+1:] for j in matrix[1:]])
    return s

print("Determinanti:",det(matrix))

