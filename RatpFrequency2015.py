import requests as req
import random
import matplotlib.pyplot as plt

plt.figure(figsize=(40, 6))
plt.xticks(fontsize=4)

def GetRatpFrequency2015():
    url = "https://data.ratp.fr/api/explore/v2.1/catalog/datasets/trafic-annuel-entrant-par-station-du-reseau-ferre-2015/records?limit=100"
    
    SelectedStations = []
    while len(SelectedStations) <= 20:
        RandomStationRank = random.randint(1,100)
        SelectedStations.append(RandomStationRank)

    print(SelectedStations)

    res = req.get(url)
    if res.status_code == 200:
        data = res.json()
        for i in SelectedStations:
            results = data.get("results", [])
            print(results[i]['station'])
            StationName = results[i]['station']
            StationTrafic = results[i]["trafic"]
            print(results[i]["trafic"])
            plt.bar(StationName, StationTrafic,width=0.5,color="#00AA91")
            plt.xticks(rotation=90)

        plt.xlabel("Station Name")   
        plt.ylabel("Traffic")


        
        plt.title("Trafic from 20 random stations RER/Metro")
        plt.legend()
        plt.grid(False)
        plt.show()        
        

        
            
            
            

        


GetRatpFrequency2015()
