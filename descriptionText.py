topText= '''
## Welcome!
This is a tool for estimating the cost of stand-alone, or "off-grid," solar-plus-storage systems in sub-Saharan Africa, with a specific emphasis on reliability that distinguishes it from other off-grid solar system calculators, such as the [European Commission's PVGIS](http://re.jrc.ec.europa.eu/pvg_tools/en/tools.html). We use the fraction of demand served (FDS) as the reliability metric of interest, which measures the ratio of energy supplied to energy demanded over a time period. The tool performs a cost-minimization: given the target reliability and technical and economic parameters below, it finds the configuration of solar and storage capacity that minimizes the [levelized cost of electricity (LCOE)](https://www.nrel.gov/analysis/tech-lcoe-documentation.html). In comparison to a software package like [HOMER](https://www.homerenergy.com/), this tool performs a similar cost-minimization calculation but only for solar-plus-storage off-grid systems. This narrower scope allows us to perform the cost-minimization across a large spatial scale, which is mapped below, and exposes a simple interface for adjusting the parameters.

The tool is intended for researchers, infrastructure planners, and off-grid system designers. This web application is meant to accompany the journal article: [Lee, Jonathan T. and Callaway, Duncan S. "The cost of reliability in decentralized solar power systems in sub-Saharan Africa." *Nature Energy* (2018).](https://doi.org/10.1038/s41560-018-0240-y) We hope that it allows researchers and planners to explore our results more fully, and to test different technical and economic assumptions, and to support a better understanding of the costs of reliability. We also hope that solar-home-system and mini-grid designrs will find it useful as a means of obtaining a quick first-order system design and cost estimate in different locations. Please see the [Quick Guide](#quickGuide) at the bottom of the page for more info. Also, we recommend using Google Chrome.

Please file issues, bugs, and feature requests for the tool on [GitHub](https://github.com/leejt489/solar-reliability-cost-web/issues) if possible. We welcome your feedback and how this beta version of the tool is useful to you or could be improved as well (please email [jtlee@berkeley.edu](mailto:jtlee@berkeley.edu)). You can also view the code for the underlying optimization in [MATLAB](https://github.com/leejt489/solar-reliability-cost-matlab) and in [Python 3](https://github.com/leejt489/solar-reliability-cost-python), and can use those repositories to file issues there as well.

We request that users refer and provide attribution to the following article for all academic research using this tool:

>Lee, Jonathan T. and Callaway, Duncan S. "The cost of reliability in decentralized solar power systems in sub-Saharan Africa." *Nature Energy* (2018). [doi:10.1038/s41560-018-0240-y](https://doi.org/10.1038/s41560-018-0240-y)
'''
guideText = '''
## Quick Guide

A full description of methods used to estimate the cost will be published shortly, and is available upon request. In essence, you can adjust the technical and economic parameters below and click the "Update Map" button to see the spatial variation in the levelized cost of electricity. You can choose between four different load profile shapes which influence how much storage is needed. The load profile shape is interpreted as the average day, and the "peak capacity" is an independent parameter that dictates the desired capacity of the power supply, which may be larger in order to handle short-term load spikes.

The program solves the cost-minimization numerically by simulating different system configurations over 11 years of daily solar irradiance provided by [NASA's Surface meteorology and Solar Energy database](https://eosweb.larc.nasa.gov/sse/). The spatial resolution is 1 degree latitude and longitude.

You can hover over locations on the map to view LCOE, capital cost, and the capacity of solar and storage needed for your system, and you can also download the data that is shown on the map by clicking the button below the map. The download has a more detailed cost breakdown. You can also select a subset of the map by clicking and dragging a box on the map. This will update the density plot below that shows how LCOE scales with reliability for all selected locations. The plot shows, for each reliability on a log scale approaching 100%, the distribution of LCOE over each location that is selected. In general, the LCOE rises and has greater variation at higher reliability. Hovering over the top right corner of the map exposes a menu that allows you to alternate between box and lasso select, and also allows you to download the plot image. Zoom in and out using a mouse wheel or track-pad.
'''
researchersText='''
## The Researchers

This research is conducted by [Jonathan Lee](https://erg.berkeley.edu/people/lee-jonathan/) and [Duncan Callaway](https://erg.berkeley.edu/people/callaway-duncan/). Jonathan is a PhD student and Duncan is a Professor in the [Energy and Resources Group](https://erg.berkeley.edu/) at the University of California, Berkeley.
'''
