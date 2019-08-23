#!/bin/bash

#declare folders=("Run2016B-Nano14Dec2018_ver1-v1" "Run2016B-Nano14Dec2018_ver2-v1" "Run2016C-Nano14Dec2018-v1" "Run2016D-Nano14Dec2018-v1" \
#                                "Run2016E-Nano14Dec2018-v1" "Run2016F-Nano14Dec2018-v1" "Run2016G-Nano14Dec2018-v1" "Run2016H-Nano14Dec2018-v1" \
#                                "Run2017B-Nano14Dec2018-v1" "Run2017C-Nano14Dec2018-v1" "Run2017D-Nano14Dec2018-v1" "Run2017E-Nano14Dec2018-v1" \
#                                "Run2017F-Nano14Dec2018-v1" "Run2018A-Nano14Dec2018-v1" "Run2018B-Nano14Dec2018-v1" "Run2018C-Nano14Dec2018-v1" "Run2018D-Nano14Dec2018-v1")

#declare pds_2016_2017=("HTMHT" "JetHT" "MET" "SingleElectron" "SingleMuon" "SinglePhoton")
#declare pds_2018=("EGamma" "JetHT" "MET" "SingleMuon")

#declare run_periods=("Run2016B" "Run2016B" "Run2016C" "Run2016D" "Run2016E" "Run2016F" "Run2016G" "Run2016H" \
#                                 "Run2017B" "Run2017C" "Run2017D" "Run2017E" "Run2017F" \
#                                 "Run2018A" "Run2018B" "Run2018C" "Run2018D")

#declare years=("Run2016" "Run2017" "Run2018")

declare folders=(Run2016B_ver2-Nano1June2019_ver2-v2 Run2016C-Nano1June2019-v1 Run2016D-Nano1June2019-v1 Run2016E-Nano1June2019-v1 Run2016F-Nano1June2019-v1 Run2016G-Nano1June2019-v1 Run2016H-Nano1June2019-v1)

declare pds_2016_2017=("JetHT")
declare pds_2018=()

declare run_periods=(${folders[@]})

declare years=("Run2016")
