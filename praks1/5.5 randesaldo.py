sisse = open("sisseranne.txt", encoding="UTF-8")
valja = open("valjaranne.txt", encoding="UTF-8")
asd = []
suurim = 0
i = 1
for rida in sisse:
    for ridaa in valja:
        asda = (int(rida) - int(ridaa))
        asd.append(asda)
        if asda > suurim:
            suurim = asda
            asdas = i
        i += 1
        break
print(asd)
print("Suurim positiivne rändesaldo oli " , asdas, ". aastal.")
    
