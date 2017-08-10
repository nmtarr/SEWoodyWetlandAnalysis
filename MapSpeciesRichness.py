# -*- coding: utf-8 -*-
"""
Feb 2, 2017 by nmtarr

Code to run analyses on the importance of floodplain forests for wildlife
"""
import sys, pandas as pd, arcpy
sys.path.append('T:/Scripts/GAPAnalysis')
sys.path.append('T:/Gap/Data')
sys.path.append('T:/Scripts/GAPProduction')
sys.path.append('P:/Proj3/USGap/Scripts/Floodplain_Forests_2016')
import gapanalysis as ga, gapproduction as gp, gapconfig as config
import FloodplainConfig as floodconfig
pd.set_option('display.width', 1000)

################################################################### Define some variables
#########################################################################################
workDir = floodconfig.workDir
dataDir = floodconfig.dataDir
tempDir = floodconfig.tempDir
resultDir = floodconfig.resultDir
habMapDir = floodconfig.habMapDir
seasonalhabMapDir = floodconfig.seasonalhabMapDir
lcMapDir = floodconfig.lcMapDir
conus_extent = floodconfig.conus_extent
snap_raster = floodconfig.snap_raster
PADUS_Man = floodconfig.PADUS_Man
PADUS_Own = floodconfig.PADUS_Own
AOI = floodconfig.AOI
AOI_TEST = floodconfig.AOI_TEST
habmapSuffix = floodconfig.habmapSuffix
                                          
######################################################################## Set environments
#########################################################################################
arcpy.ResetEnvironments()
arcpy.CheckOutExtension("Spatial")
arcpy.env.snapRaster=snap_raster
arcpy.env.overwriteOutput=True
arcpy.env.scratchWorkspace=tempDir
arcpy.env.workspace=workDir
arcpy.env.rasterStatistics="STATISTICS"
arcpy.env.extent="MAXOF"

###################################  Filter to get list of top species in terms of FF use
#########################################################################################
# Assign cutoff for filtering
cutoff = 10.0
# Filter out the records corresponding to 0/nodata/99.
dfSpFF2 = dfSpFF.loc[dfSpFF.index.get_level_values(1) != placeholder_code]
# Filter dataframe for top species and save, also make list for below
winterSp = dfSpFF2[dfSpFF2["PercWinter"] > cutoff]
winterSp.to_csv(resultDir + "TopWinterSpecies.csv")
winterSp = list(winterSp.strUC)
summerSp = dfSpFF2[dfSpFF2["PercSummer"] > cutoff]
summerSp.to_csv(resultDir + "TopSummerSpecies.csv")
summerSp = list(summerSp.strUC)

######################################### Map richness of top species (winter and summer)
#########################################################################################
# Winter
winterTiffs = [x + "_v1.tif" for x in winterSp]
wRichnessMap = ga.richness.MapRichness(spp=winterTiffs, groupName="Top_Winter",
                                           outLoc=resultDir, modelDir=seasonalhabMapDir,
                                           season="Winter", intervalSize=40,
                                           CONUSExtent=conus_extent)
# Summer
summerTiffs = [x + "_v1.tif" for x in summerSp]
sRichnessMap = ga.richness.ProcessRichness(spp=summerTiffs, groupName="Top_Summer",
                                           outLoc=resultDir, modelDir=seasonalhabMapDir,
                                           season="Summer", interval_size=40,
                                           CONUS_extent=conus_extent)
                        

#########################################################################################
#########################################################################################

#########################################################################################
#########################################################################################

#########################################################################################
#########################################################################################


#########################################################################################
#########################################################################################




