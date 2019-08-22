# Scripts
In here you will find the scripts necessary to make the ecalBadCalibFilter event lists.

## MakeEcalBadCalibFilterList.C
This code relies upon the NanoAOD file lists which would be located in $CMSSW_BASE/src/TreeMaker/ecalBadCalibFilterLists/python. In the current version of the code this basepath is fixed. And while the code can technically take any file list, only the NanoAOD trees will have the necessary branches. Therefore, the user should take special note to filter out any non-NanoAOD file lists. This can be accomplished through the use of the selector and filter lists.

The selectors will selectors will select for folder or file names with a given string. This is an inclusive list, so a folder/file need only contain one of the selectors to be added to the selected list.

The filters work in much the same way. If a folder/file contains any of the filter strings, it will be removed from the list of folders/files to consider.

By default the output files are places in the same folder as the file lists. However, this can be overridden by specifying an outpath as one of the parameters.

### Example (compile)
```bash
./compile.sh
```

### Example (run)
```bash
root -n -b -l -q 'MakeEcalBadCalibFilterList.C+("root://cmsxrootd.fnal.gov/","./",{"2018C-Nano","EGamma"},{},"Flag_ecalBadCalibFilter",true,0)'
```
