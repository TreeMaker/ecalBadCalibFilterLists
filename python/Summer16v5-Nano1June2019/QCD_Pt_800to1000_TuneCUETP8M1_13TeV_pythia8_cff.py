import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/40000/0F803FDB-2699-3143-B0E1-2EF303FF4391.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/40000/6B1E7F1D-C1F2-BA42-83F8-00FCA84126CA.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/40000/A7514371-4114-8A41-9FAD-77C19A5C7F16.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_800to1000_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/40000/B2A7B48F-C62C-DB4B-953C-A1C227F3F008.root',
] )
