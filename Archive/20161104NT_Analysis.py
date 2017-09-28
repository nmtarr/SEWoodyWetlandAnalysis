# -*- coding: utf-8 -*-
"""
Created on Fri Nov 04 16:37:53 2016 by nmtarr

Code to run analyses on the importance of floodplain forests for wildlife

"""
import sys, pandas as pd, arcpy
sys.path.append('T:/Scripts/GAPAnalysis')
import gapanalysis as ga
pd.set_option('display.width', 1000)
################################################################### Define some variables
#########################################################################################
workDir = "P:/Proj3/USGap/Analysis/Floodplain_Forests_2016/"
dataDir = workDir + "Data/"
tempDir = workDir + "Temp/"
resultDir = workDir + "Results/"
habMapDir = "P:/Proj3/USGap/Vert/Model/Output/CONUS/"
lcMapDir = "P:/Proj3/USGap/Vert/Model/data/LandCover"
conus_extent = "P:/Proj3/USGap/Vert/Model/data/conus_ext_cnt"
snap_raster = "P:/Proj3/USGap/Vert/Model/data/snapgrid"
PADUS_Man = dataDir + "padus_man.tif"
PADUS_Own = dataDir + "padus_own.tif"

# Set environments
arcpy.CheckOutExtension("Spatial")
arcpy.env.snapRaster=snap_raster
arcpy.env.overwriteOutput=True
arcpy.env.scratchWorkspace=tempDir
arcpy.env.workspace=workDir
arcpy.env.rasterStatistics="STATISTICS"
arcpy.env.extent="MAXOF"

################################################################## Map floodplain forests
#########################################################################################
# Specify "floodplain forest" map units
ffMUs = [1402, 5602]
# Reclass land cover to get a map of floodplain forests.
ffMap1 = ga.landcover.ReclassLandCover(MUlist=ffMUs, reclassTo=10, keyword="Floodplain",
                                       workDir=resultDir, lcDir=lcMapDir,
                                       lcVersion="1.1", log=workDir+"log.txt")
# Replace null data cells with "99" for use later on
arcpy.env.extent=dataDir + "/TestExtent2.shp" ################################ <-- TEMPPPP
placeholder_code = 99
ffMap2 = arcpy.sa.Con(arcpy.sa.IsNull(ffMap1), placeholder_code, ffMap1)
# Make sure valid RAT
arcpy.management.CalculateStatistics(ffMap2, skip_existing=True)
arcpy.management.BuildRasterAttributeTable(ffMap2, overwrite=True)
ffMap2.save(resultDir + "/Floodplain10&99.tif")
# Make the new floodplain forest map 32 bit pixel type
arcpy.management.CopyRaster(resultDir + "/Floodplain10&99.tif", 
                            resultDir + "/Floodplain10&99_32.tif",
                            pixel_type="32_BIT_UNSIGNED",
                            nodata_value=0)

######################################### Calculate representation on floodplains forests
#########################################################################################
# List species to assess
arcpy.env.workspace = habMapDir
sppList = arcpy.ListRasters()[500:510]
arcpy.env.workspace=workDir
# Calculate representation
dfSpFF = ga.representation.Calculate(zone_file=resultDir + "/Floodplain10&99_32.tif", 
                                     zone_name="Floodplain", 
                                     zone_field="VALUE", habitat_maps=sppList,
                                     speciesDir=habMapDir,
                                     workDir=resultDir+"Percent_FloodplainForest",
                                     snap_raster=snap_raster)


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
winterTiffs = [x + ".tif" for x in winterSp]
wRichnessMap = ga.richness.ProcessRichness(spp=winterTiffs, groupName="Top_Winter",
                                           outLoc=resultDir, modelDir=habMapDir,
                                           season="Winter", interval_size=10,
                                           log=resultDir + "Top_Winter_Richness/log.txt",
                                           expand=False, CONUS_extent=conus_extent,
                                           snap_raster=snap_raster)
# Summer
summerTiffs = [x + ".tif" for x in summerSp]
sRichnessMap = ga.richness.ProcessRichness(spp=summerTiffs, groupName="Top_Summer",
                                           outLoc=resultDir, modelDir=habMapDir,
                                           season="Summer", interval_size=10,
                                           log=resultDir + "Top_Summer_Richness/log.txt",
                                           expand=False, CONUS_extent=conus_extent,
                                           snap_raster=snap_raster)

############################################# Calculate representation on protected areas
#########################################################################################
# Summarize management for top winter species
# Use field "gap_sts"?
dfWinterSp_PAD = ga.representation.Calculate(zone_file=PADUS_Man, 
                                             zone_name="Management_Winter", 
                                             zone_field="VALUE", habitat_maps=winterSp,
                                             speciesDir=habMapDir,
                                             workDir=resultDir+"Percent_PADUS_Winter",
                                             snap_raster=snap_raster)
# Summarize management for top summer species
dfSummerSp_PAD = ga.representation.Calculate(zone_file=PADUS_Man, 
                                             zone_name="Management_Summer", 
                                             zone_field="VALUE", habitat_maps=summerSp,
                                             speciesDir=habMapDir,
                                             workDir=resultDir+"Percent_PADUS_Summer",
                                             snap_raster=snap_raster)                                 

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




