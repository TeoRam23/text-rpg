from random import randint

def start():
    global liv, mat, xp, våpen, extra, vei, delete, matt, dell, uliv, enemy, gyllent, nope

    liv = 10
    mat = 0
    delete = 0
    xp = 0
    uliv = 3
    nope = 0

    print()
    våpen = input("Du finner en kiste. Hva inneholder den? --- ")
    print(f"Du fant ditt nye våpen {våpen}")
    input()
    print("Du finner enda en kiste, hva fant du der?")
    extra = input("1: litt mat, 2: delete knapp --- ")

    while True:
        if extra == "1":
            print("Du fant litt mat!")
            matt = "spis litt mat"
            mat += 1
            break

        elif extra == "2":
            print("Du fant en delete knapp!")
            dell = "bruk delete knapp"
            delete += 1
            break
        else:
            extra = input("Ugjyldig svar, prøv på nytt --- ")

    input() 
    gyllent = randint(1,10)
    if gyllent == 1:
        enemy = "Gyllent Tre"
    else:
        enemy = "Tre"
    print(f"Du møter på et ondt {enemy}! (5 liv)")
   

    combat()


    if uliv < 1:
        input()
        print("Treet døde tragisk")
        if våpen == "ild":
            print("Du gikk opp med 69 xp")
            xp += 69
        elif gyllent == 1:
            print("Du gikk opp med 50 xp")
            xp += 50
        else:
            print("Du gikk opp med 5 xp")
            xp += 5
    else:
        print("Du slapp unna treet")
        print("Du fikk ingen xp")
    
    input()
    print("Du ser et skilt hvor veien deler seg i to inn i en skog, hvor vil du dra?")
    vei = input("1: mer xp, 2: mer mat --- ")
    while True:
        if vei == "1":
            print("Du valgte å gå veien med mer xp")
            xproom()

        elif vei == "2":
            print("Du valgte å gå veien med mer mat")
            matroom()
            
        else:
            vei = input("Ugjyldig svar, prøv på nytt --- ")

def room3():
    global nope
    input()
    print("Du kom deg ut av skogen, hva vil du gjøre?")
    veg = input("1: dra til soppelandsbyen, 2: dra tilbake for mer xp --- ")
    while True:
        if veg == "1":
            landsby()
            exit()
        elif veg == "2" and nope == 2:
            veg = input("Du har drept for mange Gyldne Busker, plis bare dra til landsbyen --- ")
        elif veg == "2":
            print("Du valgte å dra tilbake for mer xp")
            nope += 1
            xproom()
        else:
            veg = input("Ugjyldig svar, prøv på nytt --- ")


def landsby():
    global liv, mat, xp, våpen, extra, vei, delete, matt, dell, uliv, enemy, gyllent, nope, blomst, venn, nah
    nah = 0
    input()
    print("Du kom deg til landsbyen og oppdager at den er angrepet av en ond blomst!")
    print("Hva gjør du nå?")
    blomst = input("1: bekjemp blomsten, 2: prøve å slå lag med blomsten --- ")
    while True:
        if blomst == "1":
            enemy = "Blomst"
            combat()

        elif blomst == "2":
            venn = randint(1,2)
            if venn == 1:
                print("Du slo lag med blomsten og beseiret soppelandsbyen")
                print("Du gikk opp med 50 xp")
            elif venn == 2 and nah <2:
                nah += 1
                print("Blomsten ville ikke slå lag med deg,")
                blomst = input("1: bekjemp blomsten, 2: prøv å slå lag med blomsten igjen --- ")
                
            elif venn == 2 and nah >=2:
                print("Blomsten angrep deg og du gikk ned med 3 liv")
                liv -= 3
                input()
                print("Du døde tragisk av pollen allergi")
                input()
                print("Start på nytt?")
                reset = input("1: start på nytt, 2: avslutt --- ")
                while True:
                    if reset == "1":
                        start()
                    elif reset == "2":
                        exit()
                    else:
                        reset = input("Ugjyldig svar, prøv på nytt --- ")


        else:
            blomst  = input("Ugjyldig svar, prøv på nytt --- ")




def combat():
    global liv, mat, xp, våpen, extra, delete, matt, dell, uliv, enemy

    uliv =5
    while uliv > 0:
        input()
        liv = str(liv); uliv = str(uliv)
        print(f"[liv: {liv} --- fiende liv: {uliv}]")
        print("Hva gjør du?")
        liv = int(liv); uliv = int(uliv)

        if mat == 0 and delete == 0:
            attack = input(f"1: bruk {våpen}, 4: prøv å løpe vekk --- ")

        elif mat > 0 and delete == 0:
            attack = input(f"1: bruk {våpen}, 2: {matt}, 4: prøv å løpe vekk --- ")
        
        elif delete > 0 and mat == 0:
            attack = input(f"1: bruk {våpen}, 3: {dell}, 4: prøv å løpe vekk --- ")

        elif mat > 0 and delete > 0:
            attack = input(f"1: bruk {våpen}, 2: {matt}, 3: {dell}, 4: prøv å løpe vekk --- ")


        print()

        if attack == "1":
            if våpen == "ild" or våpen == "Ild":
                print(f"Du brant opp {enemy}")
                uliv -=999

            else:
                kritt = randint(1,8)
                if kritt <= 2:
                    print(f"Du slo {enemy} med {våpen} HARDT")
                    print(f"{enemy} gikk ned med 3 liv")
                    uliv -= 3
                elif kritt == 8:
                    print(f"Du slo {enemy} med {våpen} veldig svakt")
                    print(f"{enemy} gikk ned med 1 liv")
                    uliv -= 1
                else:
                    print(f"Du slo {enemy} med {våpen}")
                    print(f"{enemy} gikk ned 2 liv")
                    uliv -= 2
        
        elif attack == "2" and mat > 0:
            print("Du spiste mat og gikk opp med 10 liv")
            print("Du er nå tom for mat")
            mat -= 1
            liv += 10
            extra = "0"

        elif attack == "3" and delete > 0:
            print("Du brukte delete knappen")
            uliv -=999
        
        elif attack == "4":
            løp = randint(1,6)
            if løp == 1:
                break
            else:
                print("Du snublet og ble i kampen")
        
        else:
            print("Du skjønte ikke hva du skulle gjøre og brukte opp runden din")


        if uliv <= 0:
            break
        
        input()
        eple = randint(1,4)
        if enemy == "Tre" or enemy == "Gyllent Tre":
            if eple == 1:
                print("Treet spiste et eple")
                print("Den gikk opp med 3 liv")
                uliv += 3
            else:
                ukrit = randint(1,8)
                if ukrit <= 2:
                    print("Treet brukte rota si HARDT")
                    print("Du gikk ned med 7 liv")
                    liv -= 7
                elif ukrit == 8:
                    print("Treet brukte rota si svakt")
                    print("Du gikk ned med 3 liv")
                    liv -= 3
                else:
                    print("Treet brukte rota si")
                    print("Du gikk ned med 5 liv")
                    liv -= 5

        elif enemy == "Gylden Busk" or enemy == "Fleskete Busk":
            if eple == 1:
                print("Busken spiste et bær")
                print("Den gikk opp med 2 liv")
            else:
                ukrit = randint(1,8)
                if ukrit <= 2:
                    print("Busken brukte løvet sitt HARDT")
                    print("Du gikk ned med 2 liv")
                    liv -= 2
                elif ukrit == 8:
                    print("Busken brukte løvet sitt svakt")
                    print("Du gikk ikke ned med liv")
                    
                else:
                    print("Busken brukte løvet sitt")
                    print("Du gikk ned med 1 liv")
                    liv -= 1

        if liv <1 and enemy == "Tre" or enemy == "Gyllent Tre":
            input()
            print("Du døde tragisk in en tre ulykke")
            input()
            print("Start på nytt?")
            reset = input("1: start på nytt, 2: avslutt --- ")
            while True:
                if reset == "1":
                    start()
                elif reset == "2":
                    exit()
                else:
                    reset = input("Ugjyldig svar, prøv på nytt --- ")

        if liv <1 and enemy == "Gylden Busk" or enemy == "Fleskete Busk":
            input()
            print("Du døde tragisk i grøfta")
            input()
            print("Start på nytt?")
            reset = input("1: start på nytt, 2: avslutt --- ")
            while True:
                if reset == "1":
                    start()
                elif reset == "2":
                    exit()
                else:
                    reset = input("Ugjyldig svar, prøv på nytt --- ")

def xproom():
    global liv, mat, xp, våpen, extra, vei, delete, matt, dell, uliv, enemy, gyllent
    input()
    print("Du møter på en ond Gylden Busk!")
    enemy = "Gylden Busk"
    combat()

    if uliv < 1:
        input()
        print("Busken døde tragisk")
        if våpen == "ild":
            print("Du gikk opp med 69 xp")
            xp += 69
        else:
            print("Du gikk opp med 25 xp")
            xp += 25
    else:
        print("Du slapp unna busken")
        print("Du fikk ingen xp")
    
    room3()

def matroom():
    global liv, mat, xp, våpen, extra, vei, delete, matt, dell, uliv, enemy, gyllent
    input()
    print("Du møter på en ond Fleskete Busk!")
    enemy = "Fleskete Busk"
    combat()

    if uliv < 1:
        input()
        print("Busken døde tragisk")
        print("Du fikk 1 matbit")
        mat += 1
        matt = "spis litt mat"

    else:
        print("Du slapp unna busken")
        print("Du fikk ingen mat")

    room3()
    
    
    


start()