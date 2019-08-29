import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/60000/3CA261FB-FC5C-8C41-A3F8-FD1F8D567121.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/60000/4D472254-B7FA-2C4E-8AE2-257692E21AC5.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/60000/CA7FB0DB-76A3-2C48-91F4-5F09437593D2.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/60000/CE07A9DB-EC61-F546-A2B9-6511F9A4A029.root',
       '/store/mc/RunIISummer16NanoAODv5/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/NANOAODSIM/PUMoriond17_Nano1June2019_102X_mcRun2_asymptotic_v7-v1/60000/D4816750-E899-9546-B1F7-4E1F8C357EAC.root',
] )
