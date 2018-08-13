# -*- coding: utf-8 -*-
"""
Feb 2, 2017 by nmtarr

Code to run analyses on the importance of woody wetlands for wildlife.  
These processes are slow (1 hr per species), so I broke them up into four lists
to run simultaneously on different kernels.  To do this you have to run chunks
of the code in separate shells; if you run the whole script, the chunks will
be run succevily and take a month.
"""
import sys, pandas as pd
sys.path.append('P:/Proj3/USGap/Scripts/SE_Woody_Wetlands')
execfile("T:/Scripts/AppendGAPAnalysis.py")
execfile("T:/Scripts/AppendPaths27.py")
import gapanalysis as ga
import SEWWConfig as floodconfig
pd.set_option('display.width', 1000)

######################################### Calculate representation on floodplains forests
#########################################################################################
# Calculate representation - kernel 1
scratchDir = floodconfig.tempDir
maps = floodconfig.null123List[:150]
dfSpFF1 = ga.habitat.PercentOverlay(zoneFile=floodconfig.SEWWBinary,
                                   zoneName="SEWW",
                                   zoneField="VALUE",
                                   habmapList=maps,
                                   habDir=floodconfig.habMapDir,
                                   workDir=floodconfig.resultDir+"Percent_SEWW",
                                   snap=floodconfig.snap_raster,
                                   scratchDir=scratchDir,
                                   extent="zoneFile")
# Calculate representation - kernel 2
scratchDir = floodconfig.tempDir + "temp2/"
maps = floodconfig.null123List[150:300]
dfSpFF2 = ga.habitat.PercentOverlay(zoneFile=floodconfig.SEWWBinary,
                                   zoneName="SEWW",
                                   zoneField="VALUE",
                                   habmapList=maps,
                                   habDir=floodconfig.habMapDir,
                                   workDir=floodconfig.resultDir+"Percent_SEWW",
                                   snap=floodconfig.snap_raster,
                                   scratchDir=scratchDir,
                                   extent="zoneFile")
# Calculate representation - kernel 3
scratchDir = floodconfig.tempDir + "temp3/"
maps = floodconfig.null123List[300:450]
dfSpFF3 = ga.habitat.PercentOverlay(zoneFile=floodconfig.SEWWBinary,
                                   zoneName="SEWW",
                                   zoneField="VALUE",
                                   habmapList=maps,
                                   habDir=floodconfig.habMapDir,
                                   workDir=floodconfig.resultDir+"Percent_SEWW",
                                   snap=floodconfig.snap_raster,
                                   scratchDir=scratchDir,
                                   extent="zoneFile")
# Calculate representation - kernel 4
scratchDir = floodconfig.tempDir + "temp4/"
maps = floodconfig.null123List[450:]
dfSpFF4 = ga.habitat.PercentOverlay(zoneFile=floodconfig.SEWWBinary,
                                   zoneName="SEWW",
                                   zoneField="VALUE",
                                   habmapList=maps,
                                   habDir=floodconfig.habMapDir,
                                   workDir=floodconfig.resultDir+"Percent_SEWW",
                                   snap=floodconfig.snap_raster,
                                   scratchDir=scratchDir,
                                   extent="zoneFile")