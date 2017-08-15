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
# Calculate representation - kernel 1
scratchDir = floodconfig.tempDir
maps = floodconfig.null123List[340:363]
dfSpFF1 = ga.habitat.PercentOverlay(zoneFile=floodconfig.floodplainBinary,
                                   zoneName="Floodplain",
                                   zoneField="VALUE",
                                   habmapList=maps,
                                   habDir=floodconfig.habMapDir,
                                   workDir=floodconfig.resultDir+"Percent_FloodplainForest",
                                   snap=floodconfig.snap_raster,
                                   scratchDir=scratchDir,
                                   extent="zoneFile")
# Calculate representation - kernel 2
scratchDir = floodconfig.tempDir + "temp2/"
maps = floodconfig.null123List[363:387]
dfSpFF2 = ga.habitat.PercentOverlay(zoneFile=floodconfig.floodplainBinary,
                                   zoneName="Floodplain",
                                   zoneField="VALUE",
                                   habmapList=maps,
                                   habDir=floodconfig.habMapDir,
                                   workDir=floodconfig.resultDir+"Percent_FloodplainForest",
                                   snap=floodconfig.snap_raster,
                                   scratchDir=scratchDir,
                                   extent="zoneFile")
# Calculate representation - kernel 3
scratchDir = floodconfig.tempDir + "temp3/"
maps = floodconfig.null123List[387:400]
dfSpFF3 = ga.habitat.PercentOverlay(zoneFile=floodconfig.floodplainBinary,
                                   zoneName="Floodplain",
                                   zoneField="VALUE",
                                   habmapList=maps,
                                   habDir=floodconfig.habMapDir,
                                   workDir=floodconfig.resultDir+"Percent_FloodplainForest",
                                   snap=floodconfig.snap_raster,
                                   scratchDir=scratchDir,
                                   extent="zoneFile")
# Calculate representation - kernel 4
scratchDir = floodconfig.tempDir + "temp4/"
maps = floodconfig.null123List[400:424]
dfSpFF4 = ga.habitat.PercentOverlay(zoneFile=floodconfig.floodplainBinary,
                                   zoneName="Floodplain",
                                   zoneField="VALUE",
                                   habmapList=maps,
                                   habDir=floodconfig.habMapDir,
                                   workDir=floodconfig.resultDir+"Percent_FloodplainForest",
                                   snap=floodconfig.snap_raster,
                                   scratchDir=scratchDir,
                                   extent="zoneFile")