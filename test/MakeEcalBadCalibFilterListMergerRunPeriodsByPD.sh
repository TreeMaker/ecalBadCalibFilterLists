#!/bin/bash

source data.sh
SUFFIX=$1

for year in "${years[@]}"; do

	# Select a set of PD names based on the year
	if [[ $year == "Run2018" ]]; then
		declare pds=("${pds_2018[@]}") 
	else
		declare pds=("${pds_2016_2017[@]}")
	fi

	# Loop over the PDs and run periods
	for pd in "${pds[@]}"; do
		destination="${year}_${pd}.txt"
		declare selected_files=()
		for rp in "${run_periods[@]}"; do
			if [[ $rp == "$year"* ]]; then
				fname=${rp}_${pd}
				if [ -n "$SUFFIX" ]; then
					fname=${fname}_${SUFFIX}
				fi
				fname=${fname}.txt
				selected_files+=("${fname}")
			fi
		done

		# For a given year and PD merge the run period files
		(set -x;
		 cat "${selected_files[@]}" > ${destination}
		)
		echo
	done
done
