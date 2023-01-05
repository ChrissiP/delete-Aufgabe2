import json

with open("tsjson/accounts.json") as Datei:
    print(type(Datei))
    Liste = json.load(Datei)
    print(json.dumps(Liste, indent=10))