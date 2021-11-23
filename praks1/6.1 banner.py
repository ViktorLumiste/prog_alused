def banner(lause):
    reklaam = lause.upper()
    return(reklaam)

def reklaaam(korda):
    asd = banner(input("Sisestage reklaamilause: "))
    for i in range(1,korda + 1):
        print(asd)
        
kord = int(input("Mitu korda soovite reklaamlauset kuvada? "))
print(reklaaam(kord))