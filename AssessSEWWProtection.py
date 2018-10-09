# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 10:28:29 2017 by nmtarr

Description:  Produces results related to the protection of ecological systems
and species.  Note that some processes (lines 39-45) take up to an hour to run
and could be skipped if the floodPAD layer already exists. Also note that this
code queries the Analytic Databse.

This code may have some reduncancy in it that could be cleaned up, and it may
need some more documentation.
"""
import sys, matplotlib.pyplot as plt
sys.path.append('P:/Proj3/USGap/Scripts/SE_Woody_Wetlands')
execfile("T:/Scripts/AppendPaths27.py")
execfile("T:/Scripts/AppendGAPAnalysis.py")
import gapanalysis as ga
import gapproduction as gp
import SEWWConfig as floodconfig
import gapconfig as config
import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 10)
pd.set_option('display.width', 1000)

###### Geoprocessing environment settings
import arcpy
arcpy.ResetEnvironments()
arcpy.CheckOutExtension("Spatial")
arcpy.env.overwriteOutput=True
arcpy.env.extent = "MAXOF" 
arcpy.env.pyramid = 'PYRAMIDS'
arcpy.env.snapRaster = config.CONUS_extent
arcpy.env.rasterStatistics = "STATISTICS"
arcpy.env.cellSize = 30

###############################################  How much of SEWW is protected?
###############################################################################
'''  # Commented out to keep graph-making and slow data producing separate.
PAD = arcpy.Raster(floodconfig.PADUS_Man)
FloodBin = arcpy.Raster(floodconfig.resultDir + "SEWW.tif")

# Overlay the PAD layer and binary SEWW layer
floodPAD = PAD * (FloodBin - 9)
floodPAD.save(floodconfig.resultDir + "SEWWPAD.tif")
'''
# Make a pie chart of protection
floodPADRAT = ga.misc.RATtoDataFrame(floodconfig.resultDir + "SEWWPAD.tif")
floodPADRAT.index = ["Status " + str(j) for j in floodPADRAT.index]
ax = floodPADRAT.plot(y="cell_count", kind='Pie', figsize=(5,5), autopct='%.0f',
                 legend=False,                  
                 colors = ["#009933", "#cccc00", "#999999", "#e6e6e6"])
ax.set_ylabel("")
fig = plt.gcf()
fig.savefig(floodconfig.resultDir + "SEWW protection.png", dpi=600,
            bbox_inches="tight")