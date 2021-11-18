def eelarve(kutsutud = int(input("Mitu inimest on kutsutud? ")), tuleb = int(input("Mitu inimest tuleb? "))):
    rent = 55
    mini = tuleb * 10 + rent
    maxi = kutsutud * 10 + rent
    print("Maksimaalne eelarve: ", maxi)
    print("Minimaalne eelarve: ", mini)
eelarve()
    