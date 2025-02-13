import json
import matplotlib.pyplot as plt

Years = [2015,2016,2017,2018,2019,2020]

plt.figure(figsize=(20, 6))

for check in Years:
    filename = f'./trafic-json-ratp/trafic-annuel-entrant-par-station-du-reseau-ferre-{check}.json'    
    with open(filename, 'r') as file:        
        data = json.load(file)
        totaux = {annee: {"RER": 0, "Metro": 0} for annee in range(2015, 2020)}
        TotalRER2015, TotalMetro2015 = 0
        TotalRER2016, TotalMetro2016 = 0
        TotalRER2017, TotalMetro2017 = 0
        TotalRER2018, TotalMetro2018 = 0
        TotalRER2019, TotalMetro2019 = 0
        TotalRER2020, TotalMetro2020 = 0
        for subway in data:
            if subway['reseau'] == 'RER' and check == 2017:
                TotalRER2017 += subway['trafic']
            elif subway['reseau'] == 'M\u00e9tro' and check == 2017:
                TotalMetro2017 += subway['trafic']
        print(f"Trafic en 2017 - RER:  {TotalRER2017}")
        print(f"Trafic en 2017 - Metro: {TotalMetro2017}")

        

       




       

