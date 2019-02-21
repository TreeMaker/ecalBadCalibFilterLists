# Utility Scripts

## Typical Workflow
1. Edit the Condor JDL template (MakeEcalBadCalibFilterListTEMPLATE.jdl) and script (MakeEcalBadCalibFilterListJDL.sh) to your heart's content.
2. Edit MakeEcalBadCalibFilterList.sh to create the necessary JDLs. By default it is set up to run one job for each run period and PD (maximal separation). Then run the script to make and submit the condor jobs. You may want to try commenting out the condor_submit line first to read a JDL file before submiting.
3. Once all of the files have been returned, you will need to merge the run periods in to year/PD combinations. For this you will use MakeEcalBadCalibFilterListMergerRunPeriodsByPD.sh.
4. At the end of this you may still want to rename a gzip the contents of the files before putting them into the data folder. You might want to use commands similar to the ones below:
  * rename -- -Nano14Dec2018-v1_ _ Run201*
  * rename -- -Nano14Dec2018_ver1-v1_ _ Run201*
  * rename -- -Nano14Dec2018_ver2-v1_ _ Run201*
  * rename _ecalBadCalibFilterList.txt .txt Run201*
  * for f in Run201?_*.txt; do gzip --best ${f}; done
  * mv *.txt.gz ../data/