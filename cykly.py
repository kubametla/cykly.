zacatek = 3
konec = 10


for x in range(zacatek, konec, 2):
    print(x)
    if x == 0:
        break


    else:
        print("Cyklus je hotový")

    print("Funguješ?")
    j = 0
    while j < 3:
        print(f"Hodnota v proměnné j: {j}")
        j = j + 1
        zacatek = zacatek + 1
        
        if j == 2:
            break