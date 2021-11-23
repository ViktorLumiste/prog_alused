def pronksikarva_summa(täisarvud):
    summa = 0
    for munt in täisarvud:
        if int(munt) <= 5:
            summa += int(munt)
    return summa
fail = input("Sisestage failinimi: ")
mundid = open(fail + ".txt", encoding="UTF-8")
print("Hoiupõrsasse läheb", pronksikarva_summa(mundid), "senti.")