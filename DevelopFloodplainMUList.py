# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 11:27:20 2017 by nmtarr

Description: Code to begin the development of a list of ecological systems
of interest.  Note that a final step has to be performed by a human.
"""
import sys
sys.path.append('P:/Proj3/USGap/Scripts/Floodplain_Forests_2016')
import gapanalysis as ga, gapproduction as gp, pandas as pd
import FloodplainConfig as floodconfig

# Use wildclass sets to whittle down the list.
broadTree = gp.wildclass.hasBroadTree()
hasForest = gp.wildclass.hasForest()
needleTree = gp.wildclass.hasNeedleTree()
flooded = gp.wildclass.hasSaturatedSoil()
satBroad = broadTree & flooded & hasForest
satNeedle = needleTree & flooded
sat = satBroad | satNeedle

# Save a table version of whittled down list for manual review.
df = pd.DataFrame(list(sat))
df.rename(columns={0:"map_code"}, inplace=True)
df["system_name"] = [gp.gapdb.MUName(m) for m in df.map_code]
df.to_csv(floodconfig.intermDir + "saturated systems with trees.csv")

# The next step is to open the "saturated systems with trees.csv" and 
# put a "1" in an "include" column, then save as "Ecological systems of interest.csv"
# in the data directory.  That step has to be done by a human.