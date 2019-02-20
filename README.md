# ecalBadCalibFilterLists
This repository contains the compressed event lists for the updated ecalBadCalibFilter as well as the code used to make them.

WARNING: Some of the code in this repository is dependent upon the TreeMaker repository. You may first want to follow the instructions [here](https://github.com/TreeMaker/TreeMaker) on how to set up TreeMaker.

## Repository Contents
<!-- Made with: tree -a -I "*.condor|*.stderr|*.stdout|*.txt|METPDOnly|CACHEDIR.TAG|CMSSW_*|AllPDs|.git" -->
```
ecalBadCalibFilterLists/
|-- README.md
|-- data
|   |-- .gitignore
|   |-- Run2016_HTMHT.txt.gz
|   |-- Run2016_JetHT.txt.gz
|   |-- Run2016_MET.txt.gz
|   |-- Run2016_SingleElectron.txt.gz
|   |-- Run2016_SingleMuon.txt.gz
|   |-- Run2016_SinglePhoton.txt.gz
|   |-- Run2017_HTMHT.txt.gz
|   |-- Run2017_JetHT.txt.gz
|   |-- Run2017_MET.txt.gz
|   |-- Run2017_SingleElectron.txt.gz
|   |-- Run2017_SingleMuon.txt.gz
|   |-- Run2017_SinglePhoton.txt.gz
|   |-- Run2018_EGamma.txt.gz
|   |-- Run2018_JetHT.txt.gz
|   |-- Run2018_MET.txt.gz
|   `-- Run2018_SingleMuon.txt.gz
|-- scripts
|   |-- MakeEcalBadCalibFilterList.C
|   `-- README.md
`-- test
    |-- MakeEcalBadCalibFilterList.sh
    |-- MakeEcalBadCalibFilterListJDL.sh
    |-- MakeEcalBadCalibFilterListMergerRunPeriodsByPD.sh
    |-- MakeEcalBadCalibFilterListTEMPLATE.jdl
    `-- README.md
```
