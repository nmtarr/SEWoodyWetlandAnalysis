# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 09:21:46 2017 by nmtarr

Description:  This code summarizes the results of the CalculatePercentHabitatInSEWW.py
 and generates a descriptive table, lists of summer and winter species with dependence
 on the system, and graphs of frequency distribution of amount that species'
 habitat occurs in SE woody wetlands.
"""
import sys, pandas as pd, matplotlib.pyplot as plt, numpy as np
sys.path.append('P:/Proj3/USGap/Scripts/SE_Woody_Wetlands')
execfile("T:/Scripts/AppendPaths27.py")
execfile("T:/Scripts/AppendGAPAnalysis.py")
import gapproduction as gp
import gapanalysis as ga
import SEWWConfig as floodconfig
pd.set_option('display.max_rows', 700)
pd.set_option('display.max_columns', 10)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 100)

########################################################## Read in master table
###############################################################################
df0 = pd.read_csv(floodconfig.overlayTable)

###################################################### Add species name columns
###############################################################################
df0["common_name"] = [gp.gapdb.NameCommon(s) for s in df0.strUC]
df0["scientific_name"] = [gp.gapdb.NameSci(s) for s in df0.strUC]

############################################################# Descriptive stats
###############################################################################
# Remove placeholder rows and species with no ovelap in any season
df1 = df0[df0.Zone != floodconfig.placeholder_code]
df1 = df1[(df1.PercSummer != 0) | (df1.PercWinter != 0)]
df2 = df1.drop(["Zone", "NonHabitatPixels", "SummerPixels", "WinterPixels", 
             "AllYearPixels", "ZoneTotal", "SummerPixelTotal", "WinterPixelTotal",
             "AllYearPixelTotal", "Date", "RunTime", "GeoTiff", "strUC", 
             "PercYearRound"], axis=1)
#print("{0} species use SEWW".format(len(df2)))
df2.to_csv(floodconfig.resultDir + "Species that use SEWW systems.csv")

# Summer and winter need to be described separately so that zeros can be
# properly ommitted.
descSum0 = df2.drop(["PercWinter", "common_name", "scientific_name"],
                   axis=1)
descSum = descSum0[descSum0.PercSummer > 0].describe(percentiles=np.arange(0, 1, .01))
descSum.to_csv(floodconfig.resultDir + "Overlay descriptive statistics SUMMER.csv")
descWint0 = df2.drop(["PercSummer", "common_name", "scientific_name"],
                   axis=1)
descWint = descWint0[descWint0.PercWinter > 0].describe(percentiles=np.arange(0, 1, .01))
descWint.to_csv(floodconfig.resultDir + "Overlay descriptive statistics WINTER.csv")


################################################ Box plots of summer and winter
###############################################################################
# Manipulate tables
df1summer = df1.filter(["strUC", "PercSummer"], axis=1).set_index(["strUC"])
df1winter = df1.filter(["strUC", "PercWinter"], axis=1).set_index(["strUC"])
df1summer.rename(columns={"PercSummer":"Summer"}, inplace=True)
df1winter.rename(columns={"PercWinter":"Winter"}, inplace=True)
df1summer = df1summer[df1summer.Summer > 0]
df1winter = df1winter[df1winter.Winter > 0]

# Graph
fig = plt.figure()
plt.suptitle("Habitat in SEWW\n")
ax2 = fig.add_subplot(1,2,1)
df1summer.plot(ax = ax2, kind="box", yticks=range(0,100, 10))
ax2.set_ylabel("Percent of CONUS habitat")
ax3 = fig.add_subplot(1,2,2)
df1winter.plot(ax = ax3, kind="box", yticks=range(0,100, 10))

fig.savefig(floodconfig.resultDir + "Overlay boxplot.png", dpi=600)


############################################## Filter out non dependent species
###############################################################################
# Assign cutoff for filtering    ############################              What value to use?
threshold = 50.0

# Filter out the records corresponding to 0/nodata/99.
dfSpFF = df0.loc[df0.Zone != floodconfig.placeholder_code]

# Filter dataframe for top species and save, also make list for below
winterSp = dfSpFF[dfSpFF["PercWinter"] >= threshold]
winterSp.to_csv(floodconfig.winterTopSpList)
#print("\n{0} species have more than {1}% of winter habitat in SEWW".format(len(winterSp.strUC), threshold))
for x in [gp.gapdb.NameCommon(x) for x in list(winterSp.strUC)]:
    #print("\t" + x)
    pass

summerSp = dfSpFF[dfSpFF["PercSummer"] >= threshold]
summerSp.to_csv(floodconfig.summerTopSpList)
#print("\n{0} species have more than {1}% of summer habitat in SEWW\n".format(len(summerSp.strUC), threshold))
for x in [gp.gapdb.NameCommon(x) for x in list(summerSp.strUC)]:
    #print("\t" + x)
    pass

# Table of top species and % hab in SEWW by season
topSp = dfSpFF[(dfSpFF["PercSummer"] >= threshold) | (dfSpFF["PercWinter"] >= threshold)].copy()
topSp.to_csv(floodconfig.TopSpList)
topSp.set_index(['common_name'], inplace=True)
topSp.index.name = 'Common Name'
topSp['PercSummer'] = [int(round(x)) for x in topSp.PercSummer]
topSp['PercWinter'] = [int(round(x)) for x in topSp.PercWinter]
topSp.rename(columns={"PercSummer": "Summer(%)", "PercWinter": "Winter(%)", 
                       "scientific_name": "Scientific Name"}, inplace=True)
topSp = topSp[['Scientific Name', 'Summer(%)', 'Winter(%)']]
topSp.sort_values(inplace=True, axis=0, by='Common Name')
topSp.reset_index(inplace=True)
topSp.index = [i + 1 for i in topSp.index]
print("Table 2.  Percent habitat in woody wetlands for species with over 50% of their habitat in SEWW during summer or winter.")
print(topSp)

print("\nFigure 3.  Boxplots of the seasonal percentages of CONUS habitat that are in Southeastern Woody Wetlands for species that inhabit those systems.".format(len(df2)))
######################################### Histogram of percSummer and percWinter
################################################################################
## Summer
#df1summer = df1.filter(["strUC", "PercSummer"], axis=1).set_index(["strUC"])
#df1summer = df1summer[df1summer.PercSummer > 0]
#bins = np.arange(0, 110, 10)-5    # this enables bins to sit above x ticks, note it's 1 + desired bin number
#ax = df1summer.plot(kind="hist", legend=False, color=['y'], bins=bins, # note limit is 1 + desired bin number
#                     xlim=(0,110))
#ax.set_xlabel("Percent of Species' Total Habitat Area")
#ax.set_ylabel("Frequency (# species)")
#fig = plt.gcf()
#fig.savefig(floodconfig.resultDir + "Summer overlay histogram.png", dpi=600)
#
## Winter
#df1winter = df1.filter(["strUC", "PercWinter"], axis=1).set_index(["strUC"])
#df1winter = df1winter[df1winter.PercWinter > 0]
#ax3 = df1winter.plot(kind="hist", legend=False, bins=bins, # note limit is 1 + desired bin number
#                     xlim=(0,110))
#ax3.set_xlabel("Percent of Species' Total Habitat Area")
#ax3.set_ylabel("Frequency (# species)")
#fig3 = plt.gcf()
#fig3.savefig(floodconfig.resultDir + "Winter overlay histogram.png", dpi=600)