import json

with open('trafic-annuel-entrant-par-station-du-reseau-ferre-2015.json','r') as file:
    data = json.load(file)

print(data)