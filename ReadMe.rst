=================================
Southeast Woody Wetland Analysis Code
=================================

PURPOSE

The southeastern U.S. contains woody wetland plant communities that are unique and subject to threats related to human development and climate change.  This analysis utilizes GAP data to provide insights about which species are at high risks of exposure to loss of or changes in these wetlands, where those species occur, and how much of their habitat is protected.

INPUTS & OUTPUTS

see SEWW Inputs and Outputs.csv

Requires access to 
GAP habitat maps (https://www.sciencebase.gov/catalog/item/527d0a83e4b0850ea0518326);
GAP WHR Database;
GAP Species Database;
GAP analytic database;
2001 GAP Land Cover (https://www.sciencebase.gov/catalog/item/5540e2d7e4b0a658d79395db);
Rasterized PAD-US data.

CONSTRAINTS

see LICENSE.txt

DEPENDENCIES

see Requirements.txt and environment.yml

Python 2.7
This repository includes an environment file (environment.pyl) that can be used to load most required packages with conda.  Several variables (paths to files and file names to use) are saved in a config fil named SEWWConfig.py.  In order to run the scripts, those would need to be updated to the users computing environment.

Additional code that is not available through pip or conda is needed as well:
arcpy 10.4.1;
GAPAnalysis >=0.3 available at https://github.com/nmtarr/GAPAnalysis; 
GAPProduction >=1.6 available at https://github.com/nmtarr/GAPProduction


CODE

https://github.com/nmtarr/SEWoodyWetlandAnalysis

These scripts can be run in this order to perform an analysis of GAP habitat maps, range data, PAD, and GAP Land Cover.  Scripts with the same numbers can be run at the same times.  Alternatively, see "SEWW Assessment Report.ipynb" for a linear sequence.

The "archive" folder contains some scripts from early in the workflow development.

1. DevelopSEWW-MUList.py

2. MapSEWW.py

3. GetStudyRegionSpeciesList.py

4. MaskSpeciesRichness.py

4. CalculatePercentHabitatInSEWW.py

5. CompareRichness.py

5. SummarizeOverlap.py

6. MapSEWWSpeciesRichness.py

6. MakeSEWWPAD.py

7. AssessProtection.py

8. BuildPyramids.py
