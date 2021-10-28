ringid = int(input("Sisestage ringide arv: "))
i = 1
a = 0
por = 0
while i < ringid:
    i += 2
    por = por + 2 + a
    a += 2
print("Porgandite kogu arv on " + str(por) + ".")
 