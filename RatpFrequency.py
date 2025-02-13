import json
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

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
    
df = pd.DataFrame({
    'metro': [Total[i]['metro'] for i in range(2015, 2021)],
    'rer': [Total[i]['rer'] for i in range(2015, 2021)]
}, index=range(2015, 2021))

print(df)
ax = df.plot(kind='bar', stacked=True, title="Trafic Métro et RER par année", figsize=(10, 6))  
ax.set_xlabel("Année")
ax.set_ylabel("Trafic")
ax.legend(title="Réseau")
plt.show()










    



    



        

       




       

