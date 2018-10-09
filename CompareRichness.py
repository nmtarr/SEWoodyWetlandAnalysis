# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 09:21:46 2017 by nmtarr

Description:  Compares richness from flooded sytems and the study region to
that of CONUS. 

A figure with boxplots of richness from CONUS, SE, and floodplains would be
ideal; but it's not easy to do that with RAT/frequency tables.
"""
import sys, pandas as pd, matplotlib.pyplot as plt, numpy as np
sys.path.append('P:/Proj3/USGap/Scripts/SE_Woody_Wetlands')
execfile("T:/Scripts/AppendPaths27.py")
execfile("T:/Scripts/AppendGAPAnalysis.py")
import gapproduction as gp
import gapanalysis as ga
import SEWWConfig as floodconfig
pd.set_option('display.width', 1000)

fontSize=10

groups = floodconfig.richnessPathsCONUS.keys()
groups.sort()

for group in groups:
    mainFig = plt.figure(figsize=(11,2.5), frameon=True)
    mainFig.suptitle(group.title().replace("_", " "),
                     fontSize=12)
    
#    print group
    conusStats = ga.misc.RATStats(floodconfig.richnessPathsCONUS[group],
                                  percentile_list=[25, 50, 75],
                                  dropMax=True, dropZero=True)
    conusStats["name"] = "CONUS"
    seStats = ga.misc.RATStats(floodconfig.richnessPathsSE[group],
                                  percentile_list=[25, 50, 75],
                                  dropMax=True, dropZero=True)
    seStats["name"] = "Southeast"
    floodStats = ga.misc.RATStats(floodconfig.richnessPathsFlood[group],
                                  percentile_list=[25, 50, 75],
                                  dropZero=True)
    floodStats["name"] = "SEWW"
#    print conusStats
#    print seStats
#    print floodStats
    
    # CONUS
    conusRAT = ga.misc.RATtoDataFrame(floodconfig.richnessPathsCONUS[group])
    conusRAT = conusRAT[:-1]
    conusRAT = conusRAT[conusRAT.index > 0]/1000
    ax1 = mainFig.add_subplot(1,4,2)
    conusRAT.plot(ax=ax1, kind="line", legend=False, title="", color="blue")
    ax1.set_ylabel("Frequency (1,000 grid cells)")
    ax1.set_xlabel("Richness")
    
    # SE
    seRAT = ga.misc.RATtoDataFrame(floodconfig.richnessPathsSE[group])
    seRAT = seRAT[seRAT.index > 0]/1000
    ax3 = mainFig.add_subplot(1,4,3)
    seRAT.plot(ax=ax3, kind="line", legend=False, title="", color="orange")
    ax3.set_ylabel("Frequency (1,000 grid cells)")
    ax3.set_xlabel("Richness")
    
    # Floodplains
    floodRAT = ga.misc.RATtoDataFrame(floodconfig.richnessPathsFlood[group])
    floodRAT = floodRAT[floodRAT.index > 0]/1000
    ax2 = mainFig.add_subplot(1,4,4)
    floodRAT.plot(ax=ax2, kind="line", legend=False, title="", color="green")
    ax2.set_ylabel("Frequency (1,000 grid cells)")
    ax2.set_xlabel("Richness")
    
    # Figure with comparison of means
    meansDF = pd.DataFrame(index=["mean"], columns=["CONUS", "Southeast", 
                                                    "SEWW"])
    meansDF.loc["mean", "CONUS"] = conusStats["mean"]
    meansDF.loc["mean", "Southeast"] = seStats["mean"]
    meansDF.loc["mean", "SEWW"] = floodStats["mean"]
    ax4 = mainFig.add_subplot(1,4,1)
    meansDF.plot(ax=ax4, kind="bar")#, figsize=(5,5))
    ax4.set_ylabel("Richness")
    ax4.set_xlabel("Mean")
    ax4.axes.get_xaxis().set_ticks([])
    if group == "amphibian":
        plt.legend(loc=2)
    else:
        plt.legend(loc=3)
    
    plt.subplots_adjust(left=0.02, bottom=.04, right=.99, top=.80, 
                        wspace=.5, hspace=.3)
    
    mainFig.savefig(floodconfig.resultDir + "{0} mean chart.png".format(group),
                    bbox_inches="tight", dpi=600)