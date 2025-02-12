import requests as req
import random
import matplotlib.pyplot as plt

plt.figure(figsize=(20, 6))

def GetRatpFrequency2015():
    url = "https://data.ratp.fr/api/explore/v2.1/catalog/datasets/trafic-annuel-entrant-par-station-du-reseau-ferre-2015/records?limit=100"
    
    SelectedStations = []
    while len(SelectedStations) <= 20:
        RandomStationRank = random.randint(1,20)
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
            plt.bar(StationName, StationTrafic, label="Trafic")

        plt.xlabel("StationName")   
        plt.ylabel("Points")

        plt.title("F1 24 Constructor Standings after Round 24")
        plt.legend()
        plt.grid(True)
        plt.show()        
        

        
            
            
            

        


GetRatpFrequency2015()
