#!/usr/bin/env python
# coding: utf-8

# # 26/04/2022
# 
# # Python asoslari
# 
# # Matritsalarni ko'paytirish,qo'shish,ayirish,λ songa ko'paytirish
# 
# # Muallif: Farrux Sotivoldiyev

# In[ ]:


# UNIVERSAL Matritsa(ko'paytirish,qo'shish,ayirish,λ songa ko'paytirish)

def Chiqar(matrix):            #chiqarish
    for i in matrix:
        print(*i)
    
def Yasa(x,y):                 # Matritsa elementlarini kiritish
    k = [[int(input(f"son{i}: ")) for i in range(1,y+1)] for _ in range(x)]   
    return k

def Kopaytir(m1,n1,m2,n2,A,B):   #Matritsalar ko'paytmasi
    matrix = []
    for i in range(m1):
        temp2 = []
        for j in range(n2):
            temp1 = []
            for k in range(m2):
                temp1.append(A[i][k]*B[k][j])
            temp2.append(sum(temp1))
        matrix.append(temp2)
    return matrix

def Qosh(m1,n1,A,B):            #Matritsalar yeg'indi
    matrix = []
    for i in range(m1):
        temp = []
        for j in range(n1):
            temp.append(A[i][j]+B[i][j])
        matrix.append(temp)
    return matrix

def Ayir(m1,n1,A,B):            #Matritsalar ayirmasi
    matrix = []
    for i in range(m1):
        temp = []
        for j in range(n1):
            temp.append(A[i][j]-B[i][j])
        matrix.append(temp)
    return matrix

def Songa_kop(m1,n1,A,k):       #Matritsani songa ko'paytirish
    matrix = []
    for i in range(m1):
        temp = []
        for j in range(n1):
            temp.append(A[i][j]*k)
        matrix.append(temp)
    return matrix

while True:                      #Asosiy qism
    key = int(input("""
    Matritsalar ustida amallar.

    1.Matritsalar ko'paytmasi
    2.Matritsalar yig'indisi
    3.Matritsalar ayirmasi
    4.Matritsani songa ko'paytirish
    5.0 - Stop
    
    :::"""))

    if key == 0:
        break

    elif key==1:
        while True:
            print("A va B matritsani o'lchamlarini kiriting:")
            q = [int(input(">>> ")) for _ in range(4)] 
            if q[1]==q[2]:
                print(f"A matritsani qiymatlarini kiriting {q[0]}X{q[1]}:");A = Yasa(q[0],q[1])
                print(f"B matritsani qiymatlarini kiriting {q[2]}X{q[3]}:");B = Yasa(q[2],q[3])
                print("A:");Chiqar(A);print("B:");Chiqar(B);print("Javob:");Chiqar(Kopaytir(q[0],q[1],q[2],q[3],A,B))
                break
            else:
                print("Matritsalarni ko'paytirib bo'lmaydi\nQaytadan kiriting!")

    elif key==2:
        while True:
            print("A va B matritsani o'lchamlarini kiriting:")
            q = [int(input(">>> ")) for _ in range(4)] 
            if q[0]==q[2] and q[1]==q[3]:
                print(f"A matritsani qiymatlarini kiriting {q[0]}X{q[1]}:");A = Yasa(q[0],q[1])
                print(f"B matritsani qiymatlarini kiriting {q[2]}X{q[3]}:");B = Yasa(q[2],q[3])
                print("A:");Chiqar(A);print("B:");Chiqar(B);print("Javob:");Chiqar(Qosh(q[0],q[1],A,B))
                break
            else:
                print("Matritsalarni qo'shib bo'lmaydi\nQaytadan kiriting!")

    elif key==3:
        while True:
            print("A va B matritsani o'lchamlarini kiriting:")
            q = [int(input(">>> ")) for _ in range(4)] 
            if q[0]==q[2] and q[1]==q[3]:
                print(f"A matritsani qiymatlarini kiriting {q[0]}X{q[1]}:");A = Yasa(q[0],q[1])
                print(f"B matritsani qiymatlarini kiriting {q[2]}X{q[3]}:");B = Yasa(q[2],q[3])
                print("A:");Chiqar(A);print("B:");Chiqar(B);print("Javob:");Chiqar(Ayir(q[0],q[1],A,B))
                break
            else:
                print("Matritsalarni Ayirib bo'lmaydi\nQaytadan kiriting!")

    elif key==4:
        print("A matritsani o'lchamini kiriting:")
        q = [int(input(">>> ")) for _ in range(2)]
        print(f"A matritsani qiymatlarini kiriting {q[0]}X{q[1]}:");A = Yasa(q[0],q[1])
        k = int(input("λ sonni kiriting: "))
        print("A:");Chiqar(A);print("Javob:");Chiqar(Songa_kop(q[0],q[1],A,k))
    else:
        print("Bunday kalit yo'q qaytadan kiriting!")

print("Dastur tugadi")

