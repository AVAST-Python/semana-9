def aguja_en_pajar_1(pajar):
    contador = 0
    for cosa in pajar:
        if cosa == "aguja":
            return contador
        contador += 1



def aguja_en_pajar_2(pajar):
    for i, elemento in enumerate(pajar):
        if elemento == "aguja":
            return i



def aguja_en_pajar(pajar):
    return pajar.index("aguja")



PAJAR_1 = [1, "apple", 3.14, "banana", "aguja", 7]
PAJAR_2 = ["orange", 42, "grape", "aguja", 9.8, "pear"]
PAJAR_3 = ["aguja", 1, 2, "patata"]
PAJAR_4 = [1, 2, "aguja"]

print(aguja_en_pajar(PAJAR_1)) # 4
print(aguja_en_pajar(PAJAR_2)) # 3
print(aguja_en_pajar(PAJAR_3)) # 0
print(aguja_en_pajar(PAJAR_4)) # 2
