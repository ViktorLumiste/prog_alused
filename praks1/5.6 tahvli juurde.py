fail = input("Sisestage failinimi: ")
nimed = open(fail , encoding="UTF-8")
from datetime import *

nimii = int((datetime.now().day))
i = 1
for nimi in nimed:
    if i == nimii:
        print("Tavhli juurde tuleb: ", nimi)
        break
    else:
        i += 1