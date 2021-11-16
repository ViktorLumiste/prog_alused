fail = open("rebased.txt", encoding="UTF-8")
soov = int(input("Palun sisestage, millise aasta andmeid vajate: "))

vastuvõetud = []
aasta = 2011
for rida in fail:
    vastuvõetud.append(int(rida))
    if soov == aasta:
        break
    else:
        aasta += 1
print(aasta, " aastal oli vastuvõetuid ", rida)
    
fail.close()