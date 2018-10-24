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

#################################### How much of each SEWW system is protected?
###############################################################################
def getEcoSysProtection(ecoSys):
    '''
    (string, list) -> pandas DataFrame
    
    Description:
    A function that returns the percentage of an ecological system
        that is in the GAP PAD statuses of interest.
    
    Argument:
    ecoSys -- The name of the ecological system that you are interested in.
    '''
    blank = pd.DataFrame(index = ["1","2","3","4", "1234"], 
                         columns=["cells", "percent"])
    try:
        # Connect to analytic database
        anCur, anCon = gp.gapdb.ConnectAnalyticDB()
        
        sql = """
        --Retrieve ecological system boundary info for one system.
        WITH ESPAD AS (
        SELECT lu_boundary_gap_landfire.boundary, lu_boundary_gap_landfire.count,
               lu_boundary_gap_landfire.gap_landfire, lu_boundary.value, lu_boundary.padus1_4, 
               padus1_4.revoid, padus1_4.gap_sts
        FROM lu_boundary_gap_landfire 
        INNER JOIN lu_boundary ON lu_boundary.value = lu_boundary_gap_landfire.boundary
        LEFT JOIN padus1_4 ON lu_boundary.padus1_4 = padus1_4.revoid),
        
        --Retrieve ecological system name and code
        ECOSYS AS (
        SELECT g.ecosys_lu, g.value
        FROM gap_landfire as g
        WHERE g.ecosys_lu = '{0}')
        
        --Group records from joined data views by count
        SELECT ESPAD.gap_sts, sum(ESPAD.count) AS cells
        FROM ECOSYS INNER JOIN ESPAD ON ECOSYS.value = ESPAD.gap_landfire
        GROUP BY ESPAD.gap_sts
        """.format(ecoSys)
        
        qryDF = pd.read_sql(sql, anCon).set_index("gap_sts")
        qryDF.loc["1234", "cells"] = sum(qryDF.cells)
        qryDF["percent"] = [100*(qryDF.loc[i, "cells"]/qryDF.loc["1234", "cells"]) for i in qryDF.index]
        
        del anCur
        anCon.close()
        
        for x in qryDF.index:
            blank.loc[x, "cells"] = qryDF.loc[x, "cells"]
            blank.loc[x, "percent"] = qryDF.loc[x, "percent"]
            blank.fillna(0, inplace=True)
        return blank
    except Exception as e:
        print(e)

# Print out a table of ecol system and percent in protection.
floodSysDF = pd.read_csv(floodconfig.SEWWSystemCSV)
floodSysDF = floodSysDF[floodSysDF.include == 1]
floodSysDF.drop(["include"], inplace=True, axis=1)
floodSysDF["protected1&2(%)"] = [sum(getEcoSysProtection(i).iloc[:2].percent) for i in floodSysDF.system_name]
floodSysDF.to_csv(floodconfig.resultDir + "EcolSysProtection.csv")
floodSysDF.drop(["Unnamed: 0", "map_code", "yes Anne", "yesAlexa", "past"],
                inplace=True, axis=1)
floodSysDF.set_index(["system_name"], inplace=True)
floodSysDF.index.name = "Ecological System"
floodSysDF.rename({"protected1&2(%)": "Status 1 or 2 protection (%)"},
                   inplace=True, axis=1)
print(floodSysDF.round(2))

# Box plot of protection
ax = floodSysDF.plot(kind='box')
print("\n\nFigure 7. Boxplot of percentages protected for SEWW ecological systems.")