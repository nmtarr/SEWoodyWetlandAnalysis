# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 11:27:20 2017 by nmtarr

Description:
"""
import sys
sys.path.append('T:/GAP/Data')
sys.path.append('T:/Scripts/GAPAnalysis')
sys.path.append('T:/Scripts/GAPProduction')
sys.path.append('P:/Proj3/USGap/Scripts/Floodplain_Forests_2016')
import gapanalysis as ga, gapproduction as gp, pandas as pd
import FloodplainConfig as floodconfig

# Use wildclass sets to whittle down the list.
broadTree = gp.wildclass.hasBroadTree()
hasForest = gp.wildclass.hasForest()
flooded = gp.wildclass.hasSaturatedSoil()
satBroad = broadTree & flooded & hasForest

# Save a table version of whittled down list for manual review.
df = pd.DataFrame(list(satBroad))
df.rename(columns={0:"map_code"}, inplace=True)
df["system_name"] = [gp.gapdb.MUName(m) for m in df.map_code]
df.to_csv(floodconfig.intermDir + "saturated and broad tree systems.csv")

# The next step is to open the "saturated and broad treee systems.csv" and 
# put a "1" in an "include" column, then save as "Ecological systems of interest.csv"
# in the data directory.