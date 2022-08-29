#!/usr/bin/env python
# coding: utf-8

# # 27/09/2022
# 
# # Python asoslari
# 
# # 30-dars : OOP dan foydalanib kattaroq tizim yaratish(HEMIS)
# 
# # Muallif: Farrux Sotivoldiyev

# **`Bir biridan voris olib oxirida bitta obyektga ma'lumotlar jo'natiladi va shu tizim bilan ishlanadi`**

# In[ ]:


# HEMIS
from re import match

class Oquv_reja:
    __fanlar1 = ["O'zbekiston tarixi","Falsafa","Akademik yozuv1","Xorijiy til1","Xisob","Fizika1","Dasturlash1","Jismoniy tarbiya"]
    __fanlar2 = ["Diferensial tenglamalar","Chiziqli algebra","Akademik yozuv2","Xorijiy til2","Fizika2","Dasturlash2"] 
    __fanlar3 = ["Ma'lumotlar bazasi","Kiberxavfsizlik asoslari","Ma'lumotlar tuzulmasi va algoritmlari","Elektronika va sxemalar1","Diskret tuzilmalar"]
    __fanlar4 = ["Kompyuterning tashkil etilishi","Web dasturlashga kirish","Algoritmlarni loyihalash","Dasturiy injeneringga kirish","Extimollik va statistika"]
    __umumiy_davomat = []
    __umumiy_nazorat = []
    __reyting_daftar = {
    "semestr_1" : {
        "O'zbekiston tarixi" : {
            "fan_turi":"Majburiy",
            "yuklama":"180",
            "kredit":"6.0",
            "ball":"92",
            "baho":"5"
        },
        "Falsafa" : {
            "fan_turi":"Majburiy",
            "yuklama":"180",
            "kredit":"6.0",
            "ball":"91",
            "baho":"5"
        },
        "Akademik yozuv1" : {
            "fan_turi":"Majburiy",
            "yuklama":"180",
            "kredit":"6.0",
            "ball":"90",
            "baho":"5"
        },
        "Xorijiy til1" : {
            "fan_turi":"Majburiy",
            "yuklama":"180",
            "kredit":"6.0",
            "ball":"85",
            "baho":"4"
        },
        "Xisob" : {
            "fan_turi":"Majburiy",
            "yuklama":"180",
            "kredit":"6.0",
            "ball":"68",
            "baho":"3"
        },
        "Fizika1" : {
            "fan_turi":"Majburiy",
            "yuklama":"180",
            "kredit":"6.0",
            "ball":"92",
            "baho":"5"
        },
        "Dasturlash1" : {
            "fan_turi":"Majburiy",
            "yuklama":"180",
            "kredit":"6.0",
            "ball":"84",
            "baho":"4"
        },
        "Jismoniy tarbiya" : {
            "fan_turi":"Majburiy",
            "yuklama":"180",
            "kredit":"6.0",
            "ball":"92",
            "baho":"5"
        }
    },
    "semestr_2" : {
        "Diferensial tenglamalar" : {
            "fan_turi":"Majburiy",
            "yuklama":"180",
            "kredit":"6.0",
            "ball":"92",
            "baho":"5"
        },
        "Chiziqli algebra" : {
            "fan_turi":"Majburiy",
            "yuklama":"180",
            "kredit":"6.0",
            "ball":"91",
            "baho":"5"
        },
        "Akademik yozuv2" : {
            "fan_turi":"Majburiy",
            "yuklama":"180",
            "kredit":"6.0",
            "ball":"90",
            "baho":"5"
        },
        "Xorijiy til2" : {
            "fan_turi":"Majburiy",
            "yuklama":"180",
            "kredit":"6.0",
            "ball":"85",
            "baho":"4"
        },
        "Fizika2" : {
            "fan_turi":"Majburiy",
            "yuklama":"180",
            "kredit":"6.0",
            "ball":"92",
            "baho":"5"
        },
        "Dasturlash2" : {
            "fan_turi":"Majburiy",
            "yuklama":"180",
            "kredit":"6.0",
            "ball":"84",
            "baho":"4"
        }
    },
    "semestr_3" : {
        "Ma'lumotlar bazasi" : {
            "fan_turi":"Majburiy",
            "yuklama":"180",
            "kredit":"6.0",
            "ball":"92",
            "baho":"5"
        },
        "Kiberxavfsizlik asoslari" : {
            "fan_turi":"Majburiy",
            "yuklama":"180",
            "kredit":"6.0",
            "ball":"91",
            "baho":"5"
        },
        "Ma'lumotlar tuzulmasi" : {
            "fan_turi":"Majburiy",
            "yuklama":"180",
            "kredit":"6.0",
            "ball":"90",
            "baho":"5"
        },
        "Elektronika va sxemalar1" : {
            "fan_turi":"Majburiy",
            "yuklama":"180",
            "kredit":"6.0",
            "ball":"85",
            "baho":"4"
        },
        "Diskret tuzilmalar" : {
            "fan_turi":"Majburiy",
            "yuklama":"180",
            "kredit":"6.0",
            "ball":"92",
            "baho":"5"
        }
    },
    "semestr_4" : {
        "Kompyuterning tashkil etilishi" : {
            "fan_turi":"Majburiy",
            "yuklama":"180",
            "kredit":"6.0",
            "ball":"92",
            "baho":"5"
        },
        "Web dasturlashga kirish" : {
            "fan_turi":"Majburiy",
            "yuklama":"180",
            "kredit":"6.0",
            "ball":"91",
            "baho":"5"
        },
        "Algoritmlarni loyihalash" : {
            "fan_turi":"Majburiy",
            "yuklama":"180",
            "kredit":"6.0",
            "ball":"90",
            "baho":"5"
        },
        "Dasturiy injeneringga kirish" : {
            "fan_turi":"Majburiy",
            "yuklama":"180",
            "kredit":"6.0",
            "ball":"85",
            "baho":"4"
        },
        "Extimollik va statistika" : {
            "fan_turi":"Majburiy",
            "yuklama":"180",
            "kredit":"6.0",
            "ball":"92",
            "baho":"5"
        }
    }
}
    __darsning_jadvali = {
    "semestr_1" : {
        "Dushanba" : {
            "Fizika1":["106A","Ma'ruza","Abdullayev.J","08:30"],
            "Xorijiy til1":['205A','Amaliy',"G'aniyeva.D",'10:00']
        },
        "Seshanba" : {
            "Fizika1":["116A","Amaliy","Tulakova.S","08:30"],
            "Dasturlash1":['205A','Labaratoriya','Asrayev.M','10:00'],
            "Diferensial tenglamalar":["106A","Ma'ruza","Tulakova.Z","11:30"]
        },
        "Chorshanba" : {
            "Xorijiy til1":["116A","Amaliy","G'aniyeva.D","08:30"],
            "Chiziqli algebra":['106A',"Ma'ruza",'Nasriddinov.O','10:00'],
            "Jismoniy tarbiya":["Sport zal","Amaliy","Arabboyev.X","11:30"],
            "Dasturlash1":["105A","Ma'ruza","Kayumov.A","13:30"]
        },
        "Payshanba" : {
            "Dasturlash1":['205A','Labaratoriya','Asrayev.M','03:30'],
            "Chiziqli algebra":['106A',"Amaliy",'Shokirov.A','10:00']
        },
        "Juma" : {
            "Fizika1":["116A","Amaliy","Tulakova.S","08:30"],
            "Dasturlash1":['205A','Labaratoriya','Asrayev.M','10:00'],
            "Diferensial tenglamalar":["106A","Ma'ruza","Tulakova.Z","11:30"]
        }
    },
    "semestr_2" : {
        "Dushanba" : {
            "Fizika2":["106A","Ma'ruza","Abdullayev.J","08:30"],
            "Xorijiy til2":['205A','Amaliy',"G'aniyeva.D",'10:00']
        },
        "Seshanba" : {
            "Fizika2":["116A","Amaliy","Tulakova.S","08:30"],
            "Dasturlash2":['205A','Labaratoriya','Asrayev.M','10:00'],
            "Diferensial tenglamalar":["106A","Ma'ruza","Tulakova.Z","11:30"]
        },
        "Chorshanba" : {
            "Xorijiy til2":["116A","Amaliy","G'aniyeva.D","08:30"],
            "Chiziqli algebra":['106A',"Ma'ruza",'Nasriddinov.O','10:00'],
            "Jismoniy tarbiya":["Sport zal","Amaliy","Arabboyev.X","11:30"],
            "Dasturlash2":["105A","Ma'ruza","Kayumov.A","13:30"]
        },
        "Payshanba" : {
            "Dasturlash2":['205A','Labaratoriya','Asrayev.M','08:30'],
            "Chiziqli algebra":['106A',"Amaliy",'Shokirov.A','10:00']
        },
        "Juma" : {
            "Fizika2":["116A","Amaliy","Tulakova.S","08:30"],
            "Dasturlash2":['205A','Labaratoriya','Asrayev.M','10:00'],
            "Diferensial tenglamalar":["106A","Ma'ruza","Tulakova.Z","11:30"]
        }
    },
    "semestr_3" : {
        "Dushanba" : {
            "Ma'lumotlar bazasi":["205B","Ma'ruza","Pulatov.G'","08:30"],
            "Diskret tuzilmalar":['212A',"Ma'ruza",'Nasriddinov.O','10:00']
            
        },
        "Seshanba" : {
            "Ma'lumotlar tuzulmasi va algoritmlari":["204A","Labaratoriya","Abdulxamidov.A","08:30"],
            "Elektronika va sxemalar":['223','Labaratoriya','Ergashev.Sh','10:00'],
            "Ma'lumotlar bazasi":['117A',"Labaratoriya",'Raxmatova.G','11:30']
        },
        "Chorshanba" : {
            "Kiberxavfsizlik asoslari":["212A","Ma'ruza","G'aniyeva.Sh","08:30"],
            "Elektronika va sxemalar":['223','Labaratoriya','Ergashev.Sh','10:00'],
            "Ma'lumotlar bazasi":['117A',"Labaratoriya",'Raxmatova.G','11:30']
        },
        "Payshanba" : {
            "Ma'lumotlar bazasi":["205B","Ma'ruza","Pulatov.G'","08:30"],
            "Diskret tuzilmalar":['212A',"Ma'ruza",'Nasriddinov.O','10:00'],
            
        },
        "Juma" : {
            "Ma'lumotlar bazasi":['117A',"Labaratoriya",'Raxmatova.G','08:30'],
            "Diskret tuzilmalar":['212A',"Ma'ruza",'Nasriddinov.O','10:00'],
            "Elektronika va sxemalar":['223','Labaratoriya','Ergashev.Sh','11:30']
        }
    },
    "semestr_4" : {
        "Dushanba" : {
            "Web dasturlashga kirish":["216A","Ma'ruza","Malikov.B","08:30"],
            "Dasturiy injeneringga kirish":['201','Amaliy','Karimov.A','10:00']
        },
        "Seshanba" : {
            "Web dasturlashga kirish":["107","Ma'ruza","Malikov.B","08:30"],
            "Extimollik va statistika":['223','Labaratoriya','Bozorqulov.A','10:00'],
            "Dasturiy injeneringga kirish":["107","Ma'ruza","Shodmonov.I","11:30"]
        },
        "Chorshanba" : {
            "Kompyuterni tashkil etilishi":["212A","Ma'ruza","Jalilov.M","08:30"],
            "Extimollik va statistika":['223','Amaliy','Dilshodov.A','10:00'],
            "Web dasturlashga kirish":["107","Labaratoriya","Raximov.Q","11:30"],
            "Dasturiy injeneringga kirish":["107","Ma'ruza","Shodmonov.I","13:30"]
        },
        "Payshanba" : {
            "Web dasturlashga kirish":["107","Ma'ruza","Malikov.B","08:30"],
            "Extimollik va statistika":['223','Labaratoriya','Bozorqulov.A','10:00'],
            "Dasturiy injeneringga kirish":["107","Ma'ruza","Shodmonov.I","11:30"],
            "Algoritmlarni loyihalash":["116A","Ma'ruza","Umarov.Sh","13:30"]
        },
        "Juma" : {
            "Extimollik va statistika":['223','Labaratoriya','Bozorqulov.A','08:30'],
            "Algoritmlarni loyihalash":["116A","Ma'ruza","Umarov.Sh","10:00"]
        }
    }
    
}   
    def __init__(self,kurs,sana):
        self.kurs = kurs
        self.sana = sana
        
    def oquv_reja(self):
        semestr = int(input("Qaysi semestr fanlarini ko'rasiz 1/2/3/4: "))
        while 1>semestr and 4<semestr: 
            print("Bunday indexdagi buyruq yoq qaytadan kiriting")
            semestrlar = int(input("Qaysi semestr fanlarini ko'rasiz 1/2/3/4: "))
        if semestr==1:
            print("1-semestr:")
            for i in range(len(Oquv_reja.__fanlar1)):
                print(f"{i+1}.{Oquv_reja.__fanlar1[i]}")
        elif semestr==2:
            print("2-semestr:")
            for i in range(len(Oquv_reja.__fanlar2)):
                print(f"{i+1}.{Oquv_reja.__fanlar2[i]}")
        elif semestr==3:
            print("3-semestr:")
            for i in range(len(Oquv_reja.__fanlar3)):
                print(f"{i+1}.{Oquv_reja.__fanlar3[i]}")
        elif semestr==4:
            print("4-semestr:")
            for i in range(len(Oquv_reja.__fanlar4)):
                print(f"{i+1}.{Oquv_reja.__fanlar4[i]}")
        
    def dars_jadvali(self,semestr):
        if semestr==1:
            for k in Oquv_reja.__darsning_jadvali["semestr_1"].keys():
                sanoq = 1
                print(125*"-")
                print(k.upper())
                for i,j in Oquv_reja.__darsning_jadvali["semestr_1"][k].items():
                    print(f"{sanoq}.{i}\n{j[0]} / {j[1]} / {j[2]} / {j[3]}")
                    sanoq += 1
        elif semestr==2:
            for k in Oquv_reja.__darsning_jadvali["semestr_2"].keys():
                sanoq = 1
                print(125*"-")
                print(k.upper())
                for i,j in Oquv_reja.__darsning_jadvali["semestr_2"][k].items():
                    print(f"{sanoq}.{i}\n{j[0]} / {j[1]} / {j[2]} / {j[3]}")
                    sanoq += 1
        elif semestr==3:
            for k in Oquv_reja.__darsning_jadvali["semestr_3"].keys():
                sanoq = 1
                print(125*"-")
                print(k.upper())
                for i,j in Oquv_reja.__darsning_jadvali["semestr_3"][k].items():
                    print(f"{sanoq}.{i}\n{j[0]} / {j[1]} / {j[2]} / {j[3]}")
                    sanoq += 1
        elif semestr==4:
            for k in Oquv_reja.__darsning_jadvali["semestr_4"].keys():
                sanoq = 1
                print(125*"-")
                print(k.upper())
                for i,j in Oquv_reja.__darsning_jadvali["semestr_4"][k].items():
                    print(f"{sanoq}.{i}\n{j[0]} / {j[1]} / {j[2]} / {j[3]}")
                    sanoq += 1
        else:
            print("Kursni xato kiritdingiz!")
            
    def dars_jadvalini_yangilash(self,semestr):
        buyruq = int(input(f"Kerakli indexni tanlang:\n1.Qo'shish\n2.O'chirish\n"))
        while buyruq!=1 and buyruq!=2:
            print("Bunday indexdagi buyruq yoq qaytadan kiriting")
            buyruq = int(input(f"Kerakli indexni tanlang:\n1.Qo'shish\n2.O'chirish\n"))
        hafta_kuni = input("Hafta kuni: ").capitalize()
        fan_nomi = input("To'liq fan nomi: ").capitalize()
        if buyruq==1:
            Oquv_reja.__darsning_jadvali["semestr_"+str(semestr)][hafta_kuni][fan_nomi] = [input("Xona: "),input("Dars o'tish turi "),input("O'qituvchi: "),input("Boshlanish vaqti: ")]
            print("Muvofaqiyatli yangilandi!")
        elif buyruq==2:
            Oquv_reja.__darsning_jadvali["semestr_"+str(semestr)][hafta_kuni].pop(fan_nomi)
            print("Muvofaqiyatli yangilandi!")
            
    def nazorat_jadvaliga_qoshish(self):
        (Oquv_reja.__umumiy_nazorat).append(f"{input('Nazorat turi: ')} nazorat\n\nFan: {input('Fan nomi: ')}\nO'qituvchi: {input('Oqituvchi: ')}\nAuditoriya: {input('Auditoriya: ')}")
        print("Nazorat jadvaliga muvofaqiyatli qo'shildi!")
        
    def nazorat_jadvali(self):
        if len(Oquv_reja.__umumiy_nazorat):
            for i in range(len(Oquv_reja.__umumiy_nazorat)):
                print(125*"-")
                print(f"{Oquv_reja.__umumiy_nazorat[i]}",end="\n\n")
        else:
            print("Xech narsa topilmadi")
       
    def mb_qoyish(self):
        (Oquv_reja.__umumiy_davomat).append(f"{(str(self.semestri)+'-semestr').ljust(15)}{self.sana.center(20)}{input('Fan nomi: ').center(25)}{input('Mashgulot nomi: ').center(20)}{input('Sababli: ').center(10)}{input('Soati: ').center(10)}{input('Oqituvchi ismi: ').rjust(16)}")
        print("Muvofaqiyatli bajarildi")
        
    def davomat(self):
        if len(Oquv_reja.__umumiy_davomat):
            print("Semestr".ljust(15)+"Dars sanasi".center(20)+"Fanlar".center(25)+"Mashg'ulot".center(20)+"Sababli".center(10)+"Soatlar".center(10)+"Xodim".rjust(16))
            for i in range(len(Oquv_reja.__umumiy_davomat)):
                print(f"{Oquv_reja.__umumiy_davomat[i]}",end="\n\n")
        else:
             print("Xech narsa topilmadi")
            
        
    def imtihonlar(self):
        print("Bo'm bo'sh bo'lim")
        
    def reyting_daftarcha_ozgartirish(self):
        semestrlar = int(input("Qaysi semestr fanlarini o'zgartirasiz? 1/2/3/4: "))
        while 1>semestrlar and 4<semestrlar: 
            print("Bunday indexdagi buyruq yoq qaytadan kiriting")
            semestrlar = int(input("Qaysi semestr fanlarini ko'rasiz 1/2/3/4: "))
        semestr = None
        if semestrlar==1:
            semestr = "semestr_1"
            print("1-semestr".center(125),end="\n\n")
            k = 1
            for i in Oquv_reja.__reyting_daftar["semestr_1"].keys():
                print(f"{k}.{i}")
                k += 1
        elif semestrlar==2:
            semestr = "semestr_2" 
            print("2-semestr".center(125),end="\n\n")
            k = 1
            for i in Oquv_reja.__reyting_daftar["semestr_2"].keys():
                print(f"{k}.{i}")
                k += 1
        elif semestrlar==3:
            semestr = "semestr_3" 
            print("3-semestr".center(125),end="\n\n")
            k = 1
            for i in Oquv_reja.__reyting_daftar["semestr_3"].keys():
                print(f"{k}.{i}")
                k += 1
        elif semestrlar==4:
            semestr = "semestr_4" 
            print("4-semestr".center(125),end="\n\n")
            k = 1
            for i in Oquv_reja.__reyting_daftar["semestr_4"].keys():
                print(f"{k}.{i}")
                k += 1
                
        fan = input("Qaysi fanni o'zgartirasiz to'liq yozing: ").capitalize()
        Oquv_reja.__reyting_daftar[semestr][fan]["fan_turi"] = input("Fan turi: ").capitalize()
        Oquv_reja.__reyting_daftar[semestr][fan]["yuklama"] = input("Yuklama soati: ")
        Oquv_reja.__reyting_daftar[semestr][fan]["kredit"] = input("Kredit: ")
        ball = input("Ball: ")
        Oquv_reja.__reyting_daftar[semestr][fan]["ball"] = ball
        if match(r"(9[0-9]$|100)",ball):
            Oquv_reja.__reyting_daftar[semestr][fan]["baho"] = "5"
        elif match(r"(8[0-9]$|90)",ball):
            Oquv_reja.__reyting_daftar[semestr][fan]["baho"] = "4"
        else:
            Oquv_reja.__reyting_daftar[semestr][fan]["baho"] = "3"
        print("Muvofaqiyatli o'zgartirildi")

    def reyting_daftarcha(self):
        semestr = int(input("Qaysi semestr fanlarini ko'rasiz 1/2/3/4: "))
        while 1>semestr and 4<semestr: 
            print("Bunday indexdagi buyruq yoq qaytadan kiriting")
            semestr = int(input("Qaysi semestr fanlarini ko'rasiz 1/2/3/4: "))
            
        if semestr==1:
            print("1-semestr".center(125),end="\n\n")
            print("Fanlar".ljust(30),"Fan turi".center(20),"Yuklama".center(20),"Kredit".center(20),"Ball".center(20),"Baho".rjust(12))
            print()
            for i in Oquv_reja.__reyting_daftar["semestr_1"].keys():
                print(f"{i}".ljust(30),f"{Oquv_reja.__reyting_daftar['semestr_1'][i]['fan_turi']}".center(20),f"{Oquv_reja.__reyting_daftar['semestr_1'][i]['yuklama']}".center(20),f"{Oquv_reja.__reyting_daftar['semestr_1'][i]['kredit']}".center(20),f"{Oquv_reja.__reyting_daftar['semestr_1'][i]['ball']}".center(20),f"{Oquv_reja.__reyting_daftar['semestr_1'][i]['baho']}".rjust(12))
        elif semestr==2:
            print("2-semestr".center(125),end="\n\n")
            print("Fanlar".ljust(30),"Fan turi".center(20),"Yuklama".center(20),"Kredit".center(20),"Ball".center(20),"Baho".rjust(12))
            print()
            for i in Oquv_reja.__reyting_daftar["semestr_2"].keys():
                print(f"{i}".ljust(30),f"{Oquv_reja.__reyting_daftar['semestr_2'][i]['fan_turi']}".center(20),f"{Oquv_reja.__reyting_daftar['semestr_2'][i]['yuklama']}".center(20),f"{Oquv_reja.__reyting_daftar['semestr_2'][i]['kredit']}".center(20),f"{Oquv_reja.__reyting_daftar['semestr_2'][i]['ball']}".center(20),f"{Oquv_reja.__reyting_daftar['semestr_2'][i]['baho']}".rjust(12))
        elif semestr==3:
            print("3-semestr".center(125),end="\n\n")
            print("Fanlar".ljust(30),"Fan turi".center(20),"Yuklama".center(20),"Kredit".center(20),"Ball".center(20),"Baho".rjust(12))
            print()
            for i in Oquv_reja.__reyting_daftar["semestr_3"].keys():
                print(f"{i}".ljust(30),f"{Oquv_reja.__reyting_daftar['semestr_3'][i]['fan_turi']}".center(20),f"{Oquv_reja.__reyting_daftar['semestr_3'][i]['yuklama']}".center(20),f"{Oquv_reja.__reyting_daftar['semestr_3'][i]['kredit']}".center(20),f"{Oquv_reja.__reyting_daftar['semestr_3'][i]['ball']}".center(20),f"{Oquv_reja.__reyting_daftar['semestr_3'][i]['baho']}".rjust(12))
        elif semestr==4:
            print("4-semestr".center(125),end="\n\n")
            print("Fanlar".ljust(30),"Fan turi".center(20),"Yuklama".center(20),"Kredit".center(20),"Ball".center(20),"Baho".rjust(12))
            print()
            for i in Oquv_reja.__reyting_daftar["semestr_4"].keys():
                print(f"{i}".ljust(30),f"{Oquv_reja.__reyting_daftar['semestr_4'][i]['fan_turi']}".center(20),f"{Oquv_reja.__reyting_daftar['semestr_4'][i]['yuklama']}".center(20),f"{Oquv_reja.__reyting_daftar['semestr_4'][i]['kredit']}".center(20),f"{Oquv_reja.__reyting_daftar['semestr_4'][i]['ball']}".center(20),f"{Oquv_reja.__reyting_daftar['semestr_4'][i]['baho']}".rjust(12))
            
    def fan_tanlovi(self):
        print("Bo'm bo'sh bo'lim")

        
        
        
class Talaba_malumoti(Oquv_reja):
    __buyruqlar = []
    __shartnomalar = []
    __stipendiya_li = 11518746
    __stipendiya_siz = 6382746 
    __tolov1 = 0
    __tolov2 = 0
    
    def __init__(self,oquv_yili,sana,kurs,yonalish,semestr,shartnoma_turi,shartnoma_raqami):
        super().__init__(kurs,sana)
        self.__oquv_yili = oquv_yili
        self.__kurs = kurs
        self.__yonalish = yonalish
        self.__semestr = semestr
        self.__shartnoma_turi = shartnoma_turi
        self.__shartnoma_raqami = shartnoma_raqami
    
    def buyruq_yaratish(self):
        buyruq_raqami = input("Buyruq raqami: ")
        buyruq_sanasi = input("Buyruq sanasi: ")
        buyruq_nomi = input("Buyruq nomi: ")
        buyruq_turi = input("Buyruq turi: ")
        yaratilganligi = input("Yaratilganligi: ")
        (Talaba_malumoti.__buyruqlar).append(f"Buyruq raqami: {buyruq_raqami}\nBuyruq sanasi: {buyruq_sanasi}\nBuyruq nomi: {buyruq_nomi}\nBuruq turi: {buyruq_turi}\nYaratilganligi: {yaratilganligi}\nYuklab olish")
       
    def buyruqni_ochirish(self):
        if Talaba_malumoti.__buyruqlar:
            for i in range(len(Talaba_malumoti.__buyruqlar)):
                print(f"{i+1}.{Talaba_malumoti.__buyruqlar[i]}",end="\n\n")

            index = int(input("Qaysi indexdagi buyruqni o'chirasiz: "))
            while len(Talaba_malumoti.__buyruqlar)<index:
                print("Bunday indexdagi buyruq yoq qaytadan kiriting")
                index = int(input("Qaysi indexdagi buyruqni o'chirasiz: "))
            del Talaba_malumoti.__buyruqlar[index-1]
                print("Muvofaqiyatli bajarildi")
        else:
            print("Xech qanday buyruq topilmadi")
    
    def buyruqlar(self,):
        if len(Talaba_malumoti.__buyruqlar):
            for buyruq in Talaba_malumoti.__buyruqlar:
                print(buyruq,end="\n\n")
        else:
            print("Xech qanday buyruq topilmadi")
            
    def kontrakt_tolash(self,summa,stipendiya_li_siz):
        while stipendiya_li_siz!='stipendiyali' and stipendiya_li_siz!='stipendiyasiz':
                stipendiya_li_siz = input("To'g'ri kiriting stipendiya_li_siz: ").lower()
        
        while True:
            if stipendiya_li_siz=='stipendiyali':
                if Talaba_malumoti.__stipendiya_li>=summa:
                    Talaba_malumoti.__stipendiya_li-= summa
                    Talaba_malumoti.__tolov1 = 11518746 - Talaba_malumoti.__stipendiya_li
                    print("To'lov muvofaqiyatli bajarildi!")
                    break
                else:
                    print(f"Sizning qarzingiz {Talaba_malumoti.__stipendiya_li} so'm")
                    summa = int(input("To'liq shu summani kiriting: "))
            elif stipendiya_li_siz=='stipendiyasiz':
                if Talaba_malumoti.__stipendiya_siz>=summa:
                    Talaba_malumoti.__stipendiya_siz-= summa
                    Talaba_malumoti.__tolov2 = 6382746 - Talaba_malumoti.__stipendiya_siz
                    print("To'lov muvofaqiyatli bajarildi!")
                    break
                else:
                    print(f"Sizning qarzingiz {Talaba_malumoti.__stipendiya_siz} so'm")
                    summa = int(input("To'liq shu summani kiriting: "))
            
    def shartnomalar(self,stipendiya_li_siz):
        if self.__shartnoma_turi.lower()=="kontrakt":
            while stipendiya_li_siz!='stipendiyali' and stipendiya_li_siz!='stipendiyasiz':
                stipendiya_li_siz = input("To'g'ri kiriting stipendiya_li_siz: ").lower()
            if stipendiya_li_siz.lower()=='stipendiyali':
                print(f"O'quv yili: {self.__oquv_yili}\nShartnoma turi: Kontrakt\nShartnoma raqami: {self.__shartnoma_raqami}\nTo'landi: {Talaba_malumoti.__tolov1} so'm\nQarz: {Talaba_malumoti.__stipendiya_li} so'm\nYuklab olish")
            elif stipendiya_li_siz.lower()=='stipendiyasiz':
                print(f"O'quv yili: {self.__oquv_yili}\nShartnoma turi: Kontrakt\nShartnoma raqami: {self.__shartnoma_raqami}\nTo'landi: {Talaba_malumoti.__tolov2} so'm\nQarz: {Talaba_malumoti.__stipendiya_siz} so'm\nYuklab olish")
        else:
            print("Xech narsa topilmadi!")
            
    def __malumotnomalar(self):
        print("Bo'm bo'sh bo'lim")
        
    def talaba_hujjati(self):
        print(f"O'quv varaqa:\nKurs: {self.__kurs}-kurs\nO'quv yili: {self.__oquv_yili}\nSemestr: {self.__semestr}-semestr\nYuklab olish")
        print()
        print(f"Reyting daftarcha:\nMutaxasislik: {self.__yonalish}\nKurs: {self.__kurs}-kurs\nSemestr: {self.__semestr}-semestr\nYuklab olish")
        
    def __bitiruv_ishi(self):
        print("Bo'm bo'sh bo'lim")
        
    def __bitiruv_varaqasi(self):
        print("Bo'm bo'sh bo'lim")
        
        
        
        
class Xabarlar(Talaba_malumoti):
    __send_message = []
    __qoralama_xabarlar = []
    
    def __init__(self,oquv_yili,sana,kurs,yonalish,semestr,shartnoma_turi,shartnoma_raqami):
        super().__init__(oquv_yili,sana,kurs,yonalish,semestr,shartnoma_turi,shartnoma_raqami)
    
    def __kiruvchi_xabarlar():
        print("Bo'm bo'sh bo'lim")

    def jonatilganlar(self):
        if len(Xabarlar.__send_message):
            for message in Xabarlar.__send_message:
                print(message,end="\n\n")
        else:
            print("Jo'natilgan xabarlar yo'q")
        
    def xabar_yaratish(self):
        kimga = input("Kimga: ").title()
        mavzu = input("Mavzu: ").title()
        xabar = input("Xabar yozing: ").title()
        (Xabarlar.__send_message).append(f"Kimga: {kimga}  /  Mavzu: {mavzu}\nXabar: {xabar}")
        print("Muvofaqiyatli bajarildi")
        
    def qoralama_xabar_yaratish(self):
        kimga = input("Kimga: ").title()
        mavzu = input("Mavzu: ").title()
        xabar = input("Xabar yozing: ").title()
        (Xabarlar.__qoralama_xabarlar).append(f"Kimga: {kimga}  /  Mavzu: {mavzu}\nXabar: {xabar}")
        print("Muvofaqiyatli bajarildi")
        
    def qoralama_xabarlarni_korish(self):
        if Xabarlar.__qoralama_xabarlar:
            for message in Xabarlar.__qoralama_xabarlar:
                print(message,end="\n\n")
        else:
            print("Qoralama xabarlar yo'q")

    def korzina(self):
        print("1.Jo'natilgan xabarlar:")
        for i in range(len(Xabarlar.__send_message)):
            print(f"{i+1}.{Xabarlar.__send_message[i]}",end="\n\n")
            
        print("2.Qoralama xabarlar:")
        for i in range(len(Xabarlar.__qoralama_xabarlar)):
            print(f"{i+1}.{Xabarlar.__qoralama_xabarlar[i]}",end="\n\n")
            
        bolim = int(input("Qaysi bolimdan o'chirasiz 1 yoki 2: "))
        while bolim!=1 and bolim!=2:
            print("Xato kiritdingiz boshqatdan kiriting!")
            bolim = int(input("Qaysi bolimdan o'chirasiz 1 yoki 2: "))
            
        if bolim==1:
            if len(Xabarlar.__send_message):
                index = int(input("Qaysi indexdagisini o'chirasiz: "))
                
                 while len(Xabarlar.__qoralama_xabarlar)<index:
                    print("Xato kiritdingiz boshqatdan kiriting!")
                    index = int(input("Qaysi indexdagisini o'chirasiz: "))
                    
                del Xabarlar.__send_message[index-1]
                print("Muvofaqiyatli o'chirildi")
                
            else:
                print("Jo'natilgan xabarlar yo'q")
        elif bolim==2:
            if len(Xabarlar.__qoralama_xabarlar):
                index = int(input("Qaysi indexdagisini o'chirasiz: "))
                
                while len(Xabarlar.__qoralama_xabarlar)<index:
                    print("Xato kiritdingiz boshqatdan kiriting!")
                    index = int(input("Qaysi indexdagisini o'chirasiz: "))
                    
                del Xabarlar.__qoralama_xabarlar[index-1]
                print("Muvofaqiyatli o'chirildi")
                
            else:
                print("Qoralama xabarlar yo'q")

            
            
            
class Tizim(Xabarlar):
    __tizimga_kirish_tarixi = 0
    __loginlar = []
    __sanalar = []
    def __init__(self,ism,familya,login,parol,pasport_raqam,oquv_yili,sana,kurs,yonalish,semestr,shartnoma_turi,shartnoma_raqami):
        super().__init__(oquv_yili,sana,kurs,yonalish,semestr,shartnoma_turi,shartnoma_raqami)
        self.__ism = ism
        self.__familya = familya
        self.__login = login
        self.__parol = parol
        self.__pasport_raqam = pasport_raqam
        self.__sana = sana

        Tizim.__tizimga_kirish_tarixi += 1
        (Tizim.__loginlar).append(self.__login)
        (Tizim.__sanalar).append(self.__sana)
        
    def get_ism(self):
        return self.__ism
    
    def get_familya(self):
        return self.__familya
    
    def get_pasport_raqam(self):
        return self.__pasport_raqam
    
    def get_sana(self):
        return self.__sana
    
    def get_password(self):
        return self.__parol
        
    def update_parol(self,eski_parol,new_parol):
        while eski_parol != self.__parol:
            eski_parol = input("Eski parol xato boshqatdan kiriting: ")
        else:
            self.__parol = new_parol
            print("Parol muvofaqiyatli yangilandi!")
        
    def profil(self):
        print(f"Ismi: {self.__ism}\nFamilya: {self.__familya}\nLogin: {self.__login}\nPasport raqam: {self.__pasport_raqam}")
    
    def kirish_tarixi(self):
        if Tizim.__tizimga_kirish_tarixi:
            for i in range(Tizim.__tizimga_kirish_tarixi):
                print(f"Login: {Tizim.__loginlar[i]}    Holati: Muvofaqiyatli    Yaratilgan: {Tizim.__sanalar[i]}\n")
        else:     
            print("Xech narsa topilmadi")
            
class Hemis(Tizim):
    def __init__(self,ism,familya,login,parol,pasport_raqam,oquv_yili,sana,kurs,yonalish,semestr,shartnoma_turi,shartnoma_raqami):
        super().__init__(ism,familya,login,parol,pasport_raqam,oquv_yili,sana,kurs,yonalish,semestr,shartnoma_turi,shartnoma_raqami)
    


# In[ ]:


farrux = Hemis("Farrux","sotivoldiyev","392201100621","1102002f","AC2196805","2020-2021","26.07.2022",2,"Dasturiy injenering",4,"kontrakt","3922100527")


# In[ ]:





# In[ ]:





# **`Barcha classlar alohida bo'ladi va ular bilan alohida ishlanadi`**

# In[53]:


# HEMIS
from re import match

class Oquv_reja:
    __fanlar1 = ["O'zbekiston tarixi","Falsafa","Akademik yozuv1","Xorijiy til1","Xisob","Fizika1","Dasturlash1","Jismoniy tarbiya"]
    __fanlar2 = ["Diferensial tenglamalar","Chiziqli algebra","Akademik yozuv2","Xorijiy til2","Fizika2","Dasturlash2"] 
    __fanlar3 = ["Ma'lumotlar bazasi","Kiberxavfsizlik asoslari","Ma'lumotlar tuzulmasi va algoritmlari","Elektronika va sxemalar1","Diskret tuzilmalar"]
    __fanlar4 = ["Kompyuterning tashkil etilishi","Web dasturlashga kirish","Algoritmlarni loyihalash","Dasturiy injeneringga kirish","Extimollik va statistika"]
    __umumiy_davomat = []
    __umumiy_nazorat = []
    __reyting_daftar = {
    "semestr_1" : {
        "O'zbekiston tarixi" : {
            "fan_turi":"Majburiy",
            "yuklama":"180",
            "kredit":"6.0",
            "ball":"92",
            "baho":"5"
        },
        "Falsafa" : {
            "fan_turi":"Majburiy",
            "yuklama":"180",
            "kredit":"6.0",
            "ball":"91",
            "baho":"5"
        },
        "Akademik yozuv1" : {
            "fan_turi":"Majburiy",
            "yuklama":"180",
            "kredit":"6.0",
            "ball":"90",
            "baho":"5"
        },
        "Xorijiy til1" : {
            "fan_turi":"Majburiy",
            "yuklama":"180",
            "kredit":"6.0",
            "ball":"85",
            "baho":"4"
        },
        "Xisob" : {
            "fan_turi":"Majburiy",
            "yuklama":"180",
            "kredit":"6.0",
            "ball":"68",
            "baho":"3"
        },
        "Fizika1" : {
            "fan_turi":"Majburiy",
            "yuklama":"180",
            "kredit":"6.0",
            "ball":"92",
            "baho":"5"
        },
        "Dasturlash1" : {
            "fan_turi":"Majburiy",
            "yuklama":"180",
            "kredit":"6.0",
            "ball":"84",
            "baho":"4"
        },
        "Jismoniy tarbiya" : {
            "fan_turi":"Majburiy",
            "yuklama":"180",
            "kredit":"6.0",
            "ball":"92",
            "baho":"5"
        }
    },
    "semestr_2" : {
        "Diferensial tenglamalar" : {
            "fan_turi":"Majburiy",
            "yuklama":"180",
            "kredit":"6.0",
            "ball":"92",
            "baho":"5"
        },
        "Chiziqli algebra" : {
            "fan_turi":"Majburiy",
            "yuklama":"180",
            "kredit":"6.0",
            "ball":"91",
            "baho":"5"
        },
        "Akademik yozuv2" : {
            "fan_turi":"Majburiy",
            "yuklama":"180",
            "kredit":"6.0",
            "ball":"90",
            "baho":"5"
        },
        "Xorijiy til2" : {
            "fan_turi":"Majburiy",
            "yuklama":"180",
            "kredit":"6.0",
            "ball":"85",
            "baho":"4"
        },
        "Fizika2" : {
            "fan_turi":"Majburiy",
            "yuklama":"180",
            "kredit":"6.0",
            "ball":"92",
            "baho":"5"
        },
        "Dasturlash2" : {
            "fan_turi":"Majburiy",
            "yuklama":"180",
            "kredit":"6.0",
            "ball":"84",
            "baho":"4"
        }
    },
    "semestr_3" : {
        "Ma'lumotlar bazasi" : {
            "fan_turi":"Majburiy",
            "yuklama":"180",
            "kredit":"6.0",
            "ball":"92",
            "baho":"5"
        },
        "Kiberxavfsizlik asoslari" : {
            "fan_turi":"Majburiy",
            "yuklama":"180",
            "kredit":"6.0",
            "ball":"91",
            "baho":"5"
        },
        "Ma'lumotlar tuzulmasi" : {
            "fan_turi":"Majburiy",
            "yuklama":"180",
            "kredit":"6.0",
            "ball":"90",
            "baho":"5"
        },
        "Elektronika va sxemalar1" : {
            "fan_turi":"Majburiy",
            "yuklama":"180",
            "kredit":"6.0",
            "ball":"85",
            "baho":"4"
        },
        "Diskret tuzilmalar" : {
            "fan_turi":"Majburiy",
            "yuklama":"180",
            "kredit":"6.0",
            "ball":"92",
            "baho":"5"
        }
    },
    "semestr_4" : {
        "Kompyuterning tashkil etilishi" : {
            "fan_turi":"Majburiy",
            "yuklama":"180",
            "kredit":"6.0",
            "ball":"92",
            "baho":"5"
        },
        "Web dasturlashga kirish" : {
            "fan_turi":"Majburiy",
            "yuklama":"180",
            "kredit":"6.0",
            "ball":"91",
            "baho":"5"
        },
        "Algoritmlarni loyihalash" : {
            "fan_turi":"Majburiy",
            "yuklama":"180",
            "kredit":"6.0",
            "ball":"90",
            "baho":"5"
        },
        "Dasturiy injeneringga kirish" : {
            "fan_turi":"Majburiy",
            "yuklama":"180",
            "kredit":"6.0",
            "ball":"85",
            "baho":"4"
        },
        "Extimollik va statistika" : {
            "fan_turi":"Majburiy",
            "yuklama":"180",
            "kredit":"6.0",
            "ball":"92",
            "baho":"5"
        }
    }
}
    __darsning_jadvali = {
    "semestr_1" : {
        "Dushanba" : {
            "Fizika1":["106A","Ma'ruza","Abdullayev.J","08:30"],
            "Xorijiy til1":['205A','Amaliy',"G'aniyeva.D",'10:00']
        },
        "Seshanba" : {
            "Fizika1":["116A","Amaliy","Tulakova.S","08:30"],
            "Dasturlash1":['205A','Labaratoriya','Asrayev.M','10:00'],
            "Diferensial tenglamalar":["106A","Ma'ruza","Tulakova.Z","11:30"]
        },
        "Chorshanba" : {
            "Xorijiy til1":["116A","Amaliy","G'aniyeva.D","08:30"],
            "Chiziqli algebra":['106A',"Ma'ruza",'Nasriddinov.O','10:00'],
            "Jismoniy tarbiya":["Sport zal","Amaliy","Arabboyev.X","11:30"],
            "Dasturlash1":["105A","Ma'ruza","Kayumov.A","13:30"]
        },
        "Payshanba" : {
            "Dasturlash1":['205A','Labaratoriya','Asrayev.M','03:30'],
            "Chiziqli algebra":['106A',"Amaliy",'Shokirov.A','10:00']
        },
        "Juma" : {
            "Fizika1":["116A","Amaliy","Tulakova.S","08:30"],
            "Dasturlash1":['205A','Labaratoriya','Asrayev.M','10:00'],
            "Diferensial tenglamalar":["106A","Ma'ruza","Tulakova.Z","11:30"]
        }
    },
    "semestr_2" : {
        "Dushanba" : {
            "Fizika2":["106A","Ma'ruza","Abdullayev.J","08:30"],
            "Xorijiy til2":['205A','Amaliy',"G'aniyeva.D",'10:00']
        },
        "Seshanba" : {
            "Fizika2":["116A","Amaliy","Tulakova.S","08:30"],
            "Dasturlash2":['205A','Labaratoriya','Asrayev.M','10:00'],
            "Diferensial tenglamalar":["106A","Ma'ruza","Tulakova.Z","11:30"]
        },
        "Chorshanba" : {
            "Xorijiy til2":["116A","Amaliy","G'aniyeva.D","08:30"],
            "Chiziqli algebra":['106A',"Ma'ruza",'Nasriddinov.O','10:00'],
            "Jismoniy tarbiya":["Sport zal","Amaliy","Arabboyev.X","11:30"],
            "Dasturlash2":["105A","Ma'ruza","Kayumov.A","13:30"]
        },
        "Payshanba" : {
            "Dasturlash2":['205A','Labaratoriya','Asrayev.M','08:30'],
            "Chiziqli algebra":['106A',"Amaliy",'Shokirov.A','10:00']
        },
        "Juma" : {
            "Fizika2":["116A","Amaliy","Tulakova.S","08:30"],
            "Dasturlash2":['205A','Labaratoriya','Asrayev.M','10:00'],
            "Diferensial tenglamalar":["106A","Ma'ruza","Tulakova.Z","11:30"]
        }
    },
    "semestr_3" : {
        "Dushanba" : {
            "Ma'lumotlar bazasi":["205B","Ma'ruza","Pulatov.G'","08:30"],
            "Diskret tuzilmalar":['212A',"Ma'ruza",'Nasriddinov.O','10:00']
            
        },
        "Seshanba" : {
            "Ma'lumotlar tuzulmasi va algoritmlari":["204A","Labaratoriya","Abdulxamidov.A","08:30"],
            "Elektronika va sxemalar":['223','Labaratoriya','Ergashev.Sh','10:00'],
            "Ma'lumotlar bazasi":['117A',"Labaratoriya",'Raxmatova.G','11:30']
        },
        "Chorshanba" : {
            "Kiberxavfsizlik asoslari":["212A","Ma'ruza","G'aniyeva.Sh","08:30"],
            "Elektronika va sxemalar":['223','Labaratoriya','Ergashev.Sh','10:00'],
            "Ma'lumotlar bazasi":['117A',"Labaratoriya",'Raxmatova.G','11:30']
        },
        "Payshanba" : {
            "Ma'lumotlar bazasi":["205B","Ma'ruza","Pulatov.G'","08:30"],
            "Diskret tuzilmalar":['212A',"Ma'ruza",'Nasriddinov.O','10:00'],
            
        },
        "Juma" : {
            "Ma'lumotlar bazasi":['117A',"Labaratoriya",'Raxmatova.G','08:30'],
            "Diskret tuzilmalar":['212A',"Ma'ruza",'Nasriddinov.O','10:00'],
            "Elektronika va sxemalar":['223','Labaratoriya','Ergashev.Sh','11:30']
        }
    },
    "semestr_4" : {
        "Dushanba" : {
            "Web dasturlashga kirish":["216A","Ma'ruza","Malikov.B","08:30"],
            "Dasturiy injeneringga kirish":['201','Amaliy','Karimov.A','10:00']
        },
        "Seshanba" : {
            "Web dasturlashga kirish":["107","Ma'ruza","Malikov.B","08:30"],
            "Extimollik va statistika":['223','Labaratoriya','Bozorqulov.A','10:00'],
            "Dasturiy injeneringga kirish":["107","Ma'ruza","Shodmonov.I","11:30"]
        },
        "Chorshanba" : {
            "Kompyuterni tashkil etilishi":["212A","Ma'ruza","Jalilov.M","08:30"],
            "Extimollik va statistika":['223','Amaliy','Dilshodov.A','10:00'],
            "Web dasturlashga kirish":["107","Labaratoriya","Raximov.Q","11:30"],
            "Dasturiy injeneringga kirish":["107","Ma'ruza","Shodmonov.I","13:30"]
        },
        "Payshanba" : {
            "Web dasturlashga kirish":["107","Ma'ruza","Malikov.B","08:30"],
            "Extimollik va statistika":['223','Labaratoriya','Bozorqulov.A','10:00'],
            "Dasturiy injeneringga kirish":["107","Ma'ruza","Shodmonov.I","11:30"],
            "Algoritmlarni loyihalash":["116A","Ma'ruza","Umarov.Sh","13:30"]
        },
        "Juma" : {
            "Extimollik va statistika":['223','Labaratoriya','Bozorqulov.A','08:30'],
            "Algoritmlarni loyihalash":["116A","Ma'ruza","Umarov.Sh","10:00"]
        }
    }
    
}   
    def __init__(self,kurs,sana):
        assert 1<=kurs<=4,"kursingizni xato kiritdingiz"
        self.kurs = kurs
        self.sana = sana
        
    def oquv_reja(self):
        semestr = int(input("Qaysi semestr fanlarini ko'rasiz 1/2/3/4: "))
        if semestr==1:
            print("1-semestr:")
            for i in range(len(Oquv_reja.__fanlar1)):
                print(f"{i+1}.{Oquv_reja.__fanlar1[i]}")
        elif semestr==2:
            print("2-semestr:")
            for i in range(len(Oquv_reja.__fanlar2)):
                print(f"{i+1}.{Oquv_reja.__fanlar2[i]}")
        elif semestr==3:
            print("3-semestr:")
            for i in range(len(Oquv_reja.__fanlar3)):
                print(f"{i+1}.{Oquv_reja.__fanlar3[i]}")
        elif semestr==4:
            print("4-semestr:")
            for i in range(len(Oquv_reja.__fanlar4)):
                print(f"{i+1}.{Oquv_reja.__fanlar4[i]}")
        
    def dars_jadvali(self,semestr):
        if semestr==1:
            for k in Oquv_reja.__darsning_jadvali["semestr_1"].keys():
                sanoq = 1
                print(125*"-")
                print(k.upper())
                for i,j in Oquv_reja.__darsning_jadvali["semestr_1"][k].items():
                    print(f"{sanoq}.{i}\n{j[0]} / {j[1]} / {j[2]} / {j[3]}")
                    sanoq += 1
        elif semestr==2:
            for k in Oquv_reja.__darsning_jadvali["semestr_2"].keys():
                sanoq = 1
                print(125*"-")
                print(k.upper())
                for i,j in Oquv_reja.__darsning_jadvali["semestr_2"][k].items():
                    print(f"{sanoq}.{i}\n{j[0]} / {j[1]} / {j[2]} / {j[3]}")
                    sanoq += 1
        elif semestr==3:
            for k in Oquv_reja.__darsning_jadvali["semestr_3"].keys():
                sanoq = 1
                print(125*"-")
                print(k.upper())
                for i,j in Oquv_reja.__darsning_jadvali["semestr_3"][k].items():
                    print(f"{sanoq}.{i}\n{j[0]} / {j[1]} / {j[2]} / {j[3]}")
                    sanoq += 1
        elif semestr==4:
            for k in Oquv_reja.__darsning_jadvali["semestr_4"].keys():
                sanoq = 1
                print(125*"-")
                print(k.upper())
                for i,j in Oquv_reja.__darsning_jadvali["semestr_4"][k].items():
                    print(f"{sanoq}.{i}\n{j[0]} / {j[1]} / {j[2]} / {j[3]}")
                    sanoq += 1
        else:
            print("Kursni xato kiritdingiz!")
            
    def dars_jadvalini_yangilash(self,semestr):
        buyruq = int(input(f"Kerakli indexni tanlang:\n1.Qo'shish\n2.O'chirish\n"))
        hafta_kuni = input("Hafta kuni: ").capitalize()
        fan_nomi = input("To'liq fan nomi: ").capitalize()
        if buyruq==1:
            Oquv_reja.__darsning_jadvali["semestr_"+str(semestr)][hafta_kuni][fan_nomi] = [input("Xona: "),input("Dars o'tish turi "),input("O'qituvchi: "),input("Boshlanish vaqti: ")]
            print("Muvofaqiyatli qo'shildi")
        elif buyruq==2:
            Oquv_reja.__darsning_jadvali["semestr_"+str(semestr)][hafta_kuni].pop(fan_nomi)
            print("Muvofaqiyatli o'chirildi")
        else:
            print("Xato buyruq kiritdingiz!")
            
    def nazorat_jadvaliga_qoshish(self):
        (Oquv_reja.__umumiy_nazorat).append(f"{input('Nazorat turi: ')} nazorat\n\nFan: {input('Fan nomi: ')}\nO'qituvchi: {input('Oqituvchi: ')}\nAuditoriya: {input('Auditoriya: ')}")
        
    def nazorat_jadvali(self):
        if len(Oquv_reja.__umumiy_nazorat)==0:
            print("Xech narsa topilmadi")
        else:
            for i in range(len(Oquv_reja.__umumiy_nazorat)):
                print(125*"-")
                print(f"{Oquv_reja.__umumiy_nazorat[i]}",end="\n\n")
       
    def mb_qoyish(self):
        (Oquv_reja.__umumiy_davomat).append(f"{(str(self.semestri)+'-semestr').ljust(15)}{self.sana.center(20)}{input('Fan nomi: ').center(25)}{input('Mashgulot nomi: ').center(20)}{input('Sababli: ').center(10)}{input('Soati: ').center(10)}{input('Oqituvchi ismi: ').rjust(16)}")
        
    def davomat(self):
        if len(Oquv_reja.__umumiy_davomat)==0:
            print("Xech narsa topilmadi")
        else:
            print("Semestr".ljust(15)+"Dars sanasi".center(20)+"Fanlar".center(25)+"Mashg'ulot".center(20)+"Sababli".center(10)+"Soatlar".center(10)+"Xodim".rjust(16))
            for i in range(len(Oquv_reja.__umumiy_davomat)):
                print(f"{Oquv_reja.__umumiy_davomat[i]}",end="\n\n")
        
    def imtihonlar(self):
        print("Xech narsa topilmadi")
        
    def reyting_daftarcha_ozgartirish(self):
        semestrlar = int(input("Qaysi semestr fanlarini o'zgartirasiz? 1/2/3/4: "))
        semestr = None
        if semestrlar==1:
            semestr = "semestr_1"
            print("1-semestr".center(125),end="\n\n")
            k = 1
            for i in Oquv_reja.__reyting_daftar["semestr_1"].keys():
                print(f"{k}.{i}")
                k += 1
        elif semestrlar==2:
            semestr = "semestr_2" 
            print("2-semestr".center(125),end="\n\n")
            k = 1
            for i in Oquv_reja.__reyting_daftar["semestr_2"].keys():
                print(f"{k}.{i}")
                k += 1
        elif semestrlar==3:
            semestr = "semestr_3" 
            print("3-semestr".center(125),end="\n\n")
            k = 1
            for i in Oquv_reja.__reyting_daftar["semestr_3"].keys():
                print(f"{k}.{i}")
                k += 1
        elif semestrlar==4:
            semestr = "semestr_4" 
            print("4-semestr".center(125),end="\n\n")
            k = 1
            for i in Oquv_reja.__reyting_daftar["semestr_4"].keys():
                print(f"{k}.{i}")
                k += 1
        if semestr:
            fan = input("Qaysi fanni o'zgartirasiz to'liq yozing: ").capitalize()
            Oquv_reja.__reyting_daftar[semestr][fan]["fan_turi"] = input("Fan turi: ").capitalize()
            Oquv_reja.__reyting_daftar[semestr][fan]["yuklama"] = input("Yuklama soati: ")
            Oquv_reja.__reyting_daftar[semestr][fan]["kredit"] = input("Kredit: ")
            ball = input("Ball: ")
            Oquv_reja.__reyting_daftar[semestr][fan]["ball"] = ball
            if match(r"(9[0-9]$|100)",ball):
                Oquv_reja.__reyting_daftar[semestr][fan]["baho"] = "5"
            elif match(r"(8[0-9]$|90)",ball):
                Oquv_reja.__reyting_daftar[semestr][fan]["baho"] = "4"
            else:
                Oquv_reja.__reyting_daftar[semestr][fan]["baho"] = "3"
            print("Muvofaqiyatli o'zgartirildi")
        else:
            print("Semestr indexsini noto'g'ri kiritdingiz!")

    def reyting_daftarcha(self):
        semestr = int(input("Qaysi semestr fanlarini ko'rasiz 1/2/3/4: "))
        if semestr==1:
            print("1-semestr".center(125),end="\n\n")
            print("Fanlar".ljust(30),"Fan turi".center(20),"Yuklama".center(20),"Kredit".center(20),"Ball".center(20),"Baho".rjust(12))
            print()
            for i in Oquv_reja.__reyting_daftar["semestr_1"].keys():
                print(f"{i}".ljust(30),f"{Oquv_reja.__reyting_daftar['semestr_1'][i]['fan_turi']}".center(20),f"{Oquv_reja.__reyting_daftar['semestr_1'][i]['yuklama']}".center(20),f"{Oquv_reja.__reyting_daftar['semestr_1'][i]['kredit']}".center(20),f"{Oquv_reja.__reyting_daftar['semestr_1'][i]['ball']}".center(20),f"{Oquv_reja.__reyting_daftar['semestr_1'][i]['baho']}".rjust(12))
        elif semestr==2:
            print("2-semestr".center(125),end="\n\n")
            print("Fanlar".ljust(30),"Fan turi".center(20),"Yuklama".center(20),"Kredit".center(20),"Ball".center(20),"Baho".rjust(12))
            print()
            for i in Oquv_reja.__reyting_daftar["semestr_2"].keys():
                print(f"{i}".ljust(30),f"{Oquv_reja.__reyting_daftar['semestr_2'][i]['fan_turi']}".center(20),f"{Oquv_reja.__reyting_daftar['semestr_2'][i]['yuklama']}".center(20),f"{Oquv_reja.__reyting_daftar['semestr_2'][i]['kredit']}".center(20),f"{Oquv_reja.__reyting_daftar['semestr_2'][i]['ball']}".center(20),f"{Oquv_reja.__reyting_daftar['semestr_2'][i]['baho']}".rjust(12))
        elif semestr==3:
            print("3-semestr".center(125),end="\n\n")
            print("Fanlar".ljust(30),"Fan turi".center(20),"Yuklama".center(20),"Kredit".center(20),"Ball".center(20),"Baho".rjust(12))
            print()
            for i in Oquv_reja.__reyting_daftar["semestr_3"].keys():
                print(f"{i}".ljust(30),f"{Oquv_reja.__reyting_daftar['semestr_3'][i]['fan_turi']}".center(20),f"{Oquv_reja.__reyting_daftar['semestr_3'][i]['yuklama']}".center(20),f"{Oquv_reja.__reyting_daftar['semestr_3'][i]['kredit']}".center(20),f"{Oquv_reja.__reyting_daftar['semestr_3'][i]['ball']}".center(20),f"{Oquv_reja.__reyting_daftar['semestr_3'][i]['baho']}".rjust(12))
        elif semestr==4:
            print("4-semestr".center(125),end="\n\n")
            print("Fanlar".ljust(30),"Fan turi".center(20),"Yuklama".center(20),"Kredit".center(20),"Ball".center(20),"Baho".rjust(12))
            print()
            for i in Oquv_reja.__reyting_daftar["semestr_4"].keys():
                print(f"{i}".ljust(30),f"{Oquv_reja.__reyting_daftar['semestr_4'][i]['fan_turi']}".center(20),f"{Oquv_reja.__reyting_daftar['semestr_4'][i]['yuklama']}".center(20),f"{Oquv_reja.__reyting_daftar['semestr_4'][i]['kredit']}".center(20),f"{Oquv_reja.__reyting_daftar['semestr_4'][i]['ball']}".center(20),f"{Oquv_reja.__reyting_daftar['semestr_4'][i]['baho']}".rjust(12))
        else:
            print("Siz xato kiritdingiz")
            
    def fan_tanlovi(self):
        print("Xech narsa topilmadi")

        
        
        
class Talaba_malumoti:
    __buyruqlar = []
    __shartnomalar = []
    __stipendiya_li = 11518746
    __stipendiya_siz = 6382746 
    __tolov1 = 0
    __tolov2 = 0
    
    def __init__(self,oquv_yili,kurs,yonalish,semestr,shartnoma_turi,shartnoma_raqami):
        self.__oquv_yili = oquv_yili
        self.__kurs = kurs
        self.__yonalish = yonalish
        self.__semestr = semestr
        self.__shartnoma_turi = shartnoma_turi
        self.__shartnoma_raqami = shartnoma_raqami
    
    def buyruq_yaratish(self):
        buyruq_raqami = input("Buyruq raqami: ")
        buyruq_sanasi = input("Buyruq sanasi: ")
        buyruq_nomi = input("Buyruq nomi: ")
        buyruq_turi = input("Buyruq turi: ")
        yaratilganligi = input("Yaratilganligi: ")
        (Talaba_malumoti.__buyruqlar).append(f"Buyruq raqami: {buyruq_raqami}\nBuyruq sanasi: {buyruq_sanasi}\nBuyruq nomi: {buyruq_nomi}\nBuruq turi: {buyruq_turi}\nYaratilganligi: {yaratilganligi}\nYuklab olish")
       
    def buyruqni_ochirish(self):
        for i in range(len(Talaba_malumoti.__buyruqlar)):
            print(f"{i+1}.{Talaba_malumoti.__buyruqlar[i]}",end="\n\n")
            
        index = int(input("Qaysi indexdagi buyruqni o'chirasiz: "))
        
        if len(Talaba_malumoti.__buyruqlar)>=index:
            del Talaba_malumoti.__buyruqlar[index-1]
            print("Muvofaqiyatli o'chirildi")
        else:
            print("Bunday indexdagi buyruq yoq")
    
    def buyruqlar(self,):
        for buyruq in Talaba_malumoti.__buyruqlar:
            print(buyruq,end="\n\n")
            
    def kontrakt_tolash(self,summa,stipendiya_li_siz):
        k = stipendiya_li_siz.lower()
        if k=='stipendiyali':
            if Talaba_malumoti.__stipendiya_li>=summa:
                Talaba_malumoti.__stipendiya_li-= summa
                Talaba_malumoti.__tolov1 = 11518746 - Talaba_malumoti.__stipendiya_li
            else:
                print(f"Sizning qarzingiz {Talaba_malumoti.__stipendiya_li} so'm\nTo'liq shu summani kiriting!")
        elif k=='stipendiyasiz':
            if Talaba_malumoti.__stipendiya_siz>=summa:
                Talaba_malumoti.__stipendiya_siz-= summa
                Talaba_malumoti.__tolov2 = 6382746 - Talaba_malumoti.__stipendiya_siz
            else:
                print(f"Sizning qarzingiz {Talaba_malumoti.__stipendiya_siz} so'm\nTo'liq shu summani kiriting!")
        else:
            print("Sizda qarz mavjud emas")
            
    def shartnomalar(self,stipendiya_li_siz):
        if self.__shartnoma_turi.lower()=="kontrakt":
            if stipendiya_li_siz.lower()=='stipendiyali':
                print(f"O'quv yili: {self.__oquv_yili}\nShartnoma turi: Kontrakt\nShartnoma raqami: {self.__shartnoma_raqami}\nTo'landi: {Talaba_malumoti.__tolov1} so'm\nQarz: {Talaba_malumoti.__stipendiya_li} so'm\nYuklab olish")
            elif stipendiya_li_siz.lower()=='stipendiyasiz':
                print(f"O'quv yili: {self.__oquv_yili}\nShartnoma turi: Kontrakt\nShartnoma raqami: {self.__shartnoma_raqami}\nTo'landi: {Talaba_malumoti.__tolov2} so'm\nQarz: {Talaba_malumoti.__stipendiya_siz} so'm\nYuklab olish")
        else:
            print("Xech narsa topilmadi")
            
    def malumotnomalar(self):
        print("Xech narsa topilmadi")
        
    def talaba_hujjati(self):
        print(f"O'quv varaqa:\nKurs: {self.__kurs}-kurs\nO'quv yili: {self.__oquv_yili}\nSemestr: {self.__semestr}-semestr\nYuklab olish")
        print()
        print(f"Reyting daftarcha:\nMutaxasislik: {self.__yonalish}\nKurs: {self.__kurs}-kurs\nSemestr: {self.__semestr}-semestr\nYuklab olish")
        
    def bitiruv_ishi(self):
        print("Xech narsa topilmadi")
        
    def bitiruv_varaqasi(self):
        print("Xech narsa topilmadi")
        
        
        
        
class Xabarlar:
    __send_message = []
    __qoralama_xabarlar = []
    
    def kiruvchi_xabarlar():
        return "Xabar yo'q"

    def jonatilganlar(self):
        if len(Xabarlar.__send_message):
            for message in Xabarlar.__send_message:
                print(message,end="\n\n")
        else:
            print("Jo'natilgan xabarlar yo'q")
        
    def xabar_yaratish(self):
        kimga = input("Kimga: ").title()
        mavzu = input("Mavzu: ").title()
        xabar = input("Xabar yozing: ").title()
        (Xabarlar.__send_message).append(f"Kimga: {kimga}  /  Mavzu: {mavzu}\nXabar: {xabar}")
        
    def qoralama(self):
        kimga = input("Kimga: ").title()
        mavzu = input("Mavzu: ").title()
        xabar = input("Xabar yozing: ").title()
        (Xabarlar.__qoralama_xabarlar).append(f"Kimga: {kimga}  /  Mavzu: {mavzu}\nXabar: {xabar}")
        
    def qoralama_xabarlarni_korish(self):
        for message in Xabarlar.__qoralama_xabarlar:
            print(message,end="\n\n")

    def korzina(self):
        print("1.Jo'natilgan xabarlar:")
        for i in range(len(Xabarlar.__send_message)):
            print(f"{i+1}.{Xabarlar.__send_message[i]}",end="\n\n")
            
        print("2.Qoralama xabarlar:")
        for i in range(len(Xabarlar.__qoralama_xabarlar)):
            print(f"{i+1}.{Xabarlar.__qoralama_xabarlar[i]}",end="\n\n")
            
        bolim = int(input("Qaysi bolimdan o'chirasiz 1 yoki 2: "))
        index = int(input("Qaysi indexdagisini: "))
        
        if bolim==1:
            del Xabarlar.__send_message[index-1]
            print("Muvofaqiyatli o'chirildi")
        elif bolim==2:
            del Xabarlar.__qoralama_xabarlar[index-1]
            print("Muvofaqiyatli o'chirildi")
        else:
            print("1 yoki 2 ni tanlashingiz kerak edi!")

            
            
            
class Tizim:
    __tizimga_kirish_tarixi = 0
    __loginlar = []
    __sanalar = []
    def __init__(self,ism,familya,login,parol,pasport_raqam,sana):
        self.__ism = ism
        self.__familya = familya
        self.__login = login
        self.__parol = parol
        self.__pasport_raqam = pasport_raqam
        self.__sana = sana
        
        assert match(r"((([012][1-9]|10|20|30|31)\.(0[13578]|10|12)\.((?:19|20)[0-9]|2100))|(([012][1-9]|10|20|30)\.(0[469]|11)\.((?:19|20)[0-9]|2100))|(([012][1-9]|10|20)\.02\.(?:19|20)(?:[13579][26]|[02468][048])$)|(([0-2][1-8]|10|20|09|19)\.02\.((?:19|20)[0-9]|2100)))",self.__sana),"Sana noto'g'ri kiritildi!"
        assert match(r"\d{12}$",(self.__login)),"12 xonali login kiriting"
        assert match(r"A[A-Z]\d{7}$",(self.__pasport_raqam)),"Pasport raqam xato kiritildi"
        
        Tizim.__tizimga_kirish_tarixi += 1
        (Tizim.__loginlar).append(self.__login)
        (Tizim.__sanalar).append(self.__sana)
        
    def get_ism(self):
        return f"Ism: {self.__ism}"
    
    def get_familya(self):
        return f"Familya: {self.__familya}"
    
    def get_pasport_raqam(self):
        return f"Pasport raqam: {self.__pasport_raqam}"
    
    def get_sana(self):
        return f"Ism: {self.__sana}"
    
    def get_password(self):
        print(f"Parol: {self.__parol}")
        
    def update_parol(self,eski_parol,new_parol):
        if eski_parol==self.__parol:
            self.__parol = new_parol
            print("Muvofaqiyatli yangilandi!")
        else:
            print("Eski parol xato kiritildi!")
        
    def profil(self):
        return f"Ismi: {self.__ism}\nFamilya: {self.__familya}\nLogin: {self.__login}\nPasport raqam: {self.__pasport_raqam}"
    
    def kirish_tarixi(self):
        for i in range(Tizim.__tizimga_kirish_tarixi):
            print(f"Login: {Tizim.__loginlar[i]}    Holati: Muvofaqiyatli    Yaratilgan: {Tizim.__sanalar[i]}\n")


# In[54]:


farrux = Oquv_reja(2,"28.07.2022")
farrux1 = Talaba_malumoti("2021-2022",2,"Dasturiy injenering",4,"kontrakt","3922100527")
farrux2 = Xabarlar()
farrux3 = Tizim("Farrux","Sotivoldiyev","392201100621","1102002f","AC2196807","26.07.2022")


# In[55]:


farrux.dars_jadvali(4)


# In[56]:


farrux1.talaba_hujjati()


# In[57]:


farrux2.jonatilganlar()


# In[58]:


farrux3.kirish_tarixi()


# In[60]:


print(farrux3.profil())

