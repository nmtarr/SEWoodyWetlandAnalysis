# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 10:05:44 2018 by nmtarr

Description: Temp script for combining protection and overlay info for top
species.   Later put into the report notebook.
"""
import pandas as pd
# Import packages
import os
import pandas as pd
pd.set_option('display.max_rows', 700)
pd.set_option('display.max_columns', 10)
pd.set_option('display.width', 1200)
pd.set_option('display.max_colwidth', 80)
import SEWWConfig as floodconfig

# Read in the table of protection 
spProtDf = pd.read_csv(floodconfig.resultDir + "TopSpeciesProtection1or2.csv", 
                       index_col="Unnamed: 0")
spProtDf.set_index(["common_name"], inplace=True)
spProtDf.rename({'summer': 'Protected Summer Habitat', 
                 'winter':'Protected Winter Habitat'}, 
                 axis=1, inplace=True)

# Read in the table of SEWW overlap
spTopDf = pd.read_csv(floodconfig.resultDir + "TopSpecies.csv", 
                      index_col="Unnamed: 0")
spTopDf['Season'] = ['Year-round' 
                       if spTopDf.loc[i, 'PercSummer'] == spTopDf.loc[i, 'PercWinter']
                       else 'Replace'
                       for i in spTopDf.index]

df3 = pd.merge(spTopDf, spProtDf, how='inner', left_on="common_name", 
             right_on="common_name")
df4 = df3.filter(['PercSummer', 'PercWinter', 'Protected Summer Habitat', 
                  'Protected Winter Habitat', 'common_name', ''
                      'scientific_name', 'Season'], axis=1)

# Split out winter and summer columns into 2 dataframes
summerDf = df4.drop(["Protected Winter Habitat", 
                            'PercWinter'], axis=1)
summerDf.rename({'Protected Summer Habitat':'Percent Protected (1&2)',
                 'PercSummer':'SEWW Habitat (%)'}, 
                   axis=1, inplace=True)
summerDf['Season'] = ['Summer'
                      if i == 'Replace'
                      else i
                      for i in summerDf['Season']]

winterDf = df4.drop(["Protected Summer Habitat",
                            'PercSummer'], axis=1)
winterDf.rename({'Protected Winter Habitat':'Percent Protected (1&2)',
                 'PercWinter':'SEWW Habitat (%)'},
                   axis=1, inplace=True)
winterDf['Season'] = ['Winter'
                      if i == 'Replace'
                      else i
                      for i in winterDf['Season']]

df0 = pd.concat([summerDf, winterDf], sort=False)
df0.reset_index(inplace=True, drop=True)
df0.rename({'common_name':'Common Name',
            'scientific_name':'Scientific Name'}, inplace=True, axis=1)
df0.set_index(['Common Name', 'Scientific Name',
               'Season'], inplace=True)
df0.sort_values(inplace=True, by='SEWW Habitat (%)', ascending=False)
df1 = df0.drop_duplicates()
print(df1.round(2))

# Plot
df1.plot(kind='scatter', x='SEWW Habitat (%)', y='Percent Protected (1&2)')


