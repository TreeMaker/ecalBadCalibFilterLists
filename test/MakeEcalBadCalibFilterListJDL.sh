#!/bin/bash

source data.sh

BRANCH=Flag_EcalDeadCellBoundaryEnergyFilter

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
		sed -i "s/BRANCHNAME/${BRANCH}/g" ${jdl_name}
		condor_submit ${jdl_name}
	done
done
