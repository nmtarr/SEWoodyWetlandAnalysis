'''
Config file for a southeastern woody wetland analysis.  Below are variables 
that are more or less universal for the project.

Figure size limits are 5.28 x 8.125
Figure font helvetica or sans serif font, less than 10 pt.

Table width <= 5.25 inches wide (8.3 in landscape), 9pt Times New Roman font.
'''
workDir = "T:/SE_Woody_Wetlands/"
dataDir = workDir + "Data/"
tempDir = workDir + "Temp/"
intermDir = workDir + "Intermediate/"
resultDir = workDir + "Results/"
habMapDir = "P:/Proj3/USGap/Vert/Model/Output/CONUS/Null123/"
seasonalhabMapDir = "P:/Proj3/USGap/Vert/Model/Output/CONUS/01/"
lcMapDir = "P:/Proj3/USGap/Vert/Model/data/LandCover"
lcMap = "P:/Proj3/USGap/Analysis/Data/lcv1vertmosai"
conus_extent = "P:/Proj3/USGap/Vert/Model/data/conus_ext_cnt"
snap_raster = "P:/Proj3/USGap/Vert/Model/data/snapgrid"
PADUS_Man = "P:/Proj3/USGap/Analysis/Data/PAD14s2001.tif"
AOI = dataDir + "StudyRegion.shp"
AOI_TEST = dataDir + "/TestExtent2.shp"
habmapSuffix = "_CONUS_HabMap_2001v1.tif"
hucs = 'P:/Proj3/USGAP/Vert/Model/data/HucRng/Hucs.shp'
overlayTable = resultDir + "Percent_SEWW/Percent_in_SEWW_Master.csv"
summerRichness = resultDir + "Top_Summer/Top_Summer_Richness.tif"
winterRichness = resultDir + "Top_Winter/Top_Winter_Richness.tif"

# List of SEWW land cover map units.
SEWWSystemCSV = dataDir + "/Ecological systems of interest.csv"

# Placeholder code to use for nulls in SEWW binary map.
placeholder_code = 99

# Name of binary SEWW layer (without NoDatas)
SEWWBinary = resultDir + "SEWWs10&{0}.tif".format(placeholder_code)

# Name of SEWW layer (with NoDatas)
SEWW = resultDir + "SEWW.tif"

# Species list derived by querying range database for native species in ecoregions
# that could have SEWWs. 
import pickle
studyRegionList = pickle.load(open(resultDir + "studyRegionList.pkl"))
testExtent2List = ['aMUSAx', 'aSOFRx', 'aTWAMx', 'bAMAVx', 'bAMCRx','bAMKEx', 
'bAMREx', 'bANHIx', 'bBEKIx', 'bBHCOx', 'bBRTHx', 'bBWHAx', 'bCAEGx', 'bDEJUx',
'bFISPx', 'bFOTEx', 'bGRSCx', 'bHERGx', 'bLALOx', 'bLBDOx', 'bLEBIx', 'bLESAx',
'bLOSHx', 'bNOHAx', 'bNOPIx', 'bNSHOx', 'bPAWAx', 'bPIWAx', 'bPUFIx', 'bRBGUx',
'bRECRx', 'bRUDUx', 'bRWBLx', 'bSEPLx', 'bSSHAx', 'bTUVUx', 'bWITUx', 'bWOTHx',
'bYRWAx', 'mREFOx', 'rBLSSx', 'rBRWAx', 'rAMALx', 'rBHSKx', 'rEARAx', 'rEARIx',
'rEBTUx', 'rEDBRx', 'rEFLIx', 'rEGLIx', 'rEHNSx', 'rEMDTx', 'rEMSTx', 'rEWSNx',
'rGCRSx', 'rGRANx', 'rLBSKx', 'bDCCOx', 'bDOWOx', 'bGREGx', 'bGRHEx', 'mMARAx',
'rSTMTx', 'aBRFRx', 'aCRFRx', 'aDWWAx', 'aLGFRx', 'aMBSAx', 'aMLSAx', 'bYERAx',
'bWEVIx', 'aACSSx', 'bLEOWx', 'bRCWOx', 'bCOGRx', 'bNOMOx', 'bNRWSx', 'bGHOWx',
'bHOFIx', 'bMODOx', 'bREVIx', 'bRHWOx', 'bRTHAx', 'bROPIx', 'bSAVSx', 'bSORAx',
'bNOBOx', 'bAMWOx', 'bKILLx', 'bYBCUx', 'bHAWOx', 'bBADOx', 'mNAROx', 'bBUFFx',
'bHOWRx', 'bSEOWx', 'bPEFAx', 'bHESPx', 'bPBGRx', 'rCFLSx', 'rCHTUx', 'rCKINx',
'rCOACx', 'rCOGAx', 'mLTWEx', 'mMAORx', 'mNALSx', 'mRACCx', 'mRBEBx', 'mSHBAx',
'mSEBAx', 'mSEMYx', 'mSFSQx', 'mSNMOx', 'mSOTSx', 'mSPSHx', 'rCOPPx', 'rCOTTx',
'rDEBRx', 'mVIOPx', 'mWFDEx', 'mWOVOx', 'mWTDEx', 'bWIWRx', 'bWODUx', 'bWPWIx',
'bWTSPx', 'bYBCHx', 'bYBSAx', 'bYCNHx', 'bYTVIx', 'bYTWAx', 'mABBEx', 'mAMBEx',
'mAMMIx', 'mBBBAx', 'mBOBCx', 'mCMMUx', 'mCODEx', 'mCOYOx', 'mEACOx', 'mEAMOx',
'mEAPIx', 'mEBSQx', 'mEFSQx', 'mEHMOx', 'mERBAx', 'mEVBAx', 'mGOMOx', 'mGRFOx',
'bSCTAx', 'bSEWRx', 'bSNGOx', 'bSOSPx', 'bSUTAx', 'bSWSPx', 'bSWWAx', 'bTRESx',
'bTUTIx', 'mHCRAx', 'bWBNUx', 'bWESAx', 'bWEWAx', 'bWHSWx', 'bWISNx', 'bNSWOx',
'bOCWAx', 'bORORx', 'bOSPRx', 'bOVENx', 'bCACHx', 'bPISIx', 'bPIWOx', 'bPRAWx',
'bPROWx', 'bPUMAx', 'bPUSAx', 'bRBNUx', 'bRBWOx', 'bRCKIx', 'bREDHx', 'bRNDUx',
'bROYTx', 'bRSHAx', 'bRTHUx', 'bRUBLx', 'bHOWAx', 'bINBUx', 'bKEWAx', 'bKIRAx',
'bLBBGx', 'bLBCUx', 'bLBHEx', 'bLESCx', 'bLEYEx', 'bLOWAx', 'bMAGOx', 'bMALLx',
'bSANDx', 'bNOCAx', 'bNOFLx', 'bNOPAx', 'bEABLx', 'bEAKIx', 'bEAMEx', 'bEAPHx',
'bEASOx', 'bEATOx', 'bEAWPx', 'bEVGRx', 'bFICRx', 'bFOSPx', 'bGADWx', 'bGBHEx',
'bGCFLx', 'bGCKIx', 'bGRCAx', 'bGRSPx', 'bGRYEx', 'bGWTEx', 'bHETHx', 'bBTNWx',
'bCANGx', 'bCANVx', 'bCARWx', 'bHOGRx', 'bHOLAx', 'bHOMEx', 'bCEDWx', 'bCHSPx',
'bCHSWx', 'bCOHAx', 'bCOMOx', 'bCONIx', 'bCOYEx', 'bCWWIx', 'bDUNLx', 'bAMBIx',
'bAMCOx', 'bAMGOx', 'bAMPIx', 'bAMROx', 'bAMWIx', 'bBACSx', 'bBAEAx', 'bBANOx',
'bBARSx', 'bBAWWx', 'bBBPLx', 'bBCNHx', 'bBGGNx', 'bBHNUx', 'bBHVIx', 'bBLGRx',
'bBLJAx', 'bBLRAx', 'bBLVUx', 'bBOGUx', 'aAMBUx', 'aBATRx', 'bBRCRx', 'aCGTRx',
'aCHDSx', 'aDWSAx', 'aEANEx', 'aEASPx', 'aENMTx', 'aFOTOx', 'aFTSAx', 'aGOFRx',
'aGRFRx', 'aGRSIx', 'aGRTRx', 'aMASAx', 'aNRWAx', 'aOATOx', 'aOCFRx', 'aPBTRx',
'aPIFRx', 'aPWTRx', 'aSCFRx', 'aSLFRx', 'aSODSx', 'aSOTOx', 'aSPOSx', 'aSPPEx',
'aSQTRx', 'aSTLSx', 'aTLSAx', 'aWSSSx', 'bABDUx', 'bACFLx', 'rMGLIx', 'rMILKx',
'rNARAx', 'rPATUx', 'rPBWAx', 'rROEAx', 'rSNTUx', 'rSPTUx', 'rSGLIx', 'rPOSLx',
'mNOMYx', 'rSCARx', 'rYBKIx', 'rSOWAx', 'rRECOx', 'rRBSNx', 'rSLRAx', 'rSFLSx',
'rROGRx', 'rPRATx', 'rSESNx', 'rSMEAx', 'rTIRAx', 'rRBMUx', 'rRASNx', 'rRNSNx',
'rPWLIx', 'rSHNSx', 'aLESIx', 'rRICOx']

# studyRegionList converted to null123 raster names.
null123List = [i[0] + i[1:5].upper() + i[5:] + habmapSuffix for i in studyRegionList]

# Location of lists of species exceeding the % habitat overlay threshold
winterTopSpList = resultDir + "TopWinterSpecies.csv"
summerTopSpList = resultDir + "TopSummerSpecies.csv"
TopSpList = resultDir + "TopSpecies.csv"

# Paths to richness rasters
richnessPathsCONUS = {
"amphibian": dataDir + "Amphibian_Richness.tif",
"bird_summer": dataDir + "Bird_Summer_Richness.tif",
"bird_winter": dataDir + "Bird_Winter_Richness.tif",
"reptile": dataDir + "Reptile_Richness.tif",
"mammal": dataDir + "Mammal_Richness.tif",
"all_taxa": dataDir + "All_Richness.tif"}

richnessPathsSE = {
"amphibian": resultDir + "Amphibian_Richness_SE.tif",
"bird_summer": resultDir + "Bird_Summer_Richness_SE.tif",
"bird_winter": resultDir + "Bird_Winter_Richness_SE.tif",
"reptile": resultDir + "Reptile_Richness_SE.tif",
"mammal": resultDir + "Mammal_Richness_SE.tif",
"all_taxa": resultDir + "All_Richness_SE.tif"}    

richnessPathsFlood = {
"amphibian": resultDir + "Amphibian_Richness_Flood.tif",
"bird_summer": resultDir + "Bird_Summer_Richness_Flood.tif",
"bird_winter": resultDir + "Bird_Winter_Richness_Flood.tif",
"reptile": resultDir + "Reptile_Richness_Flood.tif",
"mammal": resultDir + "Mammal_Richness_Flood.tif",
"all_taxa": resultDir + "All_Richness_Flood.tif"}    