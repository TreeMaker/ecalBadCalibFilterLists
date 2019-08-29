import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/60000/0C790C3E-D211-984F-AB38-037BA4C27B9F.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/60000/7142F0AB-35DB-014A-8436-7CD6AAF02DFA.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/60000/E773E226-16B7-E047-B73B-27AB99733747.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_1000to1400_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/60000/EA3FF0A2-0D83-4242-9D35-38C841E707E2.root',
] )
