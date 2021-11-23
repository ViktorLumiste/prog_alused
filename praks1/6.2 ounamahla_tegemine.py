def mahlapakide_arv(kogu):
    arv = (kogu) * 0.4 / 3
    arv = round(arv)
    return arv
kogus = int(input("Mitu kilogrammi õunu on? "))
print(mahlapakide_arv(kogus))
