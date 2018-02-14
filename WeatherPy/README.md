

```python
from citipy import citipy
import pandas as pd
import numpy as np
import requests as req
import matplotlib.pyplot as plt
import seaborn as sns
```


```python
# Andy's api key
api_key = "bab6ed8714b504b5454b34baa8e421bb"
```


```python
# Generate random cities by lat,lng
# List for holding lat_lngs
lat_lngs = []
cities = []
```


```python
# create a set of random lat and lng combinations 
lats = np.random.uniform(low=-90.000, high=90.000, size=1500)
lngs = np.random.uniform(low=-180.000, high=180.000,size=1500)
lat_lngs=zip(lats, lngs)
```


```python
# identify nearest city for each lat, lng combo
for lat_lng in lat_lngs:
    city = citipy.nearest_city(lat_lng[0], lat_lng[1]).city_name
    
    # if city is unique, then add it to our cities list
    if city not in cities:
        cities.append(city)
```


```python
len(cities)
```




    609




```python
# create DataFrame for cities
cities_df = pd.DataFrame({'City': cities})
```


```python
cities_df.tail()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>City</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>604</th>
      <td>middelburg</td>
    </tr>
    <tr>
      <th>605</th>
      <td>yulara</td>
    </tr>
    <tr>
      <th>606</th>
      <td>port-gentil</td>
    </tr>
    <tr>
      <th>607</th>
      <td>moosomin</td>
    </tr>
    <tr>
      <th>608</th>
      <td>junin</td>
    </tr>
  </tbody>
</table>
</div>




```python
# randomly select 500 cities (test with 5)
selected_cities = cities_df.sample(n=600)
selected_cities.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>City</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>451</th>
      <td>aykhal</td>
    </tr>
    <tr>
      <th>505</th>
      <td>mantua</td>
    </tr>
    <tr>
      <th>235</th>
      <td>ahipara</td>
    </tr>
    <tr>
      <th>168</th>
      <td>hasaki</td>
    </tr>
    <tr>
      <th>64</th>
      <td>rungata</td>
    </tr>
  </tbody>
</table>
</div>




```python
selected_cities["Latitude"] = ""
selected_cities["Longitude"] = ""
selected_cities["Country"] = ""
selected_cities["Temperature"] = ""
selected_cities["Humidity %"] = ""
selected_cities["Wind Speed"] = ""
selected_cities["Cloudiness %"] = ""
selected_cities.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>City</th>
      <th>Latitude</th>
      <th>Longitude</th>
      <th>Country</th>
      <th>Temperature</th>
      <th>Humidity %</th>
      <th>Wind Speed</th>
      <th>Cloudiness %</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>451</th>
      <td>aykhal</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>505</th>
      <td>mantua</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>235</th>
      <td>ahipara</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>168</th>
      <td>hasaki</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>64</th>
      <td>rungata</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>
</div>




```python
# rearrange order of columns
selected_cities = selected_cities[['Country', 'City', 'Latitude', 'Longitude', 'Temperature', 'Humidity %',
                                 'Wind Speed', 'Cloudiness %']]
```


```python
selected_cities.tail()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>City</th>
      <th>Latitude</th>
      <th>Longitude</th>
      <th>Temperature</th>
      <th>Humidity %</th>
      <th>Wind Speed</th>
      <th>Cloudiness %</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>335</th>
      <td></td>
      <td>inta</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>339</th>
      <td></td>
      <td>victoria</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>575</th>
      <td></td>
      <td>kerema</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>592</th>
      <td></td>
      <td>moranbah</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th>385</th>
      <td></td>
      <td>bontang</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>
</div>




```python
selected_cities.info()
```

    <class 'pandas.core.frame.DataFrame'>
    Int64Index: 600 entries, 451 to 385
    Data columns (total 8 columns):
    Country         600 non-null object
    City            600 non-null object
    Latitude        600 non-null object
    Longitude       600 non-null object
    Temperature     600 non-null object
    Humidity %      600 non-null object
    Wind Speed      600 non-null object
    Cloudiness %    600 non-null object
    dtypes: object(8)
    memory usage: 42.2+ KB



```python
# counter 
row_count = 0

for index, row in selected_cities.iterrows():
    # Create endpoint URL
    
    city_row = row["City"]
    #target_url = "http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&units=IMPERIAL&mode=json&APPID={}".format(lat, lng,api_key)
    target_url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=IMPERIAL&mode=json&APPID={}".format(city_row,api_key)
    
    # print log to ensure loop is working correctly
    print("Now retrieving city # " + str(row_count))
    print(target_url)
    row_count +=1
    
    # run requests to grab JSON at the requested URL
    requests = req.get(target_url).json()
    
    # append the lat/lng to appropiate columns
    # use try / except to skip any cities
    
    try:
        selected_cities.set_value(index, "Country", requests["sys"]["country"])
        selected_cities.set_value(index, "Latitude", requests["coord"]["lat"])
        selected_cities.set_value(index, "Longitude", requests["coord"]["lon"])
        selected_cities.set_value(index, "Temperature", requests["main"]["temp_max"])
        selected_cities.set_value(index, "Humidity %", requests["main"]["humidity"])
        selected_cities.set_value(index, "Wind Speed", requests["wind"]["speed"])
        selected_cities.set_value(index, "Cloudiness %", requests["clouds"]["all"])
        
        print("--", end="")
    
    except:
        print(" Missing field... skipping.")

selected_cities.head()
```

    Now retrieving city # 0
    http://api.openweathermap.org/data/2.5/weather?q=aykhal&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 1
    http://api.openweathermap.org/data/2.5/weather?q=mantua&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 2
    http://api.openweathermap.org/data/2.5/weather?q=ahipara&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 3
    http://api.openweathermap.org/data/2.5/weather?q=hasaki&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 4
    http://api.openweathermap.org/data/2.5/weather?q=rungata&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 5
    http://api.openweathermap.org/data/2.5/weather?q=khandyga&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 6
    http://api.openweathermap.org/data/2.5/weather?q=bengkulu&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 7
    http://api.openweathermap.org/data/2.5/weather?q=yerbogachen&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 8
    http://api.openweathermap.org/data/2.5/weather?q=kavieng&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 9
    http://api.openweathermap.org/data/2.5/weather?q=mahaicony&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 10
    http://api.openweathermap.org/data/2.5/weather?q=cap malheureux&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 11
    http://api.openweathermap.org/data/2.5/weather?q=dali&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 12
    http://api.openweathermap.org/data/2.5/weather?q=maneadero&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 13
    http://api.openweathermap.org/data/2.5/weather?q=tuatapere&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 14
    http://api.openweathermap.org/data/2.5/weather?q=olafsvik&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 15
    http://api.openweathermap.org/data/2.5/weather?q=nizhniy kuranakh&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 16
    http://api.openweathermap.org/data/2.5/weather?q=pasil&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 17
    http://api.openweathermap.org/data/2.5/weather?q=mys shmidta&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 18
    http://api.openweathermap.org/data/2.5/weather?q=saleaula&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 19
    http://api.openweathermap.org/data/2.5/weather?q=mazara del vallo&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 20
    http://api.openweathermap.org/data/2.5/weather?q=atchison&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 21
    http://api.openweathermap.org/data/2.5/weather?q=bathsheba&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 22
    http://api.openweathermap.org/data/2.5/weather?q=hambantota&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 23
    http://api.openweathermap.org/data/2.5/weather?q=the valley&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 24
    http://api.openweathermap.org/data/2.5/weather?q=priyutnoye&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 25
    http://api.openweathermap.org/data/2.5/weather?q=sitka&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 26
    http://api.openweathermap.org/data/2.5/weather?q=nong kung si&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 27
    http://api.openweathermap.org/data/2.5/weather?q=axim&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 28
    http://api.openweathermap.org/data/2.5/weather?q=kavaratti&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 29
    http://api.openweathermap.org/data/2.5/weather?q=opuwo&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 30
    http://api.openweathermap.org/data/2.5/weather?q=inverness&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 31
    http://api.openweathermap.org/data/2.5/weather?q=ombessa&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 32
    http://api.openweathermap.org/data/2.5/weather?q=mecca&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 33
    http://api.openweathermap.org/data/2.5/weather?q=abu dhabi&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 34
    http://api.openweathermap.org/data/2.5/weather?q=ambilobe&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 35
    http://api.openweathermap.org/data/2.5/weather?q=punta arenas&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 36
    http://api.openweathermap.org/data/2.5/weather?q=porangatu&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 37
    http://api.openweathermap.org/data/2.5/weather?q=qaanaaq&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 38
    http://api.openweathermap.org/data/2.5/weather?q=hay river&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 39
    http://api.openweathermap.org/data/2.5/weather?q=carbonia&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 40
    http://api.openweathermap.org/data/2.5/weather?q=texistepec&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 41
    http://api.openweathermap.org/data/2.5/weather?q=krasnoarmeysk&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 42
    http://api.openweathermap.org/data/2.5/weather?q=priargunsk&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 43
    http://api.openweathermap.org/data/2.5/weather?q=porto torres&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 44
    http://api.openweathermap.org/data/2.5/weather?q=berlevag&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 45
    http://api.openweathermap.org/data/2.5/weather?q=marseille&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 46
    http://api.openweathermap.org/data/2.5/weather?q=qasigiannguit&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 47
    http://api.openweathermap.org/data/2.5/weather?q=zhuhai&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 48
    http://api.openweathermap.org/data/2.5/weather?q=longlac&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 49
    http://api.openweathermap.org/data/2.5/weather?q=middelburg&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 50
    http://api.openweathermap.org/data/2.5/weather?q=oranjemund&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 51
    http://api.openweathermap.org/data/2.5/weather?q=carnarvon&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 52
    http://api.openweathermap.org/data/2.5/weather?q=kachikau&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 53
    http://api.openweathermap.org/data/2.5/weather?q=goderich&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 54
    http://api.openweathermap.org/data/2.5/weather?q=falmouth&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 55
    http://api.openweathermap.org/data/2.5/weather?q=jumla&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 56
    http://api.openweathermap.org/data/2.5/weather?q=beringovskiy&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 57
    http://api.openweathermap.org/data/2.5/weather?q=buariki&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 58
    http://api.openweathermap.org/data/2.5/weather?q=nelson bay&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 59
    http://api.openweathermap.org/data/2.5/weather?q=namatanai&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 60
    http://api.openweathermap.org/data/2.5/weather?q=samusu&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 61
    http://api.openweathermap.org/data/2.5/weather?q=salinopolis&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 62
    http://api.openweathermap.org/data/2.5/weather?q=kruisfontein&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 63
    http://api.openweathermap.org/data/2.5/weather?q=pouebo&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 64
    http://api.openweathermap.org/data/2.5/weather?q=lorengau&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 65
    http://api.openweathermap.org/data/2.5/weather?q=inzhavino&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 66
    http://api.openweathermap.org/data/2.5/weather?q=ucluelet&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 67
    http://api.openweathermap.org/data/2.5/weather?q=yar-sale&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 68
    http://api.openweathermap.org/data/2.5/weather?q=kargasok&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 69
    http://api.openweathermap.org/data/2.5/weather?q=skjervoy&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 70
    http://api.openweathermap.org/data/2.5/weather?q=raudeberg&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 71
    http://api.openweathermap.org/data/2.5/weather?q=miri&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 72
    http://api.openweathermap.org/data/2.5/weather?q=cherskiy&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 73
    http://api.openweathermap.org/data/2.5/weather?q=vostok&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 74
    http://api.openweathermap.org/data/2.5/weather?q=ladnun&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 75
    http://api.openweathermap.org/data/2.5/weather?q=sola&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 76
    http://api.openweathermap.org/data/2.5/weather?q=kanashevo&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 77
    http://api.openweathermap.org/data/2.5/weather?q=petrozavodsk&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 78
    http://api.openweathermap.org/data/2.5/weather?q=broken hill&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 79
    http://api.openweathermap.org/data/2.5/weather?q=manono&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 80
    http://api.openweathermap.org/data/2.5/weather?q=lahaina&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 81
    http://api.openweathermap.org/data/2.5/weather?q=moosomin&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 82
    http://api.openweathermap.org/data/2.5/weather?q=nouadhibou&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 83
    http://api.openweathermap.org/data/2.5/weather?q=sa kaeo&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 84
    http://api.openweathermap.org/data/2.5/weather?q=litovko&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 85
    http://api.openweathermap.org/data/2.5/weather?q=big spring&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 86
    http://api.openweathermap.org/data/2.5/weather?q=anthia&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 87
    http://api.openweathermap.org/data/2.5/weather?q=oeiras do para&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 88
    http://api.openweathermap.org/data/2.5/weather?q=borova&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 89
    http://api.openweathermap.org/data/2.5/weather?q=porto seguro&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 90
    http://api.openweathermap.org/data/2.5/weather?q=hohhot&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 91
    http://api.openweathermap.org/data/2.5/weather?q=bredasdorp&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 92
    http://api.openweathermap.org/data/2.5/weather?q=vila franca do campo&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 93
    http://api.openweathermap.org/data/2.5/weather?q=pevek&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 94
    http://api.openweathermap.org/data/2.5/weather?q=abnub&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 95
    http://api.openweathermap.org/data/2.5/weather?q=kapaa&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 96
    http://api.openweathermap.org/data/2.5/weather?q=karakendzha&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 97
    http://api.openweathermap.org/data/2.5/weather?q=vao&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 98
    http://api.openweathermap.org/data/2.5/weather?q=punta alta&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 99
    http://api.openweathermap.org/data/2.5/weather?q=hofn&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 100
    http://api.openweathermap.org/data/2.5/weather?q=gazni&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 101
    http://api.openweathermap.org/data/2.5/weather?q=bethel&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 102
    http://api.openweathermap.org/data/2.5/weather?q=nanortalik&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 103
    http://api.openweathermap.org/data/2.5/weather?q=guerrero negro&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 104
    http://api.openweathermap.org/data/2.5/weather?q=oktyabrskiy&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 105
    http://api.openweathermap.org/data/2.5/weather?q=kahului&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 106
    http://api.openweathermap.org/data/2.5/weather?q=pauini&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 107
    http://api.openweathermap.org/data/2.5/weather?q=portland&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 108
    http://api.openweathermap.org/data/2.5/weather?q=bolungarvik&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 109
    http://api.openweathermap.org/data/2.5/weather?q=sayyan&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 110
    http://api.openweathermap.org/data/2.5/weather?q=esfahan&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 111
    http://api.openweathermap.org/data/2.5/weather?q=codrington&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 112
    http://api.openweathermap.org/data/2.5/weather?q=lavrentiya&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 113
    http://api.openweathermap.org/data/2.5/weather?q=barrow&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 114
    http://api.openweathermap.org/data/2.5/weather?q=bryan&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 115
    http://api.openweathermap.org/data/2.5/weather?q=tiksi&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 116
    http://api.openweathermap.org/data/2.5/weather?q=aranos&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 117
    http://api.openweathermap.org/data/2.5/weather?q=emerald&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 118
    http://api.openweathermap.org/data/2.5/weather?q=pachino&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 119
    http://api.openweathermap.org/data/2.5/weather?q=marzuq&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 120
    http://api.openweathermap.org/data/2.5/weather?q=saint anthony&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 121
    http://api.openweathermap.org/data/2.5/weather?q=zapolyarnyy&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 122
    http://api.openweathermap.org/data/2.5/weather?q=touros&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 123
    http://api.openweathermap.org/data/2.5/weather?q=katsuura&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 124
    http://api.openweathermap.org/data/2.5/weather?q=saint-raymond&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 125
    http://api.openweathermap.org/data/2.5/weather?q=presidencia roque saenz pena&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 126
    http://api.openweathermap.org/data/2.5/weather?q=ca mau&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 127
    http://api.openweathermap.org/data/2.5/weather?q=antofagasta&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 128
    http://api.openweathermap.org/data/2.5/weather?q=evensk&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 129
    http://api.openweathermap.org/data/2.5/weather?q=tyrma&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 130
    http://api.openweathermap.org/data/2.5/weather?q=dibombari&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 131
    http://api.openweathermap.org/data/2.5/weather?q=atar&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 132
    http://api.openweathermap.org/data/2.5/weather?q=puerto carreno&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 133
    http://api.openweathermap.org/data/2.5/weather?q=paamiut&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 134
    http://api.openweathermap.org/data/2.5/weather?q=chulman&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 135
    http://api.openweathermap.org/data/2.5/weather?q=khamgaon&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 136
    http://api.openweathermap.org/data/2.5/weather?q=iqaluit&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 137
    http://api.openweathermap.org/data/2.5/weather?q=gamboma&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 138
    http://api.openweathermap.org/data/2.5/weather?q=lincoln&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 139
    http://api.openweathermap.org/data/2.5/weather?q=serenje&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 140
    http://api.openweathermap.org/data/2.5/weather?q=atuona&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 141
    http://api.openweathermap.org/data/2.5/weather?q=yellowknife&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 142
    http://api.openweathermap.org/data/2.5/weather?q=mataura&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 143
    http://api.openweathermap.org/data/2.5/weather?q=lubao&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 144
    http://api.openweathermap.org/data/2.5/weather?q=cuca&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 145
    http://api.openweathermap.org/data/2.5/weather?q=mocuba&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 146
    http://api.openweathermap.org/data/2.5/weather?q=eureka&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 147
    http://api.openweathermap.org/data/2.5/weather?q=iskateley&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 148
    http://api.openweathermap.org/data/2.5/weather?q=ust-kuyga&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 149
    http://api.openweathermap.org/data/2.5/weather?q=provideniya&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 150
    http://api.openweathermap.org/data/2.5/weather?q=komsomolskiy&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 151
    http://api.openweathermap.org/data/2.5/weather?q=arraial do cabo&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 152
    http://api.openweathermap.org/data/2.5/weather?q=sinop&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 153
    http://api.openweathermap.org/data/2.5/weather?q=moron&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 154
    http://api.openweathermap.org/data/2.5/weather?q=los llanos de aridane&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 155
    http://api.openweathermap.org/data/2.5/weather?q=rio gallegos&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 156
    http://api.openweathermap.org/data/2.5/weather?q=limoux&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 157
    http://api.openweathermap.org/data/2.5/weather?q=nemuro&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 158
    http://api.openweathermap.org/data/2.5/weather?q=zafarabad&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 159
    http://api.openweathermap.org/data/2.5/weather?q=moroni&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 160
    http://api.openweathermap.org/data/2.5/weather?q=anloga&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 161
    http://api.openweathermap.org/data/2.5/weather?q=rognan&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 162
    http://api.openweathermap.org/data/2.5/weather?q=norman wells&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 163
    http://api.openweathermap.org/data/2.5/weather?q=barinas&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 164
    http://api.openweathermap.org/data/2.5/weather?q=kumluca&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 165
    http://api.openweathermap.org/data/2.5/weather?q=saskylakh&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 166
    http://api.openweathermap.org/data/2.5/weather?q=chagda&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 167
    http://api.openweathermap.org/data/2.5/weather?q=santiago del estero&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 168
    http://api.openweathermap.org/data/2.5/weather?q=qaqortoq&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 169
    http://api.openweathermap.org/data/2.5/weather?q=mayo&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 170
    http://api.openweathermap.org/data/2.5/weather?q=te anau&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 171
    http://api.openweathermap.org/data/2.5/weather?q=bijeljina&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 172
    http://api.openweathermap.org/data/2.5/weather?q=bluff&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 173
    http://api.openweathermap.org/data/2.5/weather?q=sakakah&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 174
    http://api.openweathermap.org/data/2.5/weather?q=flin flon&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 175
    http://api.openweathermap.org/data/2.5/weather?q=avera&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 176
    http://api.openweathermap.org/data/2.5/weather?q=phenix city&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 177
    http://api.openweathermap.org/data/2.5/weather?q=belushya guba&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 178
    http://api.openweathermap.org/data/2.5/weather?q=kangayam&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 179
    http://api.openweathermap.org/data/2.5/weather?q=vaini&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 180
    http://api.openweathermap.org/data/2.5/weather?q=husavik&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 181
    http://api.openweathermap.org/data/2.5/weather?q=muros&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 182
    http://api.openweathermap.org/data/2.5/weather?q=wulanhaote&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 183
    http://api.openweathermap.org/data/2.5/weather?q=aras&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 184
    http://api.openweathermap.org/data/2.5/weather?q=bolshaya glushitsa&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 185
    http://api.openweathermap.org/data/2.5/weather?q=kimbe&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 186
    http://api.openweathermap.org/data/2.5/weather?q=bambous virieux&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 187
    http://api.openweathermap.org/data/2.5/weather?q=teguise&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 188
    http://api.openweathermap.org/data/2.5/weather?q=ilam&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 189
    http://api.openweathermap.org/data/2.5/weather?q=louisbourg&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 190
    http://api.openweathermap.org/data/2.5/weather?q=kokkarion&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 191
    http://api.openweathermap.org/data/2.5/weather?q=westport&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 192
    http://api.openweathermap.org/data/2.5/weather?q=ponta do sol&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 193
    http://api.openweathermap.org/data/2.5/weather?q=qurayyat&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 194
    http://api.openweathermap.org/data/2.5/weather?q=pombal&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 195
    http://api.openweathermap.org/data/2.5/weather?q=russell&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 196
    http://api.openweathermap.org/data/2.5/weather?q=sao gabriel da cachoeira&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 197
    http://api.openweathermap.org/data/2.5/weather?q=charters towers&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 198
    http://api.openweathermap.org/data/2.5/weather?q=tasiilaq&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 199
    http://api.openweathermap.org/data/2.5/weather?q=jamestown&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 200
    http://api.openweathermap.org/data/2.5/weather?q=deloraine&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 201
    http://api.openweathermap.org/data/2.5/weather?q=hilo&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 202
    http://api.openweathermap.org/data/2.5/weather?q=turukhansk&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 203
    http://api.openweathermap.org/data/2.5/weather?q=san francisco&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 204
    http://api.openweathermap.org/data/2.5/weather?q=heidenheim&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 205
    http://api.openweathermap.org/data/2.5/weather?q=hamilton&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 206
    http://api.openweathermap.org/data/2.5/weather?q=samalaeulu&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 207
    http://api.openweathermap.org/data/2.5/weather?q=muroto&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 208
    http://api.openweathermap.org/data/2.5/weather?q=bonthe&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 209
    http://api.openweathermap.org/data/2.5/weather?q=saint-philippe&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 210
    http://api.openweathermap.org/data/2.5/weather?q=vila&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 211
    http://api.openweathermap.org/data/2.5/weather?q=juegang&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 212
    http://api.openweathermap.org/data/2.5/weather?q=takoradi&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 213
    http://api.openweathermap.org/data/2.5/weather?q=awjilah&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 214
    http://api.openweathermap.org/data/2.5/weather?q=haapu&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 215
    http://api.openweathermap.org/data/2.5/weather?q=yunguyo&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 216
    http://api.openweathermap.org/data/2.5/weather?q=burica&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 217
    http://api.openweathermap.org/data/2.5/weather?q=nalut&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 218
    http://api.openweathermap.org/data/2.5/weather?q=vardo&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 219
    http://api.openweathermap.org/data/2.5/weather?q=castelo do piaui&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 220
    http://api.openweathermap.org/data/2.5/weather?q=isangel&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 221
    http://api.openweathermap.org/data/2.5/weather?q=koumac&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 222
    http://api.openweathermap.org/data/2.5/weather?q=denpasar&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 223
    http://api.openweathermap.org/data/2.5/weather?q=manitouwadge&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 224
    http://api.openweathermap.org/data/2.5/weather?q=lumeje&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 225
    http://api.openweathermap.org/data/2.5/weather?q=dingle&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 226
    http://api.openweathermap.org/data/2.5/weather?q=calvia&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 227
    http://api.openweathermap.org/data/2.5/weather?q=waw&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 228
    http://api.openweathermap.org/data/2.5/weather?q=tasbuget&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 229
    http://api.openweathermap.org/data/2.5/weather?q=vila velha&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 230
    http://api.openweathermap.org/data/2.5/weather?q=kapoeta&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 231
    http://api.openweathermap.org/data/2.5/weather?q=fengcheng&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 232
    http://api.openweathermap.org/data/2.5/weather?q=filadelfia&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 233
    http://api.openweathermap.org/data/2.5/weather?q=matay&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 234
    http://api.openweathermap.org/data/2.5/weather?q=inongo&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 235
    http://api.openweathermap.org/data/2.5/weather?q=rundu&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 236
    http://api.openweathermap.org/data/2.5/weather?q=saint-pierre&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 237
    http://api.openweathermap.org/data/2.5/weather?q=moindou&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 238
    http://api.openweathermap.org/data/2.5/weather?q=halalo&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 239
    http://api.openweathermap.org/data/2.5/weather?q=khatanga&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 240
    http://api.openweathermap.org/data/2.5/weather?q=bramsche&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 241
    http://api.openweathermap.org/data/2.5/weather?q=grand gaube&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 242
    http://api.openweathermap.org/data/2.5/weather?q=bela vista&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 243
    http://api.openweathermap.org/data/2.5/weather?q=aue&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 244
    http://api.openweathermap.org/data/2.5/weather?q=tiznit&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 245
    http://api.openweathermap.org/data/2.5/weather?q=klaksvik&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 246
    http://api.openweathermap.org/data/2.5/weather?q=nantucket&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 247
    http://api.openweathermap.org/data/2.5/weather?q=punta cardon&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 248
    http://api.openweathermap.org/data/2.5/weather?q=koshurnikovo&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 249
    http://api.openweathermap.org/data/2.5/weather?q=ushuaia&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 250
    http://api.openweathermap.org/data/2.5/weather?q=albany&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 251
    http://api.openweathermap.org/data/2.5/weather?q=krasnoselkup&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 252
    http://api.openweathermap.org/data/2.5/weather?q=constitucion&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 253
    http://api.openweathermap.org/data/2.5/weather?q=hoquiam&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 254
    http://api.openweathermap.org/data/2.5/weather?q=ruatoria&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 255
    http://api.openweathermap.org/data/2.5/weather?q=hervey bay&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 256
    http://api.openweathermap.org/data/2.5/weather?q=san patricio&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 257
    http://api.openweathermap.org/data/2.5/weather?q=maradi&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 258
    http://api.openweathermap.org/data/2.5/weather?q=chifeng&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 259
    http://api.openweathermap.org/data/2.5/weather?q=robertsport&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 260
    http://api.openweathermap.org/data/2.5/weather?q=alugan&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 261
    http://api.openweathermap.org/data/2.5/weather?q=castro&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 262
    http://api.openweathermap.org/data/2.5/weather?q=virginia beach&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 263
    http://api.openweathermap.org/data/2.5/weather?q=praia da vitoria&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 264
    http://api.openweathermap.org/data/2.5/weather?q=muzhi&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 265
    http://api.openweathermap.org/data/2.5/weather?q=umea&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 266
    http://api.openweathermap.org/data/2.5/weather?q=impfondo&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 267
    http://api.openweathermap.org/data/2.5/weather?q=alofi&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 268
    http://api.openweathermap.org/data/2.5/weather?q=bambanglipuro&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 269
    http://api.openweathermap.org/data/2.5/weather?q=namibe&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 270
    http://api.openweathermap.org/data/2.5/weather?q=nizhniy ufaley&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 271
    http://api.openweathermap.org/data/2.5/weather?q=kamina&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 272
    http://api.openweathermap.org/data/2.5/weather?q=changji&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 273
    http://api.openweathermap.org/data/2.5/weather?q=lithakia&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 274
    http://api.openweathermap.org/data/2.5/weather?q=cabo san lucas&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 275
    http://api.openweathermap.org/data/2.5/weather?q=rabat&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 276
    http://api.openweathermap.org/data/2.5/weather?q=laguna&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 277
    http://api.openweathermap.org/data/2.5/weather?q=lasa&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 278
    http://api.openweathermap.org/data/2.5/weather?q=warqla&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 279
    http://api.openweathermap.org/data/2.5/weather?q=poronaysk&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 280
    http://api.openweathermap.org/data/2.5/weather?q=avarua&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 281
    http://api.openweathermap.org/data/2.5/weather?q=clyde river&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 282
    http://api.openweathermap.org/data/2.5/weather?q=rio grande&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 283
    http://api.openweathermap.org/data/2.5/weather?q=macusani&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 284
    http://api.openweathermap.org/data/2.5/weather?q=sidi qasim&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 285
    http://api.openweathermap.org/data/2.5/weather?q=attawapiskat&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 286
    http://api.openweathermap.org/data/2.5/weather?q=kharp&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 287
    http://api.openweathermap.org/data/2.5/weather?q=anadyr&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 288
    http://api.openweathermap.org/data/2.5/weather?q=esperance&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 289
    http://api.openweathermap.org/data/2.5/weather?q=beloha&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 290
    http://api.openweathermap.org/data/2.5/weather?q=panaba&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 291
    http://api.openweathermap.org/data/2.5/weather?q=northfield&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 292
    http://api.openweathermap.org/data/2.5/weather?q=ionia&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 293
    http://api.openweathermap.org/data/2.5/weather?q=meteti&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 294
    http://api.openweathermap.org/data/2.5/weather?q=ndele&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 295
    http://api.openweathermap.org/data/2.5/weather?q=bubaque&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 296
    http://api.openweathermap.org/data/2.5/weather?q=dasoguz&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 297
    http://api.openweathermap.org/data/2.5/weather?q=waipawa&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 298
    http://api.openweathermap.org/data/2.5/weather?q=nizhneyansk&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 299
    http://api.openweathermap.org/data/2.5/weather?q=mehamn&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 300
    http://api.openweathermap.org/data/2.5/weather?q=wanlaweyn&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 301
    http://api.openweathermap.org/data/2.5/weather?q=volsk&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 302
    http://api.openweathermap.org/data/2.5/weather?q=khorixas&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 303
    http://api.openweathermap.org/data/2.5/weather?q=barentsburg&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 304
    http://api.openweathermap.org/data/2.5/weather?q=marcona&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 305
    http://api.openweathermap.org/data/2.5/weather?q=jishou&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 306
    http://api.openweathermap.org/data/2.5/weather?q=nizhniy baskunchak&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 307
    http://api.openweathermap.org/data/2.5/weather?q=shingu&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 308
    http://api.openweathermap.org/data/2.5/weather?q=tay ninh&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 309
    http://api.openweathermap.org/data/2.5/weather?q=simpang&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 310
    http://api.openweathermap.org/data/2.5/weather?q=boddam&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 311
    http://api.openweathermap.org/data/2.5/weather?q=aklavik&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 312
    http://api.openweathermap.org/data/2.5/weather?q=kaitangata&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 313
    http://api.openweathermap.org/data/2.5/weather?q=adet&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 314
    http://api.openweathermap.org/data/2.5/weather?q=laiagam&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 315
    http://api.openweathermap.org/data/2.5/weather?q=jimo&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 316
    http://api.openweathermap.org/data/2.5/weather?q=kovdor&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 317
    http://api.openweathermap.org/data/2.5/weather?q=maniitsoq&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 318
    http://api.openweathermap.org/data/2.5/weather?q=sur&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 319
    http://api.openweathermap.org/data/2.5/weather?q=tsihombe&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 320
    http://api.openweathermap.org/data/2.5/weather?q=lebedinyy&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 321
    http://api.openweathermap.org/data/2.5/weather?q=belmonte&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 322
    http://api.openweathermap.org/data/2.5/weather?q=lowestoft&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 323
    http://api.openweathermap.org/data/2.5/weather?q=comodoro rivadavia&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 324
    http://api.openweathermap.org/data/2.5/weather?q=arawa&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 325
    http://api.openweathermap.org/data/2.5/weather?q=lebu&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 326
    http://api.openweathermap.org/data/2.5/weather?q=knysna&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 327
    http://api.openweathermap.org/data/2.5/weather?q=meulaboh&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 328
    http://api.openweathermap.org/data/2.5/weather?q=birobidzhan&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 329
    http://api.openweathermap.org/data/2.5/weather?q=richards bay&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 330
    http://api.openweathermap.org/data/2.5/weather?q=thompson&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 331
    http://api.openweathermap.org/data/2.5/weather?q=tevaitoa&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 332
    http://api.openweathermap.org/data/2.5/weather?q=luderitz&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 333
    http://api.openweathermap.org/data/2.5/weather?q=tessalit&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 334
    http://api.openweathermap.org/data/2.5/weather?q=illoqqortoormiut&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 335
    http://api.openweathermap.org/data/2.5/weather?q=chuy&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 336
    http://api.openweathermap.org/data/2.5/weather?q=bardiyah&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 337
    http://api.openweathermap.org/data/2.5/weather?q=tabas&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 338
    http://api.openweathermap.org/data/2.5/weather?q=chapais&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 339
    http://api.openweathermap.org/data/2.5/weather?q=hithadhoo&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 340
    http://api.openweathermap.org/data/2.5/weather?q=kununurra&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 341
    http://api.openweathermap.org/data/2.5/weather?q=ribeira grande&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 342
    http://api.openweathermap.org/data/2.5/weather?q=fort saint james&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 343
    http://api.openweathermap.org/data/2.5/weather?q=longyearbyen&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 344
    http://api.openweathermap.org/data/2.5/weather?q=kuche&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 345
    http://api.openweathermap.org/data/2.5/weather?q=foshan&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 346
    http://api.openweathermap.org/data/2.5/weather?q=adrar&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 347
    http://api.openweathermap.org/data/2.5/weather?q=hobyo&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 348
    http://api.openweathermap.org/data/2.5/weather?q=milkovo&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 349
    http://api.openweathermap.org/data/2.5/weather?q=junin&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 350
    http://api.openweathermap.org/data/2.5/weather?q=villazon&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 351
    http://api.openweathermap.org/data/2.5/weather?q=marrakesh&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 352
    http://api.openweathermap.org/data/2.5/weather?q=visnes&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 353
    http://api.openweathermap.org/data/2.5/weather?q=humboldt&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 354
    http://api.openweathermap.org/data/2.5/weather?q=akdagmadeni&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 355
    http://api.openweathermap.org/data/2.5/weather?q=puerto ayora&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 356
    http://api.openweathermap.org/data/2.5/weather?q=baykit&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 357
    http://api.openweathermap.org/data/2.5/weather?q=erenhot&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 358
    http://api.openweathermap.org/data/2.5/weather?q=pitimbu&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 359
    http://api.openweathermap.org/data/2.5/weather?q=manta&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 360
    http://api.openweathermap.org/data/2.5/weather?q=zhob&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 361
    http://api.openweathermap.org/data/2.5/weather?q=port lincoln&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 362
    http://api.openweathermap.org/data/2.5/weather?q=de aar&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 363
    http://api.openweathermap.org/data/2.5/weather?q=torbay&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 364
    http://api.openweathermap.org/data/2.5/weather?q=vanavara&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 365
    http://api.openweathermap.org/data/2.5/weather?q=aksum&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 366
    http://api.openweathermap.org/data/2.5/weather?q=santa rosa&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 367
    http://api.openweathermap.org/data/2.5/weather?q=moree&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 368
    http://api.openweathermap.org/data/2.5/weather?q=rawson&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 369
    http://api.openweathermap.org/data/2.5/weather?q=tondon&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 370
    http://api.openweathermap.org/data/2.5/weather?q=antalaha&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 371
    http://api.openweathermap.org/data/2.5/weather?q=ullal&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 372
    http://api.openweathermap.org/data/2.5/weather?q=thilogne&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 373
    http://api.openweathermap.org/data/2.5/weather?q=otane&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 374
    http://api.openweathermap.org/data/2.5/weather?q=taolanaro&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 375
    http://api.openweathermap.org/data/2.5/weather?q=munster&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 376
    http://api.openweathermap.org/data/2.5/weather?q=mahibadhoo&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 377
    http://api.openweathermap.org/data/2.5/weather?q=coruripe&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 378
    http://api.openweathermap.org/data/2.5/weather?q=saint-francois&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 379
    http://api.openweathermap.org/data/2.5/weather?q=kodiak&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 380
    http://api.openweathermap.org/data/2.5/weather?q=mount isa&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 381
    http://api.openweathermap.org/data/2.5/weather?q=salamiyah&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 382
    http://api.openweathermap.org/data/2.5/weather?q=hovd&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 383
    http://api.openweathermap.org/data/2.5/weather?q=roswell&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 384
    http://api.openweathermap.org/data/2.5/weather?q=alcantara&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 385
    http://api.openweathermap.org/data/2.5/weather?q=cairns&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 386
    http://api.openweathermap.org/data/2.5/weather?q=falealupo&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 387
    http://api.openweathermap.org/data/2.5/weather?q=babanusah&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 388
    http://api.openweathermap.org/data/2.5/weather?q=dikson&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 389
    http://api.openweathermap.org/data/2.5/weather?q=srednekolymsk&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 390
    http://api.openweathermap.org/data/2.5/weather?q=matinhos&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 391
    http://api.openweathermap.org/data/2.5/weather?q=mayumba&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 392
    http://api.openweathermap.org/data/2.5/weather?q=busselton&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 393
    http://api.openweathermap.org/data/2.5/weather?q=kampot&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 394
    http://api.openweathermap.org/data/2.5/weather?q=alyangula&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 395
    http://api.openweathermap.org/data/2.5/weather?q=careiro da varzea&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 396
    http://api.openweathermap.org/data/2.5/weather?q=naze&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 397
    http://api.openweathermap.org/data/2.5/weather?q=fort saint john&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 398
    http://api.openweathermap.org/data/2.5/weather?q=port hardy&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 399
    http://api.openweathermap.org/data/2.5/weather?q=aasiaat&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 400
    http://api.openweathermap.org/data/2.5/weather?q=manakara&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 401
    http://api.openweathermap.org/data/2.5/weather?q=necochea&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 402
    http://api.openweathermap.org/data/2.5/weather?q=shelburne&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 403
    http://api.openweathermap.org/data/2.5/weather?q=bogorodskoye&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 404
    http://api.openweathermap.org/data/2.5/weather?q=nushki&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 405
    http://api.openweathermap.org/data/2.5/weather?q=zalesovo&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 406
    http://api.openweathermap.org/data/2.5/weather?q=sabang&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 407
    http://api.openweathermap.org/data/2.5/weather?q=kamenskoye&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 408
    http://api.openweathermap.org/data/2.5/weather?q=bilma&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 409
    http://api.openweathermap.org/data/2.5/weather?q=hualmay&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 410
    http://api.openweathermap.org/data/2.5/weather?q=kloulklubed&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 411
    http://api.openweathermap.org/data/2.5/weather?q=lakeway&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 412
    http://api.openweathermap.org/data/2.5/weather?q=pokhara&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 413
    http://api.openweathermap.org/data/2.5/weather?q=tumannyy&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 414
    http://api.openweathermap.org/data/2.5/weather?q=trelew&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 415
    http://api.openweathermap.org/data/2.5/weather?q=lagoa&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 416
    http://api.openweathermap.org/data/2.5/weather?q=asyut&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 417
    http://api.openweathermap.org/data/2.5/weather?q=port keats&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 418
    http://api.openweathermap.org/data/2.5/weather?q=ketchikan&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 419
    http://api.openweathermap.org/data/2.5/weather?q=normandin&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 420
    http://api.openweathermap.org/data/2.5/weather?q=ponta delgada&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 421
    http://api.openweathermap.org/data/2.5/weather?q=kentau&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 422
    http://api.openweathermap.org/data/2.5/weather?q=agadir&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 423
    http://api.openweathermap.org/data/2.5/weather?q=yeppoon&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 424
    http://api.openweathermap.org/data/2.5/weather?q=sinnamary&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 425
    http://api.openweathermap.org/data/2.5/weather?q=ocean city&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 426
    http://api.openweathermap.org/data/2.5/weather?q=minbu&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 427
    http://api.openweathermap.org/data/2.5/weather?q=cape town&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 428
    http://api.openweathermap.org/data/2.5/weather?q=port-gentil&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 429
    http://api.openweathermap.org/data/2.5/weather?q=labuhan&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 430
    http://api.openweathermap.org/data/2.5/weather?q=moose factory&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 431
    http://api.openweathermap.org/data/2.5/weather?q=rikitea&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 432
    http://api.openweathermap.org/data/2.5/weather?q=marsh harbour&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 433
    http://api.openweathermap.org/data/2.5/weather?q=tabou&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 434
    http://api.openweathermap.org/data/2.5/weather?q=hokitika&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 435
    http://api.openweathermap.org/data/2.5/weather?q=pires do rio&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 436
    http://api.openweathermap.org/data/2.5/weather?q=uch&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 437
    http://api.openweathermap.org/data/2.5/weather?q=puerto baquerizo moreno&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 438
    http://api.openweathermap.org/data/2.5/weather?q=pangody&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 439
    http://api.openweathermap.org/data/2.5/weather?q=port alfred&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 440
    http://api.openweathermap.org/data/2.5/weather?q=ratnagiri&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 441
    http://api.openweathermap.org/data/2.5/weather?q=tuktoyaktuk&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 442
    http://api.openweathermap.org/data/2.5/weather?q=sao filipe&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 443
    http://api.openweathermap.org/data/2.5/weather?q=mount gambier&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 444
    http://api.openweathermap.org/data/2.5/weather?q=khash&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 445
    http://api.openweathermap.org/data/2.5/weather?q=darhan&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 446
    http://api.openweathermap.org/data/2.5/weather?q=ninghai&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 447
    http://api.openweathermap.org/data/2.5/weather?q=pousat&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 448
    http://api.openweathermap.org/data/2.5/weather?q=caxito&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 449
    http://api.openweathermap.org/data/2.5/weather?q=umm kaddadah&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 450
    http://api.openweathermap.org/data/2.5/weather?q=ararangua&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 451
    http://api.openweathermap.org/data/2.5/weather?q=hobart&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 452
    http://api.openweathermap.org/data/2.5/weather?q=port elizabeth&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 453
    http://api.openweathermap.org/data/2.5/weather?q=anshun&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 454
    http://api.openweathermap.org/data/2.5/weather?q=ulladulla&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 455
    http://api.openweathermap.org/data/2.5/weather?q=butaritari&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 456
    http://api.openweathermap.org/data/2.5/weather?q=sentyabrskiy&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 457
    http://api.openweathermap.org/data/2.5/weather?q=doka&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 458
    http://api.openweathermap.org/data/2.5/weather?q=muncar&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 459
    http://api.openweathermap.org/data/2.5/weather?q=minden&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 460
    http://api.openweathermap.org/data/2.5/weather?q=ampanihy&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 461
    http://api.openweathermap.org/data/2.5/weather?q=peniche&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 462
    http://api.openweathermap.org/data/2.5/weather?q=kerch&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 463
    http://api.openweathermap.org/data/2.5/weather?q=iquitos&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 464
    http://api.openweathermap.org/data/2.5/weather?q=gazojak&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 465
    http://api.openweathermap.org/data/2.5/weather?q=aksu&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 466
    http://api.openweathermap.org/data/2.5/weather?q=chokurdakh&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 467
    http://api.openweathermap.org/data/2.5/weather?q=hun&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 468
    http://api.openweathermap.org/data/2.5/weather?q=tinyahuarco&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 469
    http://api.openweathermap.org/data/2.5/weather?q=sulangan&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 470
    http://api.openweathermap.org/data/2.5/weather?q=kholodnyy&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 471
    http://api.openweathermap.org/data/2.5/weather?q=santa lucia&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 472
    http://api.openweathermap.org/data/2.5/weather?q=palabuhanratu&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 473
    http://api.openweathermap.org/data/2.5/weather?q=matadi&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 474
    http://api.openweathermap.org/data/2.5/weather?q=lompoc&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 475
    http://api.openweathermap.org/data/2.5/weather?q=marsa matruh&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 476
    http://api.openweathermap.org/data/2.5/weather?q=talnakh&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 477
    http://api.openweathermap.org/data/2.5/weather?q=narsaq&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 478
    http://api.openweathermap.org/data/2.5/weather?q=pemangkat&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 479
    http://api.openweathermap.org/data/2.5/weather?q=alangulam&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 480
    http://api.openweathermap.org/data/2.5/weather?q=henties bay&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 481
    http://api.openweathermap.org/data/2.5/weather?q=san ignacio&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 482
    http://api.openweathermap.org/data/2.5/weather?q=ilulissat&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 483
    http://api.openweathermap.org/data/2.5/weather?q=norrtalje&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 484
    http://api.openweathermap.org/data/2.5/weather?q=grand river south east&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 485
    http://api.openweathermap.org/data/2.5/weather?q=siderno&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 486
    http://api.openweathermap.org/data/2.5/weather?q=khromtau&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 487
    http://api.openweathermap.org/data/2.5/weather?q=grimari&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 488
    http://api.openweathermap.org/data/2.5/weather?q=esterhazy&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 489
    http://api.openweathermap.org/data/2.5/weather?q=tucuman&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 490
    http://api.openweathermap.org/data/2.5/weather?q=saldanha&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 491
    http://api.openweathermap.org/data/2.5/weather?q=caravelas&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 492
    http://api.openweathermap.org/data/2.5/weather?q=upernavik&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 493
    http://api.openweathermap.org/data/2.5/weather?q=vaitupu&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 494
    http://api.openweathermap.org/data/2.5/weather?q=abha&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 495
    http://api.openweathermap.org/data/2.5/weather?q=pisco&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 496
    http://api.openweathermap.org/data/2.5/weather?q=zgorzelec&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 497
    http://api.openweathermap.org/data/2.5/weather?q=mahebourg&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 498
    http://api.openweathermap.org/data/2.5/weather?q=salinas&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 499
    http://api.openweathermap.org/data/2.5/weather?q=severo-kurilsk&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 500
    http://api.openweathermap.org/data/2.5/weather?q=port hedland&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 501
    http://api.openweathermap.org/data/2.5/weather?q=budogoshch&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 502
    http://api.openweathermap.org/data/2.5/weather?q=tommot&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 503
    http://api.openweathermap.org/data/2.5/weather?q=malatya&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 504
    http://api.openweathermap.org/data/2.5/weather?q=cidreira&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 505
    http://api.openweathermap.org/data/2.5/weather?q=ixtapa&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 506
    http://api.openweathermap.org/data/2.5/weather?q=satitoa&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 507
    http://api.openweathermap.org/data/2.5/weather?q=khonuu&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 508
    http://api.openweathermap.org/data/2.5/weather?q=dunedin&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 509
    http://api.openweathermap.org/data/2.5/weather?q=saint george&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 510
    http://api.openweathermap.org/data/2.5/weather?q=amderma&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 511
    http://api.openweathermap.org/data/2.5/weather?q=coquimbo&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 512
    http://api.openweathermap.org/data/2.5/weather?q=gatton&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 513
    http://api.openweathermap.org/data/2.5/weather?q=eyl&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 514
    http://api.openweathermap.org/data/2.5/weather?q=pangnirtung&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 515
    http://api.openweathermap.org/data/2.5/weather?q=clearwater&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 516
    http://api.openweathermap.org/data/2.5/weather?q=mullaitivu&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 517
    http://api.openweathermap.org/data/2.5/weather?q=cockburn town&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 518
    http://api.openweathermap.org/data/2.5/weather?q=gurupi&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 519
    http://api.openweathermap.org/data/2.5/weather?q=airai&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 520
    http://api.openweathermap.org/data/2.5/weather?q=mhango&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 521
    http://api.openweathermap.org/data/2.5/weather?q=yumen&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 522
    http://api.openweathermap.org/data/2.5/weather?q=faanui&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 523
    http://api.openweathermap.org/data/2.5/weather?q=taoudenni&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 524
    http://api.openweathermap.org/data/2.5/weather?q=ozernovskiy&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 525
    http://api.openweathermap.org/data/2.5/weather?q=petropavlovsk-kamchatskiy&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 526
    http://api.openweathermap.org/data/2.5/weather?q=fairbanks&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 527
    http://api.openweathermap.org/data/2.5/weather?q=yulara&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 528
    http://api.openweathermap.org/data/2.5/weather?q=leningradskiy&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 529
    http://api.openweathermap.org/data/2.5/weather?q=yaan&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 530
    http://api.openweathermap.org/data/2.5/weather?q=burgeo&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 531
    http://api.openweathermap.org/data/2.5/weather?q=tenango del aire&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 532
    http://api.openweathermap.org/data/2.5/weather?q=pyay&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 533
    http://api.openweathermap.org/data/2.5/weather?q=tadine&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 534
    http://api.openweathermap.org/data/2.5/weather?q=koulikoro&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 535
    http://api.openweathermap.org/data/2.5/weather?q=sao joao da barra&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 536
    http://api.openweathermap.org/data/2.5/weather?q=inndyr&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 537
    http://api.openweathermap.org/data/2.5/weather?q=kirakira&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 538
    http://api.openweathermap.org/data/2.5/weather?q=korla&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 539
    http://api.openweathermap.org/data/2.5/weather?q=kiama&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 540
    http://api.openweathermap.org/data/2.5/weather?q=port moresby&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 541
    http://api.openweathermap.org/data/2.5/weather?q=marawi&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 542
    http://api.openweathermap.org/data/2.5/weather?q=maceio&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 543
    http://api.openweathermap.org/data/2.5/weather?q=coihaique&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 544
    http://api.openweathermap.org/data/2.5/weather?q=marienburg&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 545
    http://api.openweathermap.org/data/2.5/weather?q=brae&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 546
    http://api.openweathermap.org/data/2.5/weather?q=kokoda&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 547
    http://api.openweathermap.org/data/2.5/weather?q=stornoway&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 548
    http://api.openweathermap.org/data/2.5/weather?q=lata&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 549
    http://api.openweathermap.org/data/2.5/weather?q=kuantan&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 550
    http://api.openweathermap.org/data/2.5/weather?q=san carlos de bariloche&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 551
    http://api.openweathermap.org/data/2.5/weather?q=rawannawi&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 552
    http://api.openweathermap.org/data/2.5/weather?q=cuamba&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 553
    http://api.openweathermap.org/data/2.5/weather?q=vancouver&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 554
    http://api.openweathermap.org/data/2.5/weather?q=san cristobal&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 555
    http://api.openweathermap.org/data/2.5/weather?q=puerto colombia&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 556
    http://api.openweathermap.org/data/2.5/weather?q=olinda&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 557
    http://api.openweathermap.org/data/2.5/weather?q=margate&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 558
    http://api.openweathermap.org/data/2.5/weather?q=do rud&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 559
    http://api.openweathermap.org/data/2.5/weather?q=luganville&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 560
    http://api.openweathermap.org/data/2.5/weather?q=sioux lookout&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 561
    http://api.openweathermap.org/data/2.5/weather?q=new norfolk&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 562
    http://api.openweathermap.org/data/2.5/weather?q=gushikawa&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 563
    http://api.openweathermap.org/data/2.5/weather?q=mitu&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 564
    http://api.openweathermap.org/data/2.5/weather?q=nikolskoye&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 565
    http://api.openweathermap.org/data/2.5/weather?q=la seyne-sur-mer&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 566
    http://api.openweathermap.org/data/2.5/weather?q=grand-santi&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 567
    http://api.openweathermap.org/data/2.5/weather?q=buala&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 568
    http://api.openweathermap.org/data/2.5/weather?q=fort nelson&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 569
    http://api.openweathermap.org/data/2.5/weather?q=polunochnoye&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 570
    http://api.openweathermap.org/data/2.5/weather?q=porbandar&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 571
    http://api.openweathermap.org/data/2.5/weather?q=rocha&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 572
    http://api.openweathermap.org/data/2.5/weather?q=inhambane&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 573
    http://api.openweathermap.org/data/2.5/weather?q=gao&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 574
    http://api.openweathermap.org/data/2.5/weather?q=bargal&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
     Missing field... skipping.
    Now retrieving city # 575
    http://api.openweathermap.org/data/2.5/weather?q=fuyu&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 576
    http://api.openweathermap.org/data/2.5/weather?q=ugoofaaru&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 577
    http://api.openweathermap.org/data/2.5/weather?q=miraflores&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 578
    http://api.openweathermap.org/data/2.5/weather?q=hermanus&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 579
    http://api.openweathermap.org/data/2.5/weather?q=conde&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 580
    http://api.openweathermap.org/data/2.5/weather?q=targusor&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 581
    http://api.openweathermap.org/data/2.5/weather?q=tura&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 582
    http://api.openweathermap.org/data/2.5/weather?q=clarksdale&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 583
    http://api.openweathermap.org/data/2.5/weather?q=zhigansk&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 584
    http://api.openweathermap.org/data/2.5/weather?q=troy&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 585
    http://api.openweathermap.org/data/2.5/weather?q=yambio&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 586
    http://api.openweathermap.org/data/2.5/weather?q=pringsewu&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 587
    http://api.openweathermap.org/data/2.5/weather?q=pedernales&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 588
    http://api.openweathermap.org/data/2.5/weather?q=kaeo&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 589
    http://api.openweathermap.org/data/2.5/weather?q=katsina&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 590
    http://api.openweathermap.org/data/2.5/weather?q=kolaras&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 591
    http://api.openweathermap.org/data/2.5/weather?q=teya&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 592
    http://api.openweathermap.org/data/2.5/weather?q=souillac&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 593
    http://api.openweathermap.org/data/2.5/weather?q=catalina foothills&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 594
    http://api.openweathermap.org/data/2.5/weather?q=hami&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 595
    http://api.openweathermap.org/data/2.5/weather?q=inta&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 596
    http://api.openweathermap.org/data/2.5/weather?q=victoria&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 597
    http://api.openweathermap.org/data/2.5/weather?q=kerema&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 598
    http://api.openweathermap.org/data/2.5/weather?q=moranbah&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --Now retrieving city # 599
    http://api.openweathermap.org/data/2.5/weather?q=bontang&units=IMPERIAL&mode=json&APPID=bab6ed8714b504b5454b34baa8e421bb
    --




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>City</th>
      <th>Latitude</th>
      <th>Longitude</th>
      <th>Temperature</th>
      <th>Humidity %</th>
      <th>Wind Speed</th>
      <th>Cloudiness %</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>451</th>
      <td>RU</td>
      <td>aykhal</td>
      <td>66</td>
      <td>111.5</td>
      <td>-25.75</td>
      <td>37</td>
      <td>2.73</td>
      <td>68</td>
    </tr>
    <tr>
      <th>505</th>
      <td>CU</td>
      <td>mantua</td>
      <td>22.29</td>
      <td>-84.28</td>
      <td>80.41</td>
      <td>67</td>
      <td>7.09</td>
      <td>12</td>
    </tr>
    <tr>
      <th>235</th>
      <td>NZ</td>
      <td>ahipara</td>
      <td>-35.17</td>
      <td>173.17</td>
      <td>70.29</td>
      <td>71</td>
      <td>8.55</td>
      <td>0</td>
    </tr>
    <tr>
      <th>168</th>
      <td>JP</td>
      <td>hasaki</td>
      <td>35.73</td>
      <td>140.83</td>
      <td>32</td>
      <td>100</td>
      <td>1.12</td>
      <td>20</td>
    </tr>
    <tr>
      <th>64</th>
      <td></td>
      <td>rungata</td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>
</div>




```python
selected_cities.dtypes
```




    Country         object
    City            object
    Latitude        object
    Longitude       object
    Temperature     object
    Humidity %      object
    Wind Speed      object
    Cloudiness %    object
    dtype: object




```python
selected_cities.convert_objects(convert_numeric=True)
```

    /Users/andy_felicitas/anaconda/lib/python3.6/site-packages/ipykernel_launcher.py:1: FutureWarning: convert_objects is deprecated.  Use the data-type specific converters pd.to_datetime, pd.to_timedelta and pd.to_numeric.
      """Entry point for launching an IPython kernel.





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>City</th>
      <th>Latitude</th>
      <th>Longitude</th>
      <th>Temperature</th>
      <th>Humidity %</th>
      <th>Wind Speed</th>
      <th>Cloudiness %</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>451</th>
      <td>RU</td>
      <td>aykhal</td>
      <td>66.00</td>
      <td>111.50</td>
      <td>-25.75</td>
      <td>37.0</td>
      <td>2.73</td>
      <td>68.0</td>
    </tr>
    <tr>
      <th>505</th>
      <td>CU</td>
      <td>mantua</td>
      <td>22.29</td>
      <td>-84.28</td>
      <td>80.41</td>
      <td>67.0</td>
      <td>7.09</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>235</th>
      <td>NZ</td>
      <td>ahipara</td>
      <td>-35.17</td>
      <td>173.17</td>
      <td>70.29</td>
      <td>71.0</td>
      <td>8.55</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>168</th>
      <td>JP</td>
      <td>hasaki</td>
      <td>35.73</td>
      <td>140.83</td>
      <td>32.00</td>
      <td>100.0</td>
      <td>1.12</td>
      <td>20.0</td>
    </tr>
    <tr>
      <th>64</th>
      <td></td>
      <td>rungata</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>448</th>
      <td>RU</td>
      <td>khandyga</td>
      <td>62.67</td>
      <td>135.60</td>
      <td>-39.07</td>
      <td>81.0</td>
      <td>2.73</td>
      <td>56.0</td>
    </tr>
    <tr>
      <th>53</th>
      <td>ID</td>
      <td>bengkulu</td>
      <td>-3.80</td>
      <td>102.27</td>
      <td>79.11</td>
      <td>100.0</td>
      <td>4.29</td>
      <td>56.0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>RU</td>
      <td>yerbogachen</td>
      <td>61.28</td>
      <td>108.01</td>
      <td>-12.43</td>
      <td>77.0</td>
      <td>2.95</td>
      <td>68.0</td>
    </tr>
    <tr>
      <th>39</th>
      <td>PG</td>
      <td>kavieng</td>
      <td>-2.57</td>
      <td>150.80</td>
      <td>78.75</td>
      <td>100.0</td>
      <td>7.43</td>
      <td>88.0</td>
    </tr>
    <tr>
      <th>43</th>
      <td></td>
      <td>mahaicony</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>117</th>
      <td>MU</td>
      <td>cap malheureux</td>
      <td>-19.98</td>
      <td>57.61</td>
      <td>77.00</td>
      <td>78.0</td>
      <td>11.41</td>
      <td>40.0</td>
    </tr>
    <tr>
      <th>529</th>
      <td>CN</td>
      <td>dali</td>
      <td>25.70</td>
      <td>100.18</td>
      <td>30.64</td>
      <td>100.0</td>
      <td>1.95</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>415</th>
      <td>MX</td>
      <td>maneadero</td>
      <td>31.72</td>
      <td>-116.57</td>
      <td>60.66</td>
      <td>34.0</td>
      <td>4.74</td>
      <td>20.0</td>
    </tr>
    <tr>
      <th>198</th>
      <td>NZ</td>
      <td>tuatapere</td>
      <td>-46.13</td>
      <td>167.68</td>
      <td>62.19</td>
      <td>91.0</td>
      <td>3.51</td>
      <td>48.0</td>
    </tr>
    <tr>
      <th>361</th>
      <td></td>
      <td>olafsvik</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>417</th>
      <td>RU</td>
      <td>nizhniy kuranakh</td>
      <td>58.84</td>
      <td>125.49</td>
      <td>-20.71</td>
      <td>85.0</td>
      <td>2.73</td>
      <td>48.0</td>
    </tr>
    <tr>
      <th>504</th>
      <td>PH</td>
      <td>pasil</td>
      <td>17.38</td>
      <td>121.13</td>
      <td>63.76</td>
      <td>98.0</td>
      <td>1.83</td>
      <td>92.0</td>
    </tr>
    <tr>
      <th>174</th>
      <td></td>
      <td>mys shmidta</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>556</th>
      <td></td>
      <td>saleaula</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>239</th>
      <td>IT</td>
      <td>mazara del vallo</td>
      <td>37.66</td>
      <td>12.59</td>
      <td>44.60</td>
      <td>100.0</td>
      <td>2.24</td>
      <td>20.0</td>
    </tr>
    <tr>
      <th>500</th>
      <td>US</td>
      <td>atchison</td>
      <td>39.56</td>
      <td>-95.12</td>
      <td>48.20</td>
      <td>26.0</td>
      <td>24.16</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>322</th>
      <td>BB</td>
      <td>bathsheba</td>
      <td>13.22</td>
      <td>-59.52</td>
      <td>80.60</td>
      <td>94.0</td>
      <td>6.93</td>
      <td>40.0</td>
    </tr>
    <tr>
      <th>56</th>
      <td>LK</td>
      <td>hambantota</td>
      <td>6.12</td>
      <td>81.12</td>
      <td>76.14</td>
      <td>100.0</td>
      <td>4.29</td>
      <td>68.0</td>
    </tr>
    <tr>
      <th>359</th>
      <td>AI</td>
      <td>the valley</td>
      <td>18.22</td>
      <td>-63.06</td>
      <td>80.60</td>
      <td>78.0</td>
      <td>12.75</td>
      <td>20.0</td>
    </tr>
    <tr>
      <th>237</th>
      <td>RU</td>
      <td>priyutnoye</td>
      <td>46.10</td>
      <td>43.51</td>
      <td>37.40</td>
      <td>100.0</td>
      <td>17.90</td>
      <td>76.0</td>
    </tr>
    <tr>
      <th>290</th>
      <td>US</td>
      <td>sitka</td>
      <td>57.05</td>
      <td>-135.33</td>
      <td>48.20</td>
      <td>87.0</td>
      <td>24.16</td>
      <td>90.0</td>
    </tr>
    <tr>
      <th>421</th>
      <td>TH</td>
      <td>nong kung si</td>
      <td>16.65</td>
      <td>103.30</td>
      <td>64.40</td>
      <td>93.0</td>
      <td>3.36</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>139</th>
      <td>GH</td>
      <td>axim</td>
      <td>4.87</td>
      <td>-2.24</td>
      <td>83.83</td>
      <td>96.0</td>
      <td>7.99</td>
      <td>20.0</td>
    </tr>
    <tr>
      <th>86</th>
      <td>IN</td>
      <td>kavaratti</td>
      <td>10.57</td>
      <td>72.64</td>
      <td>76.81</td>
      <td>100.0</td>
      <td>7.76</td>
      <td>88.0</td>
    </tr>
    <tr>
      <th>472</th>
      <td>NA</td>
      <td>opuwo</td>
      <td>-18.06</td>
      <td>13.84</td>
      <td>75.28</td>
      <td>32.0</td>
      <td>1.39</td>
      <td>80.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>306</th>
      <td>IN</td>
      <td>porbandar</td>
      <td>21.64</td>
      <td>69.61</td>
      <td>68.13</td>
      <td>97.0</td>
      <td>14.47</td>
      <td>88.0</td>
    </tr>
    <tr>
      <th>262</th>
      <td>UY</td>
      <td>rocha</td>
      <td>-34.48</td>
      <td>-54.33</td>
      <td>71.59</td>
      <td>53.0</td>
      <td>11.68</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>21</th>
      <td>MZ</td>
      <td>inhambane</td>
      <td>-23.86</td>
      <td>35.38</td>
      <td>75.73</td>
      <td>96.0</td>
      <td>9.66</td>
      <td>88.0</td>
    </tr>
    <tr>
      <th>544</th>
      <td>ML</td>
      <td>gao</td>
      <td>16.27</td>
      <td>-0.04</td>
      <td>70.96</td>
      <td>36.0</td>
      <td>8.66</td>
      <td>76.0</td>
    </tr>
    <tr>
      <th>194</th>
      <td></td>
      <td>bargal</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>485</th>
      <td>CN</td>
      <td>fuyu</td>
      <td>45.18</td>
      <td>124.82</td>
      <td>-7.75</td>
      <td>62.0</td>
      <td>6.08</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>341</th>
      <td>MV</td>
      <td>ugoofaaru</td>
      <td>5.67</td>
      <td>73.00</td>
      <td>82.84</td>
      <td>100.0</td>
      <td>10.78</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>555</th>
      <td>CO</td>
      <td>miraflores</td>
      <td>1.34</td>
      <td>-71.95</td>
      <td>82.89</td>
      <td>80.0</td>
      <td>2.95</td>
      <td>24.0</td>
    </tr>
    <tr>
      <th>114</th>
      <td>ZA</td>
      <td>hermanus</td>
      <td>-34.42</td>
      <td>19.23</td>
      <td>64.62</td>
      <td>67.0</td>
      <td>11.23</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>188</th>
      <td>BR</td>
      <td>conde</td>
      <td>-7.26</td>
      <td>-34.91</td>
      <td>80.60</td>
      <td>78.0</td>
      <td>8.05</td>
      <td>40.0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>RO</td>
      <td>targusor</td>
      <td>44.45</td>
      <td>28.42</td>
      <td>33.80</td>
      <td>100.0</td>
      <td>8.05</td>
      <td>20.0</td>
    </tr>
    <tr>
      <th>590</th>
      <td>IN</td>
      <td>tura</td>
      <td>25.52</td>
      <td>90.22</td>
      <td>55.44</td>
      <td>85.0</td>
      <td>2.17</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>430</th>
      <td>US</td>
      <td>clarksdale</td>
      <td>34.20</td>
      <td>-90.57</td>
      <td>46.40</td>
      <td>87.0</td>
      <td>10.29</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>181</th>
      <td>RU</td>
      <td>zhigansk</td>
      <td>66.77</td>
      <td>123.37</td>
      <td>-38.53</td>
      <td>80.0</td>
      <td>4.85</td>
      <td>64.0</td>
    </tr>
    <tr>
      <th>536</th>
      <td>US</td>
      <td>troy</td>
      <td>42.61</td>
      <td>-83.15</td>
      <td>41.00</td>
      <td>38.0</td>
      <td>19.46</td>
      <td>75.0</td>
    </tr>
    <tr>
      <th>345</th>
      <td>SS</td>
      <td>yambio</td>
      <td>4.57</td>
      <td>28.40</td>
      <td>68.04</td>
      <td>86.0</td>
      <td>2.73</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>285</th>
      <td>ID</td>
      <td>pringsewu</td>
      <td>-5.36</td>
      <td>104.97</td>
      <td>73.53</td>
      <td>91.0</td>
      <td>2.06</td>
      <td>48.0</td>
    </tr>
    <tr>
      <th>226</th>
      <td>DO</td>
      <td>pedernales</td>
      <td>18.04</td>
      <td>-71.74</td>
      <td>86.00</td>
      <td>74.0</td>
      <td>16.11</td>
      <td>75.0</td>
    </tr>
    <tr>
      <th>66</th>
      <td>NZ</td>
      <td>kaeo</td>
      <td>-35.10</td>
      <td>173.78</td>
      <td>71.64</td>
      <td>63.0</td>
      <td>11.01</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>135</th>
      <td>NG</td>
      <td>katsina</td>
      <td>12.99</td>
      <td>7.60</td>
      <td>65.16</td>
      <td>29.0</td>
      <td>8.77</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>333</th>
      <td>IN</td>
      <td>kolaras</td>
      <td>25.23</td>
      <td>77.60</td>
      <td>60.16</td>
      <td>63.0</td>
      <td>2.95</td>
      <td>92.0</td>
    </tr>
    <tr>
      <th>109</th>
      <td>RU</td>
      <td>teya</td>
      <td>60.38</td>
      <td>92.63</td>
      <td>20.07</td>
      <td>81.0</td>
      <td>6.64</td>
      <td>80.0</td>
    </tr>
    <tr>
      <th>153</th>
      <td>MU</td>
      <td>souillac</td>
      <td>-20.52</td>
      <td>57.52</td>
      <td>77.00</td>
      <td>78.0</td>
      <td>11.41</td>
      <td>40.0</td>
    </tr>
    <tr>
      <th>48</th>
      <td>US</td>
      <td>catalina foothills</td>
      <td>32.30</td>
      <td>-110.92</td>
      <td>62.60</td>
      <td>56.0</td>
      <td>6.93</td>
      <td>20.0</td>
    </tr>
    <tr>
      <th>127</th>
      <td>CN</td>
      <td>hami</td>
      <td>42.80</td>
      <td>93.45</td>
      <td>16.92</td>
      <td>71.0</td>
      <td>3.06</td>
      <td>80.0</td>
    </tr>
    <tr>
      <th>335</th>
      <td>RU</td>
      <td>inta</td>
      <td>66.03</td>
      <td>60.17</td>
      <td>31.32</td>
      <td>86.0</td>
      <td>7.65</td>
      <td>88.0</td>
    </tr>
    <tr>
      <th>339</th>
      <td>CA</td>
      <td>victoria</td>
      <td>48.43</td>
      <td>-123.37</td>
      <td>42.80</td>
      <td>75.0</td>
      <td>8.05</td>
      <td>40.0</td>
    </tr>
    <tr>
      <th>575</th>
      <td>PG</td>
      <td>kerema</td>
      <td>-7.96</td>
      <td>145.78</td>
      <td>72.31</td>
      <td>100.0</td>
      <td>1.83</td>
      <td>92.0</td>
    </tr>
    <tr>
      <th>592</th>
      <td>AU</td>
      <td>moranbah</td>
      <td>-22.00</td>
      <td>148.05</td>
      <td>70.33</td>
      <td>45.0</td>
      <td>6.53</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>385</th>
      <td>ID</td>
      <td>bontang</td>
      <td>0.13</td>
      <td>117.50</td>
      <td>79.24</td>
      <td>100.0</td>
      <td>2.17</td>
      <td>48.0</td>
    </tr>
  </tbody>
</table>
<p>600 rows × 8 columns</p>
</div>




```python
# save df as a csv
selected_cities.to_csv("weather_py_data_2.csv", encoding="utf-8", index=False)
```


```python
df = pd.read_csv("weather_py_data_2.csv")
```


```python
df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>City</th>
      <th>Latitude</th>
      <th>Longitude</th>
      <th>Temperature</th>
      <th>Humidity %</th>
      <th>Wind Speed</th>
      <th>Cloudiness %</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>RU</td>
      <td>aykhal</td>
      <td>66.00</td>
      <td>111.50</td>
      <td>-25.75</td>
      <td>37.0</td>
      <td>2.73</td>
      <td>68.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>CU</td>
      <td>mantua</td>
      <td>22.29</td>
      <td>-84.28</td>
      <td>80.41</td>
      <td>67.0</td>
      <td>7.09</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NZ</td>
      <td>ahipara</td>
      <td>-35.17</td>
      <td>173.17</td>
      <td>70.29</td>
      <td>71.0</td>
      <td>8.55</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>JP</td>
      <td>hasaki</td>
      <td>35.73</td>
      <td>140.83</td>
      <td>32.00</td>
      <td>100.0</td>
      <td>1.12</td>
      <td>20.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>NaN</td>
      <td>rungata</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.shape
```




    (600, 8)




```python
df.isnull().sum()
```




    Country         84
    City             0
    Latitude        78
    Longitude       78
    Temperature     78
    Humidity %      78
    Wind Speed      78
    Cloudiness %    78
    dtype: int64




```python
new_df = df.dropna(how='any')
```


```python
new_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Country</th>
      <th>City</th>
      <th>Latitude</th>
      <th>Longitude</th>
      <th>Temperature</th>
      <th>Humidity %</th>
      <th>Wind Speed</th>
      <th>Cloudiness %</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>RU</td>
      <td>aykhal</td>
      <td>66.00</td>
      <td>111.50</td>
      <td>-25.75</td>
      <td>37.0</td>
      <td>2.73</td>
      <td>68.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>CU</td>
      <td>mantua</td>
      <td>22.29</td>
      <td>-84.28</td>
      <td>80.41</td>
      <td>67.0</td>
      <td>7.09</td>
      <td>12.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>NZ</td>
      <td>ahipara</td>
      <td>-35.17</td>
      <td>173.17</td>
      <td>70.29</td>
      <td>71.0</td>
      <td>8.55</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>JP</td>
      <td>hasaki</td>
      <td>35.73</td>
      <td>140.83</td>
      <td>32.00</td>
      <td>100.0</td>
      <td>1.12</td>
      <td>20.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>RU</td>
      <td>khandyga</td>
      <td>62.67</td>
      <td>135.60</td>
      <td>-39.07</td>
      <td>81.0</td>
      <td>2.73</td>
      <td>56.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
new_df.shape
```




    (516, 8)




```python
# plot Temperature vs Latitude

plt.scatter(new_df["Latitude"],
           new_df["Temperature"],
           edgecolor="black", linewidths=1, marker="o",
           alpha=0.8)

plt.title("Latitude vs Temperature (F) 12/5/17")
plt.xlabel("Latitude")
plt.ylabel("Temperature")
plt.grid(True)
plt.xlim([-100, 100])
plt.ylim([-100, 150])

plt.savefig("LatTemp2.png")
sns.set()
plt.show()
```


![png](output_24_0.png)



```python
plt.scatter(new_df["Latitude"],
           new_df["Humidity %"],
           edgecolor="black", linewidths=1, marker="o",
           alpha=0.8)

plt.title("Latitude vs Humidity (F) 12/5/17")
plt.xlabel("Latitude")
plt.ylabel("Humidity (%)")
plt.grid(True)
plt.xlim([-100, 100])
plt.ylim([-20, 120])

# save figure
plt.savefig("LatHumidity2.png")
sns.set()
plt.show()
```


![png](output_25_0.png)



```python
plt.scatter(new_df["Latitude"],
           new_df["Cloudiness %"],
           edgecolor="black", linewidths=1, marker="o",
           alpha=0.8)

plt.title("Latitude vs Cloudiness (%) 12/5/17")
plt.xlabel("Latitude")
plt.ylabel("Cloudiness (%)")
plt.grid(True)
plt.xlim([-100, 100])
plt.ylim([-20, 120])

# save figure
plt.savefig("LatCloud2.png")
sns.set()
plt.show()
```


![png](output_26_0.png)



```python
plt.scatter(new_df["Latitude"],
           new_df["Wind Speed"],
           edgecolor="black", linewidths=1, marker="o",
           alpha=0.8)

plt.title("Latitude vs Wind Speed 12/5/17")
plt.xlabel("Latitude")
plt.ylabel("Wind Speed (mph)")
plt.grid(True)
plt.xlim([-100, 100])
plt.ylim([-5, 50])

# save figure
plt.savefig("LatWind2.png")
sns.set()
plt.show()
```


![png](output_27_0.png)



```python

```
