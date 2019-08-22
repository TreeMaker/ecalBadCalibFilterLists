#!/bin/bash

declare run_periods=("Run2016B" "Run2016B" "Run2016C" "Run2016D" "Run2016E" "Run2016F" "Run2016G" "Run2016H" \
				 "Run2017B" "Run2017C" "Run2017D" "Run2017E" "Run2017F" \
				 "Run2018A" "Run2018B" "Run2018C" "Run2018D")

declare pds_2016_2017=("HTMHT" "JetHT" "MET" "SingleElectron" "SingleMuon" "SinglePhoton")
declare pds_2018=("EGamma" "JetHT" "MET" "SingleMuon")

declare years=("Run2016" "Run2017" "Run2018")

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
		for rp in "${run_preiods[@]}"; do
			if [[ $rp == "$year"* ]]; then
				selected_files+=("${rp}_${pd}.txt")
			fi
		done

		# For a given year and PD merge the run period files
		(set -x;
		 cat "${selected_files[@]}" > ${destination}
		)
		echo
	done
done