import json

Years = [2015,2016,2017,2018,2019,2020]

for check in Years:
    filename = f'./trafic-json-ratp/trafic-annuel-entrant-par-station-du-reseau-ferre-{check}.json'    
    with open(filename, 'r') as file:        
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

        print(f"Trafic en {check} - RER:  {TotalRER}")
        print(f"Trafic en {check} - Métro: {TotalMetro}")
        print(f"Total Trafic en {check}:  {TotalTrafic}")

        
        

       

