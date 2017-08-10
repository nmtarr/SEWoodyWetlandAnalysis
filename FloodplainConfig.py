'''
Config file for a floopdlain forest analysis.  Below are variables that are
more or less universal for the project.
'''
workDir = "T:/Floodplain_Forests_2016/"
dataDir = workDir + "Data/"
tempDir = workDir + "Temp/"
resultDir = workDir + "Results/"
habMapDir = "P:/Proj3/USGap/Vert/Model/Output/CONUS/Null123/"
seasonalhabMapDir = "P:/Proj3/USGap/Vert/Model/Output/CONUS/01/"
lcMapDir = "P:/Proj3/USGap/Vert/Model/data/LandCover"
lcMap = "P:/Proj3/USGap/Analysis/Data/lcv1vertmosai"
conus_extent = "P:/Proj3/USGap/Vert/Model/data/conus_ext_cnt"
snap_raster = "P:/Proj3/USGap/Vert/Model/data/snapgrid"
PADUS_Man = dataDir + "padus_man.tif"
PADUS_Own = dataDir + "padus_own.tif"
AOI = dataDir + "StudyRegion.shp"
AOI_TEST = dataDir + "/TestExtent2.shp"
habmapSuffix = "_CONUS_HabMap_2001v1.tif"
hucs = 'P:/Proj3/USGAP/Vert/Model/data/HucRng/Hucs.shp'
floodplainBinary = resultDir + "/Floodplain10&99.tif"
        
# List of floodplain forest map units.
floodMUs = [1402, 5602]

# Placeholder code to use for nulls in floodplain binary map.
placeholder_code = 99

# Species list derived by querying range database for native species in ecoregions
# that could have floodplain forests.                                  
studyRegionList = ['aMUSAx', 'aSOFRx', 'aTWAMx', 'bAMAVx', 'bAMCRx','bAMKEx', 
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