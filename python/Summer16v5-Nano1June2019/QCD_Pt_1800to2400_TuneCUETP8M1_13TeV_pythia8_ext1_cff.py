import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/100000/0660C410-0596-EF4C-A315-AA68E7E1F59C.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/100000/2A1B850B-DA5C-7E47-85B7-9D498F1D74DD.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_1800to2400_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7_ext1-v1/100000/A2C996D4-AF8F-DD43-8757-7199EE8BD799.root',
] )
