def kuu_nimi(jarjekord):
    kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    return kuud[int(jarjekord) - 1]
def kuupäev_sõnena(kuupäev):
    kuupaevad = kuupäev.split(".")
    kuupaev = kuupaevad[0] + "." + kuu_nimi(kuupaevad[1]) + " " + kuupaevad[2] + ". a"
    return kuupaev
kuupäev = input("Sisesta kuupäev kujul DD.MM.YYYY: ")

print(str(kuupäev_sõnena(kuupäev)))