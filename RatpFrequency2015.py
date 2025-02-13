import json
import matplotlib.pyplot as plt

Years = [2015,2016,2017,2018,2019,2020]

plt.figure(figsize=(20, 6))

for check in Years:
    filename = f'./trafic-json-ratp/trafic-annuel-entrant-par-station-du-reseau-ferre-{check}.json'    
    with open(filename, 'r') as file:        
        data = json.load(file)
        TotalRER2017 = 0
        TotalMetro2017 = 0
        TotalTrafic = 0
        TotalMetro = 0
        TotalRER = 0
        for subway in data:
            if subway['reseau'] == 'RER' and check == 2017:
                TotalRER2017 += subway['trafic']
            elif subway['reseau'] == 'M\u00e9tro' and check == 2017:
                TotalMetro2017 += subway['trafic']
        print(f"Trafic en 2017 - RER:  {TotalRER2017}")
        print(f"Trafic en 2017 - Metro: {TotalMetro2017}")

        

       




       

