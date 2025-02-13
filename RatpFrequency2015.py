import json
import matplotlib.pyplot as plt
import numpy as np

Total = {}

for i in range(2015, 2021):
    Total[i] = {  
        'metro': 0,
        'rer': 0,
        'year' : i
    }
    check = i
    filename = f'./trafic-json-ratp/trafic-annuel-entrant-par-station-du-reseau-ferre-{check}.json'
    with open(filename,'r') as file:
        data = json.load(file)
        for subway in data:
            if subway['reseau'] == 'RER':
                Total[i]['rer'] += subway['trafic']
            elif subway['reseau'] == 'M\u00e9tro': 
                Total[i]['metro'] += subway['trafic']
        print(f"Trafic Métro en {check}: {Total[i]['metro']}")
        print(f"Trafic RER en {check}: {Total[i]['rer']}")
    
    








    



    



        

       




       

