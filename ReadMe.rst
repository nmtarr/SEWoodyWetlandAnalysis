=================================
Southeast Woody Wetland Analysis Code
=================================
The "archive" folder contains some scripts from early in the workflow development.

PURPOSE
In the southeastern U.S., unique ecosystems and animal communities share landscapes with intensive, anthropogenic land use and development.  Biological diversity is exceptional in the region, including a high diversity of plant species and relatively high numbers of endemics that were long overlooked due to misconceptions about geological history, disturbance regimes, and environmental heterogeneity (Noss et al. 2015).  Hotspots of amphibian, bird, and reptile richness also occur in the region (Jenkins et al. 2015, McKerrow et al. 2018, Roll et al 2017), and rather than having one ecological system with high diversity, diversity is relatively high in multiple dissimilar communities such as longleaf pine savannahs (Noss et al. 2015) and depressional wetlands (Kirkman et al. 2012). Conservation assessments have identified an underrepresentation of riparian floodplain systems and Southeastern species in the national network of protected areas (Aycrigg et al. 2013, Jenkins et al. 2015, Aycrigg et al. 2016).  

Whereas widespread silviculture, agriculture, and urbanization converted the natural ecosystems that originally covered the region, many unique ecosystems remain extant, albeit with reduced extents.  Among those systems are ones found in the lowland Coastal Plains that experience constant or frequent flooding or whose hydrology and woody plant compositions are unique to the region.  These woody wetland ecosystems include freshwater and tidal swamps, bottomland hardwood forests, pocosins, hydric hammocks, Carolina bays, and large depressional wetlands (Batzer et al. 2012, King et al. 2012, Kirkman et al. 2012, Richardson 2012).  Southeastern woody wetlands (SEWW’s) comprise much of the remaining natural forests and shrublands in the Coastal Plain (Wharton et al. 1982).  

In the Southeastern Coastal Plain, historical threats to woody wetland systems, such as agriculture, urbanization, demand for timber, and alteration of hydrological regimes persist (Doyle et al. 2007, Batzer et al. 2012, Kirkman et al. 2012, Richardson 2012), while new forces such as increased rate of sea level rise, changes in precipitation and temperature, and demand for wood pellets develop (Connor et al. 2007a, Tarr et al. 2016, Duden et al. 2017).  Man made changes to hydrological regimes have taken many forms including ditches, dams, levees, and channelization (Doyle et al. 2007, King et al. 2012, Richardson 2012), and those changes have been the most destructive of all change agents because they have persisted for centuries, affecting hydrology, subsidence, and salinity in ways that impede the growth and regeneration of key plant species (Faulkner et al. 2007, Doyle et al. 2012, King et al. 2012).  

Swamps and bottomland forests were logged beginning in colonial times and then at fast rates within certain regions during other periods since (Batzer et al. 2012, Connor et al. 2007b, Doyle et al. 2007, Faulkner et al. 2007).  Wood pellets represent new demand for timber in the vicinity of coastal plain wetlands and places like Louisiana have seen recent interest in harvesting for cypress mulch (Faulkner et al. 2007, Evans et al. 2013).  Some wetland forests have been slow or unable to recover due to limits on regeneration associated with changing salinity and hydrology (Faulkner et al. 2007).  However, the impacts of forestry on wildlife will depend on timber management as commercial timber operations can be mechanisms to improve habitat for some species and counter effects of restricted hydrology on forest composition and structure (King et al. 2012).  

Climate change and sea level rise raise new concerns for tidal freshwater swamps and other plant communities that exist at the salt-freshwater interface because they could alter the frequency of saltwater intrusion events via drought and storm surge, which may become more frequent or of longer duration in the Southeast with climate change, and high salinity kills or impedes the growth of key nonhalophytic plant species (Connor et al. 2007, Day et al. 2007, Doyle et al. 2007, Faulkner et al. 2007, Williams et al. 2007).  Droughts reduce the freshwater inputs into tidal swamps (river flow, precipitation, and groundwater levels), allowing salinity to increase inland (Doyle et al. 207), whereas hurricane storm surge pushes saltwater further inland (Connor et al. 2007b, Doyle et al. 2007).  Furthermore, canals and shipping channels sometimes facilitate and extend saltwater intrusion (Doyle et al. 2007).  When mortality from salt intrusion occurs, forests become open water, marsh, or scrub-shrub communities (Connor et al. 2007b).  While some systems could conceivably migrate inland with the coastal interface, that is not possible for hardwood hammocks found in Florida because geomorphological features will act as a barrier to migration (Williams et al. 2007).  Changes to precipitation could also have consequences because changes in the amount or timing of rainfall could alter rain-fed swamps and depressional wetlands (Batzer et al. 2012, Kirkman et al. 2012).  
  
Many wildlife species avoid areas dominated by human land use (i.e. croplands and urban areas) so woody wetlands likely provide valuable habitat to wildlife populations in the region; however, the broad contribution of southeastern woody wetlands to wildlife habitat within the conterminous U.S. has not been examined at large extents, and identities of those species for which woody wetlands are most important are unknown.  I investigated relationships between wildlife habitat and southeastern woody wetlands at a national scale.  My objectives were to assess the distribution and protection of SEWW’s and determine 1) how species richness on SEWW’s compares to that of the Southeast and conterminous United States (CONUS), 2) which species have the largest proportion of their habitat in SEWW’s, 3) how well protected those species’ habitats are, and 4) locations of hotspots of SEWW-dependent species richness.  This study will identify species and locations to consider for further research, monitoring, and protection in the face of anticipated landscape changes in the Southeast.

INPUTS & OUTPUTS
see SEWW Inputs and Outputs.csv

CONSTRAINTS

DEPENDENCIES
see Requirements.txt and environment.yml

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

7. BuildPyramids.py  


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

Doyle, T.W., O’Neil, C.P., Melder, M.P.V., From, A.S., and Palta, M.M. 2007. Tidal freshwater swamps of the southeastern United States: Effects of land use, hurricanes, sea-level rise, and climate change. Pp. 1-28, In W.H. Connor, T.W. Doyle and K.W. Krauss (Eds.). Ecology of Tidal Freshwater Forested Wetlands of the Southeastern United States. Springer Dordrecht, The Netherlands. 505 pp.

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

