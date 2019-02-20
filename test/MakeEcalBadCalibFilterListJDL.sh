#!/bin/bash

declare folders=("Run2016B-Nano14Dec2018_ver1-v1" "Run2016B-Nano14Dec2018_ver2-v1" "Run2016C-Nano14Dec2018-v1" "Run2016D-Nano14Dec2018-v1" \
				 "Run2016E-Nano14Dec2018-v1" "Run2016F-Nano14Dec2018-v1" "Run2016G-Nano14Dec2018-v1" "Run2016H-Nano14Dec2018-v1" \
				 "Run2017B-Nano14Dec2018-v1" "Run2017C-Nano14Dec2018-v1" "Run2017D-Nano14Dec2018-v1" "Run2017E-Nano14Dec2018-v1" \
				 "Run2017F-Nano14Dec2018-v1" "Run2018A-Nano14Dec2018-v1" "Run2018B-Nano14Dec2018-v1" "Run2018C-Nano14Dec2018-v1" "Run2018D-Nano14Dec2018-v1")

declare pds_2016_2017=("HTMHT" "JetHT" "MET" "SingleElectron" "SingleMuon" "SinglePhoton")
declare pds_2018=("EGamma" "JetHT" "MET" "SingleMuon")

for folder in "${folders[@]}"; do
	if [[ $folder == "Run2018"* ]]; then
		declare pds=("${pds_2018[@]}") 
	else
		declare pds=("${pds_2016_2017[@]}")
	fi

	for pd in "${pds[@]}"; do
		jdl_name="MakeEcalBadCalibFilterList_${folder}_${pd}.jdl"
		cp MakeEcalBadCalibFilterListTEMPLATE.jdl ${jdl_name}
		sed -i "s/RUNNAME/${folder}/g" ${jdl_name}
		sed -i "s/PRIMARYDATASET/${pd}/g" ${jdl_name}
		condor_submit ${jdl_name}
	done
done