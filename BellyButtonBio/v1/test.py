import pandas as pd 

df = pd.read_csv('Belly_Button_Biodiversity_Metadata.csv', dtype=object)

df_clean = df[['AGE', 'BBTYPE', 'ETHNICITY','GENDER', 'LOCATION', 'SAMPLEID']]
print(df_clean)

df_dict = df_clean.to_dict('index')
print(df_dict)