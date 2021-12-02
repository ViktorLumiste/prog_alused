from easygui import *
arv1 = integerbox("Sisestage esimene täisarv lõigus 1-10")
nuppud = ["+", "-", "*"]
nupp = buttonbox("valige tehe", choices = nuppud)
arv2 = integerbox("Sisestage teine täisarv lõigus 1-10")
if nupp == "+":
    tulemus = arv1 + arv2
elif nupp == "*":
    tulemus = arv1 * arv2
elif nupp == "-":
    tulemus = arv1 - arv2
msgbox("Tehte tulemus on " + str(tulemus))