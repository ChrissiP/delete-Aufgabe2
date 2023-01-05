import json

with open("tsjson/accounts.json") as json_loads:
    print(type(json_loads))
    python_liste = json.load(json_loads)
    print(json.dumps(python_liste, indent=10))