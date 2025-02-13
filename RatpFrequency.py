import json
import matplotlib.pyplot as plt
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
    'Metro': [Total[i]['metro'] for i in range(2015, 2021)],
    'RER': [Total[i]['rer'] for i in range(2015, 2021)]
}, index=range(2015, 2021))


print(df)
ax = df.plot(kind='bar', stacked=True, title="METRO/RER TRAFIC per YEAR between 2015 and 2020", figsize=(10, 6), color=['#00aa91','#5f8ab5'])  
ax.set_xlabel("Année")
ax.set_ylabel("Trafic")
ax.legend(title="Réseau")
plt.show()










    



    



        

       




       

