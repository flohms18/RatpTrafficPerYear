import json

with open('trafic-annuel-entrant-par-station-du-reseau-ferre-2015.json','r') as file:
    data = json.load(file)
    TotalTrafic = 0
    TotalMetro = 0
    TotalRER = 0
    for subway in data:
        if subway['reseau'] == 'RER':
            TotalRER += subway['trafic']
        elif subway['reseau'] == 'M\u00e9tro':
            TotalMetro += subway['trafic']
        TotalTrafic = TotalMetro + TotalRER

    print(f"Trafic en 2015 - RER:  {TotalRER}")
    print(f"Trafic en 2015 - Métro:  {TotalMetro}")
    print(f"Total Trafic:  {TotalTrafic}")


        
        

       

