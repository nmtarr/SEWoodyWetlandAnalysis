# -*- coding: utf-8 -*-
"""
Feb 2, 2017 by nmtarr

Code to run analyses on the importance of floodplain forests for wildlife
"""
import sys, pandas as pd
sys.path.append('T:/Scripts/GAPAnalysis')
sys.path.append('P:/Proj3/USGap/Scripts/Floodplain_Forests_2016')
import gapanalysis as ga
import FloodplainConfig as floodconfig
pd.set_option('display.width', 1000)

######################################### Calculate representation on floodplains forests
#########################################################################################
# Calculate representation
dfSpFF = ga.habitat.PercentOverlay(zoneFile=floodconfig.floodplainBinary, 
                                   zoneName="Floodplain", 
                                   zoneField="VALUE", 
                                   habmapList=floodconfig.habMapList,
                                   habDir=floodconfig.habMapDir,
                                   workDir=floodconfig.resultDir+"Percent_FloodplainForest",
                                   snap=floodconfig.snap_raster,
                                   extent="zoneFile")


###################################  Filter to get list of top species in terms of FF use
#########################################################################################
# Assign cutoff for filtering
cutoff = 10.0

# Filter out the records corresponding to 0/nodata/99.
dfSpFF2 = dfSpFF.loc[dfSpFF.index.get_level_values(1) != floodconfig.placeholder_code]

# Filter dataframe for top species and save, also make list for below
winterSp = dfSpFF2[dfSpFF2["PercWinter"] > cutoff]
winterSp.to_csv(floodconfig.resultDir + "TopWinterSpecies.csv")
winterSp = list(winterSp.strUC)
summerSp = dfSpFF2[dfSpFF2["PercSummer"] > cutoff]
summerSp.to_csv(floodconfig.resultDir + "TopSummerSpecies.csv")
summerSp = list(summerSp.strUC)