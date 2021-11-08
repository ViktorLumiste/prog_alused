taisarv = int(input("Sisestage täisarv: "))
i = 1
nisu = 1
tera = 0
if taisarv > 64:
    print("Liiga suur arv!")
elif taisarv < 1:
    print("Arv on negativne!")    
else:
    while i < taisarv:
        tera = nisu * 2
        nisu = tera
        i += 1
    print("Nisuteri " + str(taisarv) + ". ruudu eest: " + str(nisu))
