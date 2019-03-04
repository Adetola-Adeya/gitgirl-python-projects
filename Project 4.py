#Open and read the csv on your jupyter notebook
#Write a Pandas program to get the details of the movie with title 'Grumpier Old Men'
#Write a Pandas program to sort the DataFrame based on release_date. Let the framework only display the following columns: 'title', 'release_date', 'budget', 'revenue', 'runtime'
#Write a Pandas program to get those movies whose revenue more than 2 million and spent less than 1 million. Let the framework only display the following columns: 'title', 'release_date', 'budget', 'revenue', 'runtime'

import numpy as np
import pandas as pd

ls

1. 
df = pd.read_csv("movies_metadata - movies_metadata.csv", skiprows=[29])
df.head()

2.
df.loc[df.title=="Grumpier Old Men"]

3. 
df3 = df.sort_values('release_date')[[ 'title', 'release_date', 'budget', 'revenue', 'runtime']]
df3

4.
df3["revenue"] = pd.to_numeric(df3["revenue"], errors='coerce')
df3[((df3["revenue"] > 2000000) & (df3["budget"] < 1000000))]
