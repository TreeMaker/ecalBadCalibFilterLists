#!/bin/bash

echo "Starting job on "`date` # to display the start date
echo "Running on "`uname -a` # to display the machine where the job is running
echo "System release "`cat /etc/redhat-release` # and the system release
# Can also do 'lsb_release -d' or 'lsb_release -r'
echo "CMSSW on Condor"

# check arguments
export JOBDIR=${PWD}
export USER=$(whoami)
export CMSSWVER="CMSSW_9_4_11"
export CMSSWLOC="slc7_amd64_gcc630"
export CMSSWXRD=""
#export CMSSWXRD="root://cmseos.fnal.gov//store/user/lpcsusyhad/SusyRA2Analysis2015/Run2ProductionV16/"

echo ""
echo "parameter set:"
echo "CMSSWVER: $CMSSWVER"
if [ -n "$CMSSWLOC" ]; then
	echo "CMSSWLOC: $CMSSWLOC"
fi
echo ""

# to get condor-chirp from CMSSW
export PATH="/usr/libexec/condor:$PATH"
# environment setup
source /cvmfs/cms.cern.ch/cmsset_default.sh

# three ways to get CMSSW: tarball transferred by condor, tarball transferred by xrdcp (address provided), new release (SCRAM_ARCH provided)
if [[ "$CMSSWXRD" == root:* ]]; then
	echo "Getting CMSSW via xrdcp"
	xrdcp -f ${CMSSWXRD}/${CMSSWVER}.tar.gz .
fi
if [ -n "$CMSSWLOC" ]; then
	echo "Getting CMSSW via cmsrel"
	export SCRAM_ARCH=${CMSSWLOC}
fi

pwd
ls -lh

# use a tarball if we have it, otherwise make a new release area
if [ -e ${CMSSWVER}.tar.gz ]; then
	# workaround
	if [ -n "$CMSSWLOC" ]; then
		echo "Untar + \"scram project ${CMSSWVER}\""
		mkdir tmp
		tar -xzf ${CMSSWVER}.tar.gz -C tmp
		scram project ${CMSSWVER}
		# omits hidden dirs such as .SCRAM
		cp -r tmp/${CMSSWVER}/* ${CMSSWVER}/
		cd ${CMSSWVER}
		else
		echo "Untar + \"scram b ProjectRename\""
		tar -xzf ${CMSSWVER}.tar.gz
		cd ${CMSSWVER}
		scram b ProjectRename
		fi
else
	echo "scram project ${CMSSWVER}"
	scram project ${CMSSWVER}
	cd ${CMSSWVER}
fi
# cmsenv
eval `scramv1 runtime -sh`

REDIRECTOR=$1
SELECTORS=$2
#FILTERS=$3

(set -x;
cd src/ecalBadCalibFilterLists/scripts/
ls -lh
root -n -b -l MakeEcalBadCalibFilterList.C++\(\"$REDIRECTOR\",\"$JOBDIR\",\{$SELECTORS\},{},true,0\)
ls -lh
)
