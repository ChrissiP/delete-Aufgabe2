import json
#Öffne die Datei
with open("tsjson/accounts.json","r") as Datei:
    print(type(Datei))
#Lade die JSON-Daten aus der Datei
    Liste = json.load(Datei)
    print(json.dumps(Liste, indent=10))
    