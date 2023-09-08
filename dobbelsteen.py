
aantal_zijden = int(input("Voer het aantal zijden van de dobbelsteen in: "))


while aantal_zijden > 1:
    ogen = 0


    for zijde in range(1, aantal_zijden + 1):
        ogen += zijde

    print(f"Het aantal ogen op de dobbelsteen met {aantal_zijden}-is: {ogen}")

    aantal_zijden = int(input("Voer het aantal zijden van de dobbelsteen in: "))

print("Het programma stopt omdat je een getal kleiner dan of gelijk aan 1 hebt ingevoerd.")