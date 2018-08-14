# -*- coding: utf-8 -*-
"""
Created on Mon Jul 03 14:40:57 2017 by nmtarr

Description:  Builds pyramids for the results directory.
"""
execfile("T:/Scripts/AppendPaths27.py")
import arcpy, sys
sys.path.append('P:/Proj3/USGap/Analysis/SE_Woody_Wetlands')
import SEWWConfig as cr

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
