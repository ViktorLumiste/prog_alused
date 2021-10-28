from random import randint
valik = input("Kas soovite valida ise kohta? Y/N").upper()
if valik == "Y":
    valik_aken = input('Kas soovite istuda akna ääres ("Aken") või mitte ("Vahekäigukoht")?')
    print("Istekoht valitud. " + valik_aken)
elif valik == "N":
    if randint(1, 3) == 1:
        print("Istekoht loositi. Aknakoht")
    else:
        print("Istekoht loositi. Vahekäigukoht")
else:
    print("Proovige uuesti")