fail = open("rebased.txt", encoding="UTF-8")
soov = int(input("Palun sisestage, millise aasta andmeid vajate: "))

aasta = 2011
for rida in fail:
    if soov == aasta:
        break
    aasta += 1
print(aasta, " aastal oli vastuvõetuid ", rida)
fail.close()