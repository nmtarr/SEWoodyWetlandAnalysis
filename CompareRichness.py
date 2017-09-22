# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 09:21:46 2017 by nmtarr

Description:  Compares richness from flooded sytems and the study region to
that of CONUS. 

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
import arcpy

fontSize=9

for group in floodconfig.richnessPathsCONUS.keys():
    print group
    conusStats = ga.misc.RATStats(floodconfig.richnessPathsCONUS[group],
                                  percentile_list=[25, 50, 75],
                                  dropMax=True, dropZero=True)
    seStats = ga.misc.RATStats(floodconfig.richnessPathsSE[group],
                                  percentile_list=[25, 50, 75],
                                  dropMax=True, dropZero=True)
    floodStats = ga.misc.RATStats(floodconfig.richnessPathsFlood[group],
                                  percentile_list=[25, 50, 75],
                                  dropZero=True)
    
    # CONUS
    conusRAT = ga.misc.RATtoDataFrame(floodconfig.richnessPathsCONUS[group])
    conusRAT = conusRAT[:-1]
    conusRAT = conusRAT[conusRAT.index > 0]
    ax1 = conusRAT.plot(kind="line", legend=False)
    ax1.set_ylabel("frequency (# cells)")
    
    # SE
    seRAT = ga.misc.RATtoDataFrame(floodconfig.richnessPathsSE[group])
    seRAT = seRAT[seRAT.index > 0]
    ax3 = seRAT.plot(kind="line", legend=False)
    ax3.set_ylabel("frequency (# cells)")
    seStats = ga.misc.RATStats(floodconfig.richnessPathsCONUS[group],
                                  percentile_list=[25, 50, 75],
                                  dropMax=True, dropZero=True)
    
    # Floodplains
    floodRAT = ga.misc.RATtoDataFrame(floodconfig.richnessPathsFlood[group])
    floodRAT = floodRAT[floodRAT.index > 0]
    ax2 = floodRAT.plot(kind="line", legend=False)
    ax2.set_ylabel("frequency (# cells)")
    