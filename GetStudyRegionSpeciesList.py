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

###################################################  List species in general study region
#########################################################################################
studyRegionList = gp.gaprange.SppInAOI(AOIShp = floodconfig.AOI_TEST,
                                       hucShp = floodconfig.hucs, 
                                       workDir = floodconfig.workDir,
                                       origin = [1], 
                                       season = [1, 3, 4],
                                       reproduction = [1, 2, 3],
                                       presence = [1, 2, 3])

df = pd.DataFrame(studyRegionList)
df.rename(columns={0:"strUC"}, inplace=True)
df["common_name"] = [gp.gapdb.NameCommon(x) for x in df.strUC]
df["scientific_name"] = [gp.gapdb.NameSci(x) for x in df.strUC]
df["subspecies_name"] = [gp.gapdb.NameSubspecies(x) for x in df.strUC]
df.to_csv(floodconfig.resultDir + "Study Region Species List.csv")