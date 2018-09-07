=================================
Southeast Woody Wetland Analysis Code
=================================
The "archive" folder contains some scripts from early in the workflow development.

PURPOSE



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


DEPENDENCIES

see Requirements.txt and environment.yml

Python 2.7
This repository includes an environment file (environment.pyl) that can be used to load most required packages with conda.  Several variables (paths to files and file names to use) are saved in a config fil named SEWWConfig.py.  In order to run the scripts, those would need to be updated to the users computing environment.

Additional code that is not available through pip or conda is needed as well:
arcpy 10.4.1;
GAPAnalysis >=0.3 available at https://github.com/nmtarr/GAPAnalysis; 
GAPProduction >=1.5.1 available at https://github.com/nmtarr/GAPProduction


CODE

https://github.com/nmtarr/SEWoodyWetlandAnalysis

These scripts can be run in this order to perform an analysis of GAP habitat maps, range data, PAD, and GAP Land Cover.  Scripts with the same numbers can be run at the same times.  Alternatively, see "Run Analysis.ipynb" for a linear sequence.

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


TESTS

see Tests.ipynb?


PROVENANCE

?

CITATIONS

Aycrigg, J.L., Davidson, A., Svancara, L.K., Gergely, K.J., McKerrow, A., and J.M. Scott. 2013. Representation of ecological systems within the protected areas network of the continental United States. PLoS ONE 8:e54689.

Aycrigg, J.L., Tricker, J., Belote, R.T., Dietz, M.S., Duarte, L., and G.H. Aplet. 2016. The next 50 years: opportunities for diversifying the ecological representation of the National Wilderness Preservation System within the contiguous United States. Journal of Forestry 114: 396-404.

Batzer, D.P., Day, F., and S.W. Golladay. 2012. Southeastern Swamp Complexes. 2012. Pp. 203-215, In D.P. Batzer and A.H. Baldwin (Eds.). Wetland Habitats of North America: Ecology and conservation concerns. The University of California Press Berkeley and Los Angeles, USA. 408 pp. 

Connor, W.H., Doyle, T.W., and Krauss, K.W. 2007a. Preface. Pp. xi-xiv, In W.H. Connor, T.W. Doyle and K.W. Krauss (Eds.). Ecology of Tidal Freshwater Forested Wetlands of the Southeastern United States. Springer Dordrecht, The Netherlands. 505 pp.

Connor, W.H., Krauss, K.W., and Doyle, T.W. 2007b. Ecology of tidal freshwater forests in coastal deltaic Louisiana and northeastern South Carolina. Pp. 223-253, In W.H. Connor, T.W. Doyle and K.W. Krauss (Eds.). Ecology of Tidal Freshwater Forested Wetlands of the Southeastern United States. Springer Dordrecht, The Netherlands. 505 pp.

Day, R.H., Williams, T.M., and Swarzenski, C.M. 2007. Hydrology of tidal freshwater forested wetlands of the southeastern United States. Pp. 29-63, In W.H. Connor, T.W. Doyle and K.W. Krauss (Eds.). Ecology of Tidal Freshwater Forested Wetlands of the Southeastern United States. Springer Dordrecht, The Netherlands. 505 pp.

Doyle, T.W., O�Neil, C.P., Melder, M.P.V., From, A.S., and Palta, M.M. 2007. Tidal freshwater swamps of the southeastern United States: Effects of land use, hurricanes, sea-level rise, and climate change. Pp. 1-28, In W.H. Connor, T.W. Doyle and K.W. Krauss (Eds.). Ecology of Tidal Freshwater Forested Wetlands of the Southeastern United States. Springer Dordrecht, The Netherlands. 505 pp.

Evans JM, Fletcher, Jr. RJ, Alavalapati JRR et al.2013 Forestry Bioenergy in the Southeast United States: Implications for Wildlife Habitat and Biodiversity. National Wildlife Federation, Merrifield, VA.

Faulkner, S.P., Chambers, J.L., Conner, W.H., Keim, R.F., Day, J.W., Gardiner, E.S., Hughes, M.S., King, S.L., McLeod, K.W., Miller, C.A., Nyman, J.A., and Shaffer, G.P. 2007. Conservation and use of coastal wetland forests in Louisiana Pp. 447-460 In W.H. Connor, T.W. Doyle and K.W. Krauss (Eds.). Ecology of Tidal Freshwater Forested Wetlands of the Southeastern United States. Springer Dordrecht, The Netherlands. 505 pp.

Jenkins, C.N., Van Houtan, K.S., Pimm, S.L., and J.O. Sexton. 2015. US protected lands mismatch biodiversity priorities. PNAS 112:5081-5086.

King, S.L., Battaglia, L.L., Hupp, C.R., Keim, R.F., and B.G. Lockaby. 2012. Floodplain wetlands of the Southeastern Coastal Plains. 2012. Pp. 439-262, In D.P. Batzer and A.H. Baldwin (Eds.). Wetland Habitats of North America: Ecology and conservation concerns. The University of California Press Berkeley and Los Angeles, USA. 408 pp.

Kirkman, L.K., Smith, L.L., and S.W. Golladay. 2012. Southeastern Depressional Wetlands. Pp. 203-215, In D.P. Batzer and A.H. Baldwin (Eds.). Wetland Habitats of North America: Ecology and conservation concerns. The University of California Press Berkeley and Los Angeles, USA. 408 pp.

Noss, R.F., Platt, W.J., Sorrie, B.A., Weakley, A.S., Means, D.B., Costanza, J., and R.K. Peet. 2015. How global biodiversity hotspots may go unrecognized: lessons from the North American Coastal Plain. Diversity and Distributions 21: 236-244.

Richardson, C.J. 2012. Pocosins: Evergreen shrub bogs of the Southeast. Pp. 189-202, In D.P. Batzer and A.H. Baldwin (Eds.). Wetland Habitats of North America: Ecology and conservation concerns. The University of California Press Berkeley and Los Angeles, USA. 408 pp.

Roll, U., Feldman, A., Novosolov, M. et al. 2017 The global distribution of tetrapods reveals a need for targeted reptile conservation. Nature Ecology & Evolution, 1, 1677-1682.

Tarr, N.M., Rubino, M.J., Costanza, J.K., McKerrow, A.J., Collazo, J.A., and R.C. Abt. 2016. Projected gains and losses of wildlife habitat from bioenergy-induced landscape change. Global Change Biology Bioenergy 9:909-923.

Wharton, C.H., Kitchnes, W.M., Pendleton, E.C., and Snipe, T.W. 1982. The ecology of bottomland hardwood swamps of the Southeast: a community profile.  U.S. Fish and Wildlife Service, Biological Services Program, Washington, D.C. FWS/OBS-81/37. 133pp.

Williams, K., MacDonald, M., McPherson, K., and Mirti, T.H. 2007. Ecology of coastal edge of hydric hammocks on the Gulf Coast of Florida. Pp. 255-289 In W.H. Connor, T.W. Doyle and K.W. Krauss (Eds.). Ecology of Tidal Freshwater Forested Wetlands of the Southeastern United States. Springer Dordrecht, The Netherlands. 505 pp.

