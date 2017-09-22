# -*- coding: utf-8 -*-
"""
Created on Mon Jul 03 14:40:57 2017 by nmtarr

Description:  Builds pyramids for the results directory.
"""
import arcpy, sys
sys.path.append('P:/Proj3/USGap/Analysis/Floodplain_Forests_2016')
import FloodplainConfig as cr

arcpy.env.workspace = cr.resultDir
arcpy.management.BuildPyramidsandStatistics(cr.resultDir,
                                            skip_existing=True, 
                                            include_subdirectories="NONE",
                                            build_pyramids="BUILD_PYRAMIDS",
                                            calculate_statistics="NONE")
arcpy.management.BuildPyramidsandStatistics(cr.tempDir,
                                            skip_existing=True, 
                                            include_subdirectories="NONE",
                                            build_pyramids="BUILD_PYRAMIDS",
                                            calculate_statistics="NONE")
