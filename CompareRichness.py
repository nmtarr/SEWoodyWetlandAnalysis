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
    ax1 = conusRAT.plot(kind="box", legend=False)
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
    
    # Put all tables in same dataframe
    DF0 = conusRAT
    DF0.index.name = "value"
    DF0.rename(columns={"cell_count":"CONUS"}, inplace=True)
    for i in seRAT.index:
        DF0.loc[i, "Southeast"] = seRAT.loc[i, "cell_count"]
    for i in floodRAT.index:
        DF0.loc[i, "floodplain"] = floodRAT.loc[i, "cell_count"]
        
    # Make distribution plot
    ax = DF0.plot(kind="line", legend=True, title=group,
                  color=["b", "r", "g"])
    ax.set_ylabel("Frequency (# of cells)", fontsize=fontSize)
    ax.set_xlabel("Species count", fontsize=fontSize)
    plt.legend(frameon=False)
    fig2 = ax.get_figure()
    fig2.savefig(floodconfig.resultDir + "{0} curves.png".format(group))