#!/bin/bash

source mc.sh

BRANCH=Flag_EcalDeadCellBoundaryEnergyFilter

for folder in "${folders[@]}"; do
	if [[ $folder == *Summer16* ]]; then
		declare pds=("${pds_Summer16[@]}")
	fi

	for pd in "${pds[@]}"; do
		jdl_name="MakeEcalBadCalibFilterList_${folder}_${pd}.jdl"
		cp MakeEcalBadCalibFilterListTEMPLATE.jdl ${jdl_name}
		sed -i "s/RUNNAME/${folder}/g" ${jdl_name}
		sed -i "s/PRIMARYDATASET/${pd}/g" ${jdl_name}
		sed -i "s/BRANCHNAME/${BRANCH}/g" ${jdl_name}
		sed -i "s/MCSIM/1/g" ${jdl_name}
		condor_submit ${jdl_name}
	done
done
