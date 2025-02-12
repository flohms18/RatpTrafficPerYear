import requests as req
import random

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

        
            
            
            

        


GetRatpFrequency2015()
