vanus = int(input("Sisestage enda vanus : "))
sugu = input("Sisestage enda sugu: ").lower()
trenn = int(input("Sisestage treeningu tüüp: "))

if sugu == "m":
    pulss = 220- vanus
if sugu == "n":
    pulss = (206 - vanus * 0.88)
    
if trenn == 1:
    pulss_min = round(pulss * 0.5)
    pulss_max = round(pulss * 0.7)
if trenn == 2:
    pulss_min = round(pulss * 0.7)
    pulss_max = round(pulss * 0.8)
if trenn == 3:
    pulss_min = round(pulss * 0.8)
    pulss_max = round(pulss * 0.87)

print("Pulsisagedus peaks olema vahemikus " + str(pulss_min) + " kuni " + str(pulss_max))