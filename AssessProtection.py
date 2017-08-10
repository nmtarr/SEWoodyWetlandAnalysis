# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 10:28:29 2017 by nmtarr

Description:
"""
############################################# Calculate representation on protected areas
#########################################################################################
# Summarize management for top winter species
# Use field "gap_sts"?
dfWinterSp_PAD = ga.habitat.PercentOverlay(zoneFile=PADUS_Man, 
                                           zoneName="Management_Winter", 
                                           zoneField="VALUE", 
                                           habMapList=winterSp,
                                           habDir=habMapDir,
                                           workDir=resultDir+"Percent_PADUS_Winter",
                                           snap=snap_raster,
                                           extent="zoneFile")
# Summarize management for top summer species
dfSummerSp_PAD = ga.habitat.PercentOverlay(zoneFile=PADUS_Man, 
                                           zoneName="Management_Summer", 
                                           zoneField="VALUE", 
                                           habMapList=summerSp,
                                           habDir=habMapDir,
                                           workDir=resultDir+"Percent_PADUS_Summer",
                                           snap=snap_raster,
                                           extent="zoneFile")                                 

################################################################### Calculate land owners
#########################################################################################
# Calculate ownership for top winter species
# Use field "own_name"?
dfWinterSp_PAD = ga.representation.Calculate(zone_file=PADUS_Own, 
                                             zone_name="Ownership_Winter", 
                                             zone_field="VALUE", habitat_maps=winterSp,
                                             speciesDir=habMapDir,
                                             workDir=resultDir+"Percent_PADUS_Winter",
                                             snap_raster=snap_raster)
# Calculate ownership for top summer species
dfSummerSp_PAD = ga.representation.Calculate(zone_file=PADUS_Own, 
                                             zone_name="Ownership_Summer", 
                                             zone_field="VALUE", habitat_maps=summerSp,
                                             speciesDir=habMapDir,
                                             workDir=resultDir+"Percent_PADUS_Summer",
                                             snap_raster=snap_raster)         