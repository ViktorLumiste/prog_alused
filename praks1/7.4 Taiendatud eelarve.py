fail = input("Sisesta failinimi: ")
nimikiri = open(fail, encoding = "UTF-8")
def eelarve(külalised):
    rent = 55
    summa = külalised * 10 + rent
    return summa
tulevad = 0
eitea = 0
for inimene in nimikiri:
    for mark in inimene:
        if mark == "+":
            tulevad += 1
        if mark == "?":
            eitea += 1
        else:
            break
kokku = tulevad + eitea
print("Kutsutud on" , kokku, "inimest")
print(tulevad, "inimest tuleb")
print(eitea, "inimest ei tea veel")
print("Maksimaalne eelarve: " + str(eelarve(kokku)))
print("Minimaalne eelarve: " + str(eelarve(tulevad)))

