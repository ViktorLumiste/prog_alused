ringid = int(input("Sisestage ringide arv: "))
i = 1
por = 0
while i <= ringid:
    por += i
    i += 1
print("Porgandite kogu arv on " + str(por) + ".")