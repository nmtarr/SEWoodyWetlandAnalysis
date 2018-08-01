# -*- coding: utf-8 -*-
"""
Feb 2, 2017 by nmtarr

Code to whittle down the list of species to apply the slow geoprocessing to.
The only species that need to be assessed are ones that are in the general study
region and are associated with one of the ecological systems of interest in the 
database OR are handmodeled.  This code seeks to build that list.
"""
import sys, pandas as pd, pickle
sys.path.append('P:/Proj3/USGap/Scripts/SE_Woody_Wetlands')
execfile("T:/Scripts/AppendSysPaths27.py")
execfile("T:/Scripts/AppendGAPAnalysis.py")
import gapproduction as gp
import SEWWConfig as floodconfig

###################################################  List species in general study region
#########################################################################################
studyRegionList = gp.gaprange.SppInAOI(AOIShp = floodconfig.AOI,
                                       hucShp = floodconfig.hucs, 
                                       workDir = floodconfig.workDir,
                                       origin = [1], 
                                       season = [1, 3, 4],
                                       reproduction = [1, 2, 3],
                                       presence = [1, 2, 3])

#######################################################  List species that don't use SEWW
#########################################################################################
# Get list of systems to use from Ecological systems of interest.csv
df = pd.read_csv(floodconfig.SEWWSystemCSV)
df1 = df[df["include"] == 1]
floodsystems = set(list(df1.map_code))

# Find species that use a SEWW map unit.
floodSp = []
for sp in studyRegionList:
    prim, aux = gp.gapmodeling.SpEcoSystems(spCode=sp, season='all', contiguousOnly=True)
    primaux = set(gp.gapdb.MUNamesToCodes(prim)) | set(gp.gapdb.MUCodesToNames(aux))
    if len(primaux & floodsystems) > 0:
        floodSp.append(sp)
    else:
        print(sp + " doesn't use floodplains")
floodSp = set(floodSp)

#################################################################  List handmodel species
#########################################################################################       
handmodels = set([s[:6] for s in gp.gapmodeling.HandModels()])

############################################################  Combine lists/sets and save
#########################################################################################
studyRegionList = set(studyRegionList)
slimList = (handmodels & studyRegionList) | (floodSp & studyRegionList)

# Save
pickle.dump(list(slimList), open(floodconfig.resultDir + "studyRegionList.pkl", "w"))
df = pd.DataFrame(list(slimList))
df.rename(columns={0:"strUC"}, inplace=True)
df["common_name"] = [gp.gapdb.NameCommon(x) for x in df.strUC]
df["scientific_name"] = [gp.gapdb.NameSci(x) for x in df.strUC]
df["subspecies_name"] = [gp.gapdb.NameSubspecies(x) for x in df.strUC]
df.to_csv(floodconfig.resultDir + "Study Region Species List.csv")
