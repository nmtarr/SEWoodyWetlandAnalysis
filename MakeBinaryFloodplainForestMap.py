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

######################################################################## Set environments
#########################################################################################
arcpy.ResetEnvironments()
arcpy.CheckOutExtension("Spatial")
arcpy.env.snapRaster=floodconfig.snap_raster
arcpy.env.overwriteOutput=True
arcpy.env.scratchWorkspace=floodconfig.tempDir
arcpy.env.workspace=floodconfig.workDir
arcpy.env.rasterStatistics="STATISTICS"
arcpy.env.extent="MAXOF"


################################################################## Map floodplain forests
#########################################################################################
# Reclass land cover to get a map of floodplain forests.
print("Reclassifing lcv1")
ffMap1 = ga.landcover.ReclassLandCover(MUlist=floodconfig.floodMUs, 
                                       reclassTo=10, keyword="Floodplain",
                                       workDir=floodconfig.resultDir,
                                       lcPath=floodconfig.lcMap,
                                       lcVersion="1.1", 
                                       log=floodconfig.workDir+"log.txt")
# Replace nulls with placeholder code
print("Replacing null values")
arcpy.env.extent = floodconfig.AOI_TEST
ffMap2 = arcpy.sa.Con(arcpy.sa.IsNull(ffMap1), 
                      floodconfig.placeholder_code, ffMap1)

# Make sure valid RAT
print("Checking or building statistics and RAT")
arcpy.management.CalculateStatistics(ffMap2, skip_existing=True)
arcpy.management.BuildRasterAttributeTable(ffMap2, overwrite=True)

# Save
print("Saving")
ffMap2.save(floodconfig.resultDir + "/Floodplain10&99.tif")