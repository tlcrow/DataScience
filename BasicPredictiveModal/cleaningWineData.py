import json
import random

liked = []
price = []
points = []
variety = []
winery = []
province = []
country = []

def getValues(map):
    liked.append(random.randint(0,1))
    price.append(map['price'])
    points.append(int(map['points']))
    variety.append(map['variety'])
    winery.append(map['winery'])
    province.append(map['province'])
    country.append(map['country'])

with open('originalWineData.json') as json_data:
    wineData = json.load(json_data)
for i in range (0, 20):
    liked.append(random.randint(0,1))
    price.append(wineData[i]['price'])
    points.append(int(wineData[i]['points']))
    variety.append(wineData[i]['variety'])
    winery.append(wineData[i]['winery'])
    province.append(wineData[i]['province'])
    country.append(wineData[i]['country'])
# map(getValues, wineData)
