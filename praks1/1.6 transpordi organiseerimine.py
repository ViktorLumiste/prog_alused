inim_arv = int(input("Sisestage inimeste arv: "))
buss_koht_arv = int(input("Sisestage bussi kohtade arv: "))
inimeste_jaak = inim_arv % buss_koht_arv
buss_arv = (inim_arv - inimeste_jaak) / buss_koht_arv
print("Vaja läheb " + str(int(buss_arv)) + " bussi.")
print("Maha jääb " + str(inimeste_jaak) + " inimest.")