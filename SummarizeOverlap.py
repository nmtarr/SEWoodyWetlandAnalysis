# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 09:21:46 2017 by nmtarr

Description:  This code summarizes the results of the CalculatePercentHabitatInFloodplainForest.py
 and generates a descriptive table, lists of summer and winter species with dependence
 on the system, and graphs of frequency distribution of amount that species'
 habitat occurs in floodplain forests.
"""
import sys, pandas as pd, matplotlib.pyplot as plt, numpy as np
sys.path.append('T:/Scripts/GAPAnalysis')
sys.path.append('T:/Scripts/GAPProduction')
sys.path.append('T:/GAP/data')
sys.path.append('P:/Proj3/USGap/Scripts/Floodplain_Forests_2016')
import gapproduction as gp
import gapanalysis as ga
import FloodplainConfig as floodconfig
pd.set_option('display.width', 1000)

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
df1 = df1[df1.NonHabitatPixels != df1.ZoneTotal]
descDF = df1.describe(percentiles=np.arange(0, 1, .01))
descDF.drop(["Zone", "NonHabitatPixels", "SummerPixels", "WinterPixels", 
             "AllYearPixels", "ZoneTotal", "SummerPixelTotal", "WinterPixelTotal",
             "AllYearPixelTotal"], axis=1, inplace=True)
print(descDF)
descDF.to_csv(floodconfig.resultDir + "Overlay descriptive statistics.csv")


############################################## Filter out non dependent species
###############################################################################
# Assign cutoff for filtering    ############################              What value to use?
threshold = 50.0

# Filter out the records corresponding to 0/nodata/99.
dfSpFF = df0.loc[df0.Zone != floodconfig.placeholder_code]

# Filter dataframe for top species and save, also make list for below
winterSp = dfSpFF[dfSpFF["PercWinter"] >= threshold]
winterSp.to_csv(floodconfig.winterTopSpList)
print("\n{0} species with more than {1}% of winter habitat in floodplain forests:".format(len(winterSp.strUC), threshold))
for x in [gp.gapdb.NameCommon(x) for x in list(winterSp.strUC)]:
    print("\t" + x)

summerSp = dfSpFF[dfSpFF["PercSummer"] >= threshold]
summerSp.to_csv(floodconfig.summerTopSpList)
print("\n{0} species with more than {1}% of summer habitat in floodplain forests:".format(len(summerSp.strUC), threshold))
for x in [gp.gapdb.NameCommon(x) for x in list(summerSp.strUC)]:
    print("\t" + x)


######################################## Histogram of percSummer and percWinter
###############################################################################
# Summer
df1summer = df1.filter(["strUC", "PercSummer"], axis=1).set_index(["strUC"])
bins = np.arange(0, 110, 10)-5    # this enables bins to sit above x ticks, note it's 1 + desired bin number
ax = df1summer.plot(kind="hist", legend=False, color=['y'], bins=bins, # note limit is 1 + desired bin number
                     xlim=(0,110), title="Percent Summer Habitat in Floodplain Forests")
ax.set_xlabel("Percent of Species' Total Habitat Area")
ax.set_ylabel("Frequency (# species)")
fig = plt.gcf()
fig.savefig(floodconfig.resultDir + "Summer overlay histogram.png", dpi=600)

# Winter
df1winter = df1.filter(["strUC", "PercWinter"], axis=1).set_index(["strUC"])
ax3 = df1winter.plot(kind="hist", legend=False, bins=bins, # note limit is 1 + desired bin number
                     xlim=(0,110), title="Percent Winter Habitat in Floodplain Forests")
ax3.set_xlabel("Percent of Species' Total Habitat Area")
ax3.set_ylabel("Frequency (# species)")
fig3 = plt.gcf()
fig3.savefig(floodconfig.resultDir + "Winter overlay histogram.png", dpi=600)


################################################ Box plots of summer and winter
###############################################################################
df1summerwinter = df1.filter(["strUC", "PercSummer", "PercWinter"], axis=1).set_index(["strUC"])
df1summerwinter.rename(columns={"PercSummer":"Summer", "PercWinter":"Winter"}, inplace=True)
ax2 = df1summerwinter.plot(kind="box", title="Species' habitat in floodplain forests", 
                           yticks=range(0,100, 10))
ax2.set_ylabel("%")
fig2 = plt.gcf()
fig2.savefig(floodconfig.resultDir + "Overlay boxplot.png", dpi=600)