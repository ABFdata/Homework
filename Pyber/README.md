

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```


```python
# read csv ride
ride_data = pd.read_csv('ride_data.csv')
ride_data.head()
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
      <th>city</th>
      <th>date</th>
      <th>fare</th>
      <th>ride_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Sarabury</td>
      <td>2016-01-16 13:49:27</td>
      <td>38.35</td>
      <td>5403689035038</td>
    </tr>
    <tr>
      <th>1</th>
      <td>South Roy</td>
      <td>2016-01-02 18:42:34</td>
      <td>17.49</td>
      <td>4036272335942</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Wiseborough</td>
      <td>2016-01-21 17:35:29</td>
      <td>44.18</td>
      <td>3645042422587</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Spencertown</td>
      <td>2016-07-31 14:53:22</td>
      <td>6.87</td>
      <td>2242596575892</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Nguyenbury</td>
      <td>2016-07-09 04:42:44</td>
      <td>6.28</td>
      <td>1543057793673</td>
    </tr>
  </tbody>
</table>
</div>




```python
# read csv city
city_data = pd.read_csv('city_data.csv')
city_data.head()
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
      <th>city</th>
      <th>driver_count</th>
      <th>type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Nguyenbury</td>
      <td>8</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2</th>
      <td>East Douglas</td>
      <td>12</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>3</th>
      <td>West Dawnfurt</td>
      <td>34</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Rodriguezburgh</td>
      <td>52</td>
      <td>Urban</td>
    </tr>
  </tbody>
</table>
</div>




```python
# merge csv's
pyber_merge = pd.merge(ride_data, city_data, how="outer", on="city")
pyber_merge.head()
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
      <th>city</th>
      <th>date</th>
      <th>fare</th>
      <th>ride_id</th>
      <th>driver_count</th>
      <th>type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Sarabury</td>
      <td>2016-01-16 13:49:27</td>
      <td>38.35</td>
      <td>5403689035038</td>
      <td>46</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Sarabury</td>
      <td>2016-07-23 07:42:44</td>
      <td>21.76</td>
      <td>7546681945283</td>
      <td>46</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Sarabury</td>
      <td>2016-04-02 04:32:25</td>
      <td>38.03</td>
      <td>4932495851866</td>
      <td>46</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Sarabury</td>
      <td>2016-06-23 05:03:41</td>
      <td>26.82</td>
      <td>6711035373406</td>
      <td>46</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Sarabury</td>
      <td>2016-09-30 12:48:34</td>
      <td>30.30</td>
      <td>6388737278232</td>
      <td>46</td>
      <td>Urban</td>
    </tr>
  </tbody>
</table>
</div>



**New DataFrame**


```python
test = pd.DataFrame(pyber_merge[['city', 'fare', 'type', 'ride_id', 'driver_count']])
test.head()
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
      <th>city</th>
      <th>fare</th>
      <th>type</th>
      <th>ride_id</th>
      <th>driver_count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Sarabury</td>
      <td>38.35</td>
      <td>Urban</td>
      <td>5403689035038</td>
      <td>46</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Sarabury</td>
      <td>21.76</td>
      <td>Urban</td>
      <td>7546681945283</td>
      <td>46</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Sarabury</td>
      <td>38.03</td>
      <td>Urban</td>
      <td>4932495851866</td>
      <td>46</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Sarabury</td>
      <td>26.82</td>
      <td>Urban</td>
      <td>6711035373406</td>
      <td>46</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Sarabury</td>
      <td>30.30</td>
      <td>Urban</td>
      <td>6388737278232</td>
      <td>46</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Filter's out Urban
test_urban = test[test['type'] == 'Urban']
```


```python
# Total Rides Per City for Urban 
x_urban = pd.DataFrame(test_urban.groupby('city')['fare'].count())
```


```python
# Avg Fare Per City for Urban
y_urban = pd.DataFrame(test_urban.groupby('city')['fare'].mean())
```


```python
# Driver Count Per City for Urban
z_urban = pd.DataFrame(test_urban.groupby('city')['driver_count'].count())
```


```python
# Filter's out Suburban
test_suburban = test[test['type'] =='Suburban']
```


```python
# Total Rides Per City
x_suburban = pd.DataFrame(test_suburban.groupby('city')['fare'].count())
```


```python
# Avg Fare Per City
y_suburban = pd.DataFrame(test_suburban.groupby('city')['fare'].mean())
```


```python
# Driver Count Per City
z_suburban = pd.DataFrame(test_suburban.groupby('city')['driver_count'].count())
```


```python
# Filter's out Rural
test_rural = test[test['type'] =='Rural']
```


```python
# Total Rides Per City
x_rural = pd.DataFrame(test_rural.groupby('city')['fare'].count())
```


```python
# Avg Fare Per City
y_rural = pd.DataFrame(test_rural.groupby('city')['fare'].mean())
```


```python
# Driver Count Per City
z_rural = pd.DataFrame(test_rural.groupby('city')['driver_count'].count())
```


```python
# Set y limit
plt.ylim(15, 55)
```




    (15, 55)




```python
# Set x limit
plt.xlim(0, 40)
```




    (0, 40)




```python
# Set Labels
plt.title("Pyber Ride Sharing Data 2016")
plt.xlabel("Total Number of Rides (Per City)")
plt.ylabel("Average Fare($)")
```




    <matplotlib.text.Text at 0x12330dd30>




```python
urban_plot = plt.scatter(x_urban,
            y_urban,
            s=z_urban*10,             
            c="lightcoral",
            edgecolors="black",
            alpha=0.9, linewidth=1)
```


```python
suburban_plot = plt.scatter(x_suburban,
            y_suburban,
            s=z_suburban*10,               
            c="lightskyblue",
            edgecolors="black",
            alpha=0.8, linewidth=1)
```


```python
rural_plot = plt.scatter(x_rural,
            y_rural,
            s=z_rural*10,             
            c="gold",
            edgecolors="black",
            alpha=0.8, linewidth=1)
```


```python
plt.legend((urban_plot, suburban_plot, rural_plot), ('Urban', 'Suburban', 'Rural'))
```




    <matplotlib.legend.Legend at 0x1232e80f0>




```python
sns.set()
plt.show()
```


![png](output_25_0.png)


# Part II


```python
total_fares_sum = pyber_merge['fare'].sum()
total_fares_sum
```




    63651.309999999925




```python
rural_fares = pyber_merge.query("type !='Suburban'")
rural_fares2 = rural_fares.query("type !='Urban'")
rural_fares_total = rural_fares2['fare'].sum()
```


```python
suburban_fares = pyber_merge.query("type !='Rural'")
suburban_fares2 = suburban_fares.query("type !='Urban'")
suburban_fares_total = suburban_fares2['fare'].sum()
```


```python
urban_fares = pyber_merge.query("type !='Rural'")
urban_fares2 = urban_fares.query("type !='Suburban'")
urban_fares_total = urban_fares2['fare'].sum()
```


```python
# add values to new list

pie_chart1 = []
pie_chart1.append(rural_fares_total)
pie_chart1.append(suburban_fares_total)
pie_chart1.append(urban_fares_total)
```

** % Total Fares by City Type Pie Chart **


```python
# plot pie chart 1

labels = ["Rural", "Suburan", "Urban"]
colors = ["Gold", "lightskyblue", "lightcoral"]
explode = (0.05,0.05,0)
```


```python
plt.title("% Total Fares by City Type")
plt.pie(pie_chart1, 
        explode=explode, 
        labels=labels, 
        colors=colors,
        autopct="%1.1f%%", 
        shadow=True, 
        startangle=123,)
# plt.axis("equal")
plt.legend(loc=1)
plt.tight_layout()
plt.show()
```


![png](output_34_0.png)


** Percent Total Rides by City Type **


```python
rural_rides = x_rural['fare'].count()
```


```python
suburban_rides = x_suburban['fare'].count()
```


```python
urban_rides = x_urban['fare'].count()
```


```python
# add values to new list
pie_chart2 = []
pie_chart2.append(rural_rides)
pie_chart2.append(suburban_rides)
pie_chart2.append(urban_rides)
```

** % Total Rides by City Type Pie Chart **


```python
labels = ["Rural", "Suburan", "Urban"]
colors = ["Gold", "lightskyblue", "lightcoral"]
explode = (0.05,0.05,0)

```


```python
plt.title("% Total Rides by City Type")
plt.pie(pie_chart2, 
        explode=explode, 
        labels=labels, 
        colors=colors,
        autopct="%1.1f%%",
        shadow=True,
        startangle=90)
# plt.axis("equal")
plt.legend(loc=1)
plt.tight_layout()
plt.show()
```


![png](output_42_0.png)


**% of Total Drivers by City Type**



```python
rural_total = z_rural['driver_count'].sum()
```


```python
suburban_total = z_suburban['driver_count'].sum()
```


```python
urban_total = z_urban['driver_count'].sum()
```


```python
pie_chart3 =[]
pie_chart3.append(rural_total)
pie_chart3.append(suburban_total)
pie_chart3.append(urban_total)
```


```python
labels = ["Rural", "Suburan", "Urban"]
colors = ["Gold", "lightskyblue", "lightcoral"]
explode = (0.05,0.05,0)

```


```python
plt.title("% Total Drivers by City Type")
plt.pie(pie_chart3, 
        explode=explode, 
        labels=labels, 
        colors=colors,
        autopct="%1.1f%%",
        shadow=True,
        startangle=135)
# plt.axis("equal")
plt.legend(loc=1)
plt.tight_layout()
plt.show()
```


![png](output_49_0.png)



```python

```
