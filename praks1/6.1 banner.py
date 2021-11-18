#def banner(lause):
    #reklaam = lause.upper()
    #return(reklaam)
#print (banner("osta ja sa ei kahatse!"))
def reklaaam(asd):
    kord = int(input("Mitu korda soovite reklaamlauset kuvada? "))
    asd = asd.upper()
    for i in range(1,kord + 1):
        print(asd)
reklaaam("ostan, müün ja vahetan")