class Main:
    doorgaan = True

    while doorgaan:
        totaalbedrag = 0

        aantal_gasten = int(input("Hoeveel gasten bezoeken het pretpark? "))
        klantlijst = [str(i) for i in range(1, aantal_gasten + 1)]

        for i in klantlijst:
            leeftijd = int(input(f"Wat is de leeftijd van gast {i}? "))

            #Bepaal de toegangsprijs op basis van de leeftijd
            if leeftijd < 4:
                prijs = 0
            elif leeftijd < 12:
                prijs = 10
            elif leeftijd < 65:
                prijs = 20
            else:
                prijs = 15

            print (f"De toegangsprijs voor gast {i} is: €{prijs}")
            totaalbedrag += prijs

        #Vraag naar parkeerkaartje
        parkeerkaartje = input("\nWilt u een parkeerkaartje kopen voor €5? (j/n): ")
        if parkeerkaartje.lower() == 'j':
            totaalbedrag += 5
            print("Het parkeerkaartje is toegevoegd aan het totaalbedrag.")

        #Toon totaalbedrag
        print(f"\n Totaal te betalen bedrag is: €{totaalbedrag:.2f}")

        #Vraag of gebruiker opnieuw wil beginnen
        opnieuw = input("\nWilt u nog een keer tickets invoeren? (j/n): ")
        if opnieuw.lower() != 'j':
            doorgaan = False
            print("Bedankt en tot ziens!")