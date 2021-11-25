fail = input("Sisestage failinimi: ")
telegramm = open(fail, encoding = "UTF-8")
sonum = "a"
for rida in telegramm:
    sonum = rida
telegram = []
for taht in sonum:
    taht = taht.upper()
    if taht == "Ä":
        telegram.append("AE")
    elif taht == "Õ":
        telegram.append("OE")
    elif taht == "Ö":
        telegram.append("OE")
    elif taht == "Ü":
        telegram.append("UE")
    else:
        telegram.append(taht)
telegrammm = " "
for täht in telegram:
    telegrammm = telegrammm + täht
print(str(telegrammm))