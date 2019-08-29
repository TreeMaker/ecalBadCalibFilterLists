import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/110000/0A6255FF-A06D-F444-BFDC-D4AFF0E19979.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/110000/3DA0B14D-ED18-F445-BFA7-856000989521.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/110000/55855278-910F-0540-BAB2-A5734B1525B8.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/110000/7A55EB63-2C6F-9A4A-895D-BC628FA92328.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/110000/CFA523A6-4699-664F-A78B-D41E5C5CF613.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_600to800_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/110000/EC8DF07F-FC38-A441-9CDA-D3BD90199B94.root',
] )
