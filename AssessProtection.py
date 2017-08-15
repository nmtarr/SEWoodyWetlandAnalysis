# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 10:28:29 2017 by nmtarr

Description:  
"""
import sys, matplotlib.pyplot as plt
sys.path.append('T:/GAP/Data')
sys.path.append('T:/Scripts/GAPAnalysis')
sys.path.append('T:/Scripts/GAPProduction')
import gapconfig as config
sys.path.append('P:/Proj3/USGap/Scripts/Floodplain_Forests_2016')
import gapanalysis as ga
import gapproduction as gp
import FloodplainConfig as floodconfig
import pandas as pd
pd.set_option('display.width', 1000)

######
import arcpy
arcpy.ResetEnvironments()
arcpy.CheckOutExtension("Spatial")
arcpy.env.overwriteOutput=True
arcpy.env.extent = "MAXOF" 
arcpy.env.pyramid = 'PYRAMIDS'
arcpy.env.snapRaster = config.CONUS_extent
arcpy.env.rasterStatistics = "STATISTICS"
arcpy.env.cellSize = 30

##################################  How much of floodplain forest is protected?
###############################################################################
PAD = arcpy.Raster(floodconfig.PADUS_Man)
FloodBin = arcpy.Raster(floodconfig.resultDir + "Floodplain.tif")
'''
# Overlay the PAD layer and binary floodplain layer
floodPAD = PAD * (FloodBin - 9)
floodPAD.save(floodconfig.resultDir + "FloodplainPAD.tif")
'''
# Make a pie chart of protection
floodPADRAT = ga.misc.RATtoDataFrame(floodconfig.resultDir + "FloodplainPAD.tif")
ax = floodPADRAT.plot(y="cell_count", kind='Pie', figsize=(4,4), autopct='%.2f',
                 legend=False,# title="Protection of Floodplain Systems by GAP Status",
                 colors = ["#009933", "#cccc00", "#999999", "#e6e6e6"])
ax.set_ylabel("%")
fig = plt.gcf()
fig.savefig(floodconfig.resultDir + "Flooplain protection.png", dpi=600,
            bbox_inches="tight")

###############################################  Protection of species' habitat
###############################################################################
# Function to return protection status of a species.
def getProtection(strUC, season):
    '''
    (string, string) -> dictionary
    
    Description:
    A function that returns the amount of a species' habitat that is in status
    1, 2, 3, and 4 lands by season.
    
    Arguments:
    strUC -- Species code (e.g., "mVASHx")
    season -- Season to summarize on (i.e., summer, winter, or all year)
    '''
    seasonDict = {"summer":(1,3), "winter":(2,3), "all year":(3,3)}
    conString = """DRIVER=SQL Server Native Client 10.0;
                        SERVER=CHUCK\SQL2014;
                        UID=;
                        PWD=;
                        TRUSTED_CONNECTION=Yes;
                        DATABASE=GAP_AnalyticDB;"""
    anCur, anCon = gp.gapdb.ConnectToDB(conString)
    
    sql = """
    --Retrieve species boundary info for one species.
    WITH SpPAD AS (
    SELECT lu_boundary_species.boundary, lu_boundary_species.count, 
           lu_boundary_species.season, lu_boundary_species.species_cd, 
           lu_boundary.value, lu_boundary.padus1_4, padus1_4.revoid, 
           padus1_4.gap_sts
    FROM lu_boundary_species INNER JOIN lu_boundary ON lu_boundary.value = lu_boundary_species.boundary
       					        INNER JOIN padus1_4 ON lu_boundary.padus1_4 = padus1_4.revoid
    WHERE (lu_boundary_species.species_cd = '{0}' and (lu_boundary_species.season = {1} or lu_boundary_species.season = {2})))
    
    
    --Group by count
    SELECT  s.gap_sts, sum(s.count) AS cells
    FROM SpPAD AS s
    GROUP BY s.gap_sts
    """.format(sp, str(seasonDict[season][0]), str(seasonDict[season][1]))
    
    qryDF = pd.read_sql(sql, anCon).set_index("gap_sts")
    
    del anCur
    anCon.close()
    
    return qryDF


# Get list of species to query.
summerDF = pd.read_csv(floodconfig.summerTopSpList)
summerSp = list(summerDF.strUC)
winterDF = pd.read_csv(floodconfig.winterTopSpList)
winterSp = list(winterDF.strUC)

# Empty dataframes to fill out.
summer0 = pd.DataFrame(index=summerSp, 
                       columns=["status_1", "status_2", "status_3", "status_4"])
winter0 = pd.DataFrame(index=winterSp, 
                       columns=["status_1", "status_2", "status_3", "status_4"])

#### Fill out summer DF
print("\n*** SUMMER ***")
for sp in summerSp:
    prot = getProtection(sp, season="summer")
    summer0.loc[sp, 'status_1'] = int(prot.loc["1"])
    summer0.loc[sp, 'status_2'] = int(prot.loc["2"])
    summer0.loc[sp, 'status_3'] = int(prot.loc["3"])
    summer0.loc[sp, 'status_4'] = int(prot.loc["4"])
summer0["total_cells"] = summer0.status_1 + summer0.status_2 + summer0.status_3 + summer0.status_4
summer0['status_1%'] = 100.*summer0.status_1/summer0.total_cells
summer0['status_2%'] = 100.*summer0.status_2/summer0.total_cells
summer0['status_3%'] = 100.*summer0.status_3/summer0.total_cells
summer0['status_4%'] = 100.*summer0.status_4/summer0.total_cells

# Summer protection description
summer1 = summer0.apply(pd.to_numeric)
summer1.to_csv(floodconfig.resultDir + "Summer protection.csv")
summerProtDesc = summer1.describe()
print(summerProtDesc)
summerProtDesc.to_csv(floodconfig.resultDir + "Summer protection descriptive stats.csv")
    
# Graph protection
dropCols = ["status_1", "status_2", "status_3", "status_4", "total_cells"]
# Summer
summer2 = summer1.drop(dropCols, axis=1)
summer2.rename(columns={"status_1%":"1", "status_2%":"2","status_3%":"3",
                        "status_4%":"4",}, inplace=True)
sumAx = summer2.plot(kind="box", title="Summer", yticks=range(0,100,10),
                     figsize=(5,4))
sumAx.set_ylabel("Percent of Species' Total Habitat Area")
sumAx.set_xlabel("GAP Protection Status")
fig = plt.gcf()
fig.savefig(floodconfig.resultDir + "Protection Boxplot Summer.png", dpi=600,
            bbox_inches="tight")

#### Fill out winter DF
print("\n*** WINTER ***")
for sp in winterSp:
    prot = getProtection(sp, season="winter")
    winter0.loc[sp, 'status_1'] = int(prot.loc["1"])
    winter0.loc[sp, 'status_2'] = int(prot.loc["2"])
    winter0.loc[sp, 'status_3'] = int(prot.loc["3"])
    winter0.loc[sp, 'status_4'] = int(prot.loc["4"])
winter0["total_cells"] = winter0.status_1 + winter0.status_2 + winter0.status_3 + winter0.status_4
winter0['status_1%'] = 100.*winter0.status_1/winter0.total_cells
winter0['status_2%'] = 100.*winter0.status_2/winter0.total_cells
winter0['status_3%'] = 100.*winter0.status_3/winter0.total_cells
winter0['status_4%'] = 100.*winter0.status_4/winter0.total_cells

# Winter protection description
winter1 = winter0.apply(pd.to_numeric)
winter1.to_csv(floodconfig.resultDir + "Winter protection.csv")
winterProtDesc = winter1.describe()
print(winterProtDesc)
winterProtDesc.to_csv(floodconfig.resultDir + "Winter protection descriptive stats.csv")

# Winter
winter2 = winter1.drop(dropCols, axis=1)
winter2.rename(columns={"status_1%":"1", "status_2%":"2","status_3%":"3",
                        "status_4%":"4",}, inplace=True)
wintAx = winter2.plot(kind="box", title="Winter", yticks=range(0,100,10),
                      figsize=(5,4))
wintAx.set_ylabel("Percent of Species' Total Habitat Area")
wintAx.set_xlabel("GAP Protection Status")
fig = plt.gcf()
fig.savefig(floodconfig.resultDir + "Protection Boxplot Winter.png", dpi=600,
            bbox_inches="tight")