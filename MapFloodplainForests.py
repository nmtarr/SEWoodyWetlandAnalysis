# -*- coding: utf-8 -*-
"""
Feb 2, 2017 by nmtarr

Code to run analyses on the importance of floodplain forests for wildlife
"""
import sys, arcpy
sys.path.append('T:/Scripts/GAPAnalysis')
sys.path.append('T:/Gap/Data')
sys.path.append('P:/Proj3/USGap/Scripts/Floodplain_Forests_2016')
import gapanalysis as ga
import FloodplainConfig as floodconfig
import pandas as pd

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
# Get list of systems to use from Ecological systems of interest.csv
df = pd.read_csv(floodconfig.floodplainSystemCSV)
df1 = df[df["include"] == 1]
floodsystems = list(df1.map_code)

# Reclass land cover to get a map of floodplain forests.
print("Reclassifing lcv1")
ffMap1 = ga.landcover.ReclassLandCover(MUlist=floodsystems, 
                                       reclassTo=10, keyword="Floodplain",
                                       workDir=floodconfig.resultDir,
                                       lcPath=floodconfig.lcMap,
                                       lcVersion="1.1")
# Replace nulls with placeholder code
print("Replacing null values")
arcpy.env.extent = floodconfig.conus_extent
ffMap2 = arcpy.sa.Con(arcpy.sa.IsNull(ffMap1), 
                      floodconfig.placeholder_code, ffMap1)

# Make sure valid RAT
print("Checking or building statistics and RAT")
arcpy.management.CalculateStatistics(ffMap2, skip_existing=True)

# Save
print("Saving")
ffMap2.save(floodconfig.floodplainBinary)
arcpy.management.BuildRasterAttributeTable(floodconfig.floodplainBinary, 
                                           overwrite=True)