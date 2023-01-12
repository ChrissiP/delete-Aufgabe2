import json
#Öffne die Datei
with open("tsjson/accounts.json","r") as Datei:
    print(type(Datei))
#Lade die JSON-Daten aus der Datei
    Liste = json.load(Datei)
    print(json.dumps(Liste, indent=10))
    
#Abfrage Benutzer nach Alter

age = input ("Bitte geben Sie 'alter' ein, um das Konto mit grösser 25 zu finden: ")
if age == "alter":
    #Sucht die Konten die grösser als 25 Jahre alt sind
    for user_accounts in Liste:
        if user_accounts["age"] > 25:
            #Konto wird angezeigt
            print("Konto: \n")
            print("Bild:", user_accounts["picture"])
            print("Name:", user_accounts["name"])
            print("Alter:", user_accounts["age"])
            print("Geschlecht:", user_accounts["gender"])
            print("Augenfarbe:", user_accounts["eyeColor"])
            print("Adresse:", user_accounts["address"])
            print("E-Mail:", user_accounts["email"])
            print("_________________________________________________________________________________")
        else: 
            print("\nVielen Dank für Ihren Besuch!")
balance = input ("\nBitte geben Sie 'kontostand' ein, um den höchsten Kontostand zu finden: ")
if balance == "kontostand":
    max_balance = 0
    #Sucht das Konto mit dem höchsten Kontostand
    for user_accounts in Liste:
        sum= user_accounts["balance"].replace(",","")
        sum= float(sum)
        if max_balance < sum:
            max_balance= sum
        #Konto wird angezeigt
    print("\nGehalt:",max_balance)
            