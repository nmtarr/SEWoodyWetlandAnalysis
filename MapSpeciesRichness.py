# -*- coding: utf-8 -*-
"""
Feb 2, 2017 by nmtarr

Code to run analyses on the importance of floodplain forests for wildlife
"""
import sys, pandas as pd, arcpy
sys.path.append('T:/Scripts/GAPAnalysis')
sys.path.append('P:/Proj3/USGap/Scripts/Floodplain_Forests_2016')
import gapanalysis as ga
import FloodplainConfig as floodconfig
pd.set_option('display.width', 1000)

######################################### Map richness of top species (winter and summer)
#########################################################################################
# Winter
winterDF = pd.read_csv(floodconfig.winterTopSpList)
winterSp = list(winterDF.strUC)
winterTiffs = [x + "_v1.tif" for x in winterSp]
wRichnessMap = ga.richness.MapRichness(spp=winterTiffs, groupName="Top_Winter",
                                       outLoc=floodconfig.resultDir, 
                                       modelDir=floodconfig.seasonalhabMapDir,
                                       season="Winter", 
                                       intervalSize=40,
                                       CONUSExtent=floodconfig.conus_extent)
# Summer
summerDF = pd.read_csv(floodconfig.summerTopSpList)
summerSp = list(summerDF.strUC)
summerTiffs = [x + "_v1.tif" for x in summerSp]
sRichnessMap = ga.richness.MapRichness(spp=summerTiffs, groupName="Top_Summer",
                                       outLoc=floodconfig.resultDir, 
                                       modelDir=floodconfig.seasonalhabMapDir,
                                       season="Summer", 
                                       intervalSize=40,
                                       CONUSExtent=floodconfig.conus_extent)


#########################################  Mask the richness with the floodplain layer
######################################################################################
maskedWinter = arcpy.sa.ExtractByMask(wRichnessMap, floodconfig.floodplainBinary)
maskedWinter.save(floodconfig.resultDir + "maskedRichnessWinter.tif")

maskedSummer = arcpy.sa.ExtractByMask(sRichnessMap, floodconfig.floodplainBinary)
maskedSummer.save(floodconfig.resultDir + "maskedRichnessSummer.tif")