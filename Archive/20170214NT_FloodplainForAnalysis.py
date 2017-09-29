# -*- coding: utf-8 -*-
"""
Feb 2, 2017 by nmtarr

Code to run analyses on the importance of floodplain forests for wildlife
"""
import sys, pandas as pd, arcpy
sys.path.append('T:/Scripts/GAPAnalysis')
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

###################################################  List species in general study region
#########################################################################################
studyRegionList = gp.gaprange.SppInAOI(AOIShp = AOI_TEST,
                                       hucShp = config.hucs, 
                                       workDir = workDir,
                                       origin = [1], season = [1, 3, 4],
                                       reproduction = [1, 2, 3],
                                       presence = [1, 2, 3])
# List species to assess
habMapList = [i[0] + i[1:5].upper() + i[5:] + habmapSuffix for i in studyRegionList]

################################################################## Map floodplain forests
#########################################################################################
# Specify "floodplain forest" map units
ffMUs = [1402, 5602]                                                           #####################    Needs to be completed

# Reclass land cover to get a map of floodplain forests.
print("Reclassifing lcv1") 
ffMap1 = ga.landcover.ReclassLandCover(MUlist=ffMUs, reclassTo=10, keyword="Floodplain",
                                       workDir=resultDir,
                                       lcPath="P:/Proj3/USGap/Vert/Model/data/dataMosaics/lcv1",
                                       lcVersion="1.1", log=workDir+"log.txt")
# Replace nulls with 99
print("Replacing null values")
arcpy.env.extent = AOI
placeholder_code = 99
ffMap2 = arcpy.sa.Con(arcpy.sa.IsNull(ffMap1), placeholder_code, ffMap1)

# Make sure valid RAT
print("Checking or building statistics and RAT")
arcpy.management.CalculateStatistics(ffMap2, skip_existing=True)
arcpy.management.BuildRasterAttributeTable(ffMap2, overwrite=True)

# Save
print("Saving")
ffMap2.save(resultDir + "/Floodplain10&99.tif")

######################################### Calculate representation on floodplains forests
#########################################################################################
# Calculate representation
dfSpFF = ga.habitat.PercentOverlay(zoneFile=resultDir + "/Floodplain10&99.tif", 
                                   zoneName="Floodplain", 
                                   zoneField="VALUE", 
                                   habmapList=habMapList,
                                   habDir=habMapDir,
                                   workDir=resultDir+"Percent_FloodplainForest",
                                   snap=snap_raster,
                                   extent="zoneFile")


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
#  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
############################################# Calculate representation on protected areas
#########################################################################################
# Summarize management for top winter species
# Use field "gap_sts"?
dfWinterSp_PAD = ga.habitat.PercentOverlay(zoneFile=PADUS_Man, 
                                           zoneName="Management_Winter", 
                                           zoneField="VALUE", 
                                           habMapList=winterSp,
                                           habDir=habMapDir,
                                           workDir=resultDir+"Percent_PADUS_Winter",
                                           snap=snap_raster,
                                           extent="zoneFile")
# Summarize management for top summer species
dfSummerSp_PAD = ga.habitat.PercentOverlay(zoneFile=PADUS_Man, 
                                           zoneName="Management_Summer", 
                                           zoneField="VALUE", 
                                           habMapList=summerSp,
                                           habDir=habMapDir,
                                           workDir=resultDir+"Percent_PADUS_Summer",
                                           snap=snap_raster,
                                           extent="zoneFile")                                 

################################################################### Calculate land owners
#########################################################################################
# Calculate ownership for top winter species
# Use field "own_name"?
dfWinterSp_PAD = ga.representation.Calculate(zone_file=PADUS_Own, 
                                             zone_name="Ownership_Winter", 
                                             zone_field="VALUE", habitat_maps=winterSp,
                                             speciesDir=habMapDir,
                                             workDir=resultDir+"Percent_PADUS_Winter",
                                             snap_raster=snap_raster)
# Calculate ownership for top summer species
dfSummerSp_PAD = ga.representation.Calculate(zone_file=PADUS_Own, 
                                             zone_name="Ownership_Summer", 
                                             zone_field="VALUE", habitat_maps=summerSp,
                                             speciesDir=habMapDir,
                                             workDir=resultDir+"Percent_PADUS_Summer",
                                             snap_raster=snap_raster)                                 

#########################################################################################
#########################################################################################

#########################################################################################
#########################################################################################

#########################################################################################
#########################################################################################


#########################################################################################
#########################################################################################




