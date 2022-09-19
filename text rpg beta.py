from random import randint
liv = 10
mat = 0
xp = 0


våpen = input("Du finner en kiste. Hva inneholder den? --- ")
print("Du fant ditt nye våpen", våpen)
input()
print("Du finner enda en kiste, hva fant du der?")
extra = input("1: litt mat, 2: delete knapp --- ")

while True:
  if extra == "1":
    print("Du fant litt mat!")
    pålegg = "spis litt mat"
    mat +=1
    break

  elif extra == "2":
    print("Du fant en delete knapp!")
    pålegg = "bruk delete knapp"
    break
  else:
    extra = input("Ugjyldig svar, prøv på nytt --- ")

input()
print("Du møter på et ondt tre! (5 liv)")
tre = 5


while tre > 0:
  input()
  liv = str(liv); tre = str(tre)
  print("[liv: " + liv + " --- fiende liv: " + tre + "]")
  print("Hva gjør du?")
  liv = int(liv); tre = int(tre)

  if extra == "0":
    attack = input("1: bruk "+ våpen + ", 3: prøv å løpe vekk --- ")

  else:
    attack = input("1: bruk "+ våpen + ", 2: "+ pålegg + ", 3: prøv å løpe vekk --- ")
  print()

  if attack == "1":
    if våpen == "ild":
      print("Du brente opp treet")
      tre -=999

    else:
      kritt = randint(1,8)
      if kritt <= 2:
        print("Du slot treet med", våpen , "HARDT")
        print("Treet gikk ned med 3 liv")
        tre -= 3
      elif kritt == 8:
        print("Du slot treet med", våpen , "veldig svakt")
        print("Treet gikk ned med 1 liv")
        tre -= 1
      else:
        print("Du slo treet med", våpen)
        print("Treet gikk ned 2 liv")
        tre -= 2
  
  elif attack == "2":
    if extra == "1" and mat > 0:
      print("Du spiste mat og gikk opp med 10 liv")
      print("Du er nå tom for mat")
      mat -= 1
      liv += 10
      extra = "0"

    elif extra == "2":
      print("Du brukte delete knappen")
      tre -=999
  
  elif attack == "3":
    løp = randint(1,6)
    if løp == 1:
      break
    else:
      print("Du snublet og ble i kampen")
  
  else:
    print("Du skjønte ikke hva du skulle gjøre og brukte opp runden din")


  if tre <= 0:
    break
  
  input()
  eple = randint(1,4)
  if eple == 1:
    print("Treet spiste et eple")
    print("Den gikk opp med 3 liv")
    tre += 3
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

  if liv <1:
    input()
    print("Du døde tragisk in en tre ulykke")
    exit()

if tre <= 0:
  input()
  print("Treet døde tragisk")
  if våpen == "ild":
    print("Du gikk opp med 69 xp")
    xp += 69
  else:
    print("Du gikk opp med 5 xp")
    xp += 5
else:
  print("Du slapp unna treet")
  print("Du fikk ingen xp")