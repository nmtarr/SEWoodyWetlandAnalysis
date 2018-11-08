# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 10:05:44 2018 by nmtarr

Description: Code for combining protection and overlay info for top
species.
"""
import pandas as pd
# Import packages
import pandas as pd
pd.set_option('display.max_rows', 700)
pd.set_option('display.max_columns', 10)
pd.set_option('display.width', 1200)
pd.set_option('display.max_colwidth', 80)
import SEWWConfig as floodconfig

# Read in the species protection table
spProtDf = pd.read_csv(floodconfig.resultDir + "TopSpeciesProtection1or2.csv", 
                       index_col="Unnamed: 0")
spProtDf.set_index(["common_name"], inplace=True)
spProtDf.rename({'summer': 'Protected Summer Habitat', 
                 'winter':'Protected Winter Habitat'}, 
                 axis=1, inplace=True)

# Read in the SEWW overlap table
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

# Split out winter and summer columns into 2 dataframes to then later concatenate
summerDf = df4.drop(["Protected Winter Habitat", 
                            'PercWinter'], axis=1)
summerDf.rename({'Protected Summer Habitat':'Protected (%)',
                 'PercSummer':'Habitat in SEWW (%)'}, 
                   axis=1, inplace=True)
summerDf['Season'] = ['Summer'
                      if i == 'Replace'
                      else i
                      for i in summerDf['Season']]
winterDf = df4.drop(["Protected Summer Habitat",
                            'PercSummer'], axis=1)
winterDf.rename({'Protected Winter Habitat':'Protected (%)',
                 'PercWinter':'Habitat in SEWW (%)'},
                   axis=1, inplace=True)
winterDf['Season'] = ['Winter'
                      if i == 'Replace'
                      else i
                      for i in winterDf['Season']]
# Concatenate summer and winter dataframes
df0 = pd.concat([summerDf, winterDf], sort=False)
df0.reset_index(inplace=True, drop=True)
df0.rename({'common_name':'Common Name',
            'scientific_name':'Scientific Name'}, inplace=True, axis=1)
df0.set_index(['Common Name', 'Season'], inplace=True)
df0.drop(['Scientific Name'], axis=1, inplace=True)
df0.sort_values(inplace=True, by='Habitat in SEWW (%)', ascending=False)
df1 = df0.drop_duplicates()
df1 = df1[df1['Habitat in SEWW (%)'] > 50]
df1.reset_index(inplace=True)
df1.set_index(["Common Name"], inplace=True, drop=True)

# Print table
print("Table 4.  SEWW species ranked according to the proportion of CONUS habitat that is in SEWWs.  "
      "The percentage of CONUS habitat that is protected in GAP status 1 or 2 lands is also included.")
print(df1.round(2))

# Plot rows from table as scatterplot
df1.plot(kind='scatter', x='Habitat in SEWW (%)', y='Protected (%)')
print("\n\nFigure 8.  Scatterplot of percent of CONUS habitat protected in GAP Status 1 or 2 lands versus the proportion "
      "of the species' CONUS habitat occuring within SEWWs for rows in Table 4.")