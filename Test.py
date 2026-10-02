print("""
Hej och välkommen till mitt prov om programmeringens samhällspåverkan. 
    
      |      |

     \        /
      \______/
      Av Jonte

      """)
points = 0
print("""
1. Vilka arbetade främst med programmering på 1940-talet?
    A) Ex soldater
    B) Män
    C) Kvinnor
    D) Norrmän

""")
svar = input("Svar: ")
if svar == "C" or svar == "c":
    print("Korrekt!")
    points += 1
else:
    print("Fel svar.")

print("""
2. Vem utvecklade det moderna språket COBOL?
    A) Mike Tyson
    B) Neil Armstrong
    C) En bonde
    D) Grace Hopper

""")
andrasvar = input("Svar: ")
if andrasvar == "d" or andrasvar == "D":
    print("Korrekt!")
    points += 1
else:
    print("Fel svar")

print("""
3. Vad var det stora som skedde på 1990-talet?
    A) Sverige blev stormakt
    B) Elektricitet kom till USA
    C) Internet spreds
    D) Datorn skapades

""")
tredjesvar = input("Svar: ")
if tredjesvar == "c" or tredjesvar == "C":
    print("Korrekt!")
    points += 1
else: 
    print("Fel svar")

print("""
4. I vilket av alternativen används inte programmering?
    A) Artificiell Intelligens
    B) Städning
    C) Musik
    D) Streaming

""")
fjärdesvar = input("Svar: ")
if fjärdesvar == "B" or fjärdesvar == "b":
    print("Korrekt!")
    points += 1
else: 
    print("Fel svar")

print("""
5. Vilket språk användes inte i skapandet av hemsidor på internet på 90-talet?
    A) HTML
    B) Javascript
    C) TempleOS
    D) CSS

""")
femtesvar = input("Svar: ")
if femtesvar == "C" or femtesvar == "c":
    print("Korrekt!")
    points += 1 
else:
    print("Fel svar")

print("""
6. Vad ökade mest när internet blir populärt?
    A) Global kommunikation
    B) IQ
    C) Sveriges ekonomi
    D) Matproduktion

""")
sjättesvar = input("Svar: ")
if sjättesvar == "A" or sjättesvar == "a":
    print("Korrekt!")
    points += 1 
else:
    print("Fel svar")
print("""
7. Vad förändrades i datorns utveckling?
    A) De blev större
    B) De blev mindre
    C) De blev konstigare
    D) Nånting

""")
sjundesvar = input("Svar: ")
if sjundesvar == "B" or sjundesvar == "b":
    print("Korrekt!")
    points += 1 
else:
    print("Fel svar")
print("""
8. Hur programmerade man tidiga datorer på 1900-talet?
    A) Genom att skriva på tangentbord
    B) Dra kablar till olika algoritmer
    C) Hålkort
    D) Genom att hoppas på det bästa

""")
åttondesvar = input("Svar:")
if åttondesvar == "C" or åttondesvar == "c":
    print("Korrekt!")
    points += 1 
else:
    print("Fel svar")

print("""
9. Vem ledde Apollo-programmets mjukvaruprogrammering?
    A) Niel Armstrong
    B) Göran Persson
    C) Margaret Hamilton
    D) Donald Trump

""")
niondesvar = input("Svar: ")
if niondesvar == "C" or niondesvar == "c":
    print("Korrekt!")
    points += 1 
else:
    print("Fel svar")

print("""
10. Vad blev billigare med PC revolutionen?
    A) Internet
    B) El räkningen
    C) Mark
    D) Datorer

""")
tiondesvar = input("Svar: ")
if tiondesvar == "D" or tiondesvar == "d":
    print("Korrekt!")
    points += 1 
else:
    print("Fel svar")

print("Ditt totalpoäng blev...", int(points), "/10" )
