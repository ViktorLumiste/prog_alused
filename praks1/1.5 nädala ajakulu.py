ainepunkt = int(input("Sisestage ainepunktide arv: "))
nadal_arv = int(input("Sisestage nädalate arv: "))
ajakulu = ainepunkt * 26
nadal_ajakulu = ajakulu / nadal_arv
vastus = round(nadal_ajakulu)
print(vastus)