

```python
import pandas as pd
import numpy as np
```


```python
# read file
json_file = "purchase_data.json"

purchase_data_pd = pd.read_json(json_file)
purchase_data_pd.head()
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
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Check SN to see the value counts for each player
total_players = purchase_data_pd['SN'].value_counts()
total_players.head()
```




    Undirrala66    5
    Qarwen67       4
    Mindimnya67    4
    Sondastan54    4
    Saedue76       4
    Name: SN, dtype: int64




```python
# Identify duplicate 'SN'
purchase_data_pd.SN.duplicated().sum()
```




    207




```python
# Checks to see if there are duplicated rows
purchase_data_pd.duplicated().sum()
```




    3




```python
# These 3 rows are duplicates
purchase_data_pd.loc[purchase_data_pd.duplicated(keep='last'), :]
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
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>171</th>
      <td>21</td>
      <td>Male</td>
      <td>84</td>
      <td>Arcane Gem</td>
      <td>2.23</td>
      <td>Stryanastip77</td>
    </tr>
    <tr>
      <th>226</th>
      <td>25</td>
      <td>Female</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Chamistast30</td>
    </tr>
    <tr>
      <th>237</th>
      <td>7</td>
      <td>Male</td>
      <td>121</td>
      <td>Massacre</td>
      <td>3.42</td>
      <td>Lisistaya47</td>
    </tr>
  </tbody>
</table>
</div>




```python
# The duplciated rows appear later in the data set
purchase_data_pd.loc[purchase_data_pd.duplicated(), :]
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
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>292</th>
      <td>7</td>
      <td>Male</td>
      <td>121</td>
      <td>Massacre</td>
      <td>3.42</td>
      <td>Lisistaya47</td>
    </tr>
    <tr>
      <th>415</th>
      <td>25</td>
      <td>Female</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Chamistast30</td>
    </tr>
    <tr>
      <th>440</th>
      <td>21</td>
      <td>Male</td>
      <td>84</td>
      <td>Arcane Gem</td>
      <td>2.23</td>
      <td>Stryanastip77</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Duplicate rows 
purchase_data_pd.loc[purchase_data_pd.duplicated(keep=False), :]
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
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>171</th>
      <td>21</td>
      <td>Male</td>
      <td>84</td>
      <td>Arcane Gem</td>
      <td>2.23</td>
      <td>Stryanastip77</td>
    </tr>
    <tr>
      <th>226</th>
      <td>25</td>
      <td>Female</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Chamistast30</td>
    </tr>
    <tr>
      <th>237</th>
      <td>7</td>
      <td>Male</td>
      <td>121</td>
      <td>Massacre</td>
      <td>3.42</td>
      <td>Lisistaya47</td>
    </tr>
    <tr>
      <th>292</th>
      <td>7</td>
      <td>Male</td>
      <td>121</td>
      <td>Massacre</td>
      <td>3.42</td>
      <td>Lisistaya47</td>
    </tr>
    <tr>
      <th>415</th>
      <td>25</td>
      <td>Female</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Chamistast30</td>
    </tr>
    <tr>
      <th>440</th>
      <td>21</td>
      <td>Male</td>
      <td>84</td>
      <td>Arcane Gem</td>
      <td>2.23</td>
      <td>Stryanastip77</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Getting the shape of the original data set
purchase_data_pd.shape
```




    (780, 6)




```python
# Drop Duplicates - clean the data set to get rid of the duplicated rows
CLEAN_PURCHASE_DATA = purchase_data_pd.drop_duplicates(keep='first')
CLEAN_PURCHASE_DATA.shape
```




    (777, 6)




```python
CLEAN_PURCHASE_DATA.head()
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
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Use in Gender Demographics?

all_players = CLEAN_PURCHASE_DATA['SN'].count()
all_players
```




    777



***End of Cleaning Data***


```python
# Use set to sort out duplicates in total_players

total_players_list = CLEAN_PURCHASE_DATA['SN']
total_players_list = list(set(total_players_list))
len(total_players_list)

total_players_count = len(total_players_list)
print("Total Players = " + str(total_players_count))
```

    Total Players = 573


**Total Players Data Frame**


```python
# Create a Data Frame to display Total Players 

Player_Count_df = pd.DataFrame([{'Total Players' : total_players_count}])
Player_Count_df
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
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>573</td>
    </tr>
  </tbody>
</table>
</div>



**Purchasing Analysis (Total)**


```python
# Number of Unique Items
unique_items_counts = CLEAN_PURCHASE_DATA['Item Name'].value_counts()
unique_items_counts_df = pd.DataFrame(unique_items_counts)
unique_items_counts_df = unique_items_counts_df.rename(columns={"Item Name": "Item Count"})
unique_items_counts_df.head()
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
      <th>Item Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Final Critic</th>
      <td>13</td>
    </tr>
    <tr>
      <th>Betrayal, Whisper of Grieving Widows</th>
      <td>11</td>
    </tr>
    <tr>
      <th>Stormcaller</th>
      <td>10</td>
    </tr>
    <tr>
      <th>Arcane Gem</th>
      <td>10</td>
    </tr>
    <tr>
      <th>Trickster</th>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Calculate length of unique items 
Unique_Items_Length = unique_items_counts_df['Item Count'].count()
Unique_Items_Length
```




    179




```python
# Average Purchase Price
average_purchase_price = CLEAN_PURCHASE_DATA["Price"].mean()
print("Average Purchase Price = " + str(average_purchase_price))
```

    Average Purchase Price = 2.933487773487769



```python
# Total Number of Purchases
total_number_of_purchases = CLEAN_PURCHASE_DATA["Item Name"].count()
print("Total Number of Purhases = "+ str(total_number_of_purchases))
```

    Total Number of Purhases = 777



```python
# Total Revenue 
total_revenue = CLEAN_PURCHASE_DATA["Price"].sum()
total_revenue
```




    2279.3199999999965



**Purchasing Analysis Data Frame**


```python
# Create a df for Purchasing Analysis (Total)

Purchasing_Analysis_df = pd.DataFrame([{'Number of Unique Items': Unique_Items_Length,
                                       'Average Price': average_purchase_price,
                                       'Number of Purchases': total_number_of_purchases,
                                       'Total Revenue': total_revenue}])
Purchasing_Analysis_df = Purchasing_Analysis_df[['Number of Unique Items',
                                               'Average Price',
                                                 'Number of Purchases',
                                               'Total Revenue']]
Purchasing_Analysis_df = Purchasing_Analysis_df.round(2)
Purchasing_Analysis_df
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
      <th>Number of Unique Items</th>
      <th>Average Price</th>
      <th>Number of Purchases</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>179</td>
      <td>2.93</td>
      <td>777</td>
      <td>2279.32</td>
    </tr>
  </tbody>
</table>
</div>



**Gender Demographics**



```python
# Display SN & Gender Columns

SN_Gender_columns = CLEAN_PURCHASE_DATA[["SN", "Gender"]]
```


```python
# Create new Data Frame for SN and Gender
SN_Gender_df = pd.DataFrame(SN_Gender_columns)
SN_Gender_df.head()
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
      <th>SN</th>
      <th>Gender</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Aelalis34</td>
      <td>Male</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Eolo46</td>
      <td>Male</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Assastnya25</td>
      <td>Male</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Pheusrical25</td>
      <td>Male</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Aela59</td>
      <td>Male</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Slice out Duplicates in SN_Gender_df 
# to get true value count of gender
Updated_SN_Gender_df = SN_Gender_df.drop_duplicates(['SN'], keep='last')
Updated_SN_Gender_df.head()
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
      <th>SN</th>
      <th>Gender</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>Eolo46</td>
      <td>Male</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Pheusrical25</td>
      <td>Male</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Aela59</td>
      <td>Male</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Tanimnya91</td>
      <td>Male</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Undjaskla97</td>
      <td>Male</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Test to see how many rows of 'SN' are left
Updated_SN_Gender_df.shape
```




    (573, 2)




```python
# Gender Value Count
gender_value_count = Updated_SN_Gender_df["Gender"].value_counts()
gender_value_count
```




    Male                     465
    Female                   100
    Other / Non-Disclosed      8
    Name: Gender, dtype: int64




```python
# Total Gender Count

total_gender_count = Updated_SN_Gender_df["Gender"].count()
print("Total Gender Count = " + str(total_gender_count))
```

    Total Gender Count = 573



```python
# Percentage and Count of Male Players

male_count = Updated_SN_Gender_df["Gender"].value_counts()['Male']
print("Male Count = " + str(male_count))

male_count_percentage = male_count / total_gender_count * 100
print("Male Percentage Count = " + str(male_count_percentage))
```

    Male Count = 465
    Male Percentage Count = 81.1518324607



```python
# Percentage and Count of Female Players

female_count = Updated_SN_Gender_df["Gender"].value_counts()['Female']
print("Female Count = " + str(female_count))

female_count_percentage = female_count / total_gender_count * 100
print("Female Percentage Count = " + str(female_count_percentage))
```

    Female Count = 100
    Female Percentage Count = 17.4520069808



```python
# Percentage and Count of Other / Non-Disclosed

non_disclosed_gender_count = total_gender_count - (male_count + female_count)
print("Other / Non Disclosed Gender = " + str(non_disclosed_gender_count))

non_disclosed_gender_percentage = non_disclosed_gender_count / total_gender_count * 100
print("Non Disclosed Percentage Count = " + str(non_disclosed_gender_percentage))
```

    Other / Non Disclosed Gender = 8
    Non Disclosed Percentage Count = 1.39616055846


**Gender Demographics Data Frame**


```python
# Create Gender Demographics Data Frame
# Rows = Male, Female, Other / Non Disclosed
# Columns = Percentage of Players, Total Count

Gender_Demographics_df = pd.DataFrame({'Percentage of Players':[male_count_percentage,female_count_percentage,non_disclosed_gender_count],
                                      'Total Count': [male_count, female_count,non_disclosed_gender_count]},
                                     index = ['Male', 'Female', 'Other / Non Disclosed'])

Gender_Demographics_df = Gender_Demographics_df.round(2)
Gender_Demographics_df
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
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>81.15</td>
      <td>465</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>17.45</td>
      <td>100</td>
    </tr>
    <tr>
      <th>Other / Non Disclosed</th>
      <td>8.00</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>



**Purchasing Analysis (Gender)** 



```python
# Purchase Count Male - using Clean Data Frame since some players
# bought multiple items

purchase_count_male = CLEAN_PURCHASE_DATA["Gender"].value_counts()["Male"]
```


```python
# Create new DF and drop Female and Other / Non-Disclosed

Gender_purchase_pd = CLEAN_PURCHASE_DATA[["Gender","Price"]]
```


```python
# Filter out female and update Gender_purchase_pd
Updated_Male_purchase_df = Gender_purchase_pd.query("Gender != 'Female'")
```


```python
# Filter out Other / Non-Disclosed from Updated_Male_purchase_df

Updated_Male_purchase_df2 = Updated_Male_purchase_df.query("Gender != 'Other / Non-Disclosed'")
```


```python
# Average Purchase Price Male
Average_Purchase_Price_Male = Updated_Male_purchase_df2['Price'].mean()
```


```python
# Total Purchase Value Male
Total_Purchase_Value_Male = Updated_Male_purchase_df2['Price'].sum()
```


```python
# Totals Male

print ("Purchase Count Male = " + str(purchase_count_male))
print("Average Purchase Price Male = " + str(Average_Purchase_Price_Male))
print("Total Purchase Value Male = " + str(Total_Purchase_Value_Male))
```

    Purchase Count Male = 631
    Average Purchase Price Male = 2.9509191759112494
    Total Purchase Value Male = 1862.0299999999984


**Female Purchase Analysis**


```python
purchase_count_female = CLEAN_PURCHASE_DATA["Gender"].value_counts()["Female"]
```


```python
# Filter out male and update female_purchase_pd
Updated_Female_purchase_df = Gender_purchase_pd.query("Gender != 'Male'")
```


```python
# Filter out Other / Non-Disclosed from Updated_Female_purchase_df
Updated_Female_purchase_df2 = Updated_Female_purchase_df.query("Gender != 'Other / Non-Disclosed'")
Updated_Female_purchase_df2.head()
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
      <th>Gender</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>7</th>
      <td>Female</td>
      <td>3.32</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Female</td>
      <td>1.14</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Female</td>
      <td>1.65</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Female</td>
      <td>2.52</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Female</td>
      <td>2.46</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Average Purchase Price female
Average_Purchase_Price_Female = Updated_Female_purchase_df2['Price'].mean()
```


```python
# Total Purchase Value female
Total_Purchase_Value_Female = Updated_Female_purchase_df2['Price'].sum()
```


```python
# Totals Female
print ("Purchase Count Female = " + str(purchase_count_female))
print("Average Purchase Price Female = " + str(Average_Purchase_Price_Female))
print("Total Purchase Value Female = " + str(Total_Purchase_Value_Female))
```

    Purchase Count Female = 135
    Average Purchase Price Female = 2.826296296296295
    Total Purchase Value Female = 381.54999999999984


**Other / Non-Disclosed Purchase Analysis**


```python
# Purchase Count Other / Non-Disclosed - Use orginal Data Frame since some players
# bought multiple items

purchase_count_other = CLEAN_PURCHASE_DATA["Gender"].value_counts()["Other / Non-Disclosed"]
```


```python
# Filter out male and update purchase_count_other_pd
Updated_Other_purchase_df = Gender_purchase_pd.query("Gender != 'Male'")
```


```python
# Filter out Female from Updated_Other_purchase_df
Updated_Other_purchase_df2 = Updated_Other_purchase_df.query("Gender != 'Female'")
Updated_Other_purchase_df2.head()
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
      <th>Gender</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>177</th>
      <td>Other / Non-Disclosed</td>
      <td>3.73</td>
    </tr>
    <tr>
      <th>209</th>
      <td>Other / Non-Disclosed</td>
      <td>2.21</td>
    </tr>
    <tr>
      <th>244</th>
      <td>Other / Non-Disclosed</td>
      <td>2.36</td>
    </tr>
    <tr>
      <th>267</th>
      <td>Other / Non-Disclosed</td>
      <td>1.96</td>
    </tr>
    <tr>
      <th>276</th>
      <td>Other / Non-Disclosed</td>
      <td>4.00</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Average Purchase Price Other 
Average_Purchase_Price_Other = Updated_Other_purchase_df2['Price'].mean()
```


```python
# Total Purchase Value Other
Total_Purchase_Value_Other = Updated_Other_purchase_df2['Price'].sum()
```


```python
# Totals Other
print ("Purchase Count Other / Non-Disclosed = " + str(purchase_count_other))
print("Average Purchase Price Other / Non-Disclosed = " + str(Average_Purchase_Price_Other))
print("Total Purchase Value Other / Non-Disclosed = " + str(Total_Purchase_Value_Other))
```

    Purchase Count Other / Non-Disclosed = 11
    Average Purchase Price Other / Non-Disclosed = 3.2490909090909086
    Total Purchase Value Other / Non-Disclosed = 35.739999999999995



```python
# Normalized Totals

Male_Norm = Total_Purchase_Value_Male / purchase_count_male 

Female_Norm = Total_Purchase_Value_Female / purchase_count_female

Other_Norm = Total_Purchase_Value_Other / purchase_count_other
```

**Purchasing Analysis (Gender) Data Frame**


```python
# Create Purchasing Analys (Gender) Data Frame

Purchase_Analysis_df = pd.DataFrame({'Purchase Count': [purchase_count_male, purchase_count_female, purchase_count_other],
                                    'Average Purchase Price': [Average_Purchase_Price_Male, Average_Purchase_Price_Female, Average_Purchase_Price_Other],
                                    'Total Purchase Value': [Total_Purchase_Value_Male, Total_Purchase_Value_Female, Total_Purchase_Value_Other],
                                    'Normalized Totals': [Male_Norm, Female_Norm, Other_Norm]}, columns = ['Purchase Count', 'Average Purchase Price', 'Total Purchase Value','Normalized Totals'],
                                   index = ['Male', 'Female', 'Other / Non Disclosed'])
Purchase_Analysis_df = Purchase_Analysis_df.round(2)
Purchase_Analysis_df
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
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>631</td>
      <td>2.95</td>
      <td>1862.03</td>
      <td>2.95</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>135</td>
      <td>2.83</td>
      <td>381.55</td>
      <td>2.83</td>
    </tr>
    <tr>
      <th>Other / Non Disclosed</th>
      <td>11</td>
      <td>3.25</td>
      <td>35.74</td>
      <td>3.25</td>
    </tr>
  </tbody>
</table>
</div>



**Age Demographics**

* Below each are broken into bins of 4 years (i.e. &lt;10, 10-14, 15-19, etc.) 
  * Purchase Count
  * Average Purchase Price
  * Total Purchase Value
  * Normalized Totals


```python
# Sort Data Frame into Age Demographics 

Age_Demographics_df = CLEAN_PURCHASE_DATA.loc[:,["Age", "Item Name", "Price"]]
Age_Demographics_df.head()
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
      <th>Age</th>
      <th>Item Name</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Final Critic</td>
      <td>1.36</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Create Age Bins
# 0 - 10, 10 - 14, 15 - 19, 20 - 24, 25 - 29, 30 - 34, 35 - 39, 40+
bins = [0, 10, 14, 19, 24, 29, 34, 39, 50]

Age_Bin_Groups = ['Child', 'Pre Teen', 'Teen', "Early 20's", "Late 20's", "Early 30's", "Late 30's", "40+"]
```


```python
CLEAN_PURCHASE_DATA['Age_Group'] = pd.cut(CLEAN_PURCHASE_DATA['Age'], bins, labels=Age_Bin_Groups)
CLEAN_PURCHASE_DATA.head()
```

    /Users/andy_felicitas/anaconda/lib/python3.6/site-packages/ipykernel_launcher.py:1: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
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
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
      <th>Age_Group</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
      <td>Late 30's</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
      <td>Early 20's</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
      <td>Early 30's</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
      <td>Early 20's</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
      <td>Early 20's</td>
    </tr>
  </tbody>
</table>
</div>




```python
Age_Group_Count = CLEAN_PURCHASE_DATA["Age_Group"].value_counts()
Age_Group_Count
```




    Early 20's    335
    Teen          133
    Late 20's     124
    Early 30's     64
    Late 30's      42
    Pre Teen       31
    Child          31
    40+            17
    Name: Age_Group, dtype: int64




```python
# Purchase_Count_Child 
Purchase_Count_Child = CLEAN_PURCHASE_DATA["Age_Group"].value_counts()["Child"]
Child_Percentage_of_Total = Purchase_Count_Child / all_players * 100 # changed to all_players (777) instead of total (573)
print('Child = ' + str(Purchase_Count_Child))
print('Child % = ' + str(Child_Percentage_of_Total))
```

    Child = 31
    Child % = 3.9897039897



```python
# Purchase_Count_Pre_Teen
Purchase_Count_Pre_Teen = CLEAN_PURCHASE_DATA["Age_Group"].value_counts()["Pre Teen"]
Pre_Teen_Percentage_of_Total = Purchase_Count_Pre_Teen / all_players * 100
print('Pre Teen = ' + str(Purchase_Count_Pre_Teen))
print('Teen % = ' + str(Pre_Teen_Percentage_of_Total))
```

    Pre Teen = 31
    Teen % = 3.9897039897



```python
# Purchase_Count_Teen
Purchase_Count_Teen = CLEAN_PURCHASE_DATA["Age_Group"].value_counts()["Teen"]
Teen_Percentage_of_Total = Purchase_Count_Teen / all_players * 100
print('Teen = ' + str(Purchase_Count_Teen))
print('Teen % = ' + str(Teen_Percentage_of_Total))
```

    Teen = 133
    Teen % = 17.1171171171



```python
# Purchase_Count_Early20s
Purchase_Count_Early20s = CLEAN_PURCHASE_DATA["Age_Group"].value_counts()["Early 20's"]
Early20s_Percentage_of_Total = Purchase_Count_Early20s / all_players * 100
print("Early 20's = " + str(Purchase_Count_Early20s))
print("Early 20'% s = " + str(Early20s_Percentage_of_Total))
```

    Early 20's = 335
    Early 20'% s = 43.1145431145



```python
# Purchase_Count_Late20s
Purchase_Count_Late20s = CLEAN_PURCHASE_DATA["Age_Group"].value_counts()["Late 20's"]
Late20s_Percentage_of_Total = Purchase_Count_Late20s / all_players * 100
print("Late 20's = " + str(Purchase_Count_Late20s))
print("Late 20's % = " + str(Late20s_Percentage_of_Total))

```

    Late 20's = 124
    Late 20's % = 15.9588159588



```python
# Purchase_Count_Early30s
Purchase_Count_Early30s = CLEAN_PURCHASE_DATA["Age_Group"].value_counts()["Early 30's"]
Early30s_Percentage_of_Total = Purchase_Count_Early30s / all_players * 100
print("Early 30's = " + str(Purchase_Count_Early30s))
print("Early 30's % = " + str(Early30s_Percentage_of_Total))
```

    Early 30's = 64
    Early 30's % = 8.23680823681



```python
# Purchase_Count_Late30s
Purchase_Count_Late30s = CLEAN_PURCHASE_DATA["Age_Group"].value_counts()["Late 30's"]
Late30s_Percentage_of_Total = Purchase_Count_Late30s / all_players * 100
print("Late 30's = " + str(Purchase_Count_Late30s))
print("Late 30's % = " + str(Late30s_Percentage_of_Total))
```

    Late 30's = 42
    Late 30's % = 5.40540540541



```python
# Purchase_Count_40
Purchase_Count_40 = CLEAN_PURCHASE_DATA["Age_Group"].value_counts()["40+"]
Forties_Percentage_of_Total = Purchase_Count_40 / all_players * 100
print("40's = " + str(Purchase_Count_40))
print("40's % = " + str(Forties_Percentage_of_Total))

```

    40's = 17
    40's % = 2.1879021879


***Avg Purchase Price by Age Group***


```python
# Avg_Price_Child

Avg_Price_Child_df = CLEAN_PURCHASE_DATA[CLEAN_PURCHASE_DATA.Age_Group == 'Child']
Avg_Price_Child_df.head()
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
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
      <th>Age_Group</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>70</th>
      <td>7</td>
      <td>Female</td>
      <td>158</td>
      <td>Darkheart, Butcher of the Champion</td>
      <td>3.56</td>
      <td>Eosurdru76</td>
      <td>Child</td>
    </tr>
    <tr>
      <th>121</th>
      <td>7</td>
      <td>Male</td>
      <td>175</td>
      <td>Woeful Adamantite Claymore</td>
      <td>1.24</td>
      <td>Lassjask63</td>
      <td>Child</td>
    </tr>
    <tr>
      <th>125</th>
      <td>7</td>
      <td>Female</td>
      <td>10</td>
      <td>Sleepwalker</td>
      <td>1.73</td>
      <td>Heosurnuru52</td>
      <td>Child</td>
    </tr>
    <tr>
      <th>170</th>
      <td>9</td>
      <td>Male</td>
      <td>71</td>
      <td>Demise</td>
      <td>4.07</td>
      <td>Reulae52</td>
      <td>Child</td>
    </tr>
    <tr>
      <th>237</th>
      <td>7</td>
      <td>Male</td>
      <td>121</td>
      <td>Massacre</td>
      <td>3.42</td>
      <td>Lisistaya47</td>
      <td>Child</td>
    </tr>
  </tbody>
</table>
</div>




```python
Avg_Price_Child = Avg_Price_Child_df['Price'].mean()
print("Average Price Child = " + str(Avg_Price_Child))
```

    Average Price Child = 3.0064516129032253



```python
# Avg_Price_Pre_Teen

Avg_Price_PreTeen_df =CLEAN_PURCHASE_DATA[CLEAN_PURCHASE_DATA.Age_Group == 'Pre Teen']
Avg_Price_PreTeen_df.head()
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
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
      <th>Age_Group</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>22</th>
      <td>11</td>
      <td>Female</td>
      <td>11</td>
      <td>Brimstone</td>
      <td>2.52</td>
      <td>Deural48</td>
      <td>Pre Teen</td>
    </tr>
    <tr>
      <th>24</th>
      <td>11</td>
      <td>Male</td>
      <td>65</td>
      <td>Conqueror Adamantite Mace</td>
      <td>1.96</td>
      <td>Qarwen67</td>
      <td>Pre Teen</td>
    </tr>
    <tr>
      <th>46</th>
      <td>11</td>
      <td>Male</td>
      <td>17</td>
      <td>Lazarus, Terror of the Earth</td>
      <td>3.47</td>
      <td>Palatyon26</td>
      <td>Pre Teen</td>
    </tr>
    <tr>
      <th>68</th>
      <td>11</td>
      <td>Male</td>
      <td>38</td>
      <td>The Void, Vengeance of Dark Magic</td>
      <td>2.82</td>
      <td>Qarwen67</td>
      <td>Pre Teen</td>
    </tr>
    <tr>
      <th>117</th>
      <td>11</td>
      <td>Male</td>
      <td>160</td>
      <td>Azurewrath</td>
      <td>2.22</td>
      <td>Qarwen67</td>
      <td>Pre Teen</td>
    </tr>
  </tbody>
</table>
</div>




```python
Avg_Price_PreTeen = Avg_Price_PreTeen_df['Price'].mean()
print("Average Price Pre Teen = " + str(Avg_Price_PreTeen))
```

    Average Price Pre Teen = 2.7029032258064514



```python
# Avg_Price_Teen

Avg_Price_Teen_df = CLEAN_PURCHASE_DATA[CLEAN_PURCHASE_DATA.Age_Group == 'Teen']
Avg_Price_Teen_df.head()
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
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
      <th>Age_Group</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>21</th>
      <td>15</td>
      <td>Male</td>
      <td>3</td>
      <td>Phantomlight</td>
      <td>1.79</td>
      <td>Iaralrgue74</td>
      <td>Teen</td>
    </tr>
    <tr>
      <th>23</th>
      <td>19</td>
      <td>Male</td>
      <td>183</td>
      <td>Dragon's Greatsword</td>
      <td>2.36</td>
      <td>Chanosia65</td>
      <td>Teen</td>
    </tr>
    <tr>
      <th>28</th>
      <td>15</td>
      <td>Male</td>
      <td>49</td>
      <td>The Oculus, Token of Lost Worlds</td>
      <td>4.23</td>
      <td>Ilariarin45</td>
      <td>Teen</td>
    </tr>
    <tr>
      <th>29</th>
      <td>16</td>
      <td>Female</td>
      <td>45</td>
      <td>Glinting Glass Edge</td>
      <td>2.46</td>
      <td>Phaedai25</td>
      <td>Teen</td>
    </tr>
    <tr>
      <th>31</th>
      <td>18</td>
      <td>Male</td>
      <td>37</td>
      <td>Shadow Strike, Glory of Ending Hope</td>
      <td>1.93</td>
      <td>Iarilis73</td>
      <td>Teen</td>
    </tr>
  </tbody>
</table>
</div>




```python
Avg_Price_Teen = Avg_Price_Teen_df['Price'].mean()
print("Average Price Teen = " + str(Avg_Price_Teen))
```

    Average Price Teen = 2.905413533834586



```python
# Avg_Early20s

Avg_Price_Early20s_df = CLEAN_PURCHASE_DATA[CLEAN_PURCHASE_DATA.Age_Group == "Early 20's"]
Avg_Price_Early20s_df.head()
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
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
      <th>Age_Group</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
      <td>Early 20's</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
      <td>Early 20's</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
      <td>Early 20's</td>
    </tr>
    <tr>
      <th>5</th>
      <td>20</td>
      <td>Male</td>
      <td>10</td>
      <td>Sleepwalker</td>
      <td>1.73</td>
      <td>Tanimnya91</td>
      <td>Early 20's</td>
    </tr>
    <tr>
      <th>6</th>
      <td>20</td>
      <td>Male</td>
      <td>153</td>
      <td>Mercenary Sabre</td>
      <td>4.57</td>
      <td>Undjaskla97</td>
      <td>Early 20's</td>
    </tr>
  </tbody>
</table>
</div>




```python
Avg_Price_Early20s = Avg_Price_Early20s_df['Price'].mean()
print("Average Price Early 20's = " + str(Avg_Price_Early20s))
```

    Average Price Early 20's = 2.9150447761194034



```python
Avg_Price_Late20s_df = CLEAN_PURCHASE_DATA[CLEAN_PURCHASE_DATA.Age_Group == "Late 20's"]
Avg_Price_Late20s_df.head()
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
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
      <th>Age_Group</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>7</th>
      <td>29</td>
      <td>Female</td>
      <td>169</td>
      <td>Interrogator, Blood Blade of the Queen</td>
      <td>3.32</td>
      <td>Iathenudil29</td>
      <td>Late 20's</td>
    </tr>
    <tr>
      <th>8</th>
      <td>25</td>
      <td>Male</td>
      <td>118</td>
      <td>Ghost Reaver, Longsword of Magic</td>
      <td>2.77</td>
      <td>Sondenasta63</td>
      <td>Late 20's</td>
    </tr>
    <tr>
      <th>18</th>
      <td>28</td>
      <td>Male</td>
      <td>91</td>
      <td>Celeste</td>
      <td>3.71</td>
      <td>Iskista88</td>
      <td>Late 20's</td>
    </tr>
    <tr>
      <th>26</th>
      <td>29</td>
      <td>Male</td>
      <td>132</td>
      <td>Persuasion</td>
      <td>3.90</td>
      <td>Aerithllora36</td>
      <td>Late 20's</td>
    </tr>
    <tr>
      <th>54</th>
      <td>25</td>
      <td>Female</td>
      <td>101</td>
      <td>Final Critic</td>
      <td>4.62</td>
      <td>Minduli80</td>
      <td>Late 20's</td>
    </tr>
  </tbody>
</table>
</div>




```python
Avg_Price_Late20s = Avg_Price_Late20s_df['Price'].mean()
print("Average Price Late 20's = " + str(Avg_Price_Late20s))
```

    Average Price Late 20's = 2.975564516129032



```python
# Avg_Early 30's Early 30's

Avg_Price_Early30s_df = CLEAN_PURCHASE_DATA[CLEAN_PURCHASE_DATA.Age_Group == "Early 30's"]
Avg_Price_Early30s_df.head()
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
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
      <th>Age_Group</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
      <td>Early 30's</td>
    </tr>
    <tr>
      <th>9</th>
      <td>31</td>
      <td>Male</td>
      <td>99</td>
      <td>Expiration, Warscythe Of Lost Worlds</td>
      <td>4.53</td>
      <td>Hilaerin92</td>
      <td>Early 30's</td>
    </tr>
    <tr>
      <th>12</th>
      <td>30</td>
      <td>Male</td>
      <td>81</td>
      <td>Dreamkiss</td>
      <td>4.06</td>
      <td>Iskossa88</td>
      <td>Early 30's</td>
    </tr>
    <tr>
      <th>19</th>
      <td>31</td>
      <td>Male</td>
      <td>177</td>
      <td>Winterthorn, Defender of Shifting Worlds</td>
      <td>4.89</td>
      <td>Assossa43</td>
      <td>Early 30's</td>
    </tr>
    <tr>
      <th>27</th>
      <td>34</td>
      <td>Male</td>
      <td>106</td>
      <td>Crying Steel Sickle</td>
      <td>2.29</td>
      <td>Assastnya25</td>
      <td>Early 30's</td>
    </tr>
  </tbody>
</table>
</div>




```python
Avg_Price_Early30s = Avg_Price_Early30s_df['Price'].mean()
print("Average Price Early 30's = " + str(Avg_Price_Early30s))
```

    Average Price Early 30's = 3.082031249999999



```python
Avg_Price_Late30s_df = CLEAN_PURCHASE_DATA[CLEAN_PURCHASE_DATA.Age_Group == "Late 30's"]
Avg_Price_Late30s_df.head()
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
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
      <th>Age_Group</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
      <td>Late 30's</td>
    </tr>
    <tr>
      <th>81</th>
      <td>38</td>
      <td>Male</td>
      <td>175</td>
      <td>Woeful Adamantite Claymore</td>
      <td>1.24</td>
      <td>Yaristi64</td>
      <td>Late 30's</td>
    </tr>
    <tr>
      <th>106</th>
      <td>37</td>
      <td>Female</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Chadossa56</td>
      <td>Late 30's</td>
    </tr>
    <tr>
      <th>175</th>
      <td>35</td>
      <td>Male</td>
      <td>34</td>
      <td>Retribution Axe</td>
      <td>4.14</td>
      <td>Raillydeu47</td>
      <td>Late 30's</td>
    </tr>
    <tr>
      <th>189</th>
      <td>35</td>
      <td>Male</td>
      <td>179</td>
      <td>Wolf, Promise of the Moonwalker</td>
      <td>1.88</td>
      <td>Raillydeu47</td>
      <td>Late 30's</td>
    </tr>
  </tbody>
</table>
</div>




```python
Avg_Price_Late30s = Avg_Price_Late30s_df['Price'].mean()
print("Average Price Late 30's = " + str(Avg_Price_Late30s))
```

    Average Price Late 30's = 2.842857142857143



```python
# Avg_40s 

Avg_Price_40s_df = CLEAN_PURCHASE_DATA[CLEAN_PURCHASE_DATA.Age_Group == "40+"]
Avg_Price_40s_df.head()
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
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
      <th>Age_Group</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>14</th>
      <td>40</td>
      <td>Male</td>
      <td>44</td>
      <td>Bonecarvin Battle Axe</td>
      <td>2.46</td>
      <td>Sundast29</td>
      <td>40+</td>
    </tr>
    <tr>
      <th>179</th>
      <td>40</td>
      <td>Male</td>
      <td>70</td>
      <td>Hope's End</td>
      <td>3.89</td>
      <td>Chanosiaya39</td>
      <td>40+</td>
    </tr>
    <tr>
      <th>186</th>
      <td>40</td>
      <td>Male</td>
      <td>144</td>
      <td>Blood Infused Guardian</td>
      <td>2.86</td>
      <td>Chanosiaya39</td>
      <td>40+</td>
    </tr>
    <tr>
      <th>212</th>
      <td>40</td>
      <td>Male</td>
      <td>111</td>
      <td>Misery's End</td>
      <td>2.91</td>
      <td>Yarmol79</td>
      <td>40+</td>
    </tr>
    <tr>
      <th>238</th>
      <td>40</td>
      <td>Female</td>
      <td>49</td>
      <td>The Oculus, Token of Lost Worlds</td>
      <td>4.23</td>
      <td>Chamadar27</td>
      <td>40+</td>
    </tr>
  </tbody>
</table>
</div>




```python
Avg_Price_40s = Avg_Price_40s_df['Price'].mean()
print("Average Price 40's = " + str(Avg_Price_40s))
```

    Average Price 40's = 3.161764705882353


***Age Demographics Data Frame***


```python
# Create Age Demographics Data Frame

Age_Demo_df = pd.DataFrame({'Percentage of Players': [Child_Percentage_of_Total, Pre_Teen_Percentage_of_Total,
                                                      Teen_Percentage_of_Total, Early20s_Percentage_of_Total,
                                                     Late20s_Percentage_of_Total, Early30s_Percentage_of_Total,
                                                     Late30s_Percentage_of_Total, Forties_Percentage_of_Total],
                                    'Total Count': [Purchase_Count_Child, Purchase_Count_Pre_Teen, Purchase_Count_Teen,
                                                    Purchase_Count_Early20s, Purchase_Count_Late20s, Purchase_Count_Early30s,
                                                    Purchase_Count_Late30s,Purchase_Count_40]},
                                    columns = ['Percentage of Players', 'Total Count'],
                                   index = ['Child', 'Pre Teen', 'Teen', "Early 20's", "Late 20's", "Early 30's", "Late 30's", "40+"])
Age_Demo_df = Age_Demo_df.round(2)
Age_Demo_df 
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
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Child</th>
      <td>3.99</td>
      <td>31</td>
    </tr>
    <tr>
      <th>Pre Teen</th>
      <td>3.99</td>
      <td>31</td>
    </tr>
    <tr>
      <th>Teen</th>
      <td>17.12</td>
      <td>133</td>
    </tr>
    <tr>
      <th>Early 20's</th>
      <td>43.11</td>
      <td>335</td>
    </tr>
    <tr>
      <th>Late 20's</th>
      <td>15.96</td>
      <td>124</td>
    </tr>
    <tr>
      <th>Early 30's</th>
      <td>8.24</td>
      <td>64</td>
    </tr>
    <tr>
      <th>Late 30's</th>
      <td>5.41</td>
      <td>42</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>2.19</td>
      <td>17</td>
    </tr>
  </tbody>
</table>
</div>



***Total Purchase Value***


```python
# Total Purchase Value Child

Total_Purchase_Value_Child = Avg_Price_Child_df['Price'].sum()
print("Total Purchase Value Child = " + str(Total_Purchase_Value_Child))
```

    Total Purchase Value Child = 93.19999999999999



```python
# Total Purchase Value Pre Teen
Total_Purchase_Value_PreTeen = Avg_Price_PreTeen_df['Price'].sum()
print("Total Purchase Value Pre Teen = " + str(Total_Purchase_Value_PreTeen))
```

    Total Purchase Value Pre Teen = 83.78999999999999



```python
# Total Purchase Value Teen
Total_Purchase_Value_Teen = Avg_Price_Teen_df['Price'].sum()
print("Total Purchase Teen = " + str(Total_Purchase_Value_Teen))
```

    Total Purchase Teen = 386.41999999999996



```python
# Total Purchase Value Early 20's
Total_Purchase_Value_Early20s = Avg_Price_Early20s_df['Price'].sum()
print("Total Purchase Value Early 20's = " + str(Total_Purchase_Value_Early20s))
```

    Total Purchase Value Early 20's = 976.5400000000001



```python
# Total Purchase Avg_Price_Late20s

Total_Purchase_Value_Late20s = Avg_Price_Late20s_df['Price'].sum()
print("Total Purchase Value Late 20s = " + str(Total_Purchase_Value_Late20s))
```

    Total Purchase Value Late 20s = 368.96999999999997



```python
# Total Purchase Avg Early 30s
Total_Purchase_Value_Early30s = Avg_Price_Early30s_df['Price'].sum()
print("Total Purchase Value Early 30s = " + str(Total_Purchase_Value_Early30s))
```

    Total Purchase Value Early 30s = 197.24999999999994



```python
# Total Purchase Ave Late 30s
Total_Purchase_Value_Late30s = Avg_Price_Late30s_df['Price'].sum()
print("Total Purchase Value Late 30s = " + str(Total_Purchase_Value_Late30s))
```

    Total Purchase Value Late 30s = 119.4



```python
# Total Purchase Ave 40+

Total_Purchase_Value_40s = Avg_Price_40s_df['Price'].sum()
print("Total Purchase Value 40s = " + str(Total_Purchase_Value_40s))
```

    Total Purchase Value 40s = 53.75


**Purchasing Analysis Age**



```python
Purchase_Analysis_df = pd.DataFrame({'Purchase Count': [Purchase_Count_Child, Purchase_Count_Pre_Teen, Purchase_Count_Teen,
                                                    Purchase_Count_Early20s, Purchase_Count_Late20s, Purchase_Count_Early30s,
                                                    Purchase_Count_Late30s, Purchase_Count_40],
                                    'Average Purchase Price': [Avg_Price_Child, Avg_Price_PreTeen, Avg_Price_Teen, Avg_Price_Early20s, Avg_Price_Late20s, 
                                                               Avg_Price_Early30s, Avg_Price_Late30s, Avg_Price_40s],
                                    'Total Purchase Value': [Total_Purchase_Value_Child, Total_Purchase_Value_PreTeen, Total_Purchase_Value_Teen, 
                                                             Total_Purchase_Value_Early20s, Total_Purchase_Value_Late20s, Total_Purchase_Value_Early30s, 
                                                             Total_Purchase_Value_Late30s, Total_Purchase_Value_40s]},
                                    columns = ['Purchase Count', 'Average Purchase Price', 'Total Purchase Value'],
                                   index = ['Child', 'Pre Teen', 'Teen', "Early 20's", "Late 20's", "Early 30's", "Late 30's", "40+"])
Purchase_Analysis_df = Purchase_Analysis_df.round(2)
Purchase_Analysis_df
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
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Child</th>
      <td>31</td>
      <td>3.01</td>
      <td>93.20</td>
    </tr>
    <tr>
      <th>Pre Teen</th>
      <td>31</td>
      <td>2.70</td>
      <td>83.79</td>
    </tr>
    <tr>
      <th>Teen</th>
      <td>133</td>
      <td>2.91</td>
      <td>386.42</td>
    </tr>
    <tr>
      <th>Early 20's</th>
      <td>335</td>
      <td>2.92</td>
      <td>976.54</td>
    </tr>
    <tr>
      <th>Late 20's</th>
      <td>124</td>
      <td>2.98</td>
      <td>368.97</td>
    </tr>
    <tr>
      <th>Early 30's</th>
      <td>64</td>
      <td>3.08</td>
      <td>197.25</td>
    </tr>
    <tr>
      <th>Late 30's</th>
      <td>42</td>
      <td>2.84</td>
      <td>119.40</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>17</td>
      <td>3.16</td>
      <td>53.75</td>
    </tr>
  </tbody>
</table>
</div>



**Top Spenders**

* Identify the the top 5 spenders in the game by total purchase value, then list (in a table):
  * SN
  * Purchase Count
  * Average Purchase Price
  * Total Purchase Value


```python
# Create groupby for 'SN' and 'Price' to find top 5

Top_5_Spenders= pd.DataFrame(CLEAN_PURCHASE_DATA.groupby('SN')['Price'].sum())
Top_5_Spenders.reset_index(inplace=True)
Top_5_Spenders = Top_5_Spenders.sort_values(['Price'],ascending=False)
Top_5_Spenders.head()
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
      <th>SN</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>538</th>
      <td>Undirrala66</td>
      <td>17.06</td>
    </tr>
    <tr>
      <th>428</th>
      <td>Saedue76</td>
      <td>13.56</td>
    </tr>
    <tr>
      <th>354</th>
      <td>Mindimnya67</td>
      <td>12.74</td>
    </tr>
    <tr>
      <th>181</th>
      <td>Haellysu29</td>
      <td>12.73</td>
    </tr>
    <tr>
      <th>120</th>
      <td>Eoda93</td>
      <td>11.58</td>
    </tr>
  </tbody>
</table>
</div>



***Top 5 Count***


```python
# Find Count of 'Price' on 'SN'

Top_5_Count = pd.DataFrame(CLEAN_PURCHASE_DATA.groupby('SN')['Price'].count())
Top_5_Count.reset_index(inplace=True)
Top_5_Count = Top_5_Count.sort_values(['Price'],ascending=False)
Top_5_Count.head()
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
      <th>SN</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>538</th>
      <td>Undirrala66</td>
      <td>5</td>
    </tr>
    <tr>
      <th>184</th>
      <td>Hailaphos89</td>
      <td>4</td>
    </tr>
    <tr>
      <th>385</th>
      <td>Qarwen67</td>
      <td>4</td>
    </tr>
    <tr>
      <th>354</th>
      <td>Mindimnya67</td>
      <td>4</td>
    </tr>
    <tr>
      <th>467</th>
      <td>Sondastan54</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>



***Top 5 Avg Price***


```python
# Find Avg 'Price' on 'SN'

Top_5_Avg = pd.DataFrame(CLEAN_PURCHASE_DATA.groupby('SN')['Price'].mean())
Top_5_Avg.reset_index(inplace=True)
Top_5_Avg = Top_5_Avg.sort_values(['Price'], ascending=False)
Top_5_Avg.head()
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
      <th>SN</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>388</th>
      <td>Qiluard68</td>
      <td>4.95</td>
    </tr>
    <tr>
      <th>517</th>
      <td>Tyarithn67</td>
      <td>4.95</td>
    </tr>
    <tr>
      <th>364</th>
      <td>Palurrian69</td>
      <td>4.95</td>
    </tr>
    <tr>
      <th>168</th>
      <td>Frichaststa61</td>
      <td>4.95</td>
    </tr>
    <tr>
      <th>67</th>
      <td>Assossa43</td>
      <td>4.89</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Merge tables

Top_5_Merge = pd.merge(Top_5_Spenders, Top_5_Count, on = 'SN')
Top_5_Merge.head()
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
      <th>SN</th>
      <th>Price_x</th>
      <th>Price_y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Undirrala66</td>
      <td>17.06</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Saedue76</td>
      <td>13.56</td>
      <td>4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Mindimnya67</td>
      <td>12.74</td>
      <td>4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Haellysu29</td>
      <td>12.73</td>
      <td>3</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Eoda93</td>
      <td>11.58</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Merge Avg Price with newly merged table

Top_5_Merge_Updated = pd.merge(Top_5_Merge, Top_5_Avg, on = 'SN')
Top_5_Merge_Updated.head()
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
      <th>SN</th>
      <th>Price_x</th>
      <th>Price_y</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Undirrala66</td>
      <td>17.06</td>
      <td>5</td>
      <td>3.412000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Saedue76</td>
      <td>13.56</td>
      <td>4</td>
      <td>3.390000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Mindimnya67</td>
      <td>12.74</td>
      <td>4</td>
      <td>3.185000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Haellysu29</td>
      <td>12.73</td>
      <td>3</td>
      <td>4.243333</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Eoda93</td>
      <td>11.58</td>
      <td>3</td>
      <td>3.860000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Fix Column names -----------------------

Top_5_Final = Top_5_Merge_Updated.rename(columns={'SN':'SN',
                                  'Price_x':'Total_Purchase_Value',
                                   'Price_y': 'Purhcase_Count',
                                   'Price': 'Avg_Purchase_Price'})
Top_5_Final = Top_5_Final[['SN',
                          'Purhcase_Count',
                          'Avg_Purchase_Price',
                          'Total_Purchase_Value']]
Top_5_Final = Top_5_Final.round(2)
```

**Top Spenders Data Frame**


```python
Top_5_Final.set_index('SN').head()
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
      <th>Purhcase_Count</th>
      <th>Avg_Purchase_Price</th>
      <th>Total_Purchase_Value</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Undirrala66</th>
      <td>5</td>
      <td>3.41</td>
      <td>17.06</td>
    </tr>
    <tr>
      <th>Saedue76</th>
      <td>4</td>
      <td>3.39</td>
      <td>13.56</td>
    </tr>
    <tr>
      <th>Mindimnya67</th>
      <td>4</td>
      <td>3.18</td>
      <td>12.74</td>
    </tr>
    <tr>
      <th>Haellysu29</th>
      <td>3</td>
      <td>4.24</td>
      <td>12.73</td>
    </tr>
    <tr>
      <th>Eoda93</th>
      <td>3</td>
      <td>3.86</td>
      <td>11.58</td>
    </tr>
  </tbody>
</table>
</div>



**Most Popular Items**

* Identify the 5 most popular items by purchase count, then list (in a table):
  * Item ID
  * Item Name
  * Purchase Count
  * Item Price
  * Total Purchase Value


**Most Popular Items**

* Identify the 5 most popular items by purchase count, then list (in a table):
  * Item ID
  * Item Name
  * Purchase Count
  * Item Price
  * Total Purchase Value



```python
# Create Data Frame for "Item Name" to get purchase count

Item_count = pd.DataFrame(CLEAN_PURCHASE_DATA['Item Name'].value_counts())
Item_count.reset_index(inplace=True)
Item_count.columns = ['Item Name', 'Purchase_Count']
Item_count = Item_count.sort_values(['Purchase_Count'],ascending=False)
Item_count.head()
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
      <th>Item Name</th>
      <th>Purchase_Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Final Critic</td>
      <td>13</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Betrayal, Whisper of Grieving Widows</td>
      <td>11</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Stormcaller</td>
      <td>10</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Arcane Gem</td>
      <td>10</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Trickster</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Item Name and Price Sum

Most_Popular_Name_sum = pd.DataFrame(CLEAN_PURCHASE_DATA.groupby('Item Name')['Price'].sum())
Most_Popular_Name_sum.reset_index(inplace=True)
Most_Popular_Name_sum = Most_Popular_Name_sum.sort_values(['Price'], ascending=False)
Most_Popular_Name_sum.head()
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
      <th>Item Name</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>112</th>
      <td>Retribution Axe</td>
      <td>37.26</td>
    </tr>
    <tr>
      <th>56</th>
      <td>Final Critic</td>
      <td>37.24</td>
    </tr>
    <tr>
      <th>137</th>
      <td>Stormcaller</td>
      <td>34.65</td>
    </tr>
    <tr>
      <th>132</th>
      <td>Spectral Diamond Doomblade</td>
      <td>29.75</td>
    </tr>
    <tr>
      <th>96</th>
      <td>Orenmir</td>
      <td>29.70</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Item Name and Price Count

Most_Popular_Name_count = pd.DataFrame(CLEAN_PURCHASE_DATA.groupby('Item Name')['Price'].count())
Most_Popular_Name_count.reset_index(inplace=True)
Most_Popular_Name_count = Most_Popular_Name_count.sort_values(['Price'], ascending=False)
Most_Popular_Name_count.head()
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
      <th>Item Name</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>56</th>
      <td>Final Critic</td>
      <td>13</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Betrayal, Whisper of Grieving Widows</td>
      <td>11</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Arcane Gem</td>
      <td>10</td>
    </tr>
    <tr>
      <th>137</th>
      <td>Stormcaller</td>
      <td>10</td>
    </tr>
    <tr>
      <th>173</th>
      <td>Woeful Adamantite Claymore</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Merge Item Name Price Sum and Count

Most_Popular_Name_Merge = pd.merge(Most_Popular_Name_sum, Most_Popular_Name_count, on = 'Item Name')
```


```python
# Fix Column names -----------------------

Most_Popular_Name_Merge = Most_Popular_Name_Merge.rename(columns={'Item Name':'Item Name',
                                  'Price_x':'Total_Purchase_Value',
                                   'Price_y': 'Purhcase_Count'})
Most_Popular_Name_Merge = Most_Popular_Name_Merge[['Item Name',
                          'Purhcase_Count',
                          'Total_Purchase_Value']]
Most_Popular_Name_Merge = Most_Popular_Name_Merge.round(2)
Most_Popular_Name_Merge.head()
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
      <th>Item Name</th>
      <th>Purhcase_Count</th>
      <th>Total_Purchase_Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Retribution Axe</td>
      <td>9</td>
      <td>37.26</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Final Critic</td>
      <td>13</td>
      <td>37.24</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Stormcaller</td>
      <td>10</td>
      <td>34.65</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Spectral Diamond Doomblade</td>
      <td>7</td>
      <td>29.75</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Orenmir</td>
      <td>6</td>
      <td>29.70</td>
    </tr>
  </tbody>
</table>
</div>



***Most popular items listed by Item ID, Total Purchase Value & Purchase Count***


```python
# Item ID and Price Sum

Most_Popular_ID_sum = pd.DataFrame(CLEAN_PURCHASE_DATA.groupby('Item ID')['Price'].sum())
Most_Popular_ID_sum.reset_index(inplace=True)
Most_Popular_ID_sum = Most_Popular_ID_sum.sort_values(['Price'], ascending=False)
Most_Popular_ID_sum.head()
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
      <th>Item ID</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34</th>
      <td>34</td>
      <td>37.26</td>
    </tr>
    <tr>
      <th>115</th>
      <td>115</td>
      <td>29.75</td>
    </tr>
    <tr>
      <th>32</th>
      <td>32</td>
      <td>29.70</td>
    </tr>
    <tr>
      <th>103</th>
      <td>103</td>
      <td>29.22</td>
    </tr>
    <tr>
      <th>107</th>
      <td>107</td>
      <td>28.88</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Item ID and Price Count 
Most_Popular_ID_count = pd.DataFrame(CLEAN_PURCHASE_DATA.groupby('Item ID')['Price'].count())
Most_Popular_ID_count.reset_index(inplace=True)
Most_Popular_ID_count = Most_Popular_ID_count.sort_values(['Price'], ascending=False)
Most_Popular_ID_count.head()
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
      <th>Item ID</th>
      <th>Price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <td>39</td>
      <td>11</td>
    </tr>
    <tr>
      <th>84</th>
      <td>84</td>
      <td>10</td>
    </tr>
    <tr>
      <th>31</th>
      <td>31</td>
      <td>9</td>
    </tr>
    <tr>
      <th>174</th>
      <td>175</td>
      <td>9</td>
    </tr>
    <tr>
      <th>13</th>
      <td>13</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Merge Item ID Price Sum and Count

Most_Popular_ID_Merge = pd.merge(Most_Popular_ID_sum, Most_Popular_ID_count, on = 'Item ID')
```


```python
# Fix Column names -----------------------

Most_Popular_ID_Merge = Most_Popular_ID_Merge.rename(columns={'Item ID':'Item ID',
                                  'Price_x':'Total_Purchase_Value',
                                   'Price_y': 'Purhcase_Count'})
Most_Popular_ID_Merge = Most_Popular_ID_Merge[['Item ID',
                          'Purhcase_Count',
                          'Total_Purchase_Value']]
Most_Popular_ID_Merge = Most_Popular_ID_Merge.round(2)
Most_Popular_ID_Merge.head()
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
      <th>Item ID</th>
      <th>Purhcase_Count</th>
      <th>Total_Purchase_Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>34</td>
      <td>9</td>
      <td>37.26</td>
    </tr>
    <tr>
      <th>1</th>
      <td>115</td>
      <td>7</td>
      <td>29.75</td>
    </tr>
    <tr>
      <th>2</th>
      <td>32</td>
      <td>6</td>
      <td>29.70</td>
    </tr>
    <tr>
      <th>3</th>
      <td>103</td>
      <td>6</td>
      <td>29.22</td>
    </tr>
    <tr>
      <th>4</th>
      <td>107</td>
      <td>8</td>
      <td>28.88</td>
    </tr>
  </tbody>
</table>
</div>



**Most Profitable Items**

* Identify the 5 most profitable items by total purchase value, then list (in a table):
  * Item ID
  * Item Name
  * Purchase Count
  * Item Price
  * Total Purchase Value

   ***Most Profitable Items - can be determined by Most_Popular_Name_Merge - DF***


```python
Most_Popular_Name_Merge.head()
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
      <th>Item Name</th>
      <th>Purhcase_Count</th>
      <th>Total_Purchase_Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Retribution Axe</td>
      <td>9</td>
      <td>37.26</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Final Critic</td>
      <td>13</td>
      <td>37.24</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Stormcaller</td>
      <td>10</td>
      <td>34.65</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Spectral Diamond Doomblade</td>
      <td>7</td>
      <td>29.75</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Orenmir</td>
      <td>6</td>
      <td>29.70</td>
    </tr>
  </tbody>
</table>
</div>



***Or by Most_Popular_ID_Merge -DF***


```python
Most_Popular_ID_Merge.head()
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
      <th>Item ID</th>
      <th>Purhcase_Count</th>
      <th>Total_Purchase_Value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>34</td>
      <td>9</td>
      <td>37.26</td>
    </tr>
    <tr>
      <th>1</th>
      <td>115</td>
      <td>7</td>
      <td>29.75</td>
    </tr>
    <tr>
      <th>2</th>
      <td>32</td>
      <td>6</td>
      <td>29.70</td>
    </tr>
    <tr>
      <th>3</th>
      <td>103</td>
      <td>6</td>
      <td>29.22</td>
    </tr>
    <tr>
      <th>4</th>
      <td>107</td>
      <td>8</td>
      <td>28.88</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
