def banner(lause = input("Sisestage reklaamilause: ")):
    reklaam = lause.upper()
    return(reklaam)

def reklaaam():
    kord = int(input("Mitu korda soovite reklaamlauset kuvada? "))
    asd = banner()
    for i in range(1,kord + 1):
        print(asd)
reklaaam()