import requests as req

def GetRatpFrequency2015():
    url = "https://data.ratp.fr/api/explore/v2.1/catalog/datasets/trafic-annuel-entrant-par-station-du-reseau-ferre-2015/records?limit=100"

    try:
        res = req.get(url)

        if res.status_code == 200:
            freq = res.json()
            for station in freq.get("results",[]):
                print(station['station'])
                traffic_total = 0
                traffic_total += station['trafic']
                print(traffic_total)
        else:
            print("Error", res.status_code)
            return None
    except req.exceptions.RequestException as e:
  
        print('Error:', e)
        return None

        


GetRatpFrequency2015()
