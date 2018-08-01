# -*- coding: utf-8 -*-
"""
Feb 2, 2017 by nmtarr

Code to run analyses on the importance of southeastern woody wetlands 
for wildlife
"""
import sys, pandas as pd, arcpy
sys.path.append('P:/Proj3/USGap/Scripts/SE_Woody_Wetlands')
execfile("T:/Scripts/AppendSysPaths27.py")
import FloodplainConfig as floodconfig
pd.set_option('display.width', 1000)
arcpy.CheckOutExtension("Spatial")
arcpy.env.overwriteOutput=True

#############################################  Mask the richness with the study region
######################################################################################
for group in floodconfig.richnessPathsCONUS:
    print group
    SE = arcpy.sa.ExtractByMask(arcpy.Raster(floodconfig.richnessPathsCONUS[group]),
                                floodconfig.AOI)
    SE.save(floodconfig.richnessPathsSE[group])
    
    
#############################################  Mask the richness with the study region
######################################################################################
for group in floodconfig.richnessPathsCONUS:
    print group
    MU = arcpy.sa.ExtractByMask(arcpy.Raster(floodconfig.richnessPathsCONUS[group]),
                                arcpy.Raster(floodconfig.floodplain))
    MU.save(floodconfig.richnessPathsFlood[group])