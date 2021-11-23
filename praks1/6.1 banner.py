def banner(lause):
    return lause.upper()
korda = int(input("Mitu korda soovite reklaamilauset kuvada? "))
lause = input("Sisestage reklaamilause: ")
for i in range(0, korda):
    print(banner(lause))