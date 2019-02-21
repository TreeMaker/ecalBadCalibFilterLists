# ecalBadCalibFilterLists
This repository contains the compressed event lists for the updated ecalBadCalibFilter as well as the code used to make them.

WARNING: Some of the code in this repository is dependent upon the TreeMaker repository. You may first want to follow the instructions [here](https://github.com/TreeMaker/TreeMaker) on how to set up TreeMaker.

## Repository Contents
* The [data](data) folder contains the events lists combined by run period for a given year and PD (i.e. [Run2018_MET.txt.gz](data/Run2018_MET.txt.gz)). These files are maintained in gzip files to reduce their size.
* The [scripts](scripts) folder contains the code necessary to create the event lists. In the future it may also contain other C++ code necessary to create, modify, or maintain the event lists.
* The [test](test) folder contains the bash scripts and Condor JDL files needed to create a large number of events lists.
