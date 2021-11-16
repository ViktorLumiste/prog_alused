fail = input("Palun sisestage failinimi: (jukebox, 80ndad, eesti_muusika, edm)")
faili = fail + ".txt"
tekst = open(faili, encoding="UTF-8")
print("Muusikapalade valak: ")
i = 1
for laul in tekst:
    print(i, "." , laul[:-1])
    i += 1
valik = int(input("Valige laulu järjekorranumber: "))
o = 1
tekst.close()
tekst = open(faili, encoding="UTF-8")
for laul in tekst:
    if valik == o:
        print("Mängitav muusikapala on ", laul)
        break
    else:
        o += 1
tekst.close()