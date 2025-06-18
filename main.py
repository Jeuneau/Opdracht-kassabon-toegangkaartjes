class Main:
    def __init__(self):
        self.bedrag1 = 5
        self.bedrag2 = 10
        self.bedrag3 = 8
        

    print('Hoeveel kaarten wil je kopen?')
    aantal_kaarten = int(input('Aantal kaarten: ')) #aantal kaarten invoeren
    for i in range(aantal_kaarten): #vragen naar de leeftijd en prijzen toekennen
        print('Hoe oud ben je?')
        leeftijd = int(input('Leeftijd: ')) 
        if leeftijd < 4 and aantal_kaarten < 5: #tarieven toekennen
            print('Hoeveel kinderen zijn er onder de 4 jaar?')
            aantal_kleuters = int(input('Aantal kinderen onder 4 jaar:  '))
            
            if aantal_kleuters == 0:
                print('Je hoeft niets te betalen.')
        elif leeftijd >= 4 and leeftijd <= 18:
            bedrag1 = 5
            print('Hoeveel kinderen zijn er tussen de 4 en 18 jaar?')
            aantal_kinderen = int(input('Aantal kinderen tussen 4 en 18 jaar: '))
            bedrag1_ = bedrag1 * aantal_kinderen
            print('Je moet ' + str(bedrag1_) + ' euro betalen voor de kinderen.')
        elif leeftijd >= 19 and leeftijd <= 65:
            bedrag2 = 10
            print('Hoeveel volwassenen zijn er tussen de 19 en 65 jaar?')
            aantal_volwassenen = int(input('Aantal volwassenen: '))
            bedrag2_ = bedrag2 * aantal_volwassenen
            print('Je moet ' + str(bedrag2_) + ' euro betalen voor de volwassenen.')
        elif leeftijd > 65:
            bedrag3 = 8
            print('Hoeveel senioren (65-plussers) zijn er?')
            aantal_senioren = int(input('Aantal senioren: '))
            bedrag3_ = bedrag3 * aantal_senioren
            print('Je moet ' + str(bedrag3_) + ' euro betalen voor de senioren.')

    if(aantal_kaarten > 5):
        print('Je krijgt 5 euro korting op de totale prijs.')     
    totaal_bedrag = bedrag1_ + bedrag2_ + bedrag3_ - 5 #totaalbedrag berekenen
    print('Het totaalbedrag is: ' + str(totaal_bedrag) + ' euro.')
    print("U moet nog een parkeerkaart kopen voor 9.50 euro.")
    totaal_bedrag_ = totaal_bedrag + 9.50
    print("Het totaalbedrag inclusief parkeerkaart is: " + str(totaal_bedrag_) + ' euro.') #totaalbedrag inclusief parkeerkaart
    print("Hierbij uw kassabon en uw ticket(s).") #kassabon eventueel nog grafisch maken
    print("Bedankt voor uw bezoek en tot ziens!")
    
    
