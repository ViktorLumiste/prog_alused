nimi = input("Sisestage oma nimi: ")
lub_kiirus = int(input("Sisestage lubatud kiirus (km/h): "))
teg_kiirus = int(input("Sisestage tegelik kiirus(mk/h): "))
ule_kiirus = teg_kiirus - lub_kiirus
trahv = ule_kiirus * 3
trahv_min = min(190, trahv)
print(nimi + ", kiirus ületamise eest on teie trahv " + str(trahv_min) + "eurot.")
